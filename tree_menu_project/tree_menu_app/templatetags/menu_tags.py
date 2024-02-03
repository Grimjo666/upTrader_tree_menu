from django import template
from tree_menu_app.models import TreeMenu
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = TreeMenu.objects.filter(name=menu_name).select_related('parent').prefetch_related('children')

    current_menu_item = menu_items.filter(url=current_url)  # активный текущий элемент меню

    if not current_menu_item.exists():
        current_menu_item = None
    else:
        current_menu_item = current_menu_item[0]  # если queryset не пустой, то достаём активный элемент меню

    return mark_safe(render_menu(menu_items, current_menu_item))


def render_menu(menu_items, current_menu_item):
    menu_html = ''

    if current_menu_item:
        children = current_menu_item.children.all()  # получаем детей активного элемента меню

        if current_menu_item.parent:  # если у активного элемента есть родитель
            parents_or_root = get_parents_or_root(menu_items, current_menu_item)  # получаем родителей активного элем-та
            menu_html = draw_tree_elements(parents_or_root, children, current_menu_item=current_menu_item)

        else:  # если родителя нет
            root_items = get_parents_or_root(menu_items)  # получаем корни
            menu_html = draw_tree_elements(root_items, children)  # передаём корни и детей и получаем html меню

    else:  # если нет активного элемента меню значит мны находимся в корне меню
        parents = get_parents_or_root(menu_items)
        menu_html = draw_tree_elements(parents)

    return menu_html


def get_parents_or_root(queryset, item=None):
    if item and item.parent.parent:
        return item.parent.parent.children.all()
    return queryset.filter(parent=None)


def draw_tree_elements(parents, children=None, current_menu_item=None) -> str:
    html = '<ul>'
    for parent in parents:  # проходимся по родителям
        html += f'<li><a href="{parent.url}">{parent.title}</a></li>'

        if children:

            if children[0] in parent.children.all():  # берём любого ребёнка и проверяем есть ли он у текущего родителя
                html += draw_tree_elements(children)  # рисуем ul список для детей

            # если передан активный элемент меню и кто то из детей является его ребёнком
            elif current_menu_item and children[0] in current_menu_item.children.all():

                # если текущий элемент является ребёнком родителя
                if current_menu_item in parent.children.all():
                    # получаем братьев активного элемента меню
                    brothers_of_current_parent = current_menu_item.parent.children.all()
                    html += draw_tree_elements(brothers_of_current_parent, children)

    html += '</ul>'
    return html

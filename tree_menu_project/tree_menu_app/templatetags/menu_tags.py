from django import template
from tree_menu_app.models import TreeMenu
from django.utils.html import mark_safe
from django.urls import reverse

register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = TreeMenu.objects.filter(name=menu_name).select_related('parent').prefetch_related('children')
    return mark_safe(render_menu(menu_items, current_url))


def render_menu(menu_items, current_url):
    menu_html = ''
    tree_items_dict = {'no_parents': []}
    url_dict = {}
    for item in menu_items:
        url_dict[item.url] = item

        if item.parent is None:
            tree_items_dict['no_parents'].append(item)

        else:
            parent = item.parent
            tree_items_dict[parent] = tree_items_dict.get(parent, [])
            tree_items_dict[parent].append(item)


    print(url_dict)
    print(tree_items_dict)
    tmp_html = None
    while True:
        if current_url not in url_dict:
            item_key = 'no_parents'
        else:
            item_key = url_dict[current_url]

        if not tmp_html:
            tmp_html = draw_html_list(tree_items_dict[item_key])

        if tree_items_dict[item_key][0].parent:  # Если у текущего уровня вложенности есть родитель
            parent = [tree_items_dict[item_key][0].parent]
            tmp_html = draw_html_list(parent, tmp_html)  # Добавляем ранее полученный Html список в новый список

            if tree_items_dict[item_key][0].parent.parent:  # Если у текущего уровня вложенности есть дед
                current_url = tree_items_dict[item_key][0].parent.parent.url

            else:
                menu_html += tmp_html
                break

        else:  # Если у текущего уровня вложенности нет родителя, то завершаем цикл
            menu_html += tmp_html
            break


        # print(menu_html)
        # elif item.parent.url == current_url:
        #     menu_html += f'<li><a href="{item.url}">{item.title}</a></li>'
        #     menu_html += render_menu(item.children.all(), current_url)

    return menu_html


def draw_html_list(items, html_text=None):
    html = '<ul>'
    for item in items:
        html += f'<li><a href="{item.url}">{item.title}</a></li>'
        if html_text:
            html += html_text
    html += '</ul>'
    return html

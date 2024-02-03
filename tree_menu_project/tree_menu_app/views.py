from django.shortcuts import render


def index_page(request):
    return render(request, 'tree_menu_app/index.html')


def clothes_page(request):
    return render(request, 'tree_menu_app/clothes.html')


def outerwear_page(request):
    return render(request, 'tree_menu_app/outerwear.html')


def underwear_page(request):
    return render(request, 'tree_menu_app/underwear.html')


def footwear_page(request):
    return render(request, 'tree_menu_app/footwear.html')

def bmw_page(request):
    return render(request, 'tree_menu_app/bmw.html')
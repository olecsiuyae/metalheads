from django.shortcuts import render

from translate.models import Category, Band, Song, Page


def main(request):
    return render(request, "metalheads/main.html")


def categories(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'metalheads/categories.html', context_dict)


def category(request, category_id):
    context_dict = {}

    try:

        category = Category.objects.get(pk=category_id)
        context_dict['category_name'] = category.name

        bands = Band.objects.filter(category=category)

        context_dict['bands'] = bands

        context_dict['category'] = category
    except Category.DoesNotExist:

        pass

    return render(request, 'metalheads/bands.html', context_dict)


def translates(request):
    return render(request, "metalheads/translates.html")


def contacts(request):
    return render(request, "metalheads/contacts.html")


def search(request):
    return render(request, "metalheads/search.html")
from django.shortcuts import render

from translate.models import Category, Page


def main(request):
    return render(request, "metalheads/main.html")

def categories(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'metalheads/categories.html', context_dict)

def bands(request ,category_name_slug):

    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name


        pages = Page.objects.filter(category=category)


        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:

        pass
    return render(request, "metalheads/categories.html", context_dict)



def translates(request):
    return render(request, "metalheads/translates.html")


def contacts(request):
    return render(request, "metalheads/contacts.html")


def search(request):
    return render(request, "metalheads/search.html")
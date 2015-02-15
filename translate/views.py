from django.shortcuts import render

from translate.models import Category, Band, Song


def main(request):
    return render(request, "metalheads/main.html")


def categories(request):
    category_list = Category.objects.order_by('name')
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

def band(request, band_id):
    context_dict = {}

    try:

        band = Band.objects.get(pk=band_id)
        context_dict['band_name'] = band.name

        songs = Song.objects.filter(band=band)

        context_dict['songs'] = songs

        context_dict['band'] = band
    except Category.DoesNotExist:

        pass

    return render(request, 'metalheads/songs.html', context_dict)

def translate(request, translates_id):
    context_dict = {}
    try:
        song = Song.objects.get(pk=translates_id)
        context_dict['text_ukr'] = song.text_ukr
        context_dict['text_org'] = song.text_org
        context_dict['song_name'] = song.name
    except Category.DoesNotExist:

        pass

    return render(request, "metalheads/translates.html", context_dict)


def contacts(request):

    return render(request, "metalheads/contacts.html")


def search(request):

    return render(request, "metalheads/search.html")
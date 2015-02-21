from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404

from translate.models import Category, Band, Song, NewSong

from translate.form import UserForm, UserAddSongForm


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

        songs = Song.objects.filter(band=band, is_verified=True)
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


def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
                  'metalheads/register.html',
                  {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("account is disabale")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("bad data")
    else:
        return render(request, 'metalheads/login.html')


def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/translate/')


def add_song(request):

    if request.method == 'POST':

        form = UserAddSongForm(data=request.POST)

        if form.is_valid():

            song = form.save(commit=False)
            song.user = request.user
            song.save()

        else:
            print form.errors

    else:
        form = UserAddSongForm()

    # Render the template depending on the context.
    return render(request,
                  'metalheads/addsong.html',
                  {'form': form})


@login_required
def verify_song(request):
    if request.user.is_superuser:
        submission_id = request.GET.get('id', None)
        if submission_id:
            submission = get_object_or_404(NewSong, pk=submission_id)
            band = get_object_or_404(Band, name=submission.band)
            song = Song.objects.create(
                band=band,
                name=submission.name,
                name_ukr=submission.name_ukr,
                text_org=submission.text_org,
                text_ukr=submission.text_ukr
            )
            song.save()
            submission.delete()
            return HttpResponseRedirect('/admin/translate/newsong/')
    else:
        return HttpResponseForbidden()
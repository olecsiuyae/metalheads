from django.shortcuts import render

# Create your views her
def main (request):
    return render(request, "metalheads/main.html")
def categories (request):
    return render(request, "metalheads/categories.html")
def translates (request):
    return  render(request, "metalheads/translates.html")
def contacts (request):
    return render(request, "metalheads/contacts.html")
def search (request):
    return render(request, "metalheads/search.html")
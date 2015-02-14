from django.shortcuts import render

# Create your views her
def main (request):
    return render(request, "metalheads/main.html")
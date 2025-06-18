from django.shortcuts import render

# Create your views here.

def home(request):

    content = None

    return render(request, "pages/home.html", content)

def base(request):

    content = None

    return render(request, "base.html", content)
from django.shortcuts import render
from .models import AboutPage

def about_page(request):
    about = AboutPage.objects.first()
    return render(request, 'about/about.html', {'about': about})

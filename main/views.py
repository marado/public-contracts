from django.shortcuts import render


def robots(request):
    return render(request, 'robots.txt', content_type='text/plain')


def home(request):
    return render(request, 'main_page.html')


def about(request):
    return render(request, 'about.html')

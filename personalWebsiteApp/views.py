from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {"url": ""}
    return render(request, 'personalWebsiteApp/index.html', context)

def about_me_page(request):
    context = {"url": "about-me"}
    return render(request, 'personalWebsiteApp/index.html', context)

def about_website_page(request):
    context = {"url": "about-website"}
    return render(request, 'personalWebsiteApp/index.html', context)

def projects_page(request):
    context = {"url": "projects"}
    return render(request, 'personalWebsiteApp/index.html', context)

def cv_page(request):
    context = {"url": "cv"}
    return render(request, 'personalWebsiteApp/index.html', context)

def ziad_page(request):
    context = {"url": "cv"}
    return render(request, 'personalWebsiteApp/ziad.html', context)
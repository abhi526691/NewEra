from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request, 'index.html')

def galleryPage(request):
    return render(request, 'gallery.html')

def contactPage(request):
    return render(request, 'contact.html')

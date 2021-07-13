from django.urls import path
from .views import indexPage, galleryPage, contactPage

app_name = 'homePage'

urlpatterns = [
    path('home/', indexPage),
    path('gallery/', galleryPage),
    path('contact/', contactPage)
]
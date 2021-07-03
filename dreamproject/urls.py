"""dreamproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from dreamproject.mainapp.views import blogsingle
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/',views.about, name="about"),
    path('blogsingle/',views.blogsingle, name="blogsingle"),
    path('blog/',views.blog, name="blog"),
    path('contact/',views.contact, name="contact"),
    path('portfoliosingle/',views.portfoliosingle, name="portfoliosingle"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('services/',views.services, name="services"),
    path('accounts/',include('allauth.urls')),
    path('mypage/',include('mypage.urls')),
    path('dreamrelay/',views.dreamrelay, name="dreamrelay"),
    path('story/',views.story, name="story"),
    path('music/',views.music, name="music"),
    path('illustration/',views.illustration, name="illustration"),
    path('library/', views.library, name="library"),
    path('detailS/<str:id>', views.detailS, name="detailS"),
    path('newS/', views.newS, name="newS"),
    path('createS/', views.createS, name="createS"),
    path('editS/<str:id>', views.editS, name="editS"),
    path('updateS/<str:id>', views.updateS, name="updateS"),
    path('deleteS/<str:id>', views.deleteS, name="deleteS"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



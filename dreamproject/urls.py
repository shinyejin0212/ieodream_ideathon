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
    path('create_commentS/<str:post_id>', views.create_commentS, name="create_commentS"),
    path('update_commentS/<str:post_id>/<str:comment_id>', views.update_commentS, name="update_commentS"),
    path('edit_commentS/<str:post_id>/<str:comment_id>', views.edit_commentS, name="edit_commentS"),
    path('deleteS/<str:post_id>/<str:comment_id>', views.delete_commentS, name="delete_commentS"),

    path('detailI/<str:id>', views.detailI, name="detailI"),
    path('newI/', views.newI, name="newI"),
    path('createI/', views.createI, name="createI"),
    path('editI/<str:id>', views.editI, name="editI"),
    path('updateI/<str:id>', views.updateI, name="updateI"),
    path('deleteI/<str:id>', views.deleteI, name="deleteI"),
    path('create_commentI/<str:post_id>', views.create_commentI, name="create_commentI"),
    path('update_commentI/<str:post_id>/<str:comment_id>', views.update_commentI, name="update_commentI"),
    path('edit_commentI/<str:post_id>/<str:comment_id>', views.edit_commentI, name="edit_commentI"),
    path('deleteI/<str:post_id>/<str:comment_id>', views.delete_commentI, name="delete_commentI"),

    path('detailM/<str:id>', views.detailM, name="detailM"),
    path('newM/', views.newM, name="newM"),
    path('createM/', views.createM, name="createM"),
    path('editM/<str:id>', views.editM, name="editM"),
    path('updateM/<str:id>', views.updateM, name="updateM"),
    path('deleteM/<str:id>', views.deleteM, name="deleteM"),
    path('create_commentM/<str:post_id>', views.create_commentM, name="create_commentM"),
    path('update_commentM/<str:post_id>/<str:comment_id>', views.update_commentM, name="update_commentM"),
    path('edit_commentM/<str:post_id>/<str:comment_id>', views.edit_commentM, name="edit_commentM"),
    path('deleteM/<str:post_id>/<str:comment_id>', views.delete_commentM, name="delete_commentM"),

    path('moana/', views.moana, name="moana"),
    path('Moonight/', views.Moonight, name="Moonight"),

    path('newD/', views.newD, name="newD"),
    path('createD/', views.createD, name="createD"),
    path('editD/<str:id>', views.editD, name="editD"),
    path('updateD/<str:id>', views.updateD, name="updateD"),
    path('deleteD/<str:id>', views.deleteD, name="deleteD"),
    path('detailD/<str:id>', views.detailD, name="detailD"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



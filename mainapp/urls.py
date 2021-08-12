from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('like_toggleS/<int:post_id>/',like_toggleS,name="like_toggleS"), #좋아요 기능 
    path('like_toggleI/<int:post_id>/',like_toggleI,name="like_toggleI"), #좋아요 기능 
]
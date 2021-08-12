from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('like_toggleS/<int:post_id>/',like_toggleS,name="like_toggleS"), #좋아요 기능 
    path('like_toggleI/<int:post_id>/',like_toggleI,name="like_toggleI"), #좋아요 기능 
    path('like_toggleM/<int:post_id>/',like_toggleM,name="like_toggleM"), #좋아요 기능 
    path('like_toggleSL/<int:post_id>/',like_toggleSL,name="like_toggleSL"), #좋아요 기능 
    path('like_toggleIL/<int:post_id>/',like_toggleIL,name="like_toggleIL"), #좋아요 기능 
    path('like_toggleML/<int:post_id>/',like_toggleML,name="like_toggleML"), #좋아요 기능 
]
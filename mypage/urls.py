from django.urls import path ,re_path
from .import views
from django.contrib.auth.decorators import login_required


app_name="mypage"
urlpatterns=[

    # re_path(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()), name='profile'),
    path('mypage/', views.mypage, name="mypage"),
    path('profile_update/', login_required(views.ProfileUpdateView.as_view()), name='profile_update'),

]

 
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignupForm(forms.Form):
    model = User

    def signup(self, request, user):
        profile = Profile()
        profile.user = user
        profile.save()
        user.save()
        return user
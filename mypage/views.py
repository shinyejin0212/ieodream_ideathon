from django.db import models
from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.generic import detail
from django.views.generic.detail import DetailView
from django.views import View
from .forms import  ProfileForm

from django.shortcuts import render,get_object_or_404, redirect

# 메인앱의 모델에서 스토리,음악,일러스트 가져오기 
from mainapp.models import PostS
from mainapp.models import PostM
from mainapp.models import PostI

def mypage(request):
        user = request.user
        storys = PostS.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
        musics = PostM.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
        illustrations = PostI.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
        DetailView.context_object_name='profile_user'
        DetailView.model = User 
        DetailView.template_name = 'mypage/mypage.html'
        #이야기,음악,일러스트레이트 반환하기 
        return render(request,'mypage/mypage.html',{'storys':storys,'musics':musics,'illustrations':illustrations, 'profile_user':DetailView.model})

class ProfileView(DetailView):
    context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정함
    model = User
    template_name = 'mypage/mypage.html'
    


class ProfileUpdateView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)  # 로그인중인 사용자 객체를 얻어옴


        if hasattr(user, 'profile'):  # user가 profile을 가지고 있으면 True, 없으면 False (회원가입을 한다고 profile을 가지고 있진 않으므로)
            profile = user.profile
            profile_form = ProfileForm(initial={
                'bio': profile.bio,
                'profile_photo': profile.profile_photo,
            })
        else:
            profile_form = ProfileForm()

        return render(request, 'mypage/profile_update.html', { "profile_form": profile_form})
    def post(self, request):
        u = User.objects.get(id=request.user.pk)        

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile) # 기존꺼 가져와 수정 
        else:
            profile_form = ProfileForm(request.POST, request.FILES) # 새로 만드는 것

        # Profile 폼
        if profile_form.is_valid():
            profile = profile_form.save(commit=False) # 기존의 것을 가져와 수정하는 경우가 아닌 새로 만든 경우 user를 지정해야 함
            profile.user = u
            profile.save()

        return redirect('mypage:mypage')

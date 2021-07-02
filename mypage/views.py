from django.shortcuts import render
from django.contrib.auth.models import User
#post 글 가져오기 

def mypage(request):
    user = request.user
    # novels = Novel.objects.filter(applicant=user)
    # 작성한 소설 글 가져오기 
    return render(request,'mypage/mypage.html')
    # return render(request,'mypage/mypage.html',{{'novels':novels}})

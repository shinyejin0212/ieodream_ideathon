from django.shortcuts import render
from django.contrib.auth.models import User

# 메인앱의 모델에서 스토리,음악,일러스트 가져오기 
from mainapp.models import PostS
from mainapp.models import PostM
from mainapp.models import PostI

def mypage(request):
    user = request.user
    storys = PostS.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
    musics = PostM.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
    illustrations = PostI.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
    
    #이야기,음악,일러스트레이트 반환하기 
    return render(request,'mypage/mypage.html',{'storys':storys,'musics':musics,'illustrations':illustrations})

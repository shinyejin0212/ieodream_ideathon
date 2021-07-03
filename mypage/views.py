from django.shortcuts import render
from django.contrib.auth.models import User

# 메인앱의 모델에서 스토리,음악,일러스트 가져오기 
# from mainapp.models import Post_Stroy
# from mainapp.models import Post_Music
# from mainapp.models import Post_Illustration

def mypage(request):
    user = request.user
    # storys = Post_Story.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
    # musics = Post_Music.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 
    # illustrations = Post_Illustration.objects.filter(writer=user) #로그인한 유저와 글 작성자 이름 동일하게 

    # novels = Novel.objects.filter(applicant=user)
    # 작성한 소설 글 가져오기 
    return render(request,'mypage/mypage.html')
    #이야기,음악,일러스트레이트 반환하기 
    # return render(request,'mypage/mypage.html',{'storys':stroys,'musics':musics,'illustrations':illustrations})

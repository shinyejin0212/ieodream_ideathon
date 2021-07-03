from django.http import request
from django.shortcuts import render,get_object_or_404, redirect
from .models import PostS, PostD
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def blogsingle(request):
    return render(request, 'mainapp/blog-single.html')

def blog(request):
    return render(request, 'mainapp/blog.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def portfoliosingle(request):
    return render(request, 'mainapp/portfolio-single.html')

def portfolio(request):
    return render(request, 'mainapp/portfolio.html')

def services(request):
    return render(request, 'mainapp/services.html')

def dreamrelay(request):
    return render(request, 'mainapp/dreamrelay.html')

def story(request):
    posts = PostS.objects.all()
    return render(request, 'mainapp/story.html',{'posts':posts})

def music(request):
    return render(request, 'mainapp/music.html')

def illustration(request):
    return render(request, 'mainapp/illustration.html')

def library(request):
    return render(request, 'mainapp/library.html')

def detailS(request,id):
    post = get_object_or_404(PostS, id = id)
    all_comments = post.comments.all().order_by('created_at')
    comment_count = post.comments.count()
    return render(request,'mainapp/detailS.html', {'post':post, 'comments':all_comments, 'count':comment_count})

def createS(request):
    new_post = PostS()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('detailS',new_post.id)

def newS(request):
    return render(request, 'mainapp/newS.html')

def editS(request,id):
    edit_post = PostS.objects.get(id = id)
    return render(request, 'mainapp/editS.html', {'post' : edit_post})

def updateS(request,id):
    update_post = PostS.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    if request.FILES.get('image'):
        update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('detailS',update_post.id)

def deleteS(request, id):
    delete_post = PostS.objects.get(id = id)
    delete_post.delete()
    return redirect('story')

def moana(request):
    return render(request, 'mainapp/moana.html')

def Moonight(request):
    return render(request, 'mainapp/Moonight.html')

#Dream_Diary views
def newD(request):
    return render(request, 'mainapp/newD.html')

def detailD(request,id):
    post = get_object_or_404(PostD, id = id)
    return render(request,'mainapp/detailD.html', {'post':post})

def createD(request):
    new_post = PostD()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.created_at = timezone.now()
    new_post.text = request.POST['text']
    new_post.image = request.FILES['image']
    new_post.save()
    return redirect('detailD',new_post.id)

def editD(request,id):
    edit_post = PostD.objects.get(id = id)
    return render(request, 'mainapp/editD.html', {'post' : edit_post})

def updateD(request,id):
    update_post = PostD.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.created_at = timezone.now()
    update_post.text = request.POST['text']
    update_post.save()
    return redirect('detailD',update_post.id)

def deleteD(request, id):
    delete_post = PostD.objects.get(id = id)
    delete_post.delete()
    return redirect('blog')
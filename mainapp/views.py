from django.shortcuts import render,get_object_or_404, redirect
from .models import PostS
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
    return render(request,'mainapp/detailS.html', {'post':post})

def createS(request):
	new_post = PostS()
	new_post.title = request.POST['title']
	new_post.writer = request.POST['writer']
	new_post.pub_date = timezone.now()
	new_post.body = request.POST['body']
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
    update_post.writer = request.POST['writer']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
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
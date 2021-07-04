from django.http import request
from django.shortcuts import render,get_object_or_404, redirect
from .models import CommentI, CommentM, PostS, PostD, CommentS, PostI, PostM
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def blogsingle(request):
    return render(request, 'mainapp/blog-single.html')

def blog(request):
    posts = PostD.objects.all().order_by('-created_at')
    return render(request, 'mainapp/blog.html',{'posts':posts})

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

def library(request):
    return render(request, 'mainapp/library.html')

# dreamrelay_story start

def story(request):
    posts = PostS.objects.all()
    return render(request, 'mainapp/story.html',{'posts':posts})

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

def create_commentS(request, post_id):
	if request.method == "POST":
		post = get_object_or_404(PostS, pk=post_id)
		current_user = request.user
		comment_content = request.POST.get('content')
		CommentS.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('detailS', post_id)

def update_commentS(request, post_id, comment_id):
    post = get_object_or_404(PostS, id = post_id)
    update_comment = CommentS.objects.get(id = comment_id)
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('detailS',post.pk)

def edit_commentS(request, post_id, comment_id):
    post = get_object_or_404(PostS, id = post_id)
    edit_comment = CommentS.objects.get(id = comment_id)
    return render(request, 'mainapp/edit_commentS.html', {'post':post, 'comment' : edit_comment})

def delete_commentS(request, post_id, comment_id):
    post = get_object_or_404(PostS, pk=post_id)
    comment = get_object_or_404(CommentS, pk=comment_id)
    comment.delete()
    return redirect('detailS', post.pk)

#dreamrelay_story end

#dreamrelay_illustration

def illustration(request):
    posts = PostI.objects.all()
    return render(request, 'mainapp/illustration.html', {'posts':posts})

def detailI(request,id):
    post = get_object_or_404(PostI, id = id)
    all_comments = post.comments.all().order_by('created_at')
    comment_count = post.comments.count()
    return render(request,'mainapp/detailI.html', {'post':post, 'comments':all_comments, 'count':comment_count})

def createI(request):
    new_post = PostI()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('detailI',new_post.id)

def newI(request):
    return render(request, 'mainapp/newI.html')

def editI(request,id):
    edit_post = PostI.objects.get(id = id)
    return render(request, 'mainapp/editI.html', {'post' : edit_post})

def updateI(request,id):
    update_post = PostI.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    if request.FILES.get('image'):
        update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('detailI',update_post.id)

def deleteI(request, id):
    delete_post = PostI.objects.get(id = id)
    delete_post.delete()
    return redirect('illustration')

def create_commentI(request, post_id):
	if request.method == "POST":
		post = get_object_or_404(PostI, pk=post_id)
		current_user = request.user
		comment_content = request.POST.get('content')
		CommentI.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('detailI', post_id)

def update_commentI(request, post_id, comment_id):
    post = get_object_or_404(PostI, id = post_id)
    update_comment = CommentI.objects.get(id = comment_id)
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('detailI',post.pk)

def edit_commentI(request, post_id, comment_id):
    post = get_object_or_404(PostI, id = post_id)
    edit_comment = CommentI.objects.get(id = comment_id)
    return render(request, 'mainapp/edit_commentI.html', {'post':post, 'comment' : edit_comment})

def delete_commentI(request, post_id, comment_id):
    post = get_object_or_404(PostI, pk=post_id)
    comment = get_object_or_404(CommentI, pk=comment_id)
    comment.delete()
    return redirect('detailI', post.pk)

#dreamrelay_illustration end

# dreamrelay_music start

def music(request):
    posts = PostM.objects.all()
    return render(request, 'mainapp/music.html',{'posts':posts})

def detailM(request,id):
    post = get_object_or_404(PostM, id = id)
    all_comments = post.comments.all().order_by('created_at')
    comment_count = post.comments.count()
    return render(request,'mainapp/detailM.html', {'post':post, 'comments':all_comments, 'count':comment_count})

def createM(request):
    new_post = PostM()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('detailM',new_post.id)

def newM(request):
    return render(request, 'mainapp/newM.html')

def editM(request,id):
    edit_post = PostM.objects.get(id = id)
    return render(request, 'mainapp/editM.html', {'post' : edit_post})

def updateM(request,id):
    update_post = PostM.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    if request.FILES.get('image'):
        update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('detailM',update_post.id)

def deleteM(request, id):
    delete_post = PostM.objects.get(id = id)
    delete_post.delete()
    return redirect('music')

def create_commentM(request, post_id):
	if request.method == "POST":
		post = get_object_or_404(PostM, pk=post_id)
		current_user = request.user
		comment_content = request.POST.get('content')
		CommentM.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('detailM', post_id)

def update_commentM(request, post_id, comment_id):
    post = get_object_or_404(PostS, id = post_id)
    update_comment = CommentM.objects.get(id = comment_id)
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('detailM',post.pk)

def edit_commentM(request, post_id, comment_id):
    post = get_object_or_404(PostM, id = post_id)
    edit_comment = CommentM.objects.get(id = comment_id)
    return render(request, 'mainapp/edit_commentM.html', {'post':post, 'comment' : edit_comment})

def delete_commentM(request, post_id, comment_id):
    post = get_object_or_404(PostM, pk=post_id)
    comment = get_object_or_404(CommentM, pk=comment_id)
    comment.delete()
    return redirect('detailM', post.pk)

#dreamrelay_story end

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
    new_post.writer = request.user
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
    update_post.writer = request.user
    update_post.created_at = timezone.now()
    update_post.text = request.POST['text']
    update_post.save()
    return redirect('detailD',update_post.id)

def deleteD(request, id):
    delete_post = PostD.objects.get(id = id)
    delete_post.delete()
    return redirect('blog')
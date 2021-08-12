from django.http import request
from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.utils import timezone

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json 

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def blogsingle(request):
    return render(request, 'mainapp/blog-single.html')

def blog(request):
    user = request.user
    posts = PostD.objects.filter(writer = user).order_by('-created_at')
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
    if request.FILES.get('image'):
        update_comment.image = request.FILES.get('image')  #여원수정 
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
    if request.FILES.get('image'):
        update_comment.image = request.FILES.get('image')  #여원수정 
    update_comment.save()
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
    if request.FILES.get('image'):
        update_comment.image = request.FILES.get('image')  #여원수정 
    update_comment.save()
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
    new_post.image = request.FILES.get('image')
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

#꿈도서관
def library(request):
    storys = BlogS.objects.all()
    illusts = BlogI.objects.all()
    musics = BlogM.objects.all()
    return render(request, 'mainapp/library.html', {'storys':storys, 'illusts':illusts, 'musics':musics})

def detailSL(request, id):
    story = get_object_or_404(BlogS, id = id)
    return render(request,'mainapp/detailSL.html', {'story':story})

def createSL(request, id):
    post = PostS.objects.get(id = id)
    all_comments = post.comments.all().order_by('created_at')
    story_library = BlogS()
    story_library.title = post.title
    story_library.writer = post.writer
    story_library.pub_date = post.pub_date
    story_library.body = post.body
    story_library.image = post.image
    for nextstory in all_comments:
        story_library.comment = story_library.comment + " " + nextstory.content
    story_library.save()
    return redirect('detailSL', story_library.id)

def deleteSL(request, id):
    delete_post = BlogS.objects.get(id = id)
    delete_post.delete()
    return redirect('library')

def detailIL(request, id):
    illust = get_object_or_404(BlogI, id = id)
    return render(request,'mainapp/detailIL.html', {'illust':illust})

def createIL(request, id):
    post = PostI.objects.get(id = id)
    illust_library = BlogI()
    illust_library.title = post.title
    illust_library.writer = post.writer
    illust_library.pub_date = post.pub_date
    illust_library.body = post.body
    illust_library.image = post.image
    illust_library.save()
    return redirect('detailIL', illust_library.id)

def deleteIL(request, id):
    delete_post = BlogI.objects.get(id = id)
    delete_post.delete()
    return redirect('library')

def detailML(request, id):
    music = get_object_or_404(BlogM, id = id)
    return render(request,'mainapp/detailML.html', {'music':music})

def createML(request, id):
    post = PostM.objects.get(id = id)
    music_library = BlogM()
    music_library.title = post.title
    music_library.writer = post.writer
    music_library.pub_date = post.pub_date
    music_library.body = post.body
    music_library.image = post.image
    music_library.save()
    return redirect('detailML', music_library.id)

def deleteML(request, id):
    delete_post = BlogM.objects.get(id = id)
    delete_post.delete()
    return redirect('library')

#꿈거래소
def shop(request):
    products = Shop.objects.all()
    return render(request, 'mainapp/shop.html', {'products':products})

def detail_shop(request, id):
    product = get_object_or_404(Shop, id = id)
    all_comments = product.comment_sh.all().order_by('created_at')
    return render(request, 'mainapp/detail_shop.html', {'product':product, 'comment_sh':all_comments})

def new_shop(request):
    return render(request, 'mainapp/new_shop.html')

def create_shop(request):
    new_product = Shop()
    new_product.title = request.POST['title']
    new_product.writer = request.user
    new_product.pub_date = timezone.now()
    new_product.body = request.POST['body']
    new_product.save()
    return redirect('detail_shop', new_product.id)

def edit_shop(request, id):
    edit_product = Shop.objects.get(id = id)
    return render(request, 'mainapp/edit_shop.html', {'product' : edit_product})

def update_shop(request, id):
    update_product = Shop.objects.get(id=id)
    update_product.title = request.POST['title']
    update_product.writer = request.user
    update_product.pub_date = timezone.now()
    update_product.body = request.POST['body']
    update_product.save()
    return redirect('detail_shop', update_product.id)

def delete_shop(request, id):
    delete_product = Shop.objects.get(id = id)
    delete_product.delete()
    return redirect('shop')

def create_comment_sh(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Shop, pk=product_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment_sh.objects.create(content=comment_content, writer=current_user, product=product)
    return redirect('detail_shop', product_id)

def edit_comment_sh(request, comment_id):
    edit_comment_sh = Comment_sh.objects.get(id=comment_id)
    return render(request, 'mainapp/edit_comment_sh.html', {'comment':edit_comment_sh})

def update_comment_sh(request, comment_id):
    update_comment = Comment_sh.objects.get(id=comment_id)
    update_comment.content = request.POST.get('content')
    update_comment.save()
    return redirect('detail_shop', update_comment.product_id)

def delete_comment_sh(request, comment_id):
    delete_comment = Comment_sh.objects.get(id = comment_id)
    delete_comment.delete()
    return redirect('shop')


#like,DisLike

# @require_POST
# @login_required
# def like_toggle(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

#     if not post_like_created:
#         post_like.delete()
#         result = "like_cancel"
#     else:
#         result = "like"
    
#     context = {
#         "like_count":post.like_count,
#         "result":result
#     }

#     return HttpResponse(json.dumps(context), content_type="application/json")

# @require_POST
# @login_required
# def dislike_toggle(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

#     if not post_dislike_created:
#         post_dislike.delete()
#         result = "dislike_cancel"
#     else:
#         result = "dislike"
    
#     context = {
#         "dislike_count":post.dislike_count,
#         "result":result
#     }

#     return HttpResponse(json.dumps(context), content_type="application/json")

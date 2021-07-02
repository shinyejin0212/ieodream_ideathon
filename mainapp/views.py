from django.shortcuts import render

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
    return render(request, 'mainapp/story.html')

def music(request):
    return render(request, 'mainapp/music.html')

def illustration(request):
    return render(request, 'mainapp/illustration.html')

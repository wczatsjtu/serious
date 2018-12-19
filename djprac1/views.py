from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html', locals())


def detail(request, blog_id):

    return render(request, 'detail.html', locals())
from django.shortcuts import render
from django.http import HttpResponse
import json
from . import models
import markdown,pygments
# Create your views here.

def index(request):

    entries = models.Entry.objects.all()
    return render(request, 'index.html', locals())
    # data = {"a":3, "sdfsdf": "sdfsd"}
    # return HttpResponse(json.dumps(data))

def detail(request, blog_id):

    entry = models.Entry.objects.get(id=blog_id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    entry.body = md.convert(entry.body)
    entry.toc = md.toc
    entry.increase_visiting()
    return render(request, 'detail.html', locals())
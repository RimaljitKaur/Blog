from django.shortcuts import render,HttpResponse
from .models import *
from django.views import generic
from django.db.models import F
# Create your views here.

def index_view(request):
    queryset = Blog.objects.all()
    return render(request,'index.html',{'qs':queryset})

def archieve_view(request):
    queryset = Blog.objects.all()
    return render(request,'index.html',{'qs':queryset})

def content_view(request,pk):
    blog = Blog.objects.get(pk = pk)
    if blog:
        return render(request,'detail.html',{'blog':blog})
    else:
        return HttpResponse('Article does not exist.')

def form_view(request):
    if(request.method == 'POST'):
        b_title = request.POST.get('title')
        b_decp = request.POST.get('decp')
        b_content = request.POST.get('content')

        Blog.objects.create(
            title = b_title,
            description = b_decp,
            content = b_content
        )
    return render(request,'form.html')
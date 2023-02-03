from django.shortcuts import render,HttpResponse
from .models import *
from django.views import generic
from django.db.models import Q
from taggit.models import Tag
# Create your views here.

def index_view(request):
    queryset = Blog.objects.all()
    return render(request,'index.html',{'qs':queryset})

def archieve_view(request):
    queryset = Blog.objects.all()
    date_list = []
    month_list = []
    count_list =[]
    datadict = {}

    for i in queryset:
        year = i.published_on.year
        date_list.append(year)
    date_list = list(set(date_list))

    for i in queryset:
        if i.published_on.year in date_list:
            month_list.append(i.published_on.month)
    month_list = list(set(month_list))
    print(month_list)

    for i in date_list:
        for j in month_list:
            data = Blog.objects.filter(published_on__year=2023)
            datadict[i] = {j:data}

    print(datadict)
    return render(request,'archieve.html',context={'years':date_list,'months':month_list})

def content_view(request,pk):
    blog = Blog.objects.get(pk = pk)
    if blog:
        return render(request,'detail.html',{'blog':blog})
    else:
        return HttpResponse('Article does not exist.')
    
def tag_post_view(request,tag):
    posts = Blog.objects.filter(tags__name__in=[tag])
    if posts:
        return render(request,'tagpost.html',{'post':posts})
    else:
        return HttpResponse('Articles does not exist.')

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

def about_view(request):
    return render(request,'about.html')

def tags_view(request):
    tags = Tag.objects.all()
    return render(request,'tags.html',{'tags':tags})

def project_view(request):
    return render(request,'projects.html')

def talk_view(request):
    return render(request,'talks.html')
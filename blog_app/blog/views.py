from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import Http404
# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    return render(request,'blog/post/list.html',{'posts':posts})

def post_details(request,id):
    #الطريقة الاولى 
    # try:
    #     post=Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Not Post found.")
    # return render(request,'blog/post/detail.html',{'post':post})
        
    #الطريقة الثانية 
    # يوجد شرطين 
    post=get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    return render(request,'blog/post/detail.html',{'post':post})
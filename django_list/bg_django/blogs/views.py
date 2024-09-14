from django.shortcuts import render
from django.http import HttpResponse

defaultBlogs =[
    {'id':1,"title":"blog 1","desc":"dEScription 1"},
    {'id':2,"title":"blog 2","desc":"dEScription 2"},
    {'id':3,"title":"blog 3","desc":"dEScription 3"},
    {'id':4,"title":"blog 4","desc":"dEScription 4"},
]

# Create your views here.
def getBlogList(request):
    blogContext = {'blogs':defaultBlogs};
    # return  HttpResponse("This is blog page")
    return  render(request,'blog_pages/blogs.html',context=blogContext)
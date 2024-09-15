from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog
from . import forms
from django.contrib import messages

defaultBlogs =[
    {'id':1,"title":"blog 1","desc":"dEScription 1"},
    {'id':2,"title":"blog 2","desc":"dEScription 2"},
    {'id':3,"title":"blog 3","desc":"dEScription 3"},
    {'id':4,"title":"blog 4","desc":"dEScription 4"},
]

# Create your views here.
def getBlogList(request):
    blogs = Blog.objects.all()
    print(blogs)

    blogContext = {'blogs':blogs}
    # return  HttpResponse("This is blog page")
    return  render(request,'blog_pages/blogs.html',context=blogContext)

def getBlogById(request,blog_id):
    blog = Blog.objects.all();
    print(blog)
    blogContext = {
        'blog': {
            'id': blog_id
        }
    }
    return render(request,'blog_pages/singleBlog.html',context=blogContext)

def createBlog(request):
    if request.method == 'POST':
        blogForm = forms.BlogRegistration(request.POST)

        if blogForm.is_valid():
            blog_data = blogForm.cleaned_data
            print(blog_data)
            # Add a success message to notify the user
            messages.success(request, "Blog created successfully!")

            blogContext = {
                'blog': {
                    'id': 1112121
                }
            }
            return render(request,'blog_pages/singleBlog.html',context=blogContext)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
         # When the page is accessed initially (GET request)
        blogForm = forms.BlogRegistration()

    blogForm.order_fields(field_order=['blog_id','name','email'])
    return render(request,'blog_pages/createBlogForm.html',{"blogForm":blogForm})
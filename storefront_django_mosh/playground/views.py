from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello Django!')
    userData = {
        'name':"Mr. Denial",
        'email':"denial@mail.com",
        'age': 29
    }
    return render(request,'hello.html',userData)
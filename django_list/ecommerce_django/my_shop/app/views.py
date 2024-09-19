from django.shortcuts import render
from django.views import View
from .models import Product
from django.db.models import Count
from .forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.
def home(req):
    return render(request=req,template_name='app/home.html')
def AboutUs(req):
    return render(request=req,template_name='app/about.html')

class CategoryView(View):
    def get(self,request,category_name):
        print(category_name)
        products = Product.objects.filter(category=category_name)
        titles = Product.objects.filter(category=category_name).values('title').annotate(total=Count('title'))

        ctxData = {
            'category': category_name,
            'products':products,
            'titles': titles
        }
        return render(request,template_name='app/category.html',context=ctxData)


class ProductDetailsView(View):
    def get(self,request,product_id):
        product = Product.objects.get(pk=product_id)
        ctxData = {
            'product': product,
        }
        return render(request,template_name='app/ProductDetails.html',context=ctxData)


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        ctxData = {
            'form': form
        }
        return render(request,template_name='app/CustomerRegistration.html',context=ctxData)

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations! User Register Successfully')
        else:
            messages.warning(request,'Invalid input data')

        ctxData = {
            'form': form
        }
        return render(request,template_name='app/CustomerRegistration.html',context=ctxData)

# class LoginView(View):
#     def get(self,request):
#         form = CustomerRegistrationForm()
#         ctxData = {
#             'form': form
#         }
#         return render(request,template_name='app/Login.html',context=ctxData)
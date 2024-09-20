
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm

# need the static media url if we want to show image from media folder after upload
urlpatterns = [
    path('', views.home),
    path('about', views.AboutUs),
    path('categories/<slug:category_name>', views.CategoryView.as_view(),name='category'),
    path('product_details/<int:product_id>', views.ProductDetailsView.as_view(),name='product_details'),

    # login authentication
    path('registration/', views.CustomerRegistrationView.as_view(),name='registration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

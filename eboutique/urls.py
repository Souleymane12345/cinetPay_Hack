"""eboutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontoffice import views
from django.conf import settings
from django.conf.urls.static import static
#import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('xadmin/', xadmin.site.urls),
    #path('', views.login, name="login"),
    #path('register/', views.register, name="register"),
    #path('login/', views.login_, name="login_"),
    #path('signup/', views.signup, name="signup"),
    #path('cart/<int:id>/', views.cart, name="cart"),
    #path('add_cart/<int:id>/', views.add_cart, name="add_cart"),
    path('', views.cinetpay_login, name="cinetpay_login"),
    path('cinetpay_index/<int:id>/', views.add_cart, name="cinetpay_index"),
    path('cinetpay_cart/<int:id>/', views.cart, name="cinetpay_cart"),
    path('cinetpay_login/', views.login_, name="cinetpay_login"),
    path('cinetpay_register/', views.signup, name="cinetpay_register"),
    path('cinetpay_about/', views.cinetpay_about, name="cinetpay_about"),
    path('cinetpay_failed/', views.cinetpay_failed, name="cinetpay_failed"),
    path('cinetpay_succed/', views.cinetpay_succed, name="cinetpay_succed"),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

import os
from dotenv import load_dotenv 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from backoffice.models import *
from cinetpay_sdk.s_d_k import Cinetpay
import uuid

# Create your views here.


"""
def login(request):
    return render(request, 'pages/login.html', locals())

def register(request):
    return render(request, 'pages/register.html', locals())
"""

def signup(request):
    
    if request.method == "POST":
        
        if request.POST['password'] == request.POST['password1']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'pages/cinetpay_register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                
                user = User.objects.create_user(username= request.POST['username'],password = request.POST['password'],email = request.POST['email'],first_name = request.POST['first_name'],last_name = request.POST['last_name'])
                auth.login(request,user)
                product = Product.objects.get()
                return render(request,'pages/cinetpay_index.html',locals())
        else:
            return render (request,'pages/cinetpay_register.html', {'error':'Password does not match!'})
    else:
        return render(request,'pages/cinetpay_register.html')

def login_(request):
    
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        
        if user is not None:
            auth.login(request,user)
            #return redirect('home')
            product = Product.objects.all()
            return render(request,'pages/cinetpay_index.html',locals())
        else:
            #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            return render (request,'pages/cinetpay_login.html', {'error':'Username or password is incorrect!'})
    else:
        #print('gsaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
        return render(request,'pages/cinetpay_login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    #return redirect('home')
    return render(request,'pages/login.html')

def add_cart(request,id):
    if request.method == 'POST':
        panier_data = Panier()
        panier_data.id_client = id
        panier_data.id_produit = request.POST.get("send_cart")
        paneir_id_produit = request.POST.get("send_cart")
        #print('paneir_id_produit',request.POST.get("send_cart"))
        #panier_data.save()
        user = User.objects.get(pk=id)
        ##print('user',user.id)
        #product = Product.objects.get()
        id_string = panier_data.id_produit
        if id_string is not None:
            ids = [int(id) for id in id_string.split(',')]
            product =  Product.objects.filter(id__in=ids)
            return render(request, 'pages/cinetpay_cart.html', locals())

    return render(request, 'pages/cinetpay_index.html', locals())


def cart(request,id):

    load_dotenv()
    apikey = os.environ['apikey']
    site_id = os.environ['site_id']
    data = { 
        'transaction_id': 'YOUR_TRANSACTION_D',
        'amount': 100,
        'currency': 'XOF',
        'channels': 'ALL',
        'description': 'YOUR_PAYMENT_DESCRIPTION',
        'customer_name':"",#Le nom du client
        'customer_surname':"",#Le prenom du client
        'customer_email': "",#l'email du client
        'customer_phone_number': "",#l'email du client
        'customer_address' : "",#addresse du client
        'customer_city': "",#La ville du client
        'customer_country' : "",# le code ISO du pays
        'customer_state' : "",# le code ISO l'état
        'return_url':'http://127.0.0.1:8000/cart/',
        'notify_url':'http://127.0.0.1:8000/shop/',
        'customer_zip_code' : "", # code postal       
    } 
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        client_id = Client.objects.get(pk=id)
        


        data['transaction_id'] = uuid.uuid4()
        data['customer_name'] = user.first_name
        data['customer_surname'] = user.last_name
        data['customer_email'] = user.email
        data['customer_phone_number'] = client_id.customer_phone_number
        data['customer_address'] = client_id.customer_address
        data['customer_city'] = client_id.customer_city
        data['customer_country'] = client_id.customer_country
        data['customer_state'] = client_id.customer_state
        data['customer_zip_code'] = client_id.customer_zip_code

        client = Cinetpay(apikey,site_id)
        pay_data = client.PaymentInitialization(data)
        print(pay_data['data']['payment_url'])
        return redirect(pay_data['data']['payment_url'])
















        """


    client = Cinetpay(apikey,site_id)
    data = { 
        'transaction_id': 'YOUR_TRANSACTION_ID',
        'amount': 100,
        'currency': 'XOF',
        'channels': 'ALL',
        'description': 'YOUR_PAYMENT_DESCRIPTION',
        'customer_name':"Joe",#Le nom du client
        'customer_surname':"Down",#Le prenom du client
        'customer_email': "down@test.com",#l'email du client
        'customer_phone_number': "088767611",#l'email du client
        'customer_address' : "BP 0024",#addresse du client
        'customer_city': "Antananarivo",#La ville du client
        'customer_country' : "CM",# le code ISO du pays
        'customer_state' : "CM",# le code ISO l'état
        'return_url':'http://127.0.0.1:8000/cart/',
        'notify_url':'http://127.0.0.1:8000/shop/',
        'customer_zip_code' : "06510", # code postal       
    }  
    pay_data = client.PaymentInitialization(data)
    print(pay_data['data']['payment_url'])
    return redirect(pay_data['data']['payment_url'])
    """
    #return render(request, 'pages/cart.html')
"""
"""

def cinetpay_index (request):
    return render(request, 'pages/cinetpay_index.html', locals())

def cinetpay_login (request):
    return render(request, 'pages/cinetpay_login.html', locals())

def cinetpay_register (request):
    return render(request, 'pages/cinetpay_register.html', locals())

def cinetpay_about (request):
    return render(request, 'pages/cinetpay_about.html', locals())

def cinetpay_failed (request):
    return render(request, 'pages/cinetpay_failed.html', locals())

def cinetpay_succed (request):
    return render(request, 'pages/cinetpay_succed.html', locals())

def cinetpay_cart (request):
    return render(request, 'pages/cinetpay_cart.html', locals())




"""
import os
from dotenv import load_dotenv 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from backoffice.models import *
from cinetpay_sdk.s_d_k import Cinetpay

# Create your views here.



def login(request):
    return render(request, 'pages/login.html', locals())

def register(request):
    return render(request, 'pages/register.html', locals())


def signup(request):
    
    if request.method == "POST":
        
        if request.POST['password'] == request.POST['password1']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'pages/register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                
                user = User.objects.create_user(username= request.POST['username'],password = request.POST['password'],email = request.POST['email'],first_name = request.POST['first_name'],last_name = request.POST['last_name'])
                auth.login(request,user)
                product = Product.objects.get()
                return render(request,'pages/shop.html',locals())
        else:
            return render (request,'pages/register.html', {'error':'Password does not match!'})
    else:
        return render(request,'pages/register.html')

def login_(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        
        if user is not None:
            auth.login(request,user)
            #return redirect('home')
            product = Product.objects.all()
            return render(request,'pages/shop.html',locals())
        else:
            #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            return render (request,'pages/register.html', {'error':'Username or password is incorrect!'})
    else:
        #print('gsaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
        return render(request,'pages/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    #return redirect('home')
    return render(request,'pages/login.html')

def add_cart(request,id):
    if request.method == 'POST':
        panier_data = Panier()
        panier_data.id_client = id
        panier_data.id_produit = request.POST.get("send_cart")
        paneir_id_produit = request.POST.get("send_cart")
        #print('paneir_id_produit',request.POST.get("send_cart"))
        #panier_data.save()
        user = User.objects.get(pk=id)
        ##print('user',user.id)
        #product = Product.objects.get()
        id_string = panier_data.id_produit
        if id_string is not None:
            ids = [int(id) for id in id_string.split(',')]
            product =  Product.objects.filter(id__in=ids)
            return render(request, 'pages/cart.html', locals())

    return render(request, 'pages/shop.html', locals())


def cart(request,id):

    load_dotenv()
    apikey = os.environ['apikey']
    site_id = os.environ['site_id']
    data = { 
        'transaction_id': 'YOUR_TRANSACTION_D',
        'amount': 100,
        'currency': 'XOF',
        'channels': 'ALL',
        'description': 'YOUR_PAYMENT_DESCRIPTION',
        'customer_name':"",#Le nom du client
        'customer_surname':"",#Le prenom du client
        'customer_email': "",#l'email du client
        'customer_phone_number': "",#l'email du client
        'customer_address' : "",#addresse du client
        'customer_city': "",#La ville du client
        'customer_country' : "",# le code ISO du pays
        'customer_state' : "",# le code ISO l'état
        'return_url':'http://127.0.0.1:8000/cart/',
        'notify_url':'http://127.0.0.1:8000/shop/',
        'customer_zip_code' : "", # code postal       
    } 
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        client_id = Client.objects.get(pk=id)
        data['customer_name'] = user.first_name
        data['customer_surname'] = user.last_name
        data['customer_email'] = user.email
        data['customer_phone_number'] = client_id.customer_phone_number
        data['customer_address'] = client_id.customer_address
        data['customer_city'] = client_id.customer_city
        data['customer_country'] = client_id.customer_country
        data['customer_state'] = client_id.customer_state
        data['customer_zip_code'] = client_id.customer_zip_code

        client = Cinetpay(apikey,site_id)
        pay_data = client.PaymentInitialization(data)
        print(pay_data['data']['payment_url'])
        return redirect(pay_data['data']['payment_url'])
       


    client = Cinetpay(apikey,site_id)
    data = { 
        'transaction_id': 'YOUR_TRANSACTION_ID',
        'amount': 100,
        'currency': 'XOF',
        'channels': 'ALL',
        'description': 'YOUR_PAYMENT_DESCRIPTION',
        'customer_name':"Joe",#Le nom du client
        'customer_surname':"Down",#Le prenom du client
        'customer_email': "down@test.com",#l'email du client
        'customer_phone_number': "088767611",#l'email du client
        'customer_address' : "BP 0024",#addresse du client
        'customer_city': "Antananarivo",#La ville du client
        'customer_country' : "CM",# le code ISO du pays
        'customer_state' : "CM",# le code ISO l'état
        'return_url':'http://127.0.0.1:8000/cart/',
        'notify_url':'http://127.0.0.1:8000/shop/',
        'customer_zip_code' : "06510", # code postal       
    }  
    pay_data = client.PaymentInitialization(data)
    print(pay_data['data']['payment_url'])
    return redirect(pay_data['data']['payment_url'])
    """
    #return render(request, 'pages/cart.html')
"""
"""

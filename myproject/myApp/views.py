from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myApp/index.html')

def about(request):
        return render(request, 'myApp/about.html')

def blog(request):
    return render(request, 'myApp/blog.html')

def cart(request):
    return render(request, 'myApp/cart.html')

def shop(request):
    return render(request, 'myApp/shop.html')

def thankyou(request):
    return render(request, 'myApp/thankyou.html')

def services(request):
    return render(request, 'myApp/services.html')

def checkout(request):
    return render(request, 'myApp/checkout.html')

def contact(request):
    return render(request, 'myApp/contact.html')
    
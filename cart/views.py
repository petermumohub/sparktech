from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart,CartItem,Order
from shop.models import Product
from .forms import CheckoutForm
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.models import User




def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(session_key=session_key, defaults={'user': request.user if request.user.is_authenticated else None})

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if not request.session.session_key:
        return redirect('view_cart')
    session_key = request.session.session_key

    try:
        cart_item = CartItem.objects.get(cart__session_key=session_key, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('view_cart')

def view_cart(request):
    if not request.session.session_key:
        return render(request, 'cart/cart.html', {'cart': None})

    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key, defaults={'user': request.user if request.user.is_authenticated else None})
    
    return render(request, 'cart/cart.html', {'cart': cart})

def checkout(request):
    if not request.session.session_key:
        return redirect('view_cart')

    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key, defaults={'user': request.user if request.user.is_authenticated else None})

    if request.method == 'POST':
        cart.delete()
        return redirect('home')

    return render(request, 'cart/checkout.html', {'cart': cart})

def order_success(request):
    return render(request, 'cart/checkout.html')



def complete_purchase(request):
    
    cart = get_object_or_404(Cart, session_key=request.session.session_key)

    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    street_address = request.POST.get('street_address')
    city = request.POST.get('city')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    payment_method = request.POST.get('payment_method')

    
    user = request.user if request.user.is_authenticated else None  

   
    order = Order.objects.create(
        user=user,  
        first_name=first_name,
        last_name=last_name,
        street_address=street_address,
        city=city,
        phone=phone,
        email=email,
        payment_method=payment_method,
        total_price=cart.total_price(), 
    )

    
    order.items.clear()  

    
    for item in cart.cartitem_set.all():
        order.items.add(item.product)

   
    order.save()

    
    return redirect('order_success')
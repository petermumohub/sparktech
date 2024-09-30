from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.shortcuts import render,get_object_or_404,redirect  

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    

    def __str__(self):
        return f"Cart {self.id} - User: {self.user} - Session: {self.session_key}"

    def total_price(self):
        return sum(item.total_price() for item in self.cartitem_set.all())
    
    def cart_view(request):
        cart = None
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            session_key = request.session.session_key
            cart = Cart.objects.get(session_key=session_key)
    
        context = {
        'cart': cart,
        }
    
        return render (request, 'checkout.html', context)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return f"{self.product.name} in cart of {self.cart.user.username}"

    def total_price(self):
        return self.product.price *self.quantity
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    payment_method = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField(Product)

    def __str__(self):
        return f"Order by {self.first_name} {self.last_name}"    
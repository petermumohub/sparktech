from django.shortcuts import render,get_object_or_404
from shop.models import Product
from contact.forms import SubscriberForm
from .forms import Searchform
from django.db.models import Q
from shop.models import Category
 
def home_page(request):
    products = Product.objects.all()[:12]
    forms = SubscriberForm()
    if request.method == 'POST':
        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'products': products,
        'forms': forms
    }
    return render(request, 'home.html', context)

def search(request):
    form=Searchform()
    results=[]
    if 'query' in request.GET:
        form=Searchform(request.GET)
        if form.is_valid():
            query=form.cleaned_data['query']
            results=Product.objects.filter( Q(name__icontains=query) | Q(brand__icontains=query))
            context={'form':form,'results':results}
    return render(request,'new.html',{'form':form,'results':results})

def privacy_policy(request):
    return render (request,'Items/privacy_policy.html')

def return_policy(request):
    return render (request,'Items/return_policy.html')

def shipping_policy(request):
    return render (request,'Items/shipping.html')
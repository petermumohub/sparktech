from django.shortcuts import render,get_object_or_404
from .models import Category, Product
from django.db.models import Q
from.utils import calculate_discounted_price
 


'''
    # Get or create appliances category
    appliances_category, created = Category.objects.get_or_create(name='Garment Care', photo=None)

    # Check if air fryer already exists before creating it
    air_fryer, created = Product.objects.get_or_create(
        name='STEAM IRON',
        brand='PHILIPS',
        category=appliances_category,
        defaults={
            'photo': 'bg20.jpg',
            'price': 18540,
            'details': 'LED FLOODLIGHT 50W LED43/CW 4300 LUMEN GREY',
            'is_draft': False,
            'inventory': 125
        }
    )


    j=Product.objects.filter(id=)
    j.delete()

'''
'''Televisions_category, created = Category.objects.get_or_create(name='Hisense Tvs', photo=None)
Hisense_43_smart_A6, created = Product.objects.get_or_create(
        name='Hisense 43 Inch Smart A6',
        brand='Hisense',
        category=Televisions_category,
        defaults={
            'photo': 'sharp.jpg',
            'price': 36000,
            'details': 'Smart'
                        'Bluetooth'
                        'Wi-Fi',
            'is_draft': False,
            'inventory': 125
        }
    )'''

def shop_page(request):

    products = Product.objects.filter(is_draft=False)
    categories = Category.objects.all()
    unique_category_names = []
    for category in categories:
        if category not in unique_category_names:
            unique_category_names.append(category.name)

    context = {
        'unique_category_names': set(unique_category_names),
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/shop.html', context)



def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(category__name=product_details.category.name).exclude(id=product_id)
    
    for product in related_products:
        product.new_price=product.price * 1.03
    context = {
        'product': product_details,
        'related_products': related_products,
        
    }
    return render(request, 'shop/product-details.html', context)


def discounted(request):
    product_ids=[11,1,19]

    products=Product.objects.filter(id__in=product_ids)

    discounted_prices=[]


    for product in products:
        discounted_price=calculate_discounted_price(product.price,20)
        discounted_prices.append(discounted_price)

    context= {
        'products': (products,discounted_prices)
    }    

    return render(request, 'shop/product-details.html', context)



def wishlist(request):
    return render(request, 'shop/wishlist.html')

def hisense_tvs(request):
    hisenses=Product.objects.filter(brand='HISENSE',category__name='Televisions')
    return render(request,'items/tvs/hisense.html',{'hisenses':hisenses})

def tcl_tvs(request):
    tcls= Product.objects.filter(brand='tcl',category__name='Televisions')
    return render(request,'items/tvs/tcl.html',{'tcls':tcls})

def all_brands(request):
    products= Product.objects.filter(category__name='Televisions')
    return render(request,'items/tvs.html',{'products':products})


def category_view(request,category_name):
    categorys=get_object_or_404(Category,name=category_name)
    products=Product.objects.filter(category=categorys)
    return render(request,'shop/shop.html',{'category':categorys,'products':products})


def tvs_by_brand(request,brand):
    products=Product.objects.filter(brand=brand.upper(),category__name= 'Televisions')
    return render(request,'items/tvs.html', {'products':products})

def TV_Accessories(request,name):
    products= Product.objects.filter(name=name,subcategory__name= 'TV Accessories')
    return render (request,'items/tvs.html',{'products':products})


def Audio_systems(request,subcategory):
    products=Product.objects.filter(subcategory__name=subcategory,category__name= 'Audio')
    return render(request,'items/tvs.html', {'products':products})

def audio_systems_by_price(request,min_price=None,max_price=None):
    products=Product.objects.filter(price__gte=min_price,price__lte=max_price,category__name='Audio')
    return render (request,'items/tvs.html',{'products':products})

def home_appliances(request,subcategory):
    products=Product.objects.filter(subcategory__name=subcategory,category__name='Home Appliances')
    return render (request,'Items/tvs.html',{'products':products})

def phones_tablets(request,subcategory):
    products=Product.objects.filter(subcategory__name=subcategory,category__name='Phones & Tablets')
    return render(request,'items/tvs.html',{'products':products})




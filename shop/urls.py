from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_page, name='shop'),
    path('hisense-tvs/', views.hisense_tvs, name='hisense_tvs'),
    path('tcl-tvs/', views.tcl_tvs, name='tcl_tvs'),
    path('all-brands/', views.all_brands, name='all_brands'),
    path('product/<product_id>', views.product_details, name='product-details'),
    path('shop/<int:category_id>/', views.shop_page, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('tvs/<str:brand>/', views.tvs_by_brand, name='tvs_by_brand'),
    path('Audio/<str:subcategory>/', views.Audio_systems, name='audio_systems'),
    path('TV/<str:name>/', views.TV_Accessories, name='TV_Accessories'),
    path('audio/price/<int:min_price>/<int:max_price>/', views.audio_systems_by_price, name='audio_systems_by_price'),
    path('category/<str:category_name>/', views.category_view, name='category_detail'),
    path('phones/<str:subcategory>/', views.phones_tablets, name='phones_tablets'),
    path('Home/<str:subcategory>/', views.home_appliances, name='home_appliances'),
]


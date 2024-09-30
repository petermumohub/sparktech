from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    name=models.CharField(max_length= 30)
    date=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand=models.TextField(default = '')
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.SET_NULL,null=True,blank=True)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
     

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return f"Image for {self.product.name}"
        
    
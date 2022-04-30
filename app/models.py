from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MaxValueValidator

STATE_CHOICES=(
    (' west bengal','west bengal'),
    ('assam','assam'),
    ('bihar','bihar'),
    ('orisha','orisha')
)

class Costomar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=70)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    # def __str__(self):
    #     return str(self.id)

CATAGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('H','headphone'),
    ('TW','Top wear'),
    ('BW','Bottom Wear')
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    catagory=models.CharField(choices=CATAGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='img')
    # def __str__(self):
    #     return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quality=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quality * self.Product.discount_price


STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customar=models.ForeignKey(Costomar,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=50 ,default='pending')
    # def __str__(self):
    #     return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.Product.discount_price


# class CostomarProfile(models.Model):
#     class Meta:
#         model=Costomar
#         fields=['name','location','city','state','zipcode']

from django.shortcuts import render,HttpResponse,redirect
from .models import Cart,Costomar,Product,OrderPlaced
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import auth,User
from .form import CastomarRegistationForm,LoginForm,MyPasswordChange,CostomarProfile
from django.db.models import Q
from django.http import JsonResponse



# from django.utils.translation import gettext,gettext_lazy as _
# from django.contrib.auth.forms import UserCreationForm   ,AuthenticationForm ,UsernameField,PasswordChangeForm





class Productview(View):
    def get(self,request):

        topwear=Product.objects.filter(catagory='TW')
        buttom_wear=Product.objects.filter(catagory='BW')
        mobiles=Product.objects.filter(catagory='M')
        laptops=Product.objects.filter(catagory='L')
        headphone=Product.objects.filter(catagory='H')
        

        return render(request, 'app/home.html',{'topwear':topwear,'buttom_wear':buttom_wear,'mobiles':mobiles,'laptops':laptops,'headphone':headphone})

def product_detail(request,pk):
# class product_detail(View):
#     def get(self,request,pk):

        product=Product.objects.get(pk=pk)
        item_already_in_cart=False
        item_already_in_cart=Cart.objects.filter(Q(Product=product) & Q(user=request.user))
        print(item_already_in_cart)


        return render(request, 'app/productdetail.html',{'product':product ,'item_already_in_cart':item_already_in_cart})

def add_to_cart(request):
    if request.user.is_authenticated == False :
        return redirect ('login')

    user=request.user
    product_id=request.GET.get('product_id')
    product=Product.objects.get(id=product_id)
    add_cart=Cart(user=user,Product=product)
    add_cart.save()

    return redirect ('/cart')

def show_cart(request):
    if request.user.is_authenticated == False :
        return redirect ('login')   
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==user]
    if cart_product:
        for p in cart_product:
            Pamount=(p.quality * p.Product.discount_price)
            amount= amount + Pamount
            totalAmount= amount+shipping_amount
        return render(request, 'app/addtocart.html',{'carts':cart,'totalAmount':totalAmount,'amount':amount})
    else:
        return render(request,'app/emptycart.html')


def buy_now(request):
    if request.user.is_authenticated == False :
        return redirect ('login') 
    return render(request, 'app/buynow.html')






def change_password(request):
    if request.user.is_authenticated == False :
        return redirect ('login')    
    if request.method=='POST':
        fm=MyPasswordChange(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return redirect ('/')
    else:
        fm=MyPasswordChange(user=request.user)
        # username=request.POST['username']
        # password=request.POST['password']
        # if username !=None and password != None:       
        # u = fm.objects.get(username=username)
        # u.set_password(password)
        # u.save()
    
    return render(request, 'app/passwordchange.html',{'form':fm})

def mobile(request ,data=None):
    if data==None:
        mobiles=Product.objects.filter(catagory='M')
    elif data=='redmi' or data== 'vivo'  or data =='realmi':
        mobiles=Product.objects.filter(catagory='M').filter(brand=data)
    

    return render(request, 'app/mobile.html',{'mobiles':mobiles})

#-------------------  common process =-------------
# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         if username !=None and password != None:

#             user=auth.authenticate(username=username,password=password)
            
                
#             if user is not None:
#                 auth.login(request,user)
#                 return redirect('profile')
#             else:
#                 return HttpResponse('login faild')
#         else:
#             return HttpResponse('missing ')
 
#     else:
#         return render(request,'user/login.html')

#------------common process end --------------


def login(request):
    if request.method == 'POST':
        forms=LoginForm(request=request,data=request.POST)
        if forms.is_valid():
            username=forms.cleaned_data['username']
            password=forms.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                return HttpResponse('problem')
        else:
            return redirect('/login')  

    else:

        forms=LoginForm()
        return render(request, 'app/login.html',{'forms':forms})

# class customerregistrationview(View):
#     def get(self,request):
#         forms=CastomarRegistationForm()
#         return render(request, 'app/customerregistration.html',{'fm':forms}) 
#     def post(self,request):
#         forms=CastomarRegistationForm(request.POST)
#         if forms.is_valid:
#             forms.save
#             print(forms)
#             return HttpResponse('data save')

            
#         return render(request, 'app/customerregistration.html',{'fm':forms})


def logout(request):
    auth.logout(request)
    return redirect('/login')





def customerregistration(request):
    if request.method=='POST':
        form=CastomarRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data save')
        
        return render(request, 'app/customerregistration.html',{'fm':form})
    else:
        form=CastomarRegistationForm()
        return render(request, 'app/customerregistration.html',{'fm':form})







def checkout(request):
    if request.user.is_authenticated == False :
        return redirect ('login')   
    user=request.user
    add=Costomar.objects.filter(user=user)
    cart_item=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==user]
    if cart_product:
        for p in cart_product:
            Pamount=(p.quality * p.Product.discount_price)
            amount= amount + Pamount
        totalAmount= amount+shipping_amount

    return render(request, 'app/checkout.html',{'add':add,'totalAmount':totalAmount,'cart':cart_item})



      
    
def profile(request):
    if request.user.is_authenticated == False :
        return redirect ('login')   
    if request.method=='POST':
        fm=CostomarProfile(request.POST)
        if fm.is_valid():
            user=request.user
            name=fm.cleaned_data['name']
            location=fm.cleaned_data['location']
            city=fm.cleaned_data['city']
            state=fm.cleaned_data['state']
            zipcode=fm.cleaned_data['zipcode']
            reg=Costomar(user=user,name=name,location=location,city=city,state=state,zipcode=zipcode)
            reg.save()
        

    fm=CostomarProfile()
    return render(request,'app/profile.html',{'form':fm})


def address(request):
    if request.user.is_authenticated == False :
        return redirect ('login')   
    add=Costomar.objects.filter(user=request.user)

    return render(request, 'app/address.html',{'add':add})

def paymentDone(request):
    if request.user.is_authenticated == False :
        return redirect ('login')   
    user=request.user
    custid=request.GET.get('custid')
    costomar=Costomar.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customar=costomar,Product=c.Product,quantity=c.quality).save()
        c.delete()
    return redirect('orders')

def orders(request):
    if request.user.is_authenticated == False :
        return redirect ('login')   
    op=OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'op':op})

##-----------------
def plus_cart(request,pk):
    if request.method=='GET':

        # prod_id=request.GET['prod_id']
        product=Product.objects.get(pk=pk)
        user=request.user
        print(product)
        print(user)
        c=Cart.objects.get( Q(Product=product) & Q(user=user) )
        # if c.quality >= 1:
        c.quality+=1
        c.save()
        
        return JsonResponse({'product_price': product.discount_price})

def minus_cart(request,pk):
    if request.method=='GET':

        # prod_id=request.GET['prod_id']
        product=Product.objects.get(pk=pk)
        user=request.user
        print(product)
        print(user)
        c=Cart.objects.get( Q(Product=product) & Q(user=user) )
        if c.quality >=1:
            c.quality-=1
            c.save()
        
        return JsonResponse({'product_price': product.discount_price})

def remove_cart(request,pk):
    if request.method=='GET':
        product=Product.objects.get(pk=pk)
        user=request.user
        print(product)
        print(user)
        c=Cart.objects.get( Q(Product=product) & Q(user=user) )
       
        c.delete()
        return JsonResponse({'product_price': product.discount_price})


    

from django.urls import path
from app import views
from django.contrib.auth import views as auth_view
from .form import LoginForm
urlpatterns = [
    # path('', views.home),
    path('',views.Productview.as_view(),name="home"),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    # path('product-detail/<int:pk>',views.product_detail.as_view(),name="product_detail"),

    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),


    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('passwordchange/',views.change_password,name='passwordchange'),

    path('login/', views.login, name='login'),
    # path('login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    
    
    path('registration/', views.customerregistration, name='customerregistration'),
    path('logout/',views.logout,name='logout'),

    # path('registration/', views.customerregistrationview.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentDone/',views.paymentDone, name='paymentDone'),

    path('pluscart/<int:pk>',views.plus_cart, name='pluscart'),
    path('minuscart/<int:pk>',views.minus_cart, name='minus_cart'),
    path('removecart/<int:pk>',views.remove_cart,name='remove_cart'),

    
]

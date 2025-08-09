from django.urls import path
from . import views
urlpatterns = [
    path('', views.shoplist, name='shoplist'),
    path('<int:pk>/', views.shopdetail, name='shopdetail'),
    path('mypage/', views.shopmyPage, name='mypage'),
    path('create/', views.create, name='itemcreate'),
    path('top/', views.top, name='top'),
    path('bottom/', views.bottom, name='bottom'),
    path('outer/', views.outer, name='outer'),
    path('etc/', views.etc, name='etc'),
    path('shoes/',views.shoes,name='shoes'),
    path('search/', views.search, name='search'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('mypage/order_status/', views.order_status, name='order_status'),
    path('mypage/order_history/', views.order_history, name='order_history'),
    path('mypage/wishlist/', views.wishlist, name='wishlist'),
    path('mypage/contact/', views.contact, name='contact'),
    path('mypage/contact_history/', views.contact_history, name='contact_history'),
    path('comment/<int:pk>/updatecomment/', views.updatecomment, name='updatecomment'),
    path('comment/<int:pk>/deletecomment/', views.deletecomment, name='deletecomment'),
    path('wishlist/add/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),

    ]
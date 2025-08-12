from django.urls import path
from . import views
#from .views import create_order
urlpatterns = [
    path('', views.aboutme, name='aboutme'),
    path('main/<int:pk>/', views.shopdetail, name='shopdetail'),

    path('mypage/', views.shopmyPage, name='mypage'),
    path('create/', views.create, name='itemcreate'),
    path('category/<slug:slug>/', views.category_view, name='category_view'),
    path('search/', views.search, name='search'),
    path('main/', views.shoplist, name='main'),
    path('mypage/order_status/', views.order_status, name='order_status'),
    path('mypage/wishlist/', views.wishlist, name='wishlist'),
    path('mypage/contact/', views.contact, name='contact'),
    path('mypage/contact_history/', views.contact_history, name='contact_history'),
    path('mypage/admincontact/', views.admincontact, name='admincontact'),
    path('mypage/reply/<int:comment_id>/', views.reply_comment, name='reply_comment'),
    path('mypage/create/', views.create, name='create'),
    path('comment/<int:pk>/updatecomment/', views.updatecomment, name='updatecomment'),
    path('comment/<int:pk>/deletecomment/', views.deletecomment, name='deletecomment'),
    path('wishlist/add/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:pk>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('cartlist/add/<int:pk>/', views.add_to_cartlist, name='add_to_cartlist'),
    path('cartlist/remove/<int:pk>/', views.remove_from_cartlist, name='remove_from_cartlist'),
    path('cartlist/', views.cartlist, name='cartlist'),
    path('get-messages/', views.get_messages, name='get_messages'),
    path('send-message/', views.send_message, name='send_message'),
    path('orderlist/add/<int:pk>/', views.add_to_orderlist, name='add_to_orderlist'),
    path('orderlist/remove/<int:pk>/', views.remove_from_orderlist, name='remove_from_orderlist'),
    path('orderlist/', views.orderlist, name='orderlist'),
    path('cartlist/remove_selected/', views.remove_from_cartlist_bulk, name='remove_from_cartlist_bulk'),
    path('mypage/event/', views.event, name='event'),
    path('mypage/delivery_status/', views.delivery_status, name='delivery_status'),
    path('event/finalize/<int:pk>/', views.finalize_bid, name='finalize_bid'),
    path('orders/<int:order_pk>/status/', views.update_order_status, name='update_order_status'),



    # 결제
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('success/<int:pk>/', views.success, name='success'),
    path('fail/<int:pk>/', views.fail, name='fail'),
    #path('api/orders/', create_order, name='create_order'),
    path('callback-auth', views.callback_auth, name='callback_auth'),
    ]
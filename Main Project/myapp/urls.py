from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('shop/<str:cat>/',views.shop,name='shop'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product/<str:cat>/',views.seller_view_product,name='seller-view-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('product-details/<int:pk>/',views.product_details,name='product-details'),
    path('seller-product-edit/<int:pk>/',views.seller_product_edit,name='seller-product-edit'),
    path('seller-product-delete/<int:pk>/',views.seller_product_delete,name='seller-product-delete'),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove-from-wishlist/<int:pk>/',views.remove_from_wishlist,name='remove-from-wishlist'),
]
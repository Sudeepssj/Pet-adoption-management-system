from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # admin dashboard get method url
    path('admin_dashboard_get/', views.admin_dashboard_get),

    # home page get method url
    path('homepage_get/', views.homepage_get),


    # login page get method url
    path('login_get/', views.login_get),

    # forgot pass get method url
    path('forgot_pass_get/', views.forgot_pass_get),

    # change pass get method url
    path('change_pass_get/', views.change_pass_get),

    # pet page get method url
    path('pet_get/', views.pet_get),

    # pet details page get method url
    path('pet_details_get/', views.pet_details_get),

    # edit pet page get method url
    path('edit_pet_get/', views.edit_pet_get),

    # user dashboard get method url
    path('user_dashboard_get/', views.user_dashboard_get),

    # shop signup or registration page get method url
    path('shop_signup_get/', views.shop_signup_get),

    # shop signup or registration page post method url
    path('shop_signup_post/', views.shop_signup_post),

    # User signup or registration page get method url
    path('user_signup_get/', views.user_signup_get),

    # User signup or registration page post method url
    path('user_signup_post/', views.user_signup_post),

    # shop dashboard get method url
    path('shop_dashboard_get/', views.shop_dashboard_get),

    # login post method url
    path('login_post/', views.login_post),

    # shop view pets get method url
    path('shop_view_pets_get/', views.shop_view_pets_get),

    # add pet post method url
    path('add_pet_post/', views.add_pet_post),

    # add pet get method url
    path('add_pet_get/', views.add_pet_get),

    # edit pet get method url
    path('edit_pet_get/<int:pet_id>/', views.edit_pet_get),

    # edit pet post method url
    path('edit_pet_post/', views.edit_pet_post),

    # pet delete get method url
    path('pet_delete_get/<int:pet_id>/', views.pet_delete_get),

    # shop profile get method url
    path('shop_profile_get/', views.shop_profile_get),

    # shop edit profile get method url
    path('shop_edit_profile_get/', views.shop_edit_profile_get),
    # shop edit profile post method url
    path('shop_edit_profile_post/', views.shop_edit_profile_post),

    # user profile get method url
    path('my_profile_get/', views.my_profile_get),
    
    # user edit profile get method url
    path('my_edit_profile_get/', views.my_edit_profile_get),

    # user edit profile post method url
    path('my_edit_profile_post/', views.my_edit_profile_post),

    # user view pets get method url
    path('user_view_pets_get/', views.user_view_pets_get),

    # shop add product get method url
    path('shop_add_product_get/', views.shop_add_product_get),

    # shop add product post method url
    path('shop_add_product_post/', views.shop_add_product_post), 

    # shop view products get method url
    path('shop_view_products_get/', views.shop_view_products_get),   

    # edit product get method url   
    path('edit_product_get/<int:product_id>/', views.edit_product_get),

    # edit product post method url
    path('edit_product_post/', views.edit_product_post),

    # delete product get method url
    path('delete_product/<int:product_id>/', views.delete_product), 

    # user view products get method url
    path('user_view_products_get/', views.user_view_product_get),

    # product quantity get method url
    path('product_quantity_get/<id>', views.product_quantity_get),

    # add to cart post method url
    path('add_product_to_cart_post/', views.add_product_to_cart_post), 

    # view cart get method url
    path('view_cart_get/', views.view_cart_get),  

    # order get method url
    path('order_main_get/<id>', views.order_main_get),

    # order sub get method url
    path('order_sub_get/<id>', views.order_sub_get),

    # order main status get method url
    path('order_main_status_get/', views.order_main_status_get),

    # shop order main status get method url
    path(
        "shop_view_order_status_get/",
        views.shop_view_order_status_get,
        name="shop_view_order_status_get"
    ),

    # shop order sub status get method url
    path('shop_view_order_sub_status_get/<id>/', views.shop_view_order_sub_status_get),


    # order main status search post method url
    path('order_main_status_search_post/', views.order_main_status_search_post),

    # order sub status get method url
    path('order_sub_status_get/<id>/', views.order_sub_status_get),

    # order all get method url
    path('order_all_get/', views.order_all_get),

    # user complaint get method url     
    path('user_complaint_get/', views.user_complaint_get),
    
    # user send complaint get method url
    path('user_send_complaint_get/', views.user_send_complaint_get),

    # user send complaint post method url
    path('user_send_complaint_post/', views.user_send_complaint_post),

    # Super User Admin urls Below
    path('admin_view_shops_get/', views.admin_view_shops_get),

    # Super User Admin view pets get method url
    path('admin_view_pets_get/<int:shop_id>/',views.admin_view_pets_get,name='admin_view_pets_get'),

    path('admin_view_complaints_get/', views.admin_view_complaints_get),

    path('admin_reply_get/<id>/', views.admin_reply_get),

    path('admin_reply_post/', views.admin_reply_post),

    # super user Admin in shop view products get method url
    path('admin_view_products_get/<int:shop_id>/', views.admin_view_products_get),

    # super user Admin in shop view orders get method url
    path('admin_view_orders_get/<int:shop_id>/',views.admin_view_orders_get,name='admin_view_orders_get'),

    # super user Admin dashboard view user get method url
    path('admin_view_users_get/', views.admin_view_users_get),

    # logout 
    path('logout/', views.logout_get,name='logout'),

    #super admin change password get method url
    path('super_admin_change_password_get/',views.super_admin_change_password,name='super_admin_change_password'),


    # shop change password get method url
    path('shop_change_password_get/',views.shop_change_password,name='shop_change_password'),

    # user change password get method url
    path('user_change_password_get/',views.user_change_password,name='user_change_password'),

    # forgot password get method url
    path('user_forgot_password_get/',views.user_Forgot_password,name='user_forgot_password'),

    


]

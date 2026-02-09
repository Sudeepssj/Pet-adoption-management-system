from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from myapp.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.

# admin dashboard get method
@login_required(login_url='/myapp/login_get/')
def admin_dashboard_get(request):
    user=request.user
    if user.groups.filter(name="admin").exists():
        total_shops = Shop_signup_table.objects.count()
        total_users = User_signup_table.objects.count()
        pending_complaints = User_complaint_table.objects.filter(Reply="no reply").count()
        
        context = {
            'total_shops': total_shops,
            'total_users': total_users,
            'pending_complaints': pending_complaints,
        }
        return render(request,"admin/admin_dashboard.html", context)
    else:
        return redirect('/myapp/login_get/')
    # return render(request,"admin/admin_dashboard.html", context)

# homepage get method
@login_required
def homepage_get(request):
    return render(request,"user/home.html")


# login get method
def login_get(request):
    return render(request,"user/login.html")

# login post method

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    us=authenticate(username=username,password=password)
    if us is not None:
        
        if us.groups.filter(name="user").exists():
            login(request,us)
            return redirect('/myapp/user_dashboard_get/')
        elif us.groups.filter(name="shop").exists():
            login(request,us)
            return redirect('/myapp/shop_dashboard_get/')
        elif us.groups.filter(name="admin").exists():
            login(request,us)
            return redirect('/myapp/admin_dashboard_get/')
        else:
            return redirect('/myapp/login_get/')
    else:
        return redirect('/myapp/login_get/')
        
       





# forgot password get method
def forgot_pass_get(request):
    return render(request,"user/forgot.html")

# change password get method
def change_pass_get(request):
    return render(request,"user/change.html")

# pet.html get method
@login_required
def pet_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        return render(request,"user/pet.html")
    else:
        return redirect('/myapp/login_get/')
# pet_details.html get method
@login_required
def pet_details_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        return render(request,"user/pet_details.html")
    else:
        return redirect('/myapp/login_get/')
# edit_pet.html get method
@login_required
def edit_pet_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        return render(request,"user/edit_pet.html")
    else:
        return redirect('/myapp/login_get/')
# user Dashboard get method
@login_required(login_url='/myapp/login_get/')
def user_dashboard_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        return render(request,"user/dashboard.html")
    else:
        return redirect('/myapp/login_get/')    

# shop signup registration page get method

def shop_signup_get(request):
    return render(request,"shop/shop_signup.html")

# shop signup page post method
def shop_signup_post(request):
    shop_name=request.POST['shop_name']
    owner_name=request.POST['owner_name']
    shop_photo=request.FILES['shop_photo']
    email=request.POST['email']
    phone_no=request.POST['phone_no']
    place=request.POST['place']
    post=request.POST['post_no']
    district=request.POST['district']
    pin=request.POST['pin']
    # login details
    username=request.POST['username']
    password=request.POST['password']

    fs=FileSystemStorage()
    path=fs.save(shop_photo.name,shop_photo)

    sh=Shop_signup_table()
    sh.shop_name=shop_name
    sh.owner_name=owner_name
    sh.shop_photo=path
    sh.email=email
    sh.phone_no=phone_no
    sh.place=place
    sh.post=post
    sh.district=district
    sh.pin=pin
    
    user = User.objects.create(username=username, password=make_password(password), email=email,first_name=password)    # ,shop_name=shop_name       removed
    user.save()
    user.groups.add(Group.objects.get(name="shop"))
    sh.LOGIN=user
    sh.save()



    return redirect('/myapp/login_get/')

# user signup registration page post method
def user_signup_post(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    profile_photo = request.FILES['profile_photo']
    # login details
    username = request.POST['username']
    password = request.POST['password']

    fs = FileSystemStorage()
    path = fs.save(profile_photo.name, profile_photo)

    user_signup = User_signup_table()
    user_signup.full_name = full_name
    user_signup.email = email
    user_signup.phone = phone
    user_signup.address = address
    user_signup.profile_photo = path

    user = User.objects.create(username=username, password=make_password(password), email=email,first_name=password)
    user.save()
    user.groups.add(Group.objects.get(name="user"))
    user_signup.LOGIN = user
    user_signup.save()

    return redirect('/myapp/login_get/')

# User signup registration page get method
def user_signup_get(request):
    return render(request,"user/user_signup.html") 

# shop dashboard get method
@login_required(login_url='/myapp/login_get/')
def shop_dashboard_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        return render(request,"shop/shop_dashboard.html")
    else:
        return redirect('/myapp/login_get/')
# shop view pets get method
@login_required     
def shop_view_pets_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        pets = pet.objects.filter(shop__LOGIN_id=request.user.id)
        return render(request, "shop/view_pet.html", {"pets": pets})
    else:
        return redirect('/myapp/login_get/')
   

# add pet post method
@login_required
def add_pet_post(request):
    name = request.POST['name']
    breed = request.POST['breed']
    category = request.POST['category']
    age = request.POST['age']
    vaccinated = request.POST['vaccinated']
    description = request.POST['description']
    photo = request.FILES['photo']

    fs = FileSystemStorage()
    path = fs.save(photo.name, photo)

    p = pet()
    p.name = name
    p.breed = breed
    p.category = category
    p.age = age
    p.vaccinated = vaccinated
    p.description = description
    p.photo = path
    p.shop = Shop_signup_table.objects.get(LOGIN=request.user)

    p.save()

    return redirect('/myapp/shop_view_pets_get/')

# add pet get method
@login_required
def add_pet_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        return render(request, "shop/add_pet.html")
    else:
        return redirect('/myapp/login_get/')
    

# edit pet get method
@login_required
def edit_pet_get(request, pet_id):
    user=request.user
    if user.groups.filter(name="shop").exists():
        request.session['pet_id'] = pet_id
        p = pet.objects.get(id=pet_id)
        return render(request, "shop/edit_pet.html", {"pet": p})
    else:
        return redirect('/myapp/login_get/')
    
    

# edit pet post method
@login_required
def edit_pet_post(request):
    p = pet.objects.get(id=request.session['pet_id'])

    p.name = request.POST['name']
    p.breed = request.POST['breed']
    p.category = request.POST['category']
    p.age = request.POST['age']
    p.vaccinated = request.POST['vaccinated']
    p.description = request.POST['description']

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        path = fs.save(photo.name, photo)
        p.photo = path

    p.save()

    return redirect('/myapp/shop_view_pets_get/')

# pet delete get method
@login_required
def pet_delete_get(request, pet_id):
    user=request.user
    if user.groups.filter(name="shop").exists():
        p=pet.objects.get(id=pet_id)
        p.delete()
        return redirect('/myapp/shop_view_pets_get/')
    else:
        return redirect('/myapp/login_get/')
    

# shop profile get 
@login_required
def shop_profile_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        shop = Shop_signup_table.objects.get(LOGIN=request.user)
        return render(request, "shop/shop_profile.html", {"shop": shop})
    else:
        return redirect('/myapp/login_get/')
    
# shop edit profile get method
@login_required
def shop_edit_profile_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        shop = Shop_signup_table.objects.get(LOGIN=request.user)
        return render(request, "shop/shop_edit_profile.html", {"shop": shop})
    else:
        return redirect('/myapp/login_get/')
    
    


# shop edit profile post method
# def shop_edit_profile_post(request):
#     if request.method != 'POST':
#         return redirect('/myapp/shop_edit_profile_get/')

#     shop = Shop_signup_table.objects.get(LOGIN=request.user)

#     shop.shop_name = request.POST.get('shop_name', shop.shop_name)
#     shop.owner_name = request.POST.get('owner_name', shop.owner_name)
#     shop.email = request.POST.get('email', shop.email)
#     shop.phone_no = request.POST.get('phone_no', shop.phone_no)
#     shop.place = request.POST.get('place', shop.place)
#     shop.post = request.POST.get('post', shop.post)
#     shop.district = request.POST.get('district', shop.district)
#     shop.pin = request.POST.get('pin', shop.pin)

#     # handle optional photo upload
#     if 'shop_photo' in request.FILES:
#         shop_photo = request.FILES['shop_photo']
#         fs = FileSystemStorage()
#         path = fs.save(shop_photo.name, shop_photo)
#         shop.shop_photo = path

#     shop.save()
#     return redirect('/myapp/shop_profile_get/')

# shop edit profile post method
@login_required
def shop_edit_profile_post(request):

    shop_name=request.POST['shop_name']
    owner_name=request.POST['owner_name']
    email=request.POST['email']
    phone_no=request.POST['phone_no']
    place=request.POST['place']
    post=request.POST['post_no']
    district=request.POST['district']
    pin=request.POST['pin']
    ab=Shop_signup_table.objects.get(LOGIN=request.user)


    if 'shop_photo' in request.FILES:
        shop_photo=request.FILES['shop_photo']
        fs=FileSystemStorage()
        path=fs.save(shop_photo.name,shop_photo)
        ab.shop_photo=path
        


    ab.shop_name=shop_name
    ab.owner_name=owner_name
    ab.email=email
    ab.phone_no=phone_no
    ab.place=place
    ab.post=post
    ab.district=district
    ab.pin=pin
    ab.save()

    return redirect('/myapp/shop_profile_get/')

# user profile get method
@login_required
def my_profile_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        user_profile = User_signup_table.objects.get(LOGIN=request.user)
        return render(request, "user/my_profile.html", {"user_data": user_profile})
    else:
        return redirect('/myapp/login_get/')
    

# user edit profile get method
@login_required
def my_edit_profile_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        user_data = User_signup_table.objects.get(LOGIN=request.user)
        return render(request, "user/my_edit_profile.html", {"user_data": user_data})
    else:
        return redirect('/myapp/login_get/')
    

# user edit profile post method
@login_required
def my_edit_profile_post(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    bc=User_signup_table.objects.get(LOGIN=request.user)
   
    
    if 'profile_photo' in request.FILES:
        profile_photo=request.FILES['profile_photo']
        fs=FileSystemStorage()
        path=fs.save(profile_photo.name,profile_photo)
        bc.profile_photo=path
    
    bc.full_name=full_name
    bc.email=email
    bc.phone=phone
    bc.address=address
    bc.save()
    return redirect('/myapp/my_profile_get/')

# user view pets get method
@login_required
def user_view_pets_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        pets = pet.objects.all()
        return render(request, "user/user_view_pets_table.html", {"pets": pets})
    else:
        return redirect('/myapp/login_get/')
    
        

# shop add product get method
@login_required
def shop_add_product_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        return render(request, "shop/add_product.html")
    else:
        return redirect('/myapp/login_get/')
    

# shop add product post method
@login_required
def shop_add_product_post(request):
    Product_Name = request.POST['Product_Name']
    Details = request.POST['Details']
    Photo = request.FILES['Photo']
    Price = request.POST['Price']
    Quantity = request.POST['Quantity']
    type=request.POST['type']

    fs = FileSystemStorage()
    path = fs.save(Photo.name, Photo)

    p = Product_table()
    p.Product_Name = Product_Name
    p.Details = Details
    p.Photo = path
    p.Price = Price
    p.Quantity = Quantity
    p.type=type
    p.SHOP = Shop_signup_table.objects.get(LOGIN=request.user)

    p.save()

    return redirect('/myapp/shop_dashboard_get/')

# shop view products get method
@login_required
def shop_view_products_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        products = Product_table.objects.filter(SHOP__LOGIN_id=request.user.id)
        return render(request, "shop/view_product.html", {"products": products})
    else:
        return redirect('/myapp/login_get/')    
    

# edit product get method
@login_required
def edit_product_get(request, product_id):
    user=request.user
    if user.groups.filter(name="shop").exists():
        request.session['product_id'] = product_id
        p = Product_table.objects.get(id=product_id)
        return render(request, "shop/edit_product.html", {"product": p})
    else:
        return redirect('/myapp/login_get/') 
    

# edit product post method
@login_required
def edit_product_post(request): 
    p = Product_table.objects.get(id=request.session['product_id'])

    p.Product_Name = request.POST['Product_Name']
    p.Details = request.POST['Details']
    p.Price = request.POST['Price']
    p.Quantity = request.POST['Quantity']
    p.type=request.POST['type']

    if 'Photo' in request.FILES:
        Photo = request.FILES['Photo']
        fs = FileSystemStorage()
        path = fs.save(Photo.name, Photo)
        p.Photo = path

    p.save()

    return redirect('/myapp/shop_view_products_get/')

# delete product get method
@login_required
def delete_product(request, product_id):
    user=request.user
    if user.groups.filter(name="shop").exists():
        p = Product_table.objects.get(id=product_id)
        p.delete()
        return redirect('/myapp/shop_view_products_get/')
    else:
        return redirect('/myapp/login_get/')
    

# user view product details get method
@login_required
def user_view_product_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        product = Product_table.objects.all()
        return render(request, "user/user_view_product.html", {"products": product})
    else:
        return redirect('/myapp/login_get/')
    

# product quantity get method
@login_required
def product_quantity_get(request,id):
    user=request.user
    if user.groups.filter(name="user").exists():
        request.session['product_id']=id
        return render(request, "user/product_quantity.html")
    else:
        return redirect('/myapp/login_get/')
    

# add to cart post method
@login_required
def add_product_to_cart_post(request):
    qty=request.POST['quantity']
    prod=Product_table.objects.get(id=request.session['product_id'])
    total=int(prod.Price)*int(qty)
    print(request.user.id,"lllllllllllllllllllllllllllll")
    print(request.session['product_id'],"lllllllllllllllllllllllllllll")
    ob=Cart_table.objects.filter(USER__id=request.user.id,PRODUCT__id=request.session['product_id'])
    print(ob,"kkjjjjjjjjjjjjjjjjjjjjjjj")
    if int(prod.Quantity)>=int(qty):
        if ob.exists():  
            print("if part")
            cart_item = ob.first()
            T=cart_item.Total_amount
            Q=cart_item.Quantity
            total_qty=int(Q)+int(qty)
            Total_Amount=int(prod.Price)*int(total_qty)
            cart_item.Total_amount=Total_Amount
            cart_item.Quantity=total_qty
            cart_item.save()
            return redirect('/myapp/view_cart_get/')
        else:
            print("else part")
            cart=Cart_table()
            cart.PRODUCT=Product_table.objects.get(id=request.session['product_id'])
            cart.USER=User.objects.get(id=request.user.id)    
            cart.Quantity=qty
            cart.Total_amount=total
            cart.date=datetime.today()
            cart.save()
            return redirect('/myapp/view_cart_get/')
  
    else:
        print("inside else")
        return HttpResponse('''<script>alert('items are  not available in stock');window.location="/myapp/view_cart_get/"</script>''')

# view cart get method
@login_required
def view_cart_get(request): 
    user=request.user
    if user.groups.filter(name="user").exists():
        cart_items = Cart_table.objects.filter(USER__id=request.user.id)
        tot=sum(cart_items.Total_amount for cart_items in cart_items)
        return render(request, "user/view_cart.html", {"cart_items": cart_items,"total_amount":tot})
    else:
        return redirect('/myapp/login_get/')
    

# order main get method
@login_required
def order_main_get(request,id):
    user=request.user
    if user.groups.filter(name="user").exists():
        cart_item = Cart_table.objects.get(id=id)
        order = Order_table_main()
        print(cart_item)
        order.USER = cart_item.USER
        order.Status = "pending"
        order.Date = datetime.today()
        order.Amount = cart_item.Total_amount
        order.save()

        order_sub = Order_table_sub()
        order_sub.PRODUCT = cart_item.PRODUCT
        order_sub.Quantity = cart_item.Quantity
        order_sub.Total_amount = cart_item.Total_amount
        order_sub.Status = "pending"
        order_sub.ORDER = order
        order_sub.save()


        cart_item.delete()



        return HttpResponse("Order placed successfully!")
    else:
        return redirect('/myapp/login_get/')
    

# order sub get method
@login_required
def order_sub_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        cart_items = Cart_table.objects.filter(USER__id=request.user.id)
    order = Order_table_sub()
    for item in cart_items:
        order.PRODUCT = item.PRODUCT
        order.Quantity = item.Quantity
        order.Total_amount = item.Total_amount
        order.Status = "pending"
        order.save()
        item.delete()
        return HttpResponse("All Order placed successfully!")
    else:
        return redirect('/myapp/login_get/')
    

# order status main get method
@login_required
def order_main_status_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        orders = Order_table_main.objects.filter(USER__id=request.user.id)
        return render(request, "user/order_status.html", {"orders": orders})
    else:
        return redirect('/myapp/login_get/')
    

# order status main search post method
@login_required
def order_main_status_search_post(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        status = request.POST['search']
        orders = Order_table_main.objects.filter(USER__id=request.user.id, Date__icontains=status)
        return render(request, "user/order_status.html", {"orders": orders})
    else:
        return redirect('/myapp/login_get/')
    

# shop order status main get method
@login_required
def shop_view_order_status_get(request):
    user=request.user
    if user.groups.filter(name="shop").exists():
        orders = Order_table_main.objects.all().order_by('-Date')
        return render(
        request,
        "shop/view_order_main.html",
        {"orders": orders}
    )
    else:
        return redirect('/myapp/login_get/')
    

# shop order status sub search get method
@login_required
def shop_view_order_sub_status_get(request, id):
    user=request.user
    if user.groups.filter(name="shop").exists():
        order = Order_table_main.objects.get(id=id)   # ✅ FETCH MAIN ORDER
        order_items = Order_table_sub.objects.filter(ORDER__id=id)

        return render(
            request,
            "shop/view_order_sub.html",
            {
                "order": order,            # ✅ PASS ORDER
                "order_items": order_items
            }
        )
    else:
        return redirect('/myapp/login_get/')
    


# pet search in category post method
"""def petcategorysearch_post(request):
    search=request.POST['search']
    vi=category_table.objects.filter(name__icontains=search)

    return render(request,"viewcategory.html",{"data":vi}) """

# order sub status get method
@login_required
def order_sub_status_get(request,id):
    user=request.user
    if user.groups.filter(name="user").exists():
        order_items = Order_table_sub.objects.filter(ORDER__id=id)
        return render(request, "user/order_sub.html", {"order_items": order_items})
    else:
        return redirect('/myapp/login_get/')
    

# order all get method
@login_required
def order_all_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        cart_items = Cart_table.objects.filter(USER__id=request.user.id)


        order = Order_table_main()


        total_amount = sum(item.Total_amount for item in cart_items)


        order.USER = User.objects.get(id=request.user.id)
        order.Status = "orderd"
        order.Date = datetime.today()
        order.Amount = total_amount
        order.save()

        for item in cart_items:
            order_sub = Order_table_sub()
            order_sub.PRODUCT = item.PRODUCT
            order_sub.Quantity = item.Quantity
            order_sub.Total_amount = item.Quantity * item.PRODUCT.Price
            order_sub.Status = "orderd"
            order_sub.ORDER = order
            order_sub.save()
            item.delete()

        return HttpResponse("All Orders placed successfully!")
    else:
        return redirect('/myapp/login_get/')
    

# user complaint get method
@login_required
def user_complaint_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        complaints = User_complaint_table.objects.filter(USER=request.user)
        return render(request,"user/user_complaints.html",{"complaints": complaints})
    else:
        return redirect('/myapp/login_get/')
    

# user send complaint get method
@login_required
def user_send_complaint_get(request):
    user=request.user
    if user.groups.filter(name="user").exists():
        return render(request, "user/send_complaints.html")
    else:
        return redirect('/myapp/login_get/')
    

# user send complaint post method
@login_required
def user_send_complaint_post(request):
    complaint = request.POST['complaint']

    obj = User_complaint_table()
    obj.Date = datetime.today()
    obj.USER = request.user
    obj.Complaint = complaint
    obj.save()

    return redirect('/myapp/user_complaint_get/')





#   Super User Admin Views Below

# admin view complaints get method
@login_required
def admin_view_complaints_get(request):
    user=request.user
    if user.groups.filter(name="admin").exists():
        complaints = User_complaint_table.objects.all().order_by('-Date')
        return render(request,"admin/view_complaints.html",{"complaints": complaints})
    else:
        return redirect('/myapp/login_get/')
    

# admin reply get method
@login_required
def admin_reply_get(request, id):
    user=request.user
    if user.groups.filter(name="admin").exists():
        print(id,"llllllllllllllllllllllllll")
        request.session['cid']=id

        complaint = User_complaint_table.objects.get(id=id)

        print(complaint.Complaint,"kkkkkkkkkkkkkkkkkkkkkkkkk")

        return render(request, "admin/reply_complaint.html", {"complaint": complaint})
    else:
        return redirect('/myapp/login_get/')
     

# admin reply post method
@login_required
def admin_reply_post(request):
    reply = request.POST['reply']

    complaint = User_complaint_table.objects.get(id=request.session['cid'])
    complaint.Reply = reply
    complaint.save()

    return redirect('/myapp/admin_view_complaints_get/')



# shop view all users get method
@login_required  
def admin_view_shops_get(request):
    user=request.user
    if user.groups.filter(name="admin").exists():
        shops = Shop_signup_table.objects.all()

        shop_list = []

        for shop in shops:
            pet_count = pet.objects.filter(shop=shop).count()

            product_count = Product_table.objects.filter(SHOP=shop).count()

            order_count = Order_table_sub.objects.filter(
                PRODUCT__SHOP=shop
            ).count()

            shop_list.append({
                "id": shop.id,
                "shop_name": shop.shop_name,
                "place": shop.place,
                "phone_no": shop.phone_no,
                "pet_count": pet_count,
                "product_count": product_count,
                "order_count": order_count,
            })

        return render(request,"admin/view_shops.html",{"shops": shop_list})
    else:
        return redirect('/myapp/login_get/')
    

# admin view pets get method
@login_required
def admin_view_pets_get(request, shop_id):
    user=request.user
    if user.groups.filter(name="admin").exists():
        shop = Shop_signup_table.objects.get(id=shop_id)
        pets = pet.objects.filter(shop=shop)

        return render(
            request,
            "admin/view_pets.html",
            {
                "shop": shop,
                "pets": pets
            }
        )
    else:
        return redirect('/myapp/login_get/')
    


# admin view products get method
@login_required
def admin_view_products_get(request, shop_id):
    user=request.user
    if user.groups.filter(name="admin").exists():
        shop = Shop_signup_table.objects.get(id=shop_id)
        products = Product_table.objects.filter(SHOP=shop)

        return render(
            request,
            "admin/view_products.html",
            {
                "shop": shop,
                "products": products
            }
        )
    else:
        return redirect('/myapp/login_get/')
    


# admin shop view orders get method
@login_required
def admin_view_orders_get(request, shop_id):
    user=request.user
    if user.groups.filter(name="admin").exists():
        shop = Shop_signup_table.objects.get(id=shop_id)
        order_items = Order_table_sub.objects.filter(
            PRODUCT__SHOP=shop
        ).select_related('ORDER', 'PRODUCT', 'ORDER__USER').order_by('-ORDER__Date')
        return render(request,"admin/view_orders.html",{"shop": shop,"order_items": order_items})
    else:
        return redirect('/myapp/login_get/')
    

# super admin view users get method
@login_required
def admin_view_users_get(request):
    user=request.user
    if user.groups.filter(name="admin").exists():
        users = User_signup_table.objects.all()
        return render(request,"admin/view_users.html",{"users": users})
    else:
        return redirect('/myapp/login_get/')
    


# logout
def logout_get(request):
    logout(request)
    return redirect('/myapp/login_get')

# @login_required
# def user_dashboard_get(request):
#     return render(request,"user/dashboard.html")





from django.shortcuts import render,redirect
from .models import User,Product,Wishlist,Cart
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
import stripe

YOUR_DOMAIN = 'http://localhost:8000'
stripe.api_key = settings.STRIPE_PRIVATE_KEY


# Create your views here.
def index(request):
    try:
        user=User.objects.get(email=request.session['email'])
        if user.usertype=="buyer":
            return render(request,'index.html')
        else:
            return render(request,'seller-index.html')
    except:
        return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def shop(request,cat):
    products=Product()
    if cat=="all":
        products=Product.objects.all()
    elif cat=="women":
        products=Product.objects.filter(product_category="women")
    elif cat=="men":
        products=Product.objects.filter(product_category="men")
    elif cat=="kids":
        products=Product.objects.filter(product_category="kids")
    elif cat=="accessories":
        products=Product.objects.filter(product_category="accessories")
    return render(request,'shop.html',{'products':products})

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                request.session['profile_picture']=user.profile_picture.url
                if user.usertype=="buyer":
                    wishlists=Wishlist.objects.filter(user=user)
                    request.session['wishlist_count']=len(wishlists)
                    return render(request,'index.html')
                else:
                    return render(request,'seller-index.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg="Email Not Regsistered"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    profile_picture=request.FILES['profile_picture'],
                    usertype=request.POST['usertype']
                )
                msg="User Registered Successfully"
                return render(request,'register.html',{'msg':msg})
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')
    
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['profile_picture']
        msg="Logged Out Successfully"
        return render(request,'login.html',{'msg':msg})
    except:
        msg="Logged Out Successfully"
        return render(request,'login.html',{'msg':msg})
    
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        user.address=request.POST['address']
        try:
            user.profile_picture=request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['fname']=user.fname
        request.session['profile_picture']=user.profile_picture.url
        msg="Profile Updated Successfully"
        if user.usertype=="buyer":
            return render(request,'profile.html',{'user':user,'msg':msg})
        else:
            return render(request,'seller-profile.html',{'user':user,'msg':msg})
    else:
        if user.usertype=="buyer":
            return render(request,'profile.html',{'user':user})
        else:
            return render(request,'seller-profile.html',{'user':user})
    
def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                if user.password!=request.POST['new_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    del request.session['email']
                    del request.session['fname']
                    del request.session['profile_picture']
                    msg="Profile Updfated Successfully"
                    return render(request,'login.html',{'msg':msg})
                else:
                    msg="New Password Can't Be From Your Old Password"
                    if user.usertype=="buyer":
                        return render(request,'change-password.html',{'msg':msg})
                    else:
                        return render(request,'seller-change-password.html',{'msg':msg})
            else:
                msg="New Password & Confirn New Password Does Not Matched"
                if user.usertype=="buyer":
                    return render(request,'change-password.html',{'msg':msg})
                else:
                    return render(request,'seller-change-password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Matched"
            if user.usertype=="buyer":
                return render(request,'change-password.html',{'msg':msg})
            else:
                return render(request,'seller-change-password.html',{'msg':msg})
    else:
        if user.usertype=="buyer":
            return render(request,'change-password.html')
        else:
            return render(request,'seller-change-password.html')
    
def forgot_password(request):
    if request.method=="POST":
        try:
            return render(request,'forgot-password.html')
        except Exception as e:
            print(e)
            msg="Mobile Number Not Registered"
            return render(request,'forgot-password.html',{'msg':msg})
    else:
        return render(request,'forgot-password.html')
    
def seller_add_product(request):
    seller=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        Product.objects.create(
            seller=seller,
            product_category=request.POST['product_category'],
            product_name=request.POST['product_name'],
            product_price=request.POST['product_price'],
            product_desc=request.POST['product_desc'],
            product_image=request.FILES['product_image']
        )
        msg="Product Added Successfully"
        return render(request,'seller-add-product.html',{'msg':msg})
    else:
        return render(request,'seller-add-product.html')
    
def seller_view_product(request,cat):
    products=Product()
    seller=User.objects.get(email=request.session['email'])
    if cat=='all':
        products=Product.objects.filter(seller=seller)
    elif cat=="men":
        products=Product.objects.filter(seller=seller,product_category="men")
    elif cat=="women":
        products=Product.objects.filter(seller=seller,product_category="women")
    elif cat=="kids":
        products=Product.objects.filter(seller=seller,product_category="kids")
    elif cat=="accessories":
        products=Product.objects.filter(seller=seller,product_category="accessories")
    return render(request,'seller-view-product.html',{'products':products})

def seller_product_details(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'seller-product-details.html',{'product':product})

def product_details(request,pk):
    wishlist_flag=False
    cart_flag=False
    user=User.objects.get(email=request.session['email'])
    product=Product.objects.get(pk=pk)
    try:
        Wishlist.objects.get(user=user,product=product)
        wishlist_flag=True
    except:
        pass
    try:
        Cart.objects.get(user=user,product=product,payment_status=False)
        cart_flag=True
    except:
        pass
    return render(request,'product-details.html',{'product':product,'wishlist_flag':wishlist_flag,'cart_flag':cart_flag})


def seller_product_edit(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
        product.product_category=request.POST['product_category']
        product.product_name=request.POST['product_name']
        product.product_price=request.POST['product_price']
        product.product_desc=request.POST['product_desc']
        try:
            product.product_image=request.FILES['product_image']
        except:
            pass
        product.save()
        msg="Product Updated Successfully"
        return render(request,'seller-product-edit.html',{'product':product,'msg':msg})
    else:
        return render(request,'seller-product-edit.html',{'product':product})
    
def seller_product_delete(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('index')

def add_to_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.create(user=user,product=product)
    return redirect('wishlist')

def wishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlists=Wishlist.objects.filter(user=user)
    request.session['wishlist_count']=len(wishlists)
    return render(request,'wishlist.html',{'wishlists':wishlists})

def remove_from_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect('wishlist')

def add_to_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(
        user=user,
        product=product,
        product_price=product.product_price,
        product_qty=1,
        total_price=product.product_price,
        payment_status=False
    )
    return redirect('cart')

def cart(request):
    net_price=0
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user,payment_status=False)
    for i in carts:
        net_price=net_price+i.total_price
    request.session['cart_count']=len(carts)
    return render(request,'shop-cart.html',{'carts':carts,'net_price':net_price})

def remove_from_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.get(user=user,product=product,payment_status=False)
    cart.delete()
    return redirect('cart')

def change_qty(request):
    cid=int(request.POST['cid'])
    product_qty=int(request.POST['product_qty'])
    cart=Cart.objects.get(pk=cid)
    cart.product_qty=product_qty
    cart.total_price=product_qty*cart.product_price
    cart.save()
    return redirect('cart')

@csrf_exempt
def create_checkout_session(request):
	amount = int(json.load(request)['post_data'])
	final_amount=amount*100
	user=User.objects.get(email=request.session['email'])
	user_name=f"{user.fname} {user.lname}"
	user_address=f"{user.address}"
	user_mobile=f"{user.mobile}"
	session = stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
			'price_data': {
				'currency': 'inr',
				'unit_amount': final_amount,
				'product_data': {
					'name': 'Checkout Session Data',
					'description':f'''Customer:{user_name},\n\n
					Address:{user_address},\n
					Mobile:{user_mobile}''',
				},
			},
			'quantity': 1,
			}],
		mode='payment',
		success_url=YOUR_DOMAIN + '/success.html',
		cancel_url=YOUR_DOMAIN + '/cancel.html',
		customer_email=user.email,
		shipping_address_collection={
			'allowed_countries':['IN'],
		}
		)
	return JsonResponse({'id': session.id})

def success(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	for i in carts:
		i.payment_status=True
		i.save()
	carts=Cart.objects.filter(user=user,payment_status=False)
	request.session['cart_count']=len(carts)
	return render(request,'success.html')

def cancel(request):
	return render(request,'cancel.html')


def myorders(request):
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user,payment_status=True)
    return render(request,'myorders.html',{'carts':carts})
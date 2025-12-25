from django.shortcuts import render
from .models import Contact,User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=='POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            remarks=request.POST['remarks'],
        )
        
        msg='Contact Added Successfully'
        contacts=Contact.objects.all().order_by("-id")[:3]
        return render(request,'contact.html',{'msg':msg,'contacts':contacts})
    else:
         contacts=Contact.objects.all().order_by("-id")[:3]
         return render(request,'contact.html',{'contacts':contacts})
         
   

def signup(request):
        if request.method=='POST':
                try:
                     User.objects.get(email=request.POST['email'])
                     msg="Email Already Exist"
                     return render(request,'signup.html',{'msg':msg})
                except:
                     if request.POST['password']==request.POST['cpassword']:
                        User.objects.create(
                        fname=request.POST['fname'],
                        lname=request.POST['lname'],
                        email=request.POST['email'],
                        mobile=request.POST['mobile'],
                        address=request.POST['address'],
                        password=request.POST['password'],
                        
                        )
                        msg='Sign Up Successfully'
                        return render(request,'signup.html',{'msg':msg})
                     else:
                           msg='Password and Confirm Password Does Not Match'
                           return render(request,'signup.html',{'msg':msg})
        else:
             
            return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        try:
             user=User.objects.get(email=request.POST['email'])
             if user.password==request.POST['password']:
                  request.session['email']=user.email
                  request.session['fname']=user.fname
                  return render(request,'index.html')
             else:
                  msg="Incorrect Password"
                  return render(request,'login.html',{'msg':msg})
        except:
               msg="Email Not Registered"
               return render(request,'login.html',{'msg':msg})
    else:
         
        return render(request,'login.html')
    
def logout(request):
     try:
         del request.session['email']
         del request.session['fname'] 
         msg="Logged Out Successfully"
         return render(request,'login.html',{'msg':msg})
     except:
          msg="Logged Out Successfully"
          return render(request,'login.html',{'msg':msg})
     
def change_password(request):
     user=User.objects.get(email=request.session['email'])
     if request.method=='POST':
        if user.password==request.POST['old_password']:
             if request.POST['new_password']==request.POST['cnew_password']:
                  if user.password!=request.POST['new_password']:
                       user.password=request.POST['new_password']
                       user.save()
                       del request.session['email']
                       del request.session['fname'] 
                       msg="Password Change Successfully"
                       return render(request,'login.html',{'msg':msg})
                  else:
                       msg="Your New Password Can't Be From Your Old Password"
                       return render(request,'login.html',{'msg':msg})
             else: 
                  msg="New & Confirm Password Does Not Matched"
                  return render(request,'login.html',{'msg':msg})    
        else:  
             msg="Old Password Does Not Matched"
             return render(request,'login.html',{'msg':msg}) 
     else:
           
        return render(request,'change_password.html')
     
def forgot_password(request):
     if request.method=="POST":
          try:
               user=User.objects.get(email=request.POST['email'])
               to=request.POST['email']
               subject="OTP For Forgot Password"
               otp=random.randint(1000,9999)
               message="Your OTP For Forgot Password Is  "+str(otp)
               send_mail(subject,message,settings.EMAIL_HOST_USER,[to,])
               request.session['email_to']=to
               request.session['otp']=otp
               return render(request,'otp.html')
          except:
               msg="Email Not Registered"
               return render(request,'forgot_password.html',{'msg':msg})
     else:
          
          return render(request,'forgot_password.html')

def verify_otp(request):
     if int(request.POST['otp'])==int(request.session['otp']):
          del request.session['otp']
          return render(request,'new_password.html')
     else:
          msg="Invalid OTP"
          return render(request,'otp.html',{'msg':msg})
     
def new_password(request):
     if request.POST['new_password']==request.POST['cnew_password']:
          user=User.objects.get(email=request.session['email_to'])
          user.password=request.POST['new_password']
          user.save()
          del request.session['email_to']
          msg="Password Updated Successfully"
          return render(request,'login.html',{'msg':msg})
     else:
          msg="New Password & Confirm New Password Does Not Matched"
          return render(request,'new_password.html',{'msg':msg})
from django.shortcuts import render
from .models import Contact,User
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
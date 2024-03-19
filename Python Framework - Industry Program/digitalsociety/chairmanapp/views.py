from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import random
from django.urls import reverse
from .utils import *

""""
get() : It will return object

-> It will return only single object
-> It will throw exception when it will return object
-> If conditon not match it will throw exeception
"""

# Create your views here.
def login(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        mcount=Member.objects.all().count()
        ncount=Notice.objects.all().count()
        context={
                "uid":uid,
                "cid":cid,
                "mcount":mcount,         
                "ncount":ncount,         
            }
        return render(request,"chairmanapp/index.html",context)
    else:
        return render(request,"chairmanapp/login.html")

def login_evalute(request):
    if "email" in request.session:
        return HttpResponseRedirect(reverse("loginpage"))
    else:
        try:
            print("=================this function is called.")
            email_var=request.POST["email"]
            password_var=request.POST["password"]
            print("=======>>>>email",email_var)
            print("------------<<<password",password_var)
            # ORM : object relational mapper
            uid=User.objects.get(email=email_var,password=password_var)
            print("---------->>> uid",uid)
            print("========<<<role",uid.role)
            print("==========is active",uid.is_active)


            if uid.role=="chairman":
                cid = Chairman.objects.get(userid=uid)
                print("Firstname =",cid.firstname)
                # Session Management
                request.session['email']=email_var

                context={
                    "uid":uid,
                    "cid":cid,         
                }
                return render(request,"chairmanapp/index.html",context)
            else:
                pass

            return render(request,"chairmanapp/login.html")
        except:
            e_msg="Invalid email or password"
            print("=====>> emsg",e_msg)
            return render(request,"chairmanapp/login.html",{"e_msg":e_msg})
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return HttpResponseRedirect(reverse("loginpage"))
    else:
        return HttpResponseRedirect(reverse("loginpage"))
    
def chairman_profile(request): 
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        context={
                "uid":uid,
                "cid":cid,         
            }
        return render(request,"chairmanapp/profile.html",context)
    else:
        return render(request,"chairmanapp/login.html")
    
def chairman_change_password(request):
    if request.POST:
        email=request.session['email']
        currentpassword=request.POST['currentpassword']
        newpassword=request.POST['newpassword']
        uid=User.objects.get(email=email)
        if uid:
            if uid.password==currentpassword:
                uid.password=newpassword
                uid.save()      # updtae 
                del request.session['email']
                s_msg="Successfully Password Changed"
                return render(request,"chairmanapp/login.html",{'s_msg':s_msg})
            else:
                pass
        else:
            pass 

def chairman_update_profile(request):
    if request.POST:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(userid=uid)
        cid.firstname=request.POST['firstname']
        cid.lastname=request.POST['lastname']
        cid.contactno=request.POST['contactno']
        cid.houseno=request.POST['houseno']

        if "profilepic" in request.FILES:
            picture=request.FILES['profilepic']
            cid.pic=picture
            cid.save()
        
        cid.save()
        context={
            'uid' : uid,
            'cid' : cid,
        }
        return render(request,"chairmanapp/profile.html",context)
    
def add_member(request):
    if request.POST:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        context={
                "uid":uid,
                "cid":cid,         
        }
        if "mid" in request.POST:
            mid=Member.objects.get(id=request.POST['mid'])
            mid.firstname=request.POST['firstname']
            mid.lastname=request.POST['lastname']
            mid.contactno=request.POST['contactno']
            mid.houseno=request.POST['houseno']
            mid.vehicle_details=request.POST['vehicle_details']
            mid.occupation=request.POST['occupation']
            mid.no_familymembers=request.POST['no_familymembers']
            mid.job_address=request.POST['job_address']
            mid.blood_grp=request.POST['blood_grp']
            mid.city=request.POST['city']
            mid.birthdate=request.POST['birthdate']
            mid.save()
            return render(request,"chairmanapp/add_member.html",context)
        else:
            email=request.POST['email']
            contactno=request.POST['contactno']
            l1=["x6c5","5d7sa","a6s8k","tr5u4","6bn5m","io9p8"]
            password = random.choice(l1)+email[3:6]+contactno[4:6]
            firstname=request.POST['firstname']
            muid=User.objects.create(email=email,password=password,role='member')
            mid=Member.objects.create(userid=muid,
                                    firstname=request.POST['firstname'],
                                    lastname=request.POST['lastname'],
                                    contactno=request.POST['contactno'],
                                    houseno=request.POST['houseno'],
                                    vehicle_details=request.POST['vehicle_details'],
                                    occupation=request.POST['occupation'],
                                    no_familymembers=request.POST['no_familymembers'],
                                    job_address=request.POST['job_address'],
                                    blood_grp=request.POST['blood_grp'],
                                    city=request.POST['city'],
                                    birthdate=request.POST['birthdate'])
        mysendmail("Welcome","mymailtemplate",email,{"name":firstname,"password":password})
        return HttpResponseRedirect(reverse("all-member"))
    else:
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(userid=uid)
            context={
                    "uid":uid,
                    "cid":cid,         
                }
            return render(request,"chairmanapp/add_member.html",context)
        else:
            return render(request,"chairmanapp/login.html")
        
def all_member(request):
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(userid=uid)
            mall=Member.objects.all()
            context={
                    "uid":uid,
                    "cid":cid,
                    "mall":mall,         
                }
            return render(request,"chairmanapp/members.html",context)

def cmember_profile(request,pk):
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(userid=uid)
            mid = Member.objects.get(id=pk)
            mall=Member.objects.all()
            context={
                    "uid":uid,
                    "cid":cid,
                    "mid":mid,
                    "mall":mall,         
                }
            return render(request,"chairmanapp/cmember_profile.html",context)

def cmember_edit(request,pk):
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(userid=uid)
            mid = Member.objects.get(id=pk)
            context={
                    "uid":uid,
                    "cid":cid,
                    "mid":mid,
                }
            return render(request,"chairmanapp/add_member.html",context)

def cmember_delete(request,pk):
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(userid=uid)
            mid = Member.objects.get(id=pk)
            mid.delete()
            return HttpResponseRedirect(reverse("all-member"))

def add_notice(request):
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(userid=uid)
            if request.POST:
                nid=Notice.objects.create(userid=uid,
                                        title=request.POST['notice_title'],
                                        description=request.POST['notice_description'])
                context={
                    'cid' : cid,
                    'uid' : uid,
                }
                return render(request,"chairmanapp/add_notice.html",context)
            else:
                context={
                    'cid' : cid,
                    'uid' : uid,
                }
                return render(request,"chairmanapp/add_notice.html",context)

def forgot_password(request):
    if request.POST:
        email=request.POST['email']
        uid=User.objects.get(email=email)
        otp=random.randint(1111,9999)
        uid.otp=otp
        uid.save()
        mysendmail("Forgot Password","mymailtemplateotp",email,{'otp':otp})
        return render(request,"chairmanapp/changepassword.html",{'email':email})
    else:
        return render(request,"chairmanapp/forgotpassword.html")
    
def change_password(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        otp=request.POST['otp']
        confirmpassword=request.POST['confirmpassword']

        uid=User.objects.get(email=email)
        if otp == str(uid.otp):
            if password == confirmpassword:
                uid.password=password
                uid.save()
                return render(request,"chairmanapp/login.html")

def notice(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        ncount=Notice.objects.all()
        context={
                    'cid' : cid,
                    'uid' : uid,
                    'ncount' : ncount,
                }
        return render(request,"chairmanapp/notice.html",context)

def ajax(request):
    return render(request,"chairmanapp/ajax_index.html")

def addDataPage(request):
    print(request.POST["name"])
    sid=Student.objects.create(name=request.POST['name'],
                               subject=request.POST['subject'])
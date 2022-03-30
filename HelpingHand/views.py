
import email
from os import name
from pickletools import read_unicodestring8
#from defer import return_value


from django.forms import EmailField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
import re
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist



from . models import User

import HelpingHand
# Create your views here.

email_reg=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
users=[]


def index(request):
        return render(request ,'HelpingHand/index.html',{});
def register(request):
     return render(request ,'HelpingHand/register.html',{});
def login(request):
     return render(request ,'HelpingHand/login.html',{});
def profile(request):
   
    query_results=User.objects.all().filter(email='rocky@gmail.com');
    context={'query_results':query_results}
    return render(request ,'HelpingHand/profile.html',context);

def registered(request):
    if request.method == 'POST':
        data = { 'name': request.POST['name'],
                'password': request.POST['password'],
                'email': request.POST['mail']
        }
        user=User.objects.create(name=data['name'],email=data['email'],password=data['password'])
        User.save(user)
        
        print(User.objects.all());
        
        
        if re.match(email_reg, data['email']):
            users.append(data);
            print("data ---> ", data);
            return redirect("/login")
        else:
            return redirect("/register")
    else:
        form = profile()
        return render("register.html",  {'form':form})
def Logged_in(request):
    if request.method =='POST':
        try:
            user=User.objects.get(email=request.POST['mail'], password=request.POST['password'])
            print("---------> ", user)
            return redirect('/profile')
        except User.DoesNotExist:
            return redirect("/register")
    else:
        return redirect("/")

   # return HttpResponse("Your Data has been saved");
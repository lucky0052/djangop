from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from userapp.models import CustomUser
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index.html')



def signup(request):
    if request.method == 'POST':
        data = request.POST
        uname = data.get('username')
        email = data.get('email')
        password = data.get('password')
        repassword = data.get('repassword')
        user1 = CustomUser.objects.filter(Q(username = uname.lower()) | Q(email=email))
        if user1.exists():
            messages.error(request,"Already exist")
        else:
            if password == repassword: 
                user = CustomUser(username=uname.lower(),email=email.lower())
                user.set_password(password)
                user.save()
                messages.success(request,'Account Created Successfully')
            else:
                messages.error(request,'Password must be same')
        print('Successful')
    return render(request,'signup.html')



def loginp(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('loginemail')
        password = data.get('loginpassword')
        user = CustomUser.objects.filter(email=email)
        if not user.exists():
            messages.error(request,'User doesn\'t exist')
        isuser = authenticate(request,email=email,password=password)
        if isuser is not None:
            login(request,isuser)
            return redirect('mainview')
        else:
            messages.error(request,'Invalid username and password')

    return render(request,'login.html')

@login_required
def mainpage(request):
    return HttpResponse('Main Page')


def logoutp(request):
    logout(request)
    return redirect('home_view')

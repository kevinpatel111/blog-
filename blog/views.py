from django.shortcuts import render,redirect
from blog.models import author
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from functools import wraps



def login_required(f):
    @wraps(f)
    def decorated_func(request,*args, **kwargs):
        if "email" in request.session:
           return f(request, *args, **kwargs)
        else:
            return redirect('login_user')

    return decorated_func

def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")

        if password == password_confirmation:
            try:
                user = author.objects.create(
                    name=name,
                    phone=phone,
                    email=email,
                    password=make_password(password),
                )
                return redirect('login_user')
            except Exception as e:
                print("An error occurred:", str(e))
    return render(request,"register_user.html")


def login_user(request):
    if request.method == 'POST':    
        email = request.POST.get("email", None)
        password = request.POST["password"]
        user = author.objects.filter(email=email).first() 
        
        if user:
            if check_password(password, user.password):
                request.session["email"] = email
                return redirect('postlist')
        
    return render(request,'login_user.html')

@login_required
def postlist(request):
    session_email = request.session["email"]
    queryset = Post.objects.filter(status=1)
    return render(request, 'postlist.html', {"post_list": queryset})


def PostDetail(request,slug):
    model = get_object_or_404(Post, slug=slug)
    # model = Post
    context = {
        'post': model,
    }
    return render(request,'post_detail.html',context)


def forgot_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")
        user = author.objects.all() 
        if check_password(password, user.password):
            return redirect('login_user')
    return render(request,'forgot_password.html')



def do_logout(request):
    logout(request)
    return redirect('/')

def home(request):
    # queryset = Post.objects.filter(status=1)
    return render(request,'home.html')

def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")

        if password == password_confirmation:
            try:
                user = author.objects.create(
                    name=name,
                    phone=phone,
                    email=email,
                    password=make_password(password),
                )
                return redirect('login_user')
            except Exception as e:
                print("An error occurred:", str(e))
    return render(request,"register_user.html")


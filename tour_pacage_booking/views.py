from django.shortcuts import render,redirect
from .models import Category, Product,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm,UpdateUserForm,ChangePasswordForm,UserInfoForm
from django import forms
from django.db.models import Q
import json
from cart.cart import Cart

def search(request):
     if request.method == "POST":
        searched = request.POST['searched']
        #quary for product in model product

        searched  = Product.objects.filter(Q(name__icontains = searched) | Q(discription__icontains = searched) )

        if not searched : 
            messages.success(request , 'The Product dose not exist.. please try again..')
            return render(request,'search.html',{})
        else: 
            return render(request,'search.html',{'searched':searched})
        

     else :
        return render(request,'search.html',{})


def update_info(request):
     if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None ,instance=current_user)
        if form.is_valid():
            form.save()
            
            messages.success(request,'your info has been updated !!')
            return redirect('home')
        return render(request,'update_info.html',{'form':form})
     else:
        messages.error(request,'you must be loggend in ')
        return redirect('home')
     
    

def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

    

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None ,instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,'user has been updated !!')
            return redirect('home')
        return render(request,'update_user.html',{'user_form':user_form})
    else:
        messages.error(request,'you must be loggend in ')
        return redirect('home')



def category_summary(request):
    categories = Category.objects.all()
    return render(request,'category_summary.html',{'categories':categories})


def category(request,foo):
    #replace '-' hyphens with spaces
    foo = foo.replace('-',' ')
    #grab category from url
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products , 'category':category})

    except:
        messages.success(request,('that category dosenot exist'))
        return redirect('home')


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


# Create your views here.
def home(request):
   products = Product.objects.all
   return render(request, 'home.html', {'products': products})

def about(request):
   return render(request, 'about.html')


def login_user(request):
   if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=username, password=password)
          if user is not None:
              login(request, user)
              # cart stuff 
              current_user = Profile.objects.get(user__id=request.user.id)
                #get saved cart 
              saved_cart = current_user.old_cart
              #cnvert db string to python  dicsinory 
              if saved_cart:
                   #convert to json 
                   converted_cart = json.loads(saved_cart)
                    #add loaded cart dictionary to session
                   cart = Cart(request) 
                   for key,value in converted_cart.items():
                        cart.db_add(product=key,quantity=value)





              messages.success(request,("You Have Been Logged In!"))
              return redirect('home')
          else :
            messages.success(request,("There was an error, please try again..."))
          return redirect('login')
   
   else:
      return render(request, 'login.html',{})

def logout_user(request):
   logout(request)
   messages.success(request,("your have been logged out"))
   return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Login the user after successful registration
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Username Created - Please Fill Out Your User Info Below...")
                return redirect('update_info')
            else:
                messages.error(request, "Authentication failed. Please try again.")
                return redirect('register')
        else:
            print(form.errors)  # Debugging: Print the form errors
            messages.error(request, "Whoops! There was a problem registering, please try again...")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})


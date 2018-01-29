from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import MedForm
from .forms import SignUpForm
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
def index(request):
	return HttpResponse("Hello okhati users!!!")

def home(request):
	return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    
    

    
    return render(request, 'signup.html', {'form': form})

def myStore(request):
	pass

@login_required
def formy(request):
	#r=requests.post("https://okhati.000webhostapp.com/db_connect.php",data={'username':'username','medicine':'medicine','price':'price','forDisease':'forDisease'})
	
	#r=requests.post("https://okhati.000webhostapp.com/db_connect.php",data={'username':'akeleyyy','medicine':'rasteinhj'})
	
	if request.method=='POST':
		form =MedForm(request.POST )
		if form.is_valid():
			if request.user.is_authenticated: 
				medicine = form.cleaned_data.get('medName')
				price = form.cleaned_data.get('price')
				username=request.POST.get('username')
				forDisease=form.cleaned_data.get('forDisease')
				r=requests.post("https://okhati.000webhostapp.com/db_connect.php",data={'username':'username','medicine':medicine,'price':price,'forDisease':forDisease})
				print(r.status_code, r.reason)
				print (medicine,price,username,forDisease)
				return HttpResponseRedirect('/thanks/')
			else:
				return HttpResponse('Please sign in')

			
			
			#medicine=form.cleaned_data('medName
	else:
		form=MedForm()

	
	return render(request,'medForm.html',{'form':form})


def home(request):
	
	#email=request.user.email
	username=request.user.username
	email='itsmeashutosh43@gmail.com'
	r=requests.post("https://okhati.000webhostapp.com/PharmacyReg.php",data={'name':username,'email':email})
	print (r.status_code,r.reason)

	return render (request,'homey.html')




from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        
        if form.is_valid():
            user = form.save()  
            login(request,user)
            
            return redirect('/')
    else:
        form = SignupForm()
        
    return render(request, 'accounts/signup.html',{
        'form':form,
    }) 
def profile(request):
    return render(request,'accounts/profile.html')
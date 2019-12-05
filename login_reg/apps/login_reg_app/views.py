from django.shortcuts import render, redirect, HttpResponse
from .models import Registration
from django.contrib import messages
import bcrypt

# Main loggin and Registration page
def lor(request):
    print('*'*80)
    print('Page loaded successfully')
    return render(request, 'login_reg_app/lor.html')



# Registration redirect processing
def reg_pro(request):
    errors = Registration.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print('*'*80)
        print(errors)
        return redirect('/lor')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = Registration.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email = request.POST['email'], password = pw_hash)
        request.session['registered'] = user.id
    return redirect('/success')



#Rendering page after user was sucessfully registered
def success(request):
    if 'registered' not in request.session:
        return redirect('/lor')
    else:
        context = {
            "users" : Registration.objects.get (id=int(request.session['registered']))
        }
    print('*'*80)
    print('User sucessfully registerd!!!')
    return render(request,'login_reg_app/success.html', context)



#this is the process routh for logging in   
def log_pro(request):
    errors = Registration.objects.log_val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print('*'*80)
        print(errors)
        return redirect('/lor')
    else:
        
        user = Registration.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['registered'] = user.id
            return redirect('/success')
        if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            messages.error(request, "Invalid Password.")
        return redirect('/lor')
        


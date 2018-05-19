from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request):
    return render(request, 'loginreg/index.html')

def register(request):
    # name, alias, email, password, password_confirm, dob
    user = User.objects.validateUser(request.POST['name'], request.POST['alias'], request.POST['email'], request.POST['password'], request.POST['confirm_password'], request.POST['birthday'])
    if user[0] == True:
        # user[1].name
        
        request.session['user_id']= user[1].id
        request.session['user_name'] = user[1].name


        return redirect('/quotes')
    
    for errormessage in user[1]:
        messages.error(request, errormessage)
        print errormessage
    return redirect('/')

def login(request):
    user = User.objects.validateLogin(request.POST['email'], request.POST['password'])
    print "*****"
    # print user[1].email  
    #(False, [u'Email is not found in database']) if the user is not in the datebase it prints this.
    # (True, <User: User object>) if the user is in the datebase and its a valid login
    print "*****"
    if user[0]== True:
        request.session['user_id'] = user[1].id
        request.session['user_name'] = user[1].name
        return redirect('/quotes')
    else:
        for errormessage in user[1]:
            messages.error(request, errormessage)
            print errormessage
        return redirect('/')
        

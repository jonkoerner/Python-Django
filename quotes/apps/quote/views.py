from django.shortcuts import render, redirect
from .models import User, Quote 
from django.contrib import messages


def addquote(request):
    current_user = User.objects.get(id=request.session['user_id'])
    print '*****'
    print current_user
    print '*****'
    quote = Quote.objects.validateQuote(request.POST['quoted_by'], request.POST['message'], current_user)
    return redirect('/quotes')


def showquotes(request):
    all_quotes = Quote.objects.all()
    user = User.objects.get(id=request.session['user_id'])
    notFav = Quote.objects.exclude(follower= user)
    favquotes = Quote.objects.filter(follower = user)
    context = {
        'everyquote' : all_quotes,
        'notFavorite' : notFav,
        'favorite' : favquotes
    }
    return render(request, 'quote/home.html', context)


def show_user(request, user_id):
    print user_id
    user = User.objects.get(id= user_id)
    quote = Quote.objects.filter(posted_by = user)
    context = {
        'User' : user,
        'Quote' : quote
    }
    return render(request, 'quote/user.html', context)

def addtoFav(request, quote_id):
    quote = Quote.objects.get(id= quote_id)
    user = User.objects.get(id=request.session['user_id'])
    quote.follower.add(user)
    return redirect('/quotes')


def removefromFav(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    user = User.objects.get(id=request.session['user_id'])
    quote.follower.remove(user)
    return redirect('/quotes')

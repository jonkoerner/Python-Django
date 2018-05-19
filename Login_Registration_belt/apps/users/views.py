from django.shortcuts import render, redirect

def index(request):
    return render('users/new.html')

def new(request):
    return render(request, '/users/new')

def create(request):
    print request.post
    if request.method == 'Post':
        result = User.objects.validate_registration(request.POST)
        print result
        print result['status']
    if result['status'] == False:
        for error in result['errrs']:
            messages.error(request, error)
        return redirect('/users/new')
    else:
        request.session['user_id'] =result['user'].id
    return redirect('/users/success')


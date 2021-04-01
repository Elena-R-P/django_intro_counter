from django.shortcuts import render, redirect

def index(request):
    if 'visit_counter' not in request.session:
        request.session['visit_counter'] = 0
    else:
        request.session['visit_counter'] += 1
        print("Key named counter exists")
    return render(request, 'index.html')

def plus_two(request):
    request.session['visit_counter'] += 1
    return redirect('/')
    # return render(request, 'index.html')

def destroy_session(request):
    del request.session['visit_counter']
    return redirect('/')



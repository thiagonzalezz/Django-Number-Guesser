from django.shortcuts import render
import random

# Create your views here.
def index(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1,10)
        request.session['attempts'] = 0
    
    message = ''
    if request.method == 'POST':
        guess = int(request.POST['number'])
        request.session['attempts'] += 1
        
        if guess < request.session['random_number']:
            message = 'The number is bigger'
        elif guess > request.session['random_number']:
            message = 'The number is smaller'
        else:
            message=f'You guessed the number in {request.session["attempts"]} attempts'
            del request.session['random_number']
            del request.session['attempts']
    return render(request, 'index.html', {'message': message})
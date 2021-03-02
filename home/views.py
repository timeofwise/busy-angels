from django.shortcuts import render
import random

# Create your views here.

def home(request):
    rand = random.randint(1,8)

    return render(request, 'home/home.html', {
        'rand' : rand,
    })
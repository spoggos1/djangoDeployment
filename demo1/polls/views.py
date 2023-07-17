from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<h2 style='color:blue'; font-family='sans-serif'>Hello, World!</h2>")
    return render(request, 'hello/index.html')
   
def nick(request):
    return HttpResponse("<h2 style='color:blue'; font-family='sans-serif'>Hello, Nick!</h2>")
    
def helen(request):
    return HttpResponse("<h2 style='color:blue'; font-family='sans-serif'>Hello, Helen!</h2>")

def greet(request, name):
    # return HttpResponse(f"<h2 style='color:blue'; font-family='sans-serif'>Hello, {name.capitalize()}!</h2>")
    return render(request, 'polls/greet.html', {'name': name.capitalize()})
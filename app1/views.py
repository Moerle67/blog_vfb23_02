from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'app1/start.html')

from django.shortcuts import render

def index(request):
    return render(request, 'services/index.html', {})

def web(request):
    return render(request, 'services/web.html', {})
    
def software(request):
    return render(request, 'services/software.html', {})

def training(request):
    return render(request, 'services/training.html', {})
    
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})
    
def feedback(request):
    if request.method == 'POST':
        pass
        
        redirect('about')
    else:
      redirect('about')
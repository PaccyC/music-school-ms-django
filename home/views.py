from django.shortcuts import redirect, render

# Create your views here.


def landingpage(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    return render(request, 'home/home.html')
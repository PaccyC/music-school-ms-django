from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import CustomUser
from .forms import RegisterForm,UpdateProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

@require_http_methods(["GET", "POST"])
def create_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        else:
            return JsonResponse(form.errors, status=400)

    form = RegisterForm()
    return render(request, "create_user.html", {"form": form})


@require_http_methods(["GET"])
def get_users(request):
    users = CustomUser.objects.all()
    if users.exists():
        
        return render(request, "user_list.html",{'users':users})
    else:
        return JsonResponse({"message": "No users found"}, status=404)
    



@require_http_methods(["POST"])
def update_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    form = UpdateProfileForm(request.POST, instance=user)
    
    if form.is_valid():
        user = form.save()
        return JsonResponse({"username": user.username, "email": user.email}, status=200)
    else:
        return JsonResponse(form.errors, status=400)

 
@require_http_methods(["POST", "DELETE"])  
def remove_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    user.delete()
    return JsonResponse({"message": "User deleted successfully"}, status=204)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')
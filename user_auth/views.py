from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserModelSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
# Create your views here.


@api_view(["GET","POST"])
def create_user(request):
    if request.method == "POST":
        # Create User logic here
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=200)
     
     


@api_view(["GET"])
def get_users(request):
    users= CustomUser.objects.all()
    print("Users found",users)
    if users.exists():
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data,status=200)
        
    else:
        return Response({"message": "No users found"}, status=status.HTTP_404_NOT_FOUND)
    
    

@api_view(["PUT"])
def update_user(request,pk):
    user= CustomUser.objects.get(pk=pk)
    if not user:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserModelSerializer(user, data=request.data,partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK)
        
        
 
@api_view(["DELETE"])       
def remove_user(request,pk):
    user= CustomUser.objects.get(pk=pk)
    if not user:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
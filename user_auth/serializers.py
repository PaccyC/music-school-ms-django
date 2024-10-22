from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class UserModelSerializer(ModelSerializer):
    class Meta:
        model= CustomUser
        fields= ["id","first_name","last_name","email","username","phone_number","role","password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }
        
    
    
    def create(self, validated_data):
           user=CustomUser.objects.create(
               username=validated_data["username"],
               email=validated_data["email"],
               phone_number=validated_data["phone_number"],
               role=validated_data["role"],
               first_name=validated_data["first_name"],
               last_name=validated_data["last_name"],
               )
               
           
           user.set_password(validated_data["password"])
           user.save()
           return user
       
    def update(self, instance, validated_data):
           instance.first_name=validated_data.get("first_name",instance.first_name)
           instance.last_name=validated_data.get("last_name",instance.last_name)
           instance.email=validated_data.get("email",instance.email)
           instance.phone_number=validated_data.get("phone_number",instance.phone_number)
           instance.role=validated_data.get("role",instance.role)
           instance.password=make_password(validated_data.get("password",instance.password))
           instance.save()
           return instance
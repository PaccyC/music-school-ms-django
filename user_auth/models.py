from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomUser(User):
    
    ROLE_CHOICES=[
       ( "student","Student"),
       ("teacher","Teacher"),
       ("admin","Admin"),
    ]
    
    phone_number=models.CharField(max_length=255,null=True)
    role= models.CharField(max_length=20,choices=ROLE_CHOICES)
   
    
    def __str__(self):
        return self.username 
    
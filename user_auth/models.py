from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.contrib.auth.hashers import make_password
# Create your models here.


class CustomUser(AbstractUser):

    
    ROLE_CHOICES=[
       ( "student","Student"), 
       ("teacher","Teacher"),
       ("admin","Admin"),
    ]
    
    id= models.AutoField(primary_key= True)
    phone_number=models.CharField(max_length=255,null=True)
    role= models.CharField(max_length=20,choices=ROLE_CHOICES)
   
    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if self.pk is None or not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username 

from django.db import models
from user_auth.models import CustomUser
# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    teacher=models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'teacher'})
    start_date=models.DateField()
    end_date=models.DateField()
    schedule=models.TextField()
    
    def __str__(self):
        return self.name
    

class Enrollment(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    anrollment_date=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"    
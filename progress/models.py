from django.db import models
from user_auth.models import CustomUser
from courses.models import Course
# Create your models here.


class Attendance(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    date=models.DateField()
    present= models.BooleanField(default=False)
    
    def __str__(self):
        return f"Attendance for {self.student.username} on {self.date}"
    
    
class Grade(models.Model):
      student=models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
      course=models.ForeignKey(Course,on_delete=models.CASCADE)
      score=models.DecimalField(max_digits=5,decimal_places=2)
      feedback=models.TextField(blank=True)
        
      def __str__(self):
            return f"Grade for {self.student.username} in {self.course.name}: {self.score}"
        


class Performance(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    event_name=models.CharField(max_length=100)
    date=models.DateField()
    performance_feedback= models.TextField(blank=True)
    
    
    def __str__(self):
        return f"Performance for {self.student.username} at {self.event_name} on {self.date}"
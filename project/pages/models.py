from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    studentID = models.CharField(max_length=8, unique=True)
    Email = models.EmailField()
    date = models.DateField()
    GPA = models.DecimalField(max_digits=3,decimal_places=2)
    levels = [ ('Level 1','Level 1'), ('Level 2','Level 2'),
            ('Level 3','Level 3'), ('Level 4','Level 4')]
    level = models.CharField(max_length=50, choices=levels)
    departments = [('IS', 'IS'), ('CS', 'CS'),
                   ('IT', 'IT'), ('DS', 'DS'), ('AI', 'AI')]
    department = models.CharField(max_length=50, choices=departments)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=50 ,choices=[('Female','Female'), ('Male', 'Male')])
    status = models.CharField(max_length=50,choices=[('Active', 'Active'), ('Inactive','Inactive')])
    def __str__(self):
        return self.studentID
    class Meta:
        ordering = ['status','studentID']


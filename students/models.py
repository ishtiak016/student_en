from pickle import TRUE
from django.db import models

from django.forms import ModelForm, TextInput, EmailInput
# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(max_length=100)
    smtpemail = models.EmailField(blank=True, null=True, max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class deparment_info(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    department_id = models.CharField(primary_key = True,max_length=200)
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name

class student_info(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    deparment_info =models.ForeignKey(deparment_info,on_delete=models.CASCADE)
    student_id = models.CharField(primary_key = True,max_length=200)
    student_name = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    mothers_name = models.CharField(max_length=200)
    date_of_birth=models.DateField()
    status=models.CharField(max_length=20, choices=STATUS, null=True, blank=True)
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender=models.CharField(max_length=20, choices=Gender, null=True, blank=True)
    mobile_number = models.CharField(max_length=200, null=True, blank=True)
    pre_addresss = models.CharField(max_length=200, null=True, blank=True)
    per_address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    BloodGroup = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    
    )
    BloodGroup=models.CharField(max_length=20, choices=BloodGroup, null=True, blank=True)
    def __str__(self):
        return self.student_name

class staff_info(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    deparment_info =models.ForeignKey(deparment_info,on_delete=models.CASCADE)
    staff_id = models.CharField(primary_key = True,max_length=200)
    staff_name = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    mothers_name = models.CharField(max_length=200)
    date_of_birth=models.DateField()
    status=models.CharField(max_length=20, choices=STATUS, null=True, blank=True)
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender=models.CharField(max_length=20, choices=Gender, null=True, blank=True)
    mobile_number = models.CharField(max_length=200, null=True, blank=True)
    pre_addresss = models.CharField(max_length=200, null=True, blank=True)
    per_address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    BloodGroup = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    
    )
    BloodGroup=models.CharField(max_length=20, choices=BloodGroup, null=True, blank=True)
    def __str__(self):
        return self.staff_name

class subject_info(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    deparment_info =models.ForeignKey(deparment_info,on_delete=models.CASCADE)
    subject_id = models.CharField(primary_key = True,max_length=200)
    subject_name = models.CharField(max_length=200)
    credit = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name
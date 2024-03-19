from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=10)        # chairman or member
    otp=models.IntegerField(default=143)
    is_active=models.BooleanField(default=True)
    is_verify=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

    def __str__(self) -> str:
        return self.email

class Chairman(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20,null=True)
    contactno=models.CharField(max_length=20)
    houseno=models.CharField(max_length=8)
    pic=models.FileField(upload_to='media/images/',default='Default.jpg')

    def __str__(self) -> str:
        return self.firstname

class Member(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20,null=True)
    contactno=models.CharField(max_length=20)
    houseno=models.CharField(max_length=8)
    vehicle_details=models.CharField(max_length=20,null=True)
    occupation=models.CharField(max_length=20,null=True)
    no_familymembers=models.CharField(max_length=20,null=True)
    job_address=models.TextField(null=True)
    blood_grp=models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=20,null=True)
    birthdate=models.DateField(null=True)
    joining_date=models.DateTimeField(auto_now_add=True,blank=False)
    pic=models.FileField(upload_to='media/images/',default='Default.jpg')

class Notice(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

class Student(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
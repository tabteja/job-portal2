from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from app.models import User

# Create your models here.
    
JOB_TYPE = (
    ('Full time', "Full time"),
    ('Part time', "Part time"),
    ('Internship', "Internship"),
)
EXPERIENCE = (
    ('Fresher',"Fresher"),
    ('Experience',"Experience"),
)
BENIFITS = (
    ('Work From Home',"Work From Home"),
    ('Work From Office',"Work From Office"),
    ('Remote Job',"Remote Job"),
    ('On-site Job',"On-site Job"),
    ('Hybrid Job',"Hybird Job"),
)

class Job(models.Model):  
    title = models.CharField(max_length=300)
    Experience = models.CharField(choices=EXPERIENCE, max_length=20)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    package = models.IntegerField()
    benefits = models.CharField(choices=BENIFITS, max_length=50)
    job_type = models.CharField(choices=JOB_TYPE, max_length=10)
    qualifications = models.CharField(max_length=100)
    description = models.TextField()
    last_date = models.DateTimeField()
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    @staticmethod
    def all_jobs():
        return Job.objects.all()
        
    
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.get_full_name()
    
    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
     
    def __str__(self):
        return self.username
    
    
class Resume(models.Model):
    upload = models.FileField(upload_to='Resume', max_length=200)
     
    def __str__(self):
        return self.upload
from django import forms  
from app.models import *  
    
class ResumeForm(forms.ModelForm):  
    class Meta:  
        model = Resume  
        fields = "__all__"
        
        
class JobForm(forms.ModelForm):  
    class Meta:  
        model = Job 
        fields = "__all__"
        

        
class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = "__all__"
        
        
class ApplicantForm(forms.ModelForm):  
    class Meta:  
        model = Applicant  
        fields = "__all__"
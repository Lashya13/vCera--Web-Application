# forms.py
from django import forms
from .models import manager_form, HR, Employee

class MangerOpenPosition(forms.ModelForm):
    class Meta:
        model = manager_form
        fields = ['Pillar','JobID','JobTitle','PrimarySkills','SecondarySkills','Location','Experience','Certifications']


class HR(forms.ModelForm):
    class Meta:
        model = HR
        fields = ['Pillar','JobID','JobTitle','PrimarySkills','SecondarySkills','Location', 'Experience' ]

 
class Employee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name','gin_number','current_role','previous_role','experience','pillar','location','primary_skills','secondary_skills','certifications','project_history','key_achievements','performance_data','manager_feedback','target_role']

   
class HRQueryForm(forms.Form):
    Pillar = forms.CharField(max_length=255)
    #JobID = models.CharField(max_length=100)
    #JobTitle = models.CharField(max_length=255)  # Varchar field for job title
    PrimarySkills = forms.CharField(max_length=255)  # Varchar for primary skills
    SecondarySkills = forms.CharField(max_length=255)  # Varchar for secondary skills
    Location = forms.CharField(max_length=255)  # Varchar for location
    Experience = forms.CharField(max_length=255)  # Varchar for experience

class PillarQueryForm(forms.Form):
    PILLAR_CHOICES = [
        ('OS-IT-DO', 'OS-IT-DO'),
        ('OS-IT-DES', 'OS-IT-DES'),
        ('OS-IT-SAP', 'OS-IT-SAP'),
        ('OS-IT-DA', 'OS-IT-DA'),
        # Add more choices as needed
    ]
    
    pillar = forms.ChoiceField(choices=PILLAR_CHOICES, label="Select Pillar")


class PillarSearchForm(forms.Form):
    Pillar = forms.ChoiceField(
        choices=[(manager['Pillar'], manager['Pillar']) for manager in manager_form.objects.values('Pillar').distinct()],
        label="Select the Pillar"
    )

class JobIDForm(forms.Form):
    JobID = forms.ModelChoiceField(queryset=manager_form.objects.none(), label="Select the Job ID")
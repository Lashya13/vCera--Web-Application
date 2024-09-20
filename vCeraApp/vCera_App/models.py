from django.db import models

# Create your models here.

from django.db import models

class manager_form(models.Model):
    Pillar = models.CharField(max_length=255)
    JobID = models.CharField(max_length=100, unique=True)
    JobTitle = models.CharField(max_length=255)
    PrimarySkills = models.CharField(max_length=255)  # Or use TextField if needed
    SecondarySkills = models.CharField(max_length=255, blank=True, null=True)  # Optional field
    Location = models.CharField(max_length=100)
    Experience = models.CharField(max_length=50)  # You can also use IntegerField for exact years
    Certifications = models.CharField(max_length=50)
    def __str__(self):
        return self.JobID

class HR(models.Model):
    Pillar = models.CharField(max_length=255)
    JobID = models.CharField(max_length=100)
    JobTitle = models.CharField(max_length=255)  # Varchar field for job title
    PrimarySkills = models.CharField(max_length=255)  # Varchar for primary skills
    SecondarySkills = models.CharField(max_length=255)  # Varchar for secondary skills
    Location = models.CharField(max_length=255)  # Varchar for location
    Experience = models.CharField(max_length=255)  # Varchar for experience

    def __str__(self):
        return f"{self.JobTitle} ({self.JobID})"


class Employee(models.Model):
    employee_name = models.CharField(max_length=255)  # Employee Name as a varchar
    gin_number = models.IntegerField()  # GIN number as an integer
    current_role = models.CharField(max_length=255)  # Current role
    previous_role = models.CharField(max_length=255)  # Previous role
    experience = models.CharField(max_length=255)  # Experience details
    pillar = models.CharField(max_length=255)  # Organizational pillar
    location = models.CharField(max_length=255)  # Job location
    primary_skills = models.CharField(max_length=255)  # Primary skills
    secondary_skills = models.CharField(max_length=255)  # Secondary skills
    certifications = models.CharField(max_length=255)  # Certifications
    project_history = models.TextField()  # Project history (varchar, can be large so TextField is better)
    key_achievements = models.TextField()  # Key achievements (varchar, can be large so TextField is better)
    performance_data = models.TextField()  # Performance data
    manager_feedback = models.TextField()  # Manager feedback
    target_role = models.CharField(max_length=255)  # Target role (Job Title)

    def __str__(self):
        return f"{self.employee_name} ({self.gin_number})"

from django.db import models
from django.utils import timezone

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('networking', 'Networking'),
        ('database', 'Database Management'),
        ('hardware', 'Hardware Engineering'),
        ('web', 'Web Development'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=50, help_text="Proficiency level (0-100)")
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    
    class Meta:
        ordering = ['category', '-proficiency']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tools_used = models.CharField(max_length=300, help_text="Comma-separated tools")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=Skill.CATEGORY_CHOICES)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-featured', '-created_date']
    
    def __str__(self):
        return self.title
    
    def get_tools_list(self):
        return [tool.strip() for tool in self.tools_used.split(',')]


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="General Inquiry")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, Certification
from .forms import ContactForm

def index(request):
    """Home page view"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'featured_projects': featured_projects,
    }
    return render(request, 'portfo_app/index.html', context)

def about(request):
    """About page view"""
    certifications = Certification.objects.all()
    context = {
        'certifications': certifications,
    }
    return render(request, 'portfo_app/about.html', context)

def skills(request):
    """Skills page view"""
    networking_skills = Skill.objects.filter(category='networking')
    database_skills = Skill.objects.filter(category='database')
    hardware_skills = Skill.objects.filter(category='hardware')
    web_skills = Skill.objects.filter(category='web')
    
    context = {
        'networking_skills': networking_skills,
        'database_skills': database_skills,
        'hardware_skills': hardware_skills,
        'web_skills': web_skills,
    }
    return render(request, 'portfo_app/skills.html', context)

def projects(request):
    """Projects page view"""
    all_projects = Project.objects.all()
    category_filter = request.GET.get('category', 'all')
    
    if category_filter != 'all':
        all_projects = all_projects.filter(category=category_filter)
    
    context = {
        'projects': all_projects,
        'current_filter': category_filter,
    }
    return render(request, 'portfo_app/projects.html', context)

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portfo_app/contact.html', context)
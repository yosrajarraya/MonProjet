from multiprocessing import context
from django.contrib.auth import authenticate, login
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Personnel, Project, Service
from .models import Project
from .forms import ProjectForm
from .forms import ServiceForm
from .models import Service

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PersonnelForm
from .models import Personnel

from django.shortcuts import render, get_object_or_404, redirect

from .models import Team
from .forms import TeamForm

def index(request):
    return render(request, 'artyprod/base.html')
def home_index(request):
    # récupération des 5 projets les plus récents
    recent_projects = Project.objects.order_by('-start_date')
    
    # récupération de tous les services proposés
    services = Service.objects.all()
    personnel = Personnel.objects.all()
    
    # récupération du premier projet
    first_project = Project.objects.first()
    
    # renvoi du résultat à un template HTML pour affichage
    return render(request, 'artyprod/home.html', {
        'recent_projects': recent_projects,
        'services': services,
        'personnel': personnel,
        'project': first_project,
    })

def login_index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'artyprod/login.html',{'form': form})

#@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'artyprod/project_create.html', {'form': form})

def service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceForm()
    return render(request, 'artyprod/service.html', {'form': form})

def personnel_create(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            personnel = form.save(commit=False)
            #personnel.user = request.user
            personnel.save()
            messages.success(request, 'Le personnel a été ajouté avec succès.')
            return redirect('home')
    else:
        form = PersonnelForm()
    return render(request, 'artyprod/personnel_create.html', {'form': form})




def team_list(request):
    teams = Team.objects.all()
    return render(request, 'artyprod/team_list.html', {'teams': teams})
from django.shortcuts import render, get_object_or_404
from .models import Team

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    members = team.members.all()
    projects = team.projects.all()  # Récupérer tous les projets associés à l'équipe

    return render(request, 'artyprod/team_detail.html', {'team': team, 'members': members, 'projects': projects})



def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            selected_members = form.cleaned_data['members']
            selected_projects = form.cleaned_data['projects']  # Récupérer les projets sélectionnés du formulaire
            team.members.set(selected_members)
            team.projects.set(selected_projects)  # Associer les projets sélectionnés à l'équipe
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'artyprod/team_create.html', {'form': form})



def team_update(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_detail', team_id=team_id)
    else:
        form = TeamForm(instance=team)
    return render(request, 'artyprod/team_update.html', {'form': form, 'team': team})

def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'artyprod/team_delete.html', {'team': team})





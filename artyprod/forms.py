
from django import forms
from .models import Project
from .models import Personnel
from .models import Service
from .models import Team, Personnel

from django import forms


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Personnel.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Team
        fields = ['name', 'description', 'creation_date', 'members', 'projects']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('type', 'desc')
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 4}),
        }
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'desc', 'start_date', 'end_date', 'is_done', 'details', 'services']
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['name', 'cv_file', 'photo_file', 'linkedin']
from django.contrib import admin

# Register your models here.
from .models import*
from .models import Service
admin.site.register(Service)
from .models import Detail
admin.site.register(Detail)
from .models import (Project)
admin.site.register(Project)
from .models import Team
admin.site.register(Team)
from .models import Personnel
admin.site.register(Personnel)

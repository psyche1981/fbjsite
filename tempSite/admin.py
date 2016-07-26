from django.contrib import admin

# Register your models here.

from .models import League
from .models import Team

admin.site.register(League)
admin.site.register(Team)

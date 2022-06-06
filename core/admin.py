from django.contrib import admin
from core.models import Agenda
# Register your models here.


class agendaAdm(admin.ModelAdmin):
    list_display = ('titulo', 'data_agenda',
                    'data_criacao')


admin.site.register(Agenda, agendaAdm)

from django.contrib import admin
from .models import Project, Status, Type, Ticket, Account

admin.site.register(Account)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
admin.site.register(Ticket)

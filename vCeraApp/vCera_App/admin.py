from django.contrib import admin
from .models import HR, Employee, manager_form
# Register your models here.

admin.site.register(manager_form)
admin.site.register(HR)
admin.site.register(Employee)

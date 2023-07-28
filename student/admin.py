

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import student
from .models import fees

admin.site.register(student)
admin.site.register(fees)

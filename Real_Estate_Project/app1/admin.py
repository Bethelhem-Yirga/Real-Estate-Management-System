from django.contrib import admin
from .models import Properties, Registration,Application
admin.site.register(Registration)
admin.site.register(Properties)
admin.site.register(Application)

# Register your models here.
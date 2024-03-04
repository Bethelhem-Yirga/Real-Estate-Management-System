from django.contrib import admin
from .models import MarketingManager, Properties, Registration
admin.site.register(Registration)
admin.site.register(Properties)
admin.site.register(MarketingManager)
# Register your models here.
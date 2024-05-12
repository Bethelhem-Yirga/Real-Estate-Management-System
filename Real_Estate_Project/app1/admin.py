from django.contrib import admin

from .models import AskMaintenance, ContactMessage, Employee, MarketingManager, Properties, Registration ,Salesperson


from .models import Properties, Registration,Application,Report

admin.site.register(Registration)
admin.site.register(Properties)
admin.site.register(Application)
admin.site.register(Report)

from .models import MarketingManager, Properties, Registration,Maintenance,Applicationrent,Finance

admin.site.register(Maintenance)

admin.site.register(MarketingManager)
admin.site.register(Employee)
admin.site.register(ContactMessage)
admin.site.register(Applicationrent)
admin.site.register(Finance)
admin.site.register(AskMaintenance)
admin.site.register(Salesperson)
# Register your models here.
from django.contrib import admin

from .models import ContactMessage, Employee, MarketingManager, Properties, Registration


from .models import Properties, Registration,Application

admin.site.register(Registration)
admin.site.register(Properties)
admin.site.register(Application)

from .models import MarketingManager, Properties, Registration,Maintenance

admin.site.register(Maintenance)

admin.site.register(MarketingManager)
admin.site.register(Employee)
admin.site.register(ContactMessage)

# Register your models here.
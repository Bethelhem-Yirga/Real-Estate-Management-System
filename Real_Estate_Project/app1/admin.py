from django.contrib import admin

from .models import Employee, MarketingManager, Properties, Registration


from .models import Properties, Registration,Application

admin.site.register(Registration)
admin.site.register(Properties)
admin.site.register(Application)

from .models import MarketingManager, Properties, Registration

admin.site.register(MarketingManager)

admin.site.register(Employee)


# Register your models here.
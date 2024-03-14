from django.contrib import admin
<<<<<<< HEAD
from .models import Employee, MarketingManager, Properties, Registration
=======

from .models import Properties, Registration,Application
>>>>>>> de79c0d65a6817f3badb78b8cfa0ccc4d028b3e6
admin.site.register(Registration)
admin.site.register(Properties)
admin.site.register(Application)

from .models import MarketingManager, Properties, Registration

admin.site.register(MarketingManager)
<<<<<<< HEAD
admin.site.register(Employee)
=======
>>>>>>> de79c0d65a6817f3badb78b8cfa0ccc4d028b3e6

# Register your models here.
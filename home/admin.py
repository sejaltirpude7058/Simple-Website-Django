from django.contrib import admin
from home.models import Home
from home.models import Registration
from home.models import Contact

# Register your models here.
admin.site.register(Home)

admin.site.register(Registration)

admin.site.register(Contact)

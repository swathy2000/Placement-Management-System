from django.contrib import admin


# Register your models here.
from django.contrib.auth.models import User 
from trial.forms import UserModelForm

# admin.site.register(User)

class UserModelAdmin(admin.ModelAdmin):
    model = User
    form = UserModelForm

# admin.site.unregister(User)
# admin.site.register(User,UserModelAdmin)
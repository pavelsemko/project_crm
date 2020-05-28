from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from account.models import User, Leads, Planning, TelegramApi
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('role','telegram','closer')}),
    )

admin.site.register(User,MyUserAdmin)
admin.site.register(Leads)
admin.site.register(Planning)
admin.site.register(TelegramApi)

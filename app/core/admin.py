from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from django.utils.translation import gettext as _

from user import models as user
from fantasy import models as fantasy
from account import models as account

class UserAdmin(BaseUserAdmin): 
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields' : ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(account.Account)
admin.site.register(account.PrelaunchEmail)
admin.site.register(account.Asset)
admin.site.register(account.Collection)
admin.site.register(account.SalesOrder)
admin.site.register(fantasy.Game)
admin.site.register(fantasy.GameSchedule)
admin.site.register(fantasy.GameTeam)
admin.site.register(fantasy.GameAthlete)
admin.site.register(fantasy.GameAsset)
admin.site.register(fantasy.GameAthleteStat)
admin.site.register(user.User, UserAdmin)

@admin.register(fantasy.Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'api_id', 'position')

@admin.register(fantasy.Team)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'name')

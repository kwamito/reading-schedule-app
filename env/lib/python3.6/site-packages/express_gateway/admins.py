from django.contrib import admin

from express_gateway.models import SocialUser


class SocialUserAdmin(admin.ModelAdmin):
    list_display = ['social_id', 'provider', 'user']


admin.site.register(SocialUser, SocialUserAdmin)

from django.contrib import admin

from .models import Cfp, Donor, Theme, Zone
# admin.site.register(Donor)

@admin.register(Cfp)
class CfpAdmin(admin.ModelAdmin):
    list_display = ('donor', 'cfp_title', 'pub_date')


# admin.site.register(Cfp, CfpAdmin)
admin.site.register(Donor)
admin.site.register(Theme)
admin.site.register(Zone)

from django.contrib import admin

from .models import Cfp, Donor, Theme, Zone
# admin.site.register(Donor)


class CfpAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cfp, CfpAdmin)
admin.site.register(Donor)
admin.site.register(Theme)
admin.site.register(Zone)

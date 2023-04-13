from django.contrib import admin
from .models import RegistrationCode , Profile , Committee

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'committee']
    list_filter = ['committee']
    search_fields = ['user__username', 'user__first_name', 'user__last_name',"committee__name"]

class RegistrationCodeAdmin(admin.ModelAdmin):
    list_per_page = 10
admin.site.register(RegistrationCode,RegistrationCodeAdmin)

admin.site.register(Profile,ProfileAdmin)


admin.site.register(Committee)





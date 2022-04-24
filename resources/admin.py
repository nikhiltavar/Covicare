from django.contrib import admin
from .models import *
from django.contrib.auth.models import User





class hospitalAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs ["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Hospital,hospitalAdmin)


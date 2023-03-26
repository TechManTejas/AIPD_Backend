from django.contrib import admin
from patient.models import Patient
from doctor.models import Doctor
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class PatientInline(admin.TabularInline):
    model = Patient
    can_delete = False
    verbose_name_plural = 'patient'
    fk_name = 'user'


class DoctorInline(admin.TabularInline):
    model = Doctor
    can_delete = False
    verbose_name_plural = 'doctor'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    def get_inline_instances(self, request, obj=None):
        if obj is not None and hasattr(obj, 'patient'):
            return [PatientInline(self.model, self.admin_site)]
        elif obj is not None and hasattr(obj, 'doctor'):
            return [DoctorInline(self.model, self.admin_site)]
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

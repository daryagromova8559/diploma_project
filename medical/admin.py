from django.contrib import admin

from medical.models import Doctor, Service


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'patronymic', 'surname')
    list_filter = ('id',)
    search_fields = ('name', 'patronymic',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('id',)
    search_fields = ('name', 'description',)


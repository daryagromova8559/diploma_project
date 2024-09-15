from django.contrib import admin

from users.models import User, Record


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    list_filter = ('id',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'created_at')
    list_filter = ('id', 'created_at')
    search_fields = ('user', 'created_at',)
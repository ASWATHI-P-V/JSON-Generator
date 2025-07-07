from django.contrib import admin

from .models import ProjectSpec
@admin.register(ProjectSpec)
class ProjectSpecAdmin(admin.ModelAdmin):       
    list_display = ('project_name', 'created_at', 'updated_at')
    search_fields = ('project_name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Division, Position, Employee


@admin.register(Division)
class DivisionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Position)
class PositionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Employee)
class EmployeeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'division', 'position', 'created_at', 'salary',
                    'parent_id', 'child_id')
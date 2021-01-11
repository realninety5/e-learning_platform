from django.contrib import admin
from .models import Course, Module, Subject

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
# Creates an inline of Module with Course, added below
class ModuleInline(admin.StackedInline):
    model = Module

# Course administration interface
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inline = [ModuleInline]

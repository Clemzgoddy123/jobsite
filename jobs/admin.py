from django.contrib import admin

from .models import Job, JobApplication


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'is_remote', 'posted_at')
    list_filter = ('is_remote', 'company', 'location')
    search_fields = ('title', 'company', 'description')
    date_hierarchy = 'posted_at'


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_at')
    list_filter = ('job', 'applied_at')
    search_fields = ('name', 'email', 'job__title')
    date_hierarchy = 'applied_at'

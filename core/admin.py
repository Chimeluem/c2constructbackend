from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job, Contact, SiteDetail
# Register your models here.
from django.contrib.auth.models import Group
from django.utils.html import mark_safe
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import TokenProxy

def update_contact_to_responded(modeladmin, request, queryset):
    queryset.update(processed=True)


update_contact_to_responded.short_description = 'update contact support to responded'

class AdminUsercontact(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'phone',

        'processed',
        'info',
        'timestamp',

    ]
    list_display_links = [
        'email',

    ]

    list_filter = [
        'processed',
        'email',
    ]

    search_fields = [
        'email',
        'processed',

    ]
    actions = [update_contact_to_responded]






def update_job_to_responded(modeladmin, request, queryset):
    queryset.update(processed=True)


update_job_to_responded.short_description = 'update job to responded'

class AdminUserjob(admin.ModelAdmin):
    list_display = [
        'email',
        'firstName',
        'lastName',
        'phoneNumber',

        'processed',
        'first_aider',
        'cscs_card',
        'Fire_Marshall',
        'driving_license',
        'licenseType',
        'state',
        'city',
        'country',
        'zipCode',
        'address1',
        'address2',
        'additionalInfo',
        'timestamp'

    ]
    list_display_links = [
        'email',

    ]

    list_filter = [
        'processed',
        'email',
    ]

    search_fields = [
        'email',
        'processed',

    ]
    actions = [update_job_to_responded]

class AdminSiteDetail(admin.ModelAdmin):
    list_display = [
        'phone',
        'address',

    ]


admin.site.register(Contact, AdminUsercontact)
admin.site.register(Job, AdminUserjob)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
admin.site.register(SiteDetail, AdminSiteDetail)
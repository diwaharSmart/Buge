from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as MainUserAdmin

from base.forms.user_form import UserAdminChangeForm , UserAdminCreationForm

from base.model.company_model import *
from base.model.model_model import *
from base.model.view_model import *
from base.model.controller_model import *
from base.model.page_model import *

from base.admins.company_admin import CompanyAdmin

User = get_user_model()
# Remove Group Model from admin. We're not using it.

admin.site.unregister(Group)


class UserAdmin(MainUserAdmin):
    # These forms forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email','is_staff']
    list_filter = ['is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Company,CompanyAdmin)


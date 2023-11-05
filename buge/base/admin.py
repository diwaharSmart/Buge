from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as MainUserAdmin
from base.models import *
from base.forms import UserChangeForm , UserCreationForm

User = get_user_model()
# Remove Group Model from admin. We're not using it.

admin.site.unregister(Group)


class UserAdmin(MainUserAdmin):
    # These forms forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

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
admin.site.register(Version)


admin.site.register(App)


class ModelFieldParametersAdmin(admin.TabularInline):
    model = ModelFieldParameters


class ModelFieldAdmin(admin.ModelAdmin):
    inlines = [ModelFieldParametersAdmin]


class DecoratorInline(admin.TabularInline):
    model = DataModelDecorators
    exclude = ["version","created_by","updated_by"]

class DataModelAdmin(admin.ModelAdmin):
    inlines = [DecoratorInline]

class FieldParametersAdmin(admin.ModelAdmin):
    list_display = ["parameter_name"]
    list_filter  = ["parameter_group"]


# Model
admin.site.register(DataModel,DataModelAdmin)
admin.site.register(DataField)
admin.site.register(FieldParameters,FieldParametersAdmin)
admin.site.register(ModelField,ModelFieldAdmin)
admin.site.register(ModelFieldParameters)




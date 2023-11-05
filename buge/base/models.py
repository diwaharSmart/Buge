import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils import timezone
from django.utils.functional import cached_property
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from base.managers import UserManager



# Create your models here.

"""
Custom User Model
description:

"""
class User(AbstractBaseUser, PermissionsMixin):
    username      = None
    email         = models.EmailField(_('email_address'), unique=True, max_length=200)
    date_joined   = models.DateTimeField(default=timezone.now)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    admin         = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True


    def staff(self):
        "Is the user a member of staff?"
        return self.is_staff


    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


    def __str__(self):
        return self.email



"""
Pass request while saving this model.
Version.save(request=request)
"""
class Version(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    version = models.PositiveIntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ('title', 'version')

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)

    @cached_property
    def previous_version(self):
        return Version.objects.filter(title=self.title, version=self.version - 1).first()

    def __str__(self):
        return "v_"+str(self.version)

class App(models.Model):
    version   = models.ForeignKey(Version,blank=True,null=True,on_delete=models.CASCADE)
    app_name  = models.CharField(max_length=255,blank=True,null=True,unique=True)
    app_icon  = models.ImageField(upload_to="app/icons",blank=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_name

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)


class DataModelDecorators(models.Model):
    version    = models.ForeignKey(Version, blank=True, null=True, on_delete=models.CASCADE)
    data_model        = models.ForeignKey('DataModel',blank=True,null=True,on_delete=models.CASCADE)
    content           = models.TextField(blank=True,null=True)
    created_by        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_by        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at        = models.DateTimeField(auto_now=True)
    
    
class DataModel(models.Model):
    version           = models.ForeignKey(Version, blank=True, null=True, on_delete=models.CASCADE)
    model_name        = models.CharField(max_length=255,blank=True,null=True)
    model_description = models.TextField(blank=True,null=True)
    created_by        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_by        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at        = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)

class DataField(models.Model):
    version = models.ForeignKey(Version, blank=True, null=True, on_delete=models.CASCADE)
    field_name        = models.CharField(max_length=255,blank=True,null=True,unique=True)
    field_description = models.TextField()
    created_by        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_by        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at        = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.field_name

GROUP_PARAMETERES=(
    ("Common Field Parameters","Common Field Parameters"),
    ("Text Fields","Text Fields"),
    ("Numeric Fields","Numeric Fields"),
    ("Date/Time Fields","Date/Time Fields"),
    ("Relationship Fields","Relationship Fields"),
    ("File/Image Fields","File/Image Fields"),
    ("Miscellaneous Fields", "Miscellaneous Fields"),
)
class FieldParameters(models.Model):
    version = models.ForeignKey(Version, blank=True, null=True, on_delete=models.CASCADE)
    data_field            = models.ManyToManyField(DataField,blank=True)
    parameter_name   = models.CharField(max_length=255,blank=True,null=True)
    description      = models.TextField(blank=True,null=True)
    parameter_group  = models.CharField(choices=GROUP_PARAMETERES,max_length=255,blank=True,null=True)
    created_by       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_by       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at       = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)


    def __str__(self):
        return self.parameter_name




class ModelField(models.Model):
    version = models.ForeignKey(Version, blank=True, null=True, on_delete=models.CASCADE)
    data_model      = models.ForeignKey(DataModel,blank=True,null=True,on_delete=models.CASCADE)
    data_field      = models.ForeignKey(DataField,blank=True,null=True,on_delete=models.CASCADE)
    field_description = models.TextField()
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at  = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)


class ModelFieldParameters(models.Model):
    model_feild = models.ForeignKey(ModelField,blank=True,null=True,on_delete=models.CASCADE)
    parameter   = models.ForeignKey(FieldParameters,blank=True,null=True,on_delete=models.CASCADE)
    value       = models.CharField(max_length=255,blank=True,null=True)
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at  = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)



class CustomMethod(models.Model):
    version      = models.ForeignKey(Version,blank=True,null=True,on_delete=models.CASCADE)
    data_model   = models.ForeignKey(DataModel,blank=True,null=True,on_delete=models.CASCADE)
    content      = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            user = request.user
            if not self.pk:  # object is being created
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)




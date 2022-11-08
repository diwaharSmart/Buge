from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from base.managers import UserManager
from base.model.company_model import *
from base.model.model_model import *
from base.model.view_model import *
from base.model.controller_model import *
from base.model.page_model import *

# Create your models here.

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
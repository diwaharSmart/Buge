from django.db import models


class Company(models.Model):
    company_name  = models.CharField('Company Name',max_length=255,help_text="Enter your company name",blank=True,null=True)
    slug          = models.SlugField(unique=True,max_length=10)


    def __str__(self):
        return self.slug

    def __unicode__(self):
        return self.id

class CompanyInfo(models.Model):
    company       = models.OneToOneField(Company,on_delete=models.CASCADE,blank=True,null=True)
    address       = models.TextField('Company Address',max_length=1500,help_text="Enter your company address",blank=True,null=True)
    pincode       = models.CharField('Pincode',max_length=12,help_text="Enter pincode",blank=True,null=True)
    city          = models.CharField('City',max_length=255,help_text="Enter city",blank=True,null=True)
    state         = models.CharField('State',max_length=255,help_text="Enter state",blank=True,null=True)
    country       = models.CharField('Country',max_length=255,help_text="Enter country",blank=True,null=True)
    email_address = models.EmailField(blank=True,null=True)
    phone_number  = models.CharField('Phone Number',max_length=30,blank=True,null=True,help_text="Enter phone number")



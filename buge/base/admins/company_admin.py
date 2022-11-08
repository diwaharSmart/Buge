from django.contrib import admin
from base.model.company_model import CompanyInfo,Company


class InfoInline(admin.StackedInline):
    model = CompanyInfo

class CompanyAdmin(admin.ModelAdmin):
    inlines = [InfoInline]

    class Meta:
        model = Company
        fields ="__all__"






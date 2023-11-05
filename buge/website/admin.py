from django.contrib import admin
from website.models import  *
# Register your models here.


class CascadeStyleInline(admin.StackedInline):
    model = CascadeStyle
    extra = 1

class JavaScriptInline(admin.StackedInline):
    model = JavaScript
    extra = 1

class MetaInline(admin.TabularInline):
    model = Meta
    extra = 1

class PageAdmin(admin.ModelAdmin):
    inlines = [CascadeStyleInline,JavaScriptInline,MetaInline]
    class Meta:
        model = Page



class SerializerInline(admin.StackedInline):
    model = JsonSerializer.api.through
    extra = 1


class ApiAdmin(admin.ModelAdmin):
    inlines = [SerializerInline]
    class Meta:
        model = Api


admin.site.register(Page,PageAdmin)
admin.site.register(Widget)
admin.site.register(Api,ApiAdmin)
admin.site.register(JsonSerializer)
admin.site.register(View)

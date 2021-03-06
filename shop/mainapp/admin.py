from django.contrib import admin
from django.forms import ModelChoiceField
# Register your models here.
from .models import *


class NotebookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request,**kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request,**kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Castomer)
admin.site.register(CartPrpduct)
admin.site.register(Cart)


from django.contrib import admin
from input.models import Good, Level_1, Level_2, Level_3
from import_export import resources
from import_export.admin import ImportMixin
#from input.forms import GoodImportForm, GoodConfirmImportForm
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class GoodResource(resources.ModelResource):

    class Meta:
        model = Good

'''class CustomBookAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = GoodResource

    def get_import_form(self):
        return GoodImportForm

    def get_confirm_import_form(self):
        return GoodConfirmImportForm

    def get_form_kwargs(self, form, *args, **kwargs):
        if isinstance(form, GoodImportForm):
            if form.is_valid():
                author = form.cleaned_data['author']
                kwargs.update({'author': author.id})
        return kwargs'''


admin.site.register(Good, ImportExportModelAdmin)
admin.site.register(Level_1)
admin.site.register(Level_2)
admin.site.register(Level_3)


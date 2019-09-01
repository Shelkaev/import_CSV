from django.contrib import admin
from input.models import Good, Level_1, Level_2, Level_3
from import_export import resources
from import_export.admin import ImportMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class GoodResource(resources.ModelResource):

    class Meta:
        model = Good


admin.site.register(Good, ImportExportModelAdmin)
admin.site.register(Level_1)
admin.site.register(Level_2)
admin.site.register(Level_3)


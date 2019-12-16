from django.contrib import admin
from productapp.models import  Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

@admin.register(Product)

class ProductAdmin(ImportExportModelAdmin):
    pass

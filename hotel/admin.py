from django.contrib import admin
from hotel.models import  Hotel
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class HotelResource(resources.ModelResource):
    class Meta:
        model = Hotel

@admin.register(Hotel)

class HotelAdmin(ImportExportModelAdmin):
    pass
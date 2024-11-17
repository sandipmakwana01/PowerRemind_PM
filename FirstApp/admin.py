from django.contrib import admin
from FirstApp.models import *
# Register your models here.
class AuthenticationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('id', 'user_name', 'password')  # Replace with your actual field names

    # Fields to display in the form view (when adding or editing)
    # fields = ('id', 'user_name', 'password')  # Replace with your actual field names

    # Optional: you can include search functionality for some fields
    search_fields = ['id', 'user_name', 'password']  # Replace with fields you want to search by

    # Optional: filters can also be added for the list view
    list_filter = ('id', 'user_name', 'password')  # Replace with fields you want to filter by

admin.site.register(Authentication,AuthenticationAdmin)

class ClientAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('user','id', 'name', 'contact_number','start_date','amount')  # Replace with your actual field names

    # Fields to display in the form view (when adding or editing)
    # fields = ('id', 'user_name', 'password')  # Replace with your actual field names

    # Optional: you can include search functionality for some fields
    # search_fields = ['user','id', 'name', 'contact_number']  # Replace with fields you want to search by

    # # Optional: filters can also be added for the list view
    # list_filter = ('user','id', 'name', 'contact_number')  # Replace with fields you want to filter by


admin.site.register(Client,ClientAdmin)

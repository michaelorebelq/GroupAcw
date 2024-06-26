from django.contrib import admin
from .models import Location, Category, Equipment, User, Reservation, Alert, Report

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(Alert)
admin.site.register(Report)

admin.site.site_header = 'Westminster University Inventory Admin Login'
admin.site.site_title = 'Admin Login'


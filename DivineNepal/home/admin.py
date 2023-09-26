from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "DivineJourneyNepal | Admin"


admin.site.register(Contact)
admin.site.register(Information)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Destination)
admin.site.register(Team)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(PackageDetail)
admin.site.register(AboutBooking)

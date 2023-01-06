from django.contrib import admin
from .models import DEPARTMENT
from .models import DOCTOR
from .models import booking

# Register your models here.
admin.site.register(DEPARTMENT)
admin.site.register(DOCTOR)
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(booking,BookingAdmin)
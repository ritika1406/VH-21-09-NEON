from django.contrib import admin

from analysis.models import Ambulance, Beds, ICU_Beds, Oxygen, Plasma, Vaccination, Patient_Status

# Register your models here.
admin.site.register(ICU_Beds)
admin.site.register(Beds)
admin.site.register(Ambulance)
admin.site.register(Oxygen)
admin.site.register(Vaccination)
admin.site.register(Plasma)
admin.site.register(Patient_Status)
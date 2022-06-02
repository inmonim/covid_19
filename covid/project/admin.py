from django.contrib import admin
from .models import CovidByCity
from .models import VaccinePercentage
from .models import DailyCovid
from .models import CovidHospital
from .models import CovidInfoBar
from .models import GlobalCovid

# Register your models here.
admin.site.register(CovidByCity)
admin.site.register(VaccinePercentage)
admin.site.register(DailyCovid)
admin.site.register(CovidHospital)
admin.site.register(CovidInfoBar)
admin.site.register(GlobalCovid)
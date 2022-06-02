from django.db import models

# Create your models here.
class CovidByCity(models.Model):
    city = models.CharField(max_length = 10)
    covid_num_bycity = models.CharField(max_length = 20)

class VaccinePercentage(models.Model):
    the_order_vaccine = models.CharField(max_length = 5)
    percentage = models.CharField(max_length = 10)

class DailyCovid(models.Model):
    covid_date = models.CharField(max_length = 20)
    covid_num_daily = models.CharField(max_length = 20)

class CovidHospital(models.Model):
    hospi_city = models.CharField(max_length = 10)
    county = models.CharField(max_length = 20)
    hospi_name = models.CharField(max_length = 50)
    addr = models.CharField(max_length = 100)
    hospi_time = models.CharField(max_length = 100)
    sat = models.CharField(max_length = 50)
    hol = models.CharField(max_length = 50)
    tele = models.CharField(max_length = 50)

class CovidInfoBar(models.Model):
    info_bar_title = models.CharField(max_length = 10)
    info_bar_num = models.CharField(max_length = 20)

class GlobalCovid(models.Model):
    continent = models.CharField(max_length = 10)
    country = models.CharField(max_length = 30)
    country_num = models.CharField(max_length = 50)
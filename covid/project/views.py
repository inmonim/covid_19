from django.shortcuts import render
from .models import CovidByCity
from .models import VaccinePercentage
from .models import DailyCovid
from .models import CovidInfoBar
from .models import GlobalCovid
from sqlalchemy import create_engine
import pymysql
import pandas as pd

engine = create_engine("mysql+pymysql://bigdata:Bigdata123!!@localhost:3306/covid")
conn = engine.connect()


# Create your views here.
def index(request):   
    order_vaccine = "1차" # request.GET.get("order_vaccine")
    sql_stmt = "SELECT city, covid_num_bycity, CAST(CAST(covid_num_bycity AS UNSIGNED) / (SELECT max(cast(covid_num_bycity as UNSIGNED)) FROM project_covidbycity) * 100 as unsigned) as per FROM project_covidbycity"
    covidbycity = pd.read_sql(sql_stmt,conn)
    covidbycity = covidbycity.to_dict('r')
    vaccine = VaccinePercentage.objects.filter(the_order_vaccine = order_vaccine).values()
    daily = DailyCovid.objects.values()
    info = CovidInfoBar.objects.values()

    result = {'covidcity' : covidbycity, 'vac' : vaccine, 'dailynum' : daily, "info" : info}
    return render(request, "index.html", result)

def index2(request):   
    order_vaccine = "2차" # request.GET.get("order_vaccine")
    sql_stmt = "SELECT city, covid_num_bycity, CAST(CAST(covid_num_bycity AS UNSIGNED) / (SELECT max(cast(covid_num_bycity as UNSIGNED)) FROM project_covidbycity) * 100 as unsigned) as per FROM project_covidbycity"
    covidbycity = pd.read_sql(sql_stmt,conn)
    covidbycity = covidbycity.to_dict('r')
    vaccine = VaccinePercentage.objects.filter(the_order_vaccine = order_vaccine).values()
    daily = DailyCovid.objects.values()
    info = CovidInfoBar.objects.values()
    result = {'covidcity' : covidbycity, 'vac' : vaccine, 'dailynum' : daily, "info" : info}
    return render(request, "index2.html", result)

def index3(request):   
    order_vaccine = "3차" # request.GET.get("order_vaccine")
    sql_stmt = "SELECT city, covid_num_bycity, CAST(CAST(covid_num_bycity AS UNSIGNED) / (SELECT max(cast(covid_num_bycity as UNSIGNED)) FROM project_covidbycity) * 100 as unsigned) as per FROM project_covidbycity"
    covidbycity = pd.read_sql(sql_stmt,conn)
    covidbycity = covidbycity.to_dict('r')
    vaccine = VaccinePercentage.objects.filter(the_order_vaccine = order_vaccine).values()
    daily = DailyCovid.objects.values()
    info = CovidInfoBar.objects.values()
    result = {'covidcity' : covidbycity, 'vac' : vaccine, 'dailynum' : daily, "info" : info}
    return render(request, "index3.html", result)

def line_graph(request):
    return render(request, "line_graph.html")

def baro1(request):
    return render(request, "baro1.html")
def baro2(request):
    return render(request, "baro2.html")
def baro3(request):
    return render(request, "baro3.html")
def baro4(request):
    return render(request, "baro4.html")

def movement1(request):
    daily = DailyCovid.objects.values()
    result = {'dailynum' : daily}
    return render(request, "movement1.html", result)

def movement2(request):
    sql_stmt = "SELECT * FROM project_globalcovid WHERE continent = '아시아'"
    asiacovid = pd.read_sql(sql_stmt, conn)
    asiacovid = asiacovid.to_dict('r')

    sql_stmt = "SELECT * FROM project_globalcovid WHERE continent = '중동'"
    centercovid = pd.read_sql(sql_stmt, conn)
    centercovid = centercovid.to_dict('r')

    sql_stmt = "SELECT * FROM project_globalcovid WHERE continent = '아메리카'"
    americacovid = pd.read_sql(sql_stmt, conn)
    americacovid = americacovid.to_dict('r')

    sql_stmt = "SELECT * FROM project_globalcovid WHERE continent = '유럽'"
    europecovid = pd.read_sql(sql_stmt, conn)
    europecovid = europecovid.to_dict('r')

    sql_stmt = "SELECT * FROM project_globalcovid WHERE continent = '오세아니아'"
    oceaniacovid = pd.read_sql(sql_stmt, conn)
    oceaniacovid = oceaniacovid.to_dict('r')

    sql_stmt = "SELECT * FROM project_globalcovid WHERE continent = '아프리카'"
    africacovid = pd.read_sql(sql_stmt, conn)
    africacovid = africacovid.to_dict('r')

    sql_stmt = "select * from project_globalcovid where continent = '기타'"
    restcovid = pd.read_sql(sql_stmt, conn)
    restcovid = restcovid.to_dict('r')

    sql_stmt = "select * from project_globalcovid where continent = '합계'"
    sumcovid = pd.read_sql(sql_stmt, conn)
    sumcovid = sumcovid.to_dict('r')

    result = {'asia' : asiacovid, 'center' : centercovid, 'america' : americacovid, 'europe' : europecovid, 'oceania' : oceaniacovid,
    'africa' : africacovid, 'rest' : restcovid, 'sum' : sumcovid}
    return render(request, "movement2.html", result)

def movement3(request):
    sql_stmt = "SELECT city, covid_num_bycity, CAST(CAST(covid_num_bycity AS UNSIGNED) / (SELECT max(cast(covid_num_bycity as UNSIGNED)) FROM project_covidbycity) * 100 as unsigned) as per FROM project_covidbycity"
    citycovid = pd.read_sql(sql_stmt, conn)
    citycovid = citycovid.to_dict('r')
    result = {'citycov' : citycovid}
    return render(request, "movement3.html", result)

def vaccine1(request):
    return render(request, "vaccine1.html")
def vaccine2(request):
    return render(request, "vaccine2.html")
def vaccine3(request):
    return render(request, "vaccine3.html")
def vaccine1_2(request):
    return render(request, "vaccine1_2.html")
def vaccine1_3(request):
    return render(request, "vaccine1_3.html")

def mask1(request):
    return render(request, "mask1.html")
def mask2(request):
    return render(request, "mask2.html")

def test(request):
    return render(request, "test.html")
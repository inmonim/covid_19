import requests
from bs4 import BeautifulSoup
import os
import django
from django.shortcuts import render

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid.settings")
django.setup()

from project.models import DailyCovid

def daily_covid():
    # 웹 데이터
    req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=')
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    daily_data = soup.select('table.num')

    # daily_data = 일별 확진자수(최근 일주일) 
    data = []
    for dt in daily_data:
        data.append(dt.text)
    data = data[3].split('\n')
    cnt = 0
    for i in range(len(data)):
        if data[i-cnt] == "":
            del data[i-cnt]
            cnt += 1
    daily_data = data

    # covid_list = 일별 확진자수(천단위 구분 쉼표(,) 제거)
    covid_list = []
    for dt in daily_data[11:19]:
        covid_list.append(int(dt.replace(",","")))

    # date_list = 날짜 리스트
    date_list = []
    for dt in daily_data[2:9]:
        date_list.append(dt)

    # result = (날짜, 일별확진자수)를 리스트 형태로 저장
    result = []
    for i in range(len(date_list)):
        result.append((date_list[i], covid_list[i]))
    return result

if __name__=='__main__':
    i = 0
    while(i<len(daily_covid())):
        a = DailyCovid(covid_date = daily_covid()[i][0], covid_num_daily = daily_covid()[i][1])
        a.save()
        i += 1
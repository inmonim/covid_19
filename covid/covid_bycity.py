import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid.settings")
django.setup()

from project.models import CovidByCity

def covid_by_city():
    # 웹 데이터
    req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=')
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    covid_data = soup.select('td.number')

    # data에 [서울확진자수, 부산확진자수, ..., max값]로 저장
    data = []
    for dt in covid_data[7::6]:
        data.append(int(dt.text.replace(",","")))
    data[len(data) - 1] = (max(data)+20000)

    #result에 [(서울, 확진자수), (부산, 확진자수), ..., (최대값, max값)]로 저장
    result = []
    city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '최대값']
    for i in range(len(city)):
        result.append((city[i], data[i]))
    return result
    

if __name__=='__main__':
    i = 0
    while(i<len(covid_by_city())):
        a = CovidByCity(city = covid_by_city()[i][0], covid_num_bycity = covid_by_city()[i][1])
        a.save()
        i += 1
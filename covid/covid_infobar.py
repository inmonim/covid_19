import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid.settings")
django.setup()

from project.models import CovidInfoBar

def covid_info_bar():
    # 웹 데이터
    req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=2&acq=%EC%BD%94%EB%A1%9C%EB%82%98&qdt=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98')
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')

    # 제목
    info_title = soup.select('strong.info_title')

    # 숫자
    info_num = soup.select('p.info_num')

    # data에 [서울확진자수, 부산확진자수, ..., max값]로 저장
    title = []
    for dt in info_title[0:4]:
        title.append(dt.text)
    num = []
    for dt in info_num[0:4]:
        num.append(dt.text)

    #result에 [(서울, 확진자수), (부산, 확진자수), ..., (최대값, max값)]로 저장
    info_data = []
    for i in range(4):
        info_data.append((title[i], num[i]))
    return info_data
    

if __name__=='__main__':
    i = 0
    while(i<len(covid_info_bar())):
        a = CovidInfoBar(info_bar_title = covid_info_bar()[i][0], info_bar_num = covid_info_bar()[i][1])
        a.save()
        i += 1
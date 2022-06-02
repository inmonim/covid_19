import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid.settings")
django.setup()

from project.models import VaccinePercentage

def vaccine_per():
    # 웹 데이터
    req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%B1%EC%8B%A0%EC%A0%91%EC%A2%85')
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    covid_data = soup.select('p.info_num')

    # data 변수에 (백신차수, 퍼센티지)의 리스트로 저장
    data = []
    i = 1
    for dt in covid_data[0:3]:
        data.append((f"{i}차", dt.text[0:4]))
        i += 1
    return data
    

if __name__=='__main__':
    i = 0
    while(i<len(vaccine_per())):
        a = VaccinePercentage(the_order_vaccine = vaccine_per()[i][0], percentage = vaccine_per()[i][1])
        a.save()
        i += 1
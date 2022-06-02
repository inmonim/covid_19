from bs4 import BeautifulSoup
import requests


url_1 = """http://ncov.mohw.go.kr/baroView.do?brdId=&brdGubun=&dataGubun=&ncvContSeq=&contSeq=&board_id=&gubun="""

response = requests.get(url_1)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    코로나19란 = soup.select_one("#content > div > p")

else:
    print(response.status_code)

코로나19란 = 코로나19란.text

print(코로나19란)


url_2 = """http://ncov.mohw.go.kr/baroView2.do?brdId=4&brdGubun=42"""

response = requests.get(url_2)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    방역체계 = soup.select_one("#content > div > h4 > span")

else:
    print(response.status_code)

방역체계 = 방역체계.text

print(방역체계)


url_3 = """http://ncov.mohw.go.kr/baroView3.do?brdId=4&brdGubun=43"""

response = requests.get(url_3)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    환자치료= soup.select_one("#content > div > div:nth-child(3) > div.bn_t > p")

else:
    print(response.status_code)

환자치료 = 환자치료.text

print(환자치료)


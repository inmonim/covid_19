import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid.settings")
django.setup()

from project.models import GlobalCovid

def global_covid():
    req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun=')
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    data_title = soup.select('table.num')

    data = []
    for dt in data_title:
        data.append(dt.text)

    data2 = []
    for i in range(len(data)):
        data[i] = data[i].replace('\t','')
        data[i] = data[i].replace('\r','')
        data2.append(data[i].split('\n'))
    data3 = []
    for i in data2[0]:
        if i == '':
            pass
        else:
            data3.append(i)
    data3 = data3[3:]
    cnt = 0
    for i in range(len(data3)):
        if data3[i][0] == '(':
            data3[i-1] += data3[i]
    data4 = []
    for i in data3:
        if i[0] != '(':
            data4.append(i)
    data5 = []
    for i in data4:
        if i[0] not in ['0','1','2','3','4','5','6','7','8','9']:
            check = 0
            for j in range(len(i)):
                if i[j] in ['0','1','2','3','4','5','6','7','8','9']:
                    data5.append(i[0:j])
                    data5.append(i[j:])
                    check = 1
                    break
            if check == 0:
                data5.append(i)
        else:
            data5.append(i)
            
    result = []
    for i in data5:
        if i in ['아시아', '중동', '아메리카', '유럽', '오세아니아', '아프리카', '기타']:
            continent = i
        elif i == "합계":
            continent = i
            country = i
        elif i[0] not in ['0','1','2','3','4','5','6','7','8','9']:
            country = i
        else:
            dt_data = (continent , country, i)
            result.append(dt_data)

    return result

if __name__=='__main__':
    i = 0
    while(i<len(global_covid())):
        a = GlobalCovid(continent = global_covid()[i][0], country = global_covid()[i][1], country_num = global_covid()[i][2])
        a.save()
        i += 1
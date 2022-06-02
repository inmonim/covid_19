from bs4 import BeautifulSoup
import requests
from time import *
import pymysql
import pandas as pd
from sqlalchemy import create_engine, text
from random import *

###################

user = 'bigdata'
password = 'Bigdata123!!'
host = '192.168.56.101'
port = '3306'
db = 'covid19'

connect_script = f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'
engine = create_engine(connect_script)
Co = engine.connect()

###################


url = """
http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=
"""

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    K_DT = soup.select_one('#content > div > div.caseTable > div:nth-child(1) > ul > li:nth-child(1) > dl > dd')
    K_DT10 = soup.select_one('#content > div > div.caseTable > div:nth-child(1) > ul > li:nth-child(2) > dl > dd')
    K_WT = soup.select_one('#content > div > div.caseTable > div:nth-child(2) > ul > li:nth-child(1) > dl > dd')
    K_WT10 = soup.select_one('#content > div > div.caseTable > div:nth-child(2) > ul > li:nth-child(2) > dl > dd')
    K_NT = soup.select_one('#content > div > div.caseTable > div:nth-child(3) > ul > li:nth-child(1) > dl > dd')
    K_N10 = soup.select_one('#content > div > div.caseTable > div:nth-child(3) > ul > li:nth-child(2) > dl > dd')
    K_DeT = soup.select_one('#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(1) > dl > dd')
    K_De10 = soup.select_one('#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(2) > dl > dd')
    
    #Kr Dead Today                  -일일사망자
    #Kr Dead Today / 10M
    #Kr Warning Today               -재원 위중증
    #Kr Warning Today / 10M
    #Kr New hospitalization today   -신규 입원
    #Kr New hospitalization today / 10M
    #Kr Definite diagnosis          -확진자
    #Kr Definite diagnosis / 10M
     
    KNL = [K_DT, K_DT10, K_WT, K_WT10, K_NT, K_N10, K_DeT, K_De10]



    D7T = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    D710 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    D6T = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(3)')
    D610 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(3)')
    D5T = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(4)')
    D510 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(4)')
    D4T = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(5)')
    D410 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(5)')
    D3T = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(6)')
    D310 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(6)')
    D2T = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(7)')
    D210 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(7)')
    D1T = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(8)')
    D110 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(8)')

    #Dead Today           -      일일 사망자
    #Dead Today / 10M

    DTL = [D7T,D6T,D5T,D4T,D3T,D2T,D1T]
    DT10L = [D710,D610,D510,D410,D310,D210,D110]

    #Dead Averege Weekend    -    주 평균 사망자
    #Dead Averege Weekend / 10M

    D_A_W = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(9)')
    D_A_W_10 = soup.select_one('#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td:nth-child(9)')

    D6 = soup.select_one('#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(2)')
    D5 = soup.select_one('#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(3)')
    D4 = soup.select_one('#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(4)')
    D3 = soup.select_one('#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(5)')
    D2 = soup.select_one('#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(6)')
    D1 = soup.select_one('#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(7)')
    DD = soup.select_one('#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(8)')

    # Day = 날짜

    DL = [D6,D5,D4,D3,D2,D1,DD]

    De6 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    De5 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(3)')
    De4 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(4)')
    De3 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(5)')
    De2 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(6)')
    De1 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(7)')
    De0 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(8)')


    #Defnitie diagnosis today    =    확진자

    DeL = [De6,De5,De4,De3,De2,De1,De0]

    De610 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    De510 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(3)')
    De410 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(4)')
    De310 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(5)')  
    De210 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(6)')  
    De110 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(7)')  
    De010 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(8)')

    #Defninte diagnosis today / 10M   

    De10L = [De610,De510,De410,De310,De210,De110,De010]

    #Defninte diagnosis Averege
    #Defninte diagnosis Averege / 10M
    
    DeA = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(9)')
    DeA10 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(2) > td:nth-child(9)')

    




    daylist = []
    for i in DL:
        daylist.extend(i)

    krnewlist = []
    for i in KNL:
        krnewlist.extend(i)

    krdead10list = []
    for i in DT10L:
        krdead10list.extend(i)

    krdeadlist = []
    for i in DTL:
        krdeadlist.extend(i)

    DeLlist = []
    for i in DeL:
        DeLlist.extend(i)

    De10list = []
    for i in De10L:
        De10list.extend(i)

else:
    print(response.status_code)

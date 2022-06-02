import plotly.express as px
import plotly
import pandas as pd
from sqlalchemy import create_engine, text
import pymysql

proto = "mysql+pymysql://"
user = 'bigdata'
password = 'Bigdata123!!'
host = '192.168.56.101'
port = '3306'
db = 'covid'
engine = create_engine(f"{proto}{user}:{password}@{host}:{port}/{db}")
conn = engine.connect()

stmt = "select * from project_dailycovid"
co_date = pd.read_sql(text(stmt), conn).to_dict('records')
for i in co_date:
    i["covid_num_daily"] = int(i["covid_num_daily"])
    i["covid_date"] = i["covid_date"][0:5]
fig = px.line(co_date, x="covid_date", y="covid_num_daily", range_y = [100000, 300000])
plotly.offline.plot(fig,filename='line_graph.html',config={'displayModeBar':False})
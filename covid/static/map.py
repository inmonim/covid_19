import pandas as pd
from sqlalchemy import create_engine, text
import pymysql
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly_express as px
import numpy as np
import plotly

proto = "mysql+pymysql://"
user = 'bigdata'
password = 'Bigdata123!!'
host = '192.168.56.101'
port = '3306'
db = 'covid'
engine = create_engine(f"{proto}{user}:{password}@{host}:{port}/{db}")
conn = engine.connect()

stmt = "select covid_num_bycity from project_covidbycity order by city"
co_data = pd.read_sql(text(stmt), conn)

co_data = co_data.to_dict('records')

data = []
for i in co_data:
    data.append(int(i['covid_num_bycity']))

gdf = gpd.read_file("TL_SCCO_CTPRVN.shp", encoding="cp949")
gdf = gdf.assign(cnt = data)

fig, ax = plt.subplots(figsize=(16,16))
map_fig = gdf.plot(ax=ax, column='cnt',cmap="Reds",edgecolor="grey", linewidth=0.4, legend=True)


from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://bigdata:Bigdata123!!@localhost:3306/covid")
conn = engine.connect()

sql_stmt = "select tele from project_covidhospital"
tele  = pd.read_sql(sql_stmt, conn)
tele  = tele.to_dict('r')


print(tele)
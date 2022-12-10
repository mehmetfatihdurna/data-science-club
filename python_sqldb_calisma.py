import pandas as pd
#Create engine
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Northwind.sqlite')

#Databasedeki tabloların adları
table_names = engine.table_names()
print(table_names)

#Connect to database
con = engine.connect()
rs = con.execute('SELECT * FROM Orders')

#Pandas veri çerçevesi olark kaydetme
#Fetchall tüm satırları getirir.
df = pd.DataFrame(rs.fetchall())

#Fetchmany istenilen sayıda satırı aktarır.
df = pd.DataFrame(rs.fetchmany(size=5))

#Sütun adlarını dataframe'e aktarır	
df.columns = rs.keys()

#Yukarıdaki kodların yerine kullanılabilecek kod bloğu tek satırda halledebiliyoruz.
df = pd.read_sql_query('SELECT * FROM Orders',engine)

#Dataframe'in ilk 5 satırını yazdır.
print(df.head())

#Bağlantıyı kapatır
con.close()

#With ile yazmada .close methodu kullanılmaz

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Orders')
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()


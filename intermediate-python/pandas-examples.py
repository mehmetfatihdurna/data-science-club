#pandas örnekleri yapacağız
import pandas as pd

#Sözlük tanımlıyoruz
dictionary = {
'country': ['Brazil','Russia','India','China','South Africa'],
'capital': ['Brasilia','Moscow','New Delhi','Beijing','Pretoria'],
'area': [8.516, 17.10, 3.286, 9.597, 1.221],
'population': [200.4, 143.5, 1252, 1357, 52.98]
}

#Sözlükten bir dataframe oluşturuyoruz
brics = pd.DataFrame(dictionary)

#Benzersiz satır etikleri oluşturuyoruz
brics.index = ['BR','RU','IN','CH','SA']

#Verilerimiz csv formatında da olabilir.
#index_col ile satır indexinde ne olacağı belirlenir.
brics = pd.read_csv('csv dosya pathi', index_col=0)


#dataframe de belirtilen kolonlara erişmek
brics[['country','capital']]

#loc
brics.loc['RU'] # RU etiketine sahip olan satırı getirir
brics.loc[['RU','IN','CH'],['country','capital']]
brics.loc[:,['country','capital']]

#iloc
brics.iloc[[1]] # 1 indeksli satırı getirir.
brics.iloc[:, [0,1]] #country ve capital sütunlarını getirir.


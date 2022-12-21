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

#Filtering pandas Dataframe
import numpy as np
print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)])


# Iterating over data
import pandas as pd
result = []
#chunksize ile alacağımız verinin boyutunu belirtiyoruz
for chunk in pd.read_csv('data.csv', chunksize=1000):
    result.append(sum(chunk['x']))
total = sum(result)
print(total)






# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in read_csv('tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)






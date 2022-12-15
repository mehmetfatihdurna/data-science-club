#Sözlükler için 
a = {'ahmet' : 38, 'mehmet': 25,'aslı': 18}
for key, value in a.items():
    print(key + ' -- ' + str(value))

#2B numpy array için her öğeyi tek tek yazdırmak istersek
import numpy as np
array = np.array([1,2,3,4,5,6],[7,8,9,10,11,12])

for val in np.nditer(array):
    print(val)

#pandas için for döngüsü
import pandas as pd
brics = pd.read_csv('brics.csv', index_col = 0)

#lab satır etiketini row satırdaki verileri getirir
for lab, row in brics.iterrows():
    print(lab)
    print(row) # row['capital'] şeklinde de  kullanılabilir

#dataframe e yeni bir sütun ekleyelim.
for lab, row in brics.iterrows():
    brics.loc[lab, 'name_length'] = len(row['country'])

#yukarıdaki kod evet işimizi görebilir ancak verimlilik açısından kötüdür.
#aynı işi apply methoduyla da yapabiliriz.

brics['name_lenght'] = brics['country'].apply(len) #str.upper











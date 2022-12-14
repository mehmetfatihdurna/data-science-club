import numpy as np

"""
Not: Numpy dizisindeki elemanlar aynı
tür olmak zorundadır.
Numpy dizisi tanımlama:
"""
height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

""" 
Numpy listeleriyle aritmetik operatörleri
kullanarak işlem yapabiliriz. Boy ve kilo değerleriyle
bmi değerlerini hesaplayalım.
"""

bmies = weight / height ** 2

"""
Numpy ile 2D array tanımlama 
"""

array = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                 [65.4, 59.2, 63.6, 88.4, 68.7]])

#Numpy listemizin boyutlarını öğrenmek için
print(array.shape)
#bize çıktı olarak (2, 5) verir. yani 2 satır 5 kolon

"""
2D arrayden eleman seçmek için
"""
array[0][2] # >  1.71
array[0, 2] # > 1.71

#ikinci ve üçüncü aile üyelerinin boy ve kiloları
array[:, 1:3] # > [[1.68, 1.71],[59.2, 63.6]] 


"""
np_city adında bir numpy array'imiz olsun
burada 5000 kişinin boyu ve kilosu bulunsun
"""

np_city = np.array([[1.78,1.88,...],[65.4, 80.3,...]])

#5000 kişinin boyunun ortalamasını almak için
np.mean(np_city[0, :])

#5000 kişinin kilosunun medyanını bulmak için
np.median(np_city[1,:])

#Boy kilonun ilişkili olup olmadığını hesaplama
np.corrcoef(np_city[0,:], np_city[1,:])

#Standart sapma boy için
np.std(np_city[0, :])

#Numpy ile veri üretme

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.notmal(60.32, 15, 5000), 2)

#İki listeyi satır satır yapıştırır
np_city = np.row_stack((height, weight))

#İki listeyi kolon olarak yapıştırır.
np_city = np.column_stack((height, weight))



#Mantıksal operatörleri kullanma
#And operatörünü kullanma
np.logical_and(bmi > 21, bmi < 22) #Bu bize true false değerler döndürür.
bmi[np.logical_and(bmi > 21, bmi < 22)] #21 büyük 22den küçük değerleri elde edebiliriz.

np.logical_not()
np.logical_or()

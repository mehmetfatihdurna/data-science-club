import matplotlib.pyplot as plt

#Yıl ve popülasyon adında iki liste oluşturuyoruz
year = [1950, 1970, 1990, 2010]
pop = [2.5191, 3.692, 5.263, 6.972]

#Ekrana yazdırıyoruz ilki x ikinicisi y ekseni
plt.plot(year, pop)
plt.show()

#Scatter plot için
plt.scatter(year, pop)
plt.show()

# x eksenin ölçeklendirmesini logoritmik yapma
plt.xscale('log')

#Histogram oluşturma bins değeri kaç kutuya bölüneceğini belirtir.
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins=3)
plt.show()

#Temizlemek için
plt.clf()

#Eksenlere etiket yazmak için 
plt.xlabel('Year')
plt.ylabel('Population')

#Tablomuza başlık için
plt.title('World Population Projections')

# y ekseninin gözükmesini istediğimiz değerlerini yazıyoruz,
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])




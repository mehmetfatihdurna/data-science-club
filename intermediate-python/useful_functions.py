#Using enumerate

avengers = ['hawkeye','iron man','thor','quicksilver']

for index, value in enumerate(avengers, start = 10):
    print(index, value)

#Using zip
avengers = ['hawkeye','iron man','thor','quicksilver']
names = ['barton', 'stark', 'odinson','maximoff']

z = zip(avengers, names)
print(*z)

#Unzipping 
hero, name = zip(*z)

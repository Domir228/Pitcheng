import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('home.csv')
print('Фильмы с Бенедиктом Камбербэтчом лучше чем с Доменико Торетто')
vin_diesil_films = 0
films = []
rating = 0
def vin_films(row):
    global vin_diesil_films, films, rating
    if row['Actors'].find('Vin Diesel') != -1:
        vin_diesil_films += 1
        films.append(row['Title'])
        rating += row['Rating']
    return False
df.apply(vin_films, axis = 1)
DwayneJohnson_films = 0
films2 = []
rating2 = 0
def vin_films(row):
    global DwayneJohnson_films, films2, rating2
    if row['Actors'].find('Benedict Cumberbatch') != -1:
        DwayneJohnson_films += 1
        films2.append(row['Title'])
        rating2 += row['Rating']
    return False
df.apply(vin_films, axis = 1)
ckala = round(rating2/len(films2))
semia = round(rating/len(films))
s = pd.Series(data = [ckala, semia], index = ['Бенедикт Кимбербетч', 'Доменико Торетто'])
s.plot(kind = 'pie')
plt.show()



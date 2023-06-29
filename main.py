import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('home.csv')
com_count = 0
com_rating = 0
fan_count = 0
fan_rating = 0
def comedy(row):
    global com_count, com_rating
    if row['Genre'].find('Comedy') != -1:
        com_rating += row['Rating']
        com_count += 1
    return False
df.apply(comedy, axis = 1)
def fontastica(row):
    global fan_count, fan_rating
    if row['Genre'].find('Fantasy') != -1:
        fan_rating += row['Rating']
        fan_count += 1
    return False
df.apply(fontastica, axis = 1)
a = pd.Series(data = [round(com_rating/com_count, 2), round(fan_rating/fan_count)], index = ['Комедия', 'Фантастика'])
a.plot(kind = 'barh')
plt.show()
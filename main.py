import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# zad 1
# x = np.arange(20)
#
# plt.plot(x, 1/(x+1), label='f(x)=1/x ')
#
# plt.legend()
# plt.ylabel('f(x)')
# plt.xlabel('x')
#
# plt.ylim([0, 1])
# plt.xlim([0, len(x)])
# plt.show()

# zad 2
# x = np.arange(20)
#
# plt.plot(x, 1/(x+1), 'g:>', label='f(x)=1/x ')
#
# plt.legend()
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.title('Wykres funkcji f(x) dla x [1, 20]')
#
# plt.ylim([0, 1])
# plt.xlim([0, len(x)])
#
# plt.yticks(np.arange(0,1.1,0.2))
# plt.xticks(np.arange(0,20.1,2.5))

# zad 3
# x = np.arange(0, 30, 0.1)
# plt.figure(figsize=(8, 6))
# plt.plot(x, np.sin(x), label='sin(x)', c='#affaaa')
# plt.plot(x, np.cos(x), label='cos(x)', c='#abcdef')
#
# plt.ylim([-1.5, 1.5])
#
# plt.title('Wykres funkci sin(x) i cos(x) dla x [0, 30]', fontdict={'fontname': 'Comic Sans MS', 'fontsize':16} )
# plt.ylabel('y', loc='top', rotation=0, fontdict={'fontname': 'Arial', 'fontsize':15})
# plt.xlabel('x', loc='right', fontdict={'fontname': 'Arial', 'fontsize':15})
# plt.legend()
#
# plt.xticks(rotation=45)
# plt.yticks(rotation=90)
#
# plt.show()

# zad 4
df = pd.read_csv("iris.data", sep=",", header=None)
df.rename(columns = {0:'sepal lenght', 1:'sepal width',4:'Name'}, inplace = True)
x = df['sepal lenght']
y = df['sepal width']

# data = {'a': np.arange(50),
#         'c': np.random.randint(0,50,50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
#
# plt.scatter('a','b', c='c', s='d',  data=data)

#
# plt.scatter(x,y, c=np.random.randint(0,50,150), s=abs(x-y),)
# plt.xlabel('sepal lenght')
# plt.ylabel('sepal width')
# plt.title('iris')
#
# plt.show()

# zad 4

# xlsx = pd.read_excel('imiona.xlsx', header=0)
# df = pd.DataFrame(data=xlsx)
#
# k = df.groupby('Plec').sum().iloc[0,1]
# m = df.groupby('Plec').sum().iloc[1,1]
#
# plt.rcParams["figure.figsize"] = (12,8)                               # rozmiar
#
# fig, axs = plt.subplots(1,3)
# axs[0].bar('Dziewczynki', k,color=['olive'], label='Dziewczynki', )
# axs[0].bar('Chłopcy', m,color=['teal'], label='Chłopcy')
# axs[0].set_ylabel('Liczba urodzin w mln', fontdict={'fontname': 'Arial', 'fontsize':15}, loc='bottom')
# axs[0].set_yticks(np.arange(3000000,4000000.1,100000))
# axs[0].set_title('[2000-2017]')
# axs[0].tick_params(axis='x', labelrotation = 45)
# axs[0].grid(axis="y", color="black", alpha=.4, linewidth=.2)
#
# grupa = df.groupby(['Rok', 'Plec'])
# etykiety = grupa.groups.keys()
# wartosci = grupa.agg('Liczba').sum()
#
#
# dfm = df.loc[df['Plec'].str.contains('M', regex=True)]
# dfk = df.loc[df['Plec'].str.contains('K', regex=True)]
#
# grupak = dfk.groupby('Rok')
# grupam = dfm.groupby('Rok')
#
# latak = list(grupak.groups.keys())
# liczba_k = list(grupak.agg('Liczba').sum())
#
# liczba_m = list(grupam.agg('Liczba').sum())
# latam = list(grupam.groups.keys())
#
# axs[1].plot(latak, liczba_k, label='Kobiety')
# axs[1].plot(latam,liczba_m, label="Mężczyźni")
# axs[1].legend()
# axs[1].set_ylabel('Liczba', fontdict={'fontname': 'Arial', 'fontsize':10})
# axs[1].set_xlabel('Rok', fontdict={'fontname': 'Arial', 'fontsize':10})
# axs[1].tick_params(axis='x', labelrotation = 45)
# axs[1].tick_params(axis='y', labelrotation = 45)
# axs[1].set_title('Liczba urodzin\n z podziałem na płeć')
#
# grupa_r = df.groupby(['Rok'])
# etykiety = list(grupa_r.groups.keys())
# wartosci = (grupa_r.agg('Liczba').sum())
# axs[2].bar(etykiety, wartosci, color=['skyblue','olive'])
# axs[2].set_ylabel('Liczba', fontdict={'fontname': 'Arial', 'fontsize':10})
# axs[2].set_xlabel('Rok', fontdict={'fontname': 'Arial', 'fontsize':10})
# axs[2].tick_params(axis='x', labelrotation = 45)
# axs[2].tick_params(axis='y', labelrotation = 45)
# axs[2].set_title('Liczba wszystkich urodzin')
# axs[2].grid(axis="y", color="black", alpha=.5, linewidth=.4)                      #customowa siatka osi oy

# fig.tight_layout()                                                                #odstępy między wykresami
# plt.show()

# zad 5

csv = pd.read_csv('zamowienia.csv', sep=';', header=0, decimal='.')
zam = pd.DataFrame(csv)
seria = zam.groupby(['Sprzedawca'])['Utarg'].sum()
explode = np.linspace(0,0.1,len(seria))
colors = np.random.rand(len(seria),3)                                           # randomowe kolory RGB (3) albo RGBA (4)

wedges, texts, autotext = plt.pie(x=seria,
                                explode=explode,
                                labels=seria.index,
                                autopct='%1.1f%%',
                                textprops=dict(color="black"),
                                colors=colors,
                                shadow=True                                     # cienie
                                )
plt.show()


# -*- coding: utf-8 -*-
from pylab import *
# plt.rcParams['font.sans-serif'] = ['SimHei']

def showStatistics():
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from pandas.core.frame import DataFrame
    from pandas.core.series import Series
    matplotlib.rcParams['font.family'] = 'SimHei'

    data = pd.read_csv('D:/movie&tv/movie_EN.csv', encoding="gb2312",
                       names=['Title_EN', 'Year', 'Title_CH', 'Director', 'Cast', 'Link', 'Comment', 'Rating'])
    year = data['Year']
    # min = year.min()
    # max = year.max()
    # num = max - min
    # year.hist(bins=num)
    # plt.show()
    plt.figure(1)
    counts = year.value_counts().sort_index()
    fig1 = counts.plot(kind='bar',title='Num-Year').figure
    fig1.set_size_inches(10,5)
    fig1.show()
    # plt.show()
    # anal = year.describe()
    # print(anal)

    casts = data['Cast']
    result = []
    result1 = pd.Series()
    for cast in casts:
        person = cast.split('/')
        personSeries = pd.Series(person)
        result1 = result1.append(personSeries)
        # result.append(person)
    plt.figure(2)
    # castdata = DataFrame(result)
    freq = result1.value_counts()
    top10 = freq.head(10)
    # print(top10)
    fig2 = top10.plot(kind='bar',title='Num-Cast',fontsize=8).figure
    fig2.show()

    plt.figure(3)
    dir = data['Director']
    num = dir.value_counts()
    top10 = num.head(10)
    fig3 = top10.plot(kind='bar',title='Num-Director').figure

    plt.show()
    # plt.show()
    # castdata.dropna()
    # print(castdata1)
showStatistics()

import pandas as pd
import numpy as np
import requests
import re
from bs4 import BeautifulSoup

def updateRating(html,rating):
    soup = BeautifulSoup(html,"html.parser")
    rating_num = float(soup.find('strong',attrs={'class':'ll rating_num'}).get_text())
    if (rating_num != rating):
        return rating_num
    else:
        return 0

data = pd.read_csv('D:/movie&tv/movie_EN.csv', encoding="gb2312", names=['Title_EN','Year','Title_CH','Director','Cast','Link','Comment','Rating'])
k = 0

while k < data.__len__():
    link = data.iloc[k,-3]
    # print(link)
    rating = data.iloc[k,-1]
    try:
        r = requests.get(link)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        result = updateRating(html,rating)
        if (result != 0):
            title = data.iloc[k,2]
            print("The rating of %s is updated to %s" % (title,result))
        k += 1
    except requests.exceptions.HTTPError as err:
        title = data.iloc[k, 2]
        print("The page of %s is not found!" % title)
        print(err)
        k += 1
print("Finish updating!")



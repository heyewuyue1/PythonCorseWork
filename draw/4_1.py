import requests
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
import pandas as pd
import numpy as np
import json

name = ['北京', '上海' ,'广州', '深圳', '廊坊']
colors = ['r', 'y', 'b', 'g', 'purple']

bj_data = pd.read_csv('data/bj.csv')
sh_data = pd.read_csv('data/sh.csv')
gz_data = pd.read_csv('data/gz.csv')
sz_data = pd.read_csv('data/sz.csv')
lf_data = pd.read_csv('data/lf.csv') 

def geocoding(city, address):
    """
    address convert lat and lng
    :param address: address
    :param currentkey: AK
    :return: places_ll
    """
    url = 'http://api.map.baidu.com/place/v2/search?'
    params = {
        "query": address,
        "region": city,
        "output": 'json',
        "ak": 'SO6ItulU4QGOTniCsG6UskGd866sx6Ur',
        "page_size": 1,
        "page_num":1,
        "scope": 1,
        "city_limit": True
    }
    response = requests.get(url, params=params)
    answer = response.json()
    places_ll = []
    if answer['status'] == 0:
        tmpList = answer['results'][0]
        coordString = tmpList['location']
        coordList = [coordString['lng'], coordString['lat']]
        places_ll.append([address, float(coordList[0]), float(coordList[1])])
        print([address, float(coordList[0]), float(coordList[1])])
        return float(coordList[0]), float(coordList[1])

bj_loc = pd.DataFrame(columns=['name', 'avg', 'x', 'y'])
bj_area = bj_data.板块.unique()
for i in range(len(bj_area)):
    x, y = geocoding('北京', bj_area[i])
    bj_loc.loc[i] = [bj_area[i], bj_data.loc[bj_data.板块 == bj_area[i], 'rent'].mean(), x, y]
bj_loc.to_csv('data/bj_loc.csv', index=False)

sh_loc = pd.DataFrame(columns=['name', 'avg', 'x', 'y'])
sh_area = sh_data.板块.unique()
for i in range(len(sh_area)):
    x, y = geocoding('上海', sh_area[i])
    sh_loc.loc[i] = [sh_area[i], sh_data.loc[sh_data.板块 == sh_area[i], 'rent'].mean(), x, y]
sh_loc.to_csv('data/sh_loc.csv', index=False)
    
gz_loc = pd.DataFrame(columns=['name', 'avg', 'x', 'y'])
gz_area = gz_data.板块.unique()
for i in range(len(gz_area)):
    x, y = geocoding('广州', gz_area[i])
    gz_loc.loc[i] = [gz_area[i], gz_data.loc[gz_data.板块 == gz_area[i], 'rent'].mean(), x, y]
gz_loc.to_csv('data/gz_loc.csv', index=False)
    
sz_loc = pd.DataFrame(columns=['name', 'avg', 'x', 'y'])
sz_area = sz_data.板块.unique()
for i in range(len(sz_area)):
    x, y = geocoding('深圳', sz_area[i])
    sz_loc.loc[i] = [sz_area[i], sz_data.loc[sz_data.板块 == sz_area[i], 'rent'].mean(), x, y]
sz_loc.to_csv('data/sz_loc.csv', index=False)
    
lf_loc = pd.DataFrame(columns=['name', 'avg', 'x', 'y'])
lf_area = lf_data.板块.unique()
for i in range(len(lf_area)):
    x, y = geocoding('廊坊', lf_area[i])
    lf_loc.loc[i] = [lf_area[i], lf_data.loc[lf_data.板块 == lf_area[i], 'rent'].mean(), x, y]
lf_loc.to_csv('data/lf_loc.csv', index=False)
    
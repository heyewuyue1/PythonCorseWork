import requests
import pandas as pd
from lxml import etree


cities = ['bj', 'sh', 'gz', 'sz', 'lf']
url_root = "https://{}.lianjia.com/zufang/"

bj_data = pd.read_csv('data/bj.csv')
sh_data = pd.read_csv('data/sh.csv')
gz_data = pd.read_csv('data/gz.csv')
sz_data = pd.read_csv('data/sz.csv')
lf_data = pd.read_csv('data/lf.csv')

for c in cities:
    if c == 'bj':
        data = pd.read_csv('data/bj.csv')
    if c == 'sh':
        data = pd.read_csv('data/sh.csv')
    if c == 'gz':
        data = pd.read_csv('data/gz.csv')
    if c == 'sz':
        data = pd.read_csv('data/sz.csv')
    if c == 'lf':
        data = pd.read_csv('data/lf.csv')
    url = url_root.format(c)
    for ID in 
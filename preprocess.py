import pandas as pd
import matplotlib.pyplot as plt
bj_data = pd.read_csv('spider/bj.csv')
sh_data = pd.read_csv('spider/sh.csv')
gz_data = pd.read_csv('spider/gz.csv')
sz_data = pd.read_csv('spider/sz.csv')
lf_data = pd.read_csv('spider/lf.csv')

bj_data.drop_duplicates(inplace=True)
sh_data.drop_duplicates(inplace=True)
gz_data.drop_duplicates(inplace=True)
sz_data.drop_duplicates(inplace=True)
lf_data.drop_duplicates(inplace=True)


rent = pd.DataFrame()
rent['bj'] = bj_data['租金'] / bj_data['面积']
rent['sh'] = sh_data['租金'] / sh_data['面积']
rent['gz'] = gz_data['租金'] / gz_data['面积']
rent['sz'] = sz_data['租金'] / sz_data['面积']
rent['lf'] = lf_data['租金'] / lf_data['面积']
rent.boxplot()
plt.show()

def drop_abnormal(data, name):
    q1 = rent[name].quantile(q=0.25)
    q3 = rent[name].quantile(q=0.75)
    low_limit = q1 - 1.5 * (q3 - q1)
    high_limit = q3 + 1.5 * (q3 - q1)
    data.drop(rent[(rent[name] > high_limit)|(rent[name] < low_limit)].index, inplace=True)

drop_abnormal(bj_data, 'bj')
drop_abnormal(sh_data, 'sh')
drop_abnormal(gz_data, 'gz')
drop_abnormal(sz_data, 'sz')
drop_abnormal(lf_data, 'lf')

bj_data['rent'] = bj_data['租金'] / bj_data['面积']
sh_data['rent'] = sh_data['租金'] / sh_data['面积']
gz_data['rent']  = gz_data['租金'] / gz_data['面积']
sz_data['rent']  = sz_data['租金'] / sz_data['面积']
lf_data['rent']  = lf_data['租金'] / lf_data['面积']

bj_data.to_csv('data/bj.csv', index=False)
sh_data.to_csv('data/sh.csv', index=False)
gz_data.to_csv('data/gz.csv', index=False)
sz_data.to_csv('data/sz.csv', index=False)
lf_data.to_csv('data/lf.csv', index=False)

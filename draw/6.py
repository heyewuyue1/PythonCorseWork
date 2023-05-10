import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
cities = ['bj', 'sh', 'gz', 'sz', 'lf']
name = ['北京', '上海' ,'广州', '深圳', '廊坊']
colors = ['r', 'y', 'b', 'g', 'purple']

bj_data = pd.read_csv('data/bj.csv')
sh_data = pd.read_csv('data/sh.csv')
gz_data = pd.read_csv('data/gz.csv')
sz_data = pd.read_csv('data/sz.csv')
lf_data = pd.read_csv('data/lf.csv')

rent = pd.DataFrame()
rent['bj'] = bj_data['租金'] / bj_data['面积']
rent['sh'] = sh_data['租金'] / sh_data['面积']
rent['gz'] = gz_data['租金'] / gz_data['面积']
rent['sz'] = sz_data['租金'] / sz_data['面积']
rent['lf'] = lf_data['租金'] / lf_data['面积']

mean = rent.mean().to_list()
print(mean)

bj_gdp = 18.4
sh_gdp = 17.36
gz_gdp = 15.04
sz_gdp = 17.37
lf_gdp= 6.45

gdp = [bj_gdp, sh_gdp, gz_gdp, sz_gdp, lf_gdp]
print(gdp)

y = [gdp[i] * 10000 / mean[i] for i in range(5)]

plt.bar(name, y, color=colors)
plt.grid(axis='y', linestyle='--', alpha=0.8)
plt.xlabel('城市', fontsize=10)
plt.ylabel('人均GDP/平均单位面积租金', fontsize=10)
for x, y in zip(name, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.suptitle('不同城市的人均GDP和平均单位面积租金比例')
plt.show()

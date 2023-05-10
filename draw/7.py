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

# mean = pd.DataFrame(rent.mean().to_numpy().reshape(1, 5))
mean = rent.mean().to_list()
print(mean)

# 国家统计局
bj_income = 75002
sh_income = 78027
gz_income = 68900
sz_income = 70800
lf_income= 37300

income = [bj_income, sh_income, gz_income, sz_income, lf_income]
print(income)

y = [income[i] / mean[i] for i in range(5)]

plt.bar(name, y, color=colors)
plt.grid(axis='y', linestyle='--', alpha=0.8)
plt.xlabel('城市', fontsize=10)
plt.ylabel('人均可支配收入/平均单位面积租金', fontsize=10)
for x, y in zip(name, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.suptitle('不同城市的人均可支配收入和平均单位面积租金比例')
plt.show()

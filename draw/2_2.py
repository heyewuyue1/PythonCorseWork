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

y1 = rent.mean()
y2 = rent.max()
y3 = rent.min()
y4 = rent.median()

fig, axs = plt.subplots(2, 2)
axs[0, 0].bar(name, y1, color=colors)
axs[0, 0].set_title('单位面积租金均值')
for x, y in zip(name,y1):
    axs[0, 0].text(x, y, '%.2f' % y, ha='center', va='bottom')

axs[0, 1].bar(name, y2, color=colors)
axs[0, 1].set_title('单位面积租金最大值')
for x, y in zip(name,y2):
    axs[0, 1].text(x, y, '%.2f' % y, ha='center', va='bottom')

axs[1, 0].bar(name, y3, color=colors)
axs[1, 0].set_title('单位面积租金最小值')
for x, y in zip(name,y3):
    axs[1, 0].text(x, y, '%.2f' % y, ha='center', va='bottom')

axs[1, 1].bar(name, y4, color=colors)
axs[1, 1].set_title('单位面积租金中位数')
for x, y in zip(name,y4):
    axs[1, 1].text(x, y, '%.2f' % y, ha='center', va='bottom')

for i in range(2):
    for j in range(2):
        axs[i, j].grid(axis='y', linestyle='--', alpha=0.8)
        axs[i, j].set_xlabel('城市', fontsize=10)
        axs[i, j].set_ylabel('租金（单位：元）', fontsize=10)

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.suptitle('单位面积租金情况')
plt.show()
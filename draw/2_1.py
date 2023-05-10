import pandas as pd
import matplotlib.pyplot as plt

bj_data = pd.read_csv('data/bj.csv')
sh_data = pd.read_csv('data/sh.csv')
gz_data = pd.read_csv('data/gz.csv')
sz_data = pd.read_csv('data/sz.csv')
lf_data = pd.read_csv('data/lf.csv')

plt.rcParams['font.sans-serif'] = ['SimHei']
cities = ['bj', 'sh', 'gz', 'sz', 'lf']
name = ['北京', '上海' ,'广州', '深圳', '廊坊']
colors = ['r', 'y', 'b', 'g', 'purple']

bj_mean = bj_data.loc[:, '租金'].mean()
bj_max = bj_data.loc[:, '租金'].max()
bj_min = bj_data.loc[:, '租金'].min()
bj_mid = bj_data.loc[:, '租金'].median()

sh_mean = sh_data.loc[:, '租金'].mean()
sh_max = sh_data.loc[:, '租金'].max()
sh_min = sh_data.loc[:, '租金'].min()
sh_mid = sh_data.loc[:, '租金'].median()

gz_mean = gz_data.loc[:, '租金'].mean()
gz_max = gz_data.loc[:, '租金'].max()
gz_min = gz_data.loc[:, '租金'].min()
gz_mid = gz_data.loc[:, '租金'].median()

sz_mean = sz_data.loc[:, '租金'].mean()
sz_max = sz_data.loc[:, '租金'].max()
sz_min = sz_data.loc[:, '租金'].min()
sz_mid = sz_data.loc[:, '租金'].median()

lf_mean = lf_data.loc[:, '租金'].mean()
lf_max = lf_data.loc[:, '租金'].max()
lf_min = lf_data.loc[:, '租金'].min()
lf_mid = lf_data.loc[:, '租金'].median()

y1 = [bj_mean, sh_mean, gz_mean, sz_mean, lf_mean]
y2 = [bj_max, sh_max, gz_max, sz_max, lf_max]
y3 = [bj_min, sh_min, gz_min, sz_min, lf_min]
y4 = [bj_mid, sh_mid, gz_mid, sz_mid, lf_mid]

fig, axs = plt.subplots(2, 2)
axs[0, 0].bar(name, y1, color=colors)
axs[0, 0].set_title('总体租金均值')
for x, y in zip(name,y1):
    axs[0, 0].text(x, y, '%.2f' % y, ha='center', va='bottom')

axs[0, 1].bar(name, y2, color=colors)
axs[0, 1].set_title('总体租金最大值')
for x, y in zip(name,y2):
    axs[0, 1].text(x, y, '%.2f' % y, ha='center', va='bottom')

axs[1, 0].bar(name, y3, color=colors)
axs[1, 0].set_title('总体租金最小值')
for x, y in zip(name,y3):
    axs[1, 0].text(x, y, '%.2f' % y, ha='center', va='bottom')

axs[1, 1].bar(name, y4, color=colors)
axs[1, 1].set_title('总体租金中位数')
for x, y in zip(name,y4):
    axs[1, 1].text(x, y, '%.2f' % y, ha='center', va='bottom')

for i in range(2):
    for j in range(2):
        axs[i, j].grid(axis='y', linestyle='--', alpha=0.8)
        axs[i, j].set_xlabel('城市', fontsize=10)
        axs[i, j].set_ylabel('租金（单位：元）', fontsize=10)

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.suptitle('总体租金情况')
plt.show()

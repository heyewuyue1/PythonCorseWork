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


fig, axs = plt.subplots(4, 3)
for j in range(0, 4):
    for i in range(1, 4):
        if i < 3:
            if j == 0:
                y = [bj_data.loc[bj_data.房型 == i, '租金'].mean(),sh_data.loc[sh_data.房型 == i, '租金'].mean(),
                gz_data.loc[gz_data.房型 == i, '租金'].mean(),sz_data.loc[sz_data.房型 == i, '租金'].mean(),
                lf_data.loc[lf_data.房型 == i, '租金'].mean()]
                axs[j, i - 1].set_title(str(i) + '居总体租金均值')
            if j == 1:
                y = [bj_data.loc[bj_data.房型 == i, '租金'].max(),sh_data.loc[sh_data.房型 == i, '租金'].max(),
                gz_data.loc[gz_data.房型 == i, '租金'].max(),sz_data.loc[sz_data.房型 == i, '租金'].max(),
                lf_data.loc[lf_data.房型 == i, '租金'].max()]
                axs[j, i - 1].set_title(str(i) + '居总体租金最大值')
            if j == 2:
                y = [bj_data.loc[bj_data.房型 == i, '租金'].min(),sh_data.loc[sh_data.房型 == i, '租金'].min(),
                gz_data.loc[gz_data.房型 == i, '租金'].min(),sz_data.loc[sz_data.房型 == i, '租金'].min(),
                lf_data.loc[lf_data.房型 == i, '租金'].min()]
                axs[j, i - 1].set_title(str(i) + '居总体租金最小值')
            if j == 3:
                y = [bj_data.loc[bj_data.房型 == i, '租金'].median(),sh_data.loc[sh_data.房型 == i, '租金'].median(),
                gz_data.loc[gz_data.房型 == i, '租金'].median(),sz_data.loc[sz_data.房型 == i, '租金'].median(),
                lf_data.loc[lf_data.房型 == i, '租金'].median()]
                axs[j, i - 1].set_title(str(i) + '居总体租金中位数')
        else:
            if j == 0:
                y = [bj_data.loc[bj_data.房型 >= i, '租金'].mean(),sh_data.loc[sh_data.房型 >= i, '租金'].mean(),
                    gz_data.loc[gz_data.房型 >= i, '租金'].mean(),sz_data.loc[sz_data.房型 >= i, '租金'].mean(),
                    lf_data.loc[lf_data.房型 >= i, '租金'].mean()]
                axs[j, i - 1].set_title('3居及3居以上总体租金均值')
            if j == 1:
                y = [bj_data.loc[bj_data.房型 >= i, '租金'].max(),sh_data.loc[sh_data.房型 >= i, '租金'].max(),
                gz_data.loc[gz_data.房型 >= i, '租金'].max(),sz_data.loc[sz_data.房型 >= i, '租金'].max(),
                lf_data.loc[lf_data.房型 >= i, '租金'].max()]
                axs[j, i - 1].set_title('3居及3居以上总体租金最大值')
            if j == 2:
                y = [bj_data.loc[bj_data.房型 >= i, '租金'].min(),sh_data.loc[sh_data.房型 >= i, '租金'].min(),
                gz_data.loc[gz_data.房型 >= i, '租金'].min(),sz_data.loc[sz_data.房型 >= i, '租金'].min(),
                lf_data.loc[lf_data.房型 >= i, '租金'].min()]
                axs[j, i - 1].set_title('3居及3居以上总体租金最小值')
            if j == 3:
                y = [bj_data.loc[bj_data.房型 >= i, '租金'].median(),sh_data.loc[sh_data.房型 >= i, '租金'].median(),
                gz_data.loc[gz_data.房型 >= i, '租金'].median(),sz_data.loc[sz_data.房型 >= i, '租金'].median(),
                lf_data.loc[lf_data.房型 >= i, '租金'].median()]
                axs[j, i - 1].set_title('3居及3居以上总体租金中位数')
        
        axs[j, i - 1].bar(name, y, color=colors)
        axs[j, i - 1].grid(axis='y', linestyle='--', alpha=0.8)
        axs[j, i - 1].set_xlabel('城市', fontsize=10)
        axs[j, i - 1].set_ylabel('租金（单位：元）', fontsize=10)
        axs[j, i - 1].spines['top'].set_visible(False)
        axs[j, i - 1].spines['right'].set_visible(False)
        for x, y in zip(name, y):
            axs[j, i - 1].text(x, y, '%.2f' % y, ha='center', va='bottom')

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.suptitle('不同城市不同户型总体租金情况')
plt.show()
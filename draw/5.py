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


faces = ['东', '西', '南', '北', 'a', 'b', 'c', 'd']
f_str = ['东', '西', '南', '北', '东南', '东北', '西南', '西北']

for i in range(4, 8):
    bj_data['朝向'] = bj_data['朝向'].replace(f_str[i], faces[i])
    sh_data['朝向'] = sh_data['朝向'].replace(f_str[i], faces[i])
    gz_data['朝向'] = gz_data['朝向'].replace(f_str[i], faces[i])
    sz_data['朝向'] = sz_data['朝向'].replace(f_str[i], faces[i])
    lf_data['朝向'] = lf_data['朝向'].replace(f_str[i], faces[i])

fig, ax = plt.subplots(5, 1)

price = []

for j in range(5): 
    avg_price = []
    if j == 0:
        for i in range(8):
            avg_price.append(bj_data.loc[bj_data['朝向'].str.contains(faces[i], na=False), 'rent'].mean())
        ax[j].bar(f_str, avg_price, label='北京', color=colors[j])
    if j == 1:
        for i in range(8):
            avg_price.append(sh_data.loc[sh_data['朝向'].str.contains(faces[i], na=False), 'rent'].mean())
        ax[j].bar(f_str, avg_price, label='上海', color=colors[j])
    if j == 2:
        for i in range(8):
            avg_price.append(gz_data.loc[gz_data['朝向'].str.contains(faces[i], na=False), 'rent'].mean())
        ax[j].bar(f_str, avg_price, label='广州', color=colors[j])

    if j == 3:
        for i in range(8):
            avg_price.append(sz_data.loc[sz_data['朝向'].str.contains(faces[i], na=False), 'rent'].mean())
        ax[j].bar(f_str, avg_price, label='深圳', color=colors[j])

    if j == 4:
        for i in range(8):
            avg_price.append(lf_data.loc[lf_data['朝向'].str.contains(faces[i], na=False), 'rent'].mean())
        ax[j].bar(f_str, avg_price, label='廊坊', color=colors[j])
    price.append(avg_price)
    ax[j].set_xlabel('朝向', fontsize=10)
    ax[j].set_ylabel('单位面积租金', fontsize=10)
    ax[j].spines['top'].set_visible(False)
    ax[j].spines['right'].set_visible(False)
    ax[j].set_title(name[j], fontsize=10)
    for x, y in zip(f_str, avg_price):
        ax[j].text(x, y, '%.2f' % y, ha='center', va='bottom')
    ax[j].grid(axis='y', linestyle='--', alpha=0.8)


price = pd.DataFrame(price)
print(price.sum())

plt.subplots_adjust(hspace=0.8)
plt.suptitle('不同朝向租金情况')
plt.show()
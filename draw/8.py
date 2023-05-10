import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

data = pd.read_csv('./data/floor.csv')

floors = data.floor.unique()
floors.sort()
f_price = pd.DataFrame(columns=['x', 'y'])
for i in range(len(floors)):
    f_price.loc[i] = [floors[i], data.loc[data.floor == floors[i], 'rent'].mean()]

plt.title('北京市租房平均单位面积租金与楼层之间的关系')
plt.grid(linestyle='--')
plt.xlabel('楼层')
plt.ylabel('平均单位面积租金（单位：元）')
plt.tick_params(axis='y', direction='in', color='r', grid_color='r')
plt.plot(f_price.x, f_price.y)
plt.show()
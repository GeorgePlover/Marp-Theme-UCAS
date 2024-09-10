

import pandas as pd
import matplotlib.pyplot as plt

data = {'正式选手参赛人数': [71, 115, 141, 172, 48], '总参赛人数': [174, 556, 172, 490, 79]}
df = pd.DataFrame(data)
df.index = ['12月赛', '1月赛', '4月赛', '5月赛', '6月赛']

plt.plot(df.index, df['正式选手参赛人数'], label='正式选手参赛人数')
plt.plot(df.index, df['总参赛人数'], label='总参赛人数')

plt.xlabel('比赛月份')
plt.ylabel('参赛人数')
plt.title('比赛参赛人数')

plt.legend()
plt.savefig("g.png")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置全局字体为 Times New Roman
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']

# 10种语言名称
languages = ['Arabic', 'Greek', 'French', 'German', 'Italian', 'Portuguese',
             'Russian', 'Japanese', 'Turkish', 'Vietnamese']

# 随机生成每种语言的3个数据点（20-70范围）
np.random.seed(42)  # 固定随机种子保证可复现
values = [np.random.randint(20, 70, 3).tolist() for _ in range(10)]

# 参数设置
N = len(languages)
angle_step = 2 * np.pi / N
width = angle_step * 0.28  # 稍微增大宽度以提高可读性
offsets = [-1*width, 0, 1*width]  # 3个偏移量对应每组3个数据
bottom = 15  # 降低底部基准线

# 计算角度
angles = [i * angle_step for i in range(N)]

# 颜色设置（每个类别一个颜色）
colors = plt.cm.tab10(np.linspace(0, 1, N))  # 使用更鲜明的色系

# 创建极坐标图
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.spines['polar'].set_visible(False)
# 绘制柱子
for i, (lang, data) in enumerate(zip(languages, values)):
    for j, val in enumerate(data):
        angle = angles[i] + offsets[j]
        ax.bar(angle, val, width=width, bottom=30,
               color=colors[i], edgecolor='black', label=lang if j == 0 else "")

# 设置标签和样式
ax.set_xticks(angles)
ax.set_xticklabels(languages, fontsize=10)
ax.set_yticklabels([])
ax.set_theta_offset(np.pi / 2)  # 调整起始角度
ax.set_rlim(bottom, 100)  # 统一设置最大值

# 设置图例（分两列显示）
# handles, labels = ax.get_legend_handles_labels()
# by_label = dict(zip(labels, handles))
# ax.legend(by_label.values(), by_label.keys(), 
#          loc='upper right', 
#          bbox_to_anchor=(1.2, 1.1),
#          ncol=2,  # 分两列显示
#          fontsize=9)

plt.tight_layout()
plt.savefig('polar_bar_chart.pdf')
plt.show()
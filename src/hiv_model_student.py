import numpy as np
import matplotlib.pyplot as plt

# 定义时间序列
time = np.linspace(0, 1, 11)

# 定义模型参数
A = 1000
alpha = 0.3
beta = 0.1

# 定义病毒载量模型
def viral_load(t, A, alpha, beta):
    return A * np.exp(-alpha * t) + beta * np.exp(-beta * t)

# 计算病毒载量
viral_load_values = viral_load(time, A, alpha, beta)

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(time, viral_load_values, label='Viral Load')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Viral Load Over Time')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# 1.1 探索模型
# 生成时间序列
time = np.linspace(0, 10, 100)  # 更精细的时间序列

# 设置模型参数
A = 1000    # 初始参数值
B = 500     # 初始参数值
alpha = 0.5 # 初始参数值
beta = 0.1  # 初始参数值

# 计算病毒载量
viral_load = A * np.exp(-alpha * time) + B * np.exp(-beta * time)

# 绘制病毒载量随时间变化的图表
plt.figure(figsize=(10, 6))
plt.plot(time, viral_load, label='V(t) = A*exp(-αt) + B*exp(-βt)')
plt.xlabel('时间 (天)')
plt.ylabel('病毒载量')
plt.title('HIV 病毒载量随时间变化')
plt.legend()
plt.grid(True)
plt.show()

# 1.2 拟合实验数据
# 加载实验数据
data = np.loadtxt('HIVseries.csv', delimiter=',', skiprows=1)  # 假设 CSV 文件格式
# 或者使用 NPZ 文件
# data = np.load('HIVseries.npz')
# time_data = data['time_in_days']
# viral_load_data = data['viral_load']

# 提取时间和病毒载量数据
time_data = data[:, 0]
viral_load_data = data[:, 1]

# 绘制实验数据点
plt.figure(figsize=(10, 6))
plt.scatter(time_data, viral_load_data, color='red', label='实验数据')
plt.xlabel('时间 (天)')
plt.ylabel('病毒载量')
plt.title('HIV 病毒载量实验数据')
plt.legend()
plt.grid(True)
plt.show()

# 作业 a: 在方程的函数图上叠加实验数据点
plt.figure(figsize=(10, 6))
plt.plot(time, viral_load, label='模型预测')
plt.scatter(time_data, viral_load_data, color='red', label='实验数据')
plt.xlabel('时间 (天)')
plt.ylabel('病毒载量')
plt.title('模型预测与实验数据对比')
plt.legend()
plt.grid(True)
plt.show()

# 作业 b: 调整模型参数
# 这里需要手动调整参数，直到模型与数据一致
# 例如：
A = 800
B = 300
alpha = 0.3
beta = 0.05

viral_load_adjusted = A * np.exp(-alpha * time) + B * np.exp(-beta * time)

plt.figure(figsize=(10, 6))
plt.plot(time, viral_load_adjusted, label='调整后的模型')
plt.scatter(time_data, viral_load_data, color='red', label='实验数据')
plt.xlabel('时间 (天)')
plt.ylabel('病毒载量')
plt.title('调整后的模型与实验数据对比')
plt.legend()
plt.grid(True)
plt.show()

# 作业 c: 分析潜伏期与 1/α 的关系
# 根据调整后的参数计算 1/α
latent_period = 1 / alpha
print(f"T 细胞感染率的倒数 1/α: {latent_period} 天")

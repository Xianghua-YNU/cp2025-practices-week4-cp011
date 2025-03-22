import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1.1 探索模型
# 生成时间序列
time = np.linspace(0, 1, 11)

# 定义病毒载量模型
def viral_load(t, A, alpha, beta, B):
    return A * np.exp(-alpha * t) + B * np.exp(-beta * t)

# 绘制不同参数下的病毒载量曲线
A_values = [1, 2, 3]
alpha_values = [0.1, 0.2, 0.3]
beta_values = [0.05, 0.1, 0.15]

plt.figure(figsize=(10, 6))
for A in A_values:
    for alpha in alpha_values:
        for beta in beta_values:
            viral = viral_load(time, A, alpha, beta, 0)
            plt.plot(time, viral, label=f'A={A}, alpha={alpha}, beta={beta}')

plt.xlabel('Time')
plt.ylabel('Viral Load')
plt.title('Viral Load over Time with Different Parameters')
plt.legend()
plt.grid(True)
plt.show()

# 1.2 拟合实验数据
# 读取实验数据
url = 'http://www.physics.upenn.edu/biology/PMLS/Datasets/1HIVseries.csv'
data = pd.read_csv(url, header=None)
hiv_data = data.values

# 绘制实验数据
plt.figure(figsize=(10, 6))
plt.plot(hiv_data[:, 0], hiv_data[:, 1], 'o', label='Experimental Data')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Experimental HIV Data')
plt.legend()
plt.grid(True)
plt.show()

# 定义损失函数
def loss_function(params, data, time):
    A, alpha, beta, B = params
    predicted = A * np.exp(-alpha * time) + B * np.exp(-beta * time)
    return np.mean((predicted - data) ** 2)

# 使用scipy.optimize进行参数优化
from scipy.optimize import minimize

initial_guess = [1, 0.1, 0.05, 1]
result = minimize(loss_function, initial_guess, args=(hiv_data[:, 1], hiv_data[:, 0]))

# 输出优化后的参数
optimized_params = result.x
print(f'Optimized Parameters: A={optimized_params[0]}, alpha={optimized_params[1]}, beta={optimized_params[2]}, B={optimized_params[3]}')

# 绘制拟合曲线
optimized_viral_load = viral_load(hiv_data[:, 0], *optimized_params)
plt.figure(figsize=(10, 6))
plt.plot(hiv_data[:, 0], hiv_data[:, 1], 'o', label='Experimental Data')
plt.plot(hiv_data[:, 0], optimized_viral_load, '-', label='Fitted Model')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Fitted HIV Data')
plt.legend()
plt.grid(True)
plt.show()

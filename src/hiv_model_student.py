import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 定义时间序列
time = np.linspace(0, 1, 11)

# 定义模型参数
A = 1000	
alpha = 0.3	
beta = 0.1
def viral_load(t, A, alpha, beta):
    return A * np.exp(-alpha * t) + beta * np.exp(-beta * t)

# 使用不同的模型参数绘制图像
plt.figure(figsize=(10, 6))
plt.plot(time, viral_load(time, 1000, 0.3, 0.1), label='A=1000, alpha=0.3, beta=0.1')
plt.plot(time, viral_load(time, 500, 0.5, 0.2), label='A=500, alpha=0.5, beta=0.2')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Viral Load Over Time with Different Parameters')
plt.legend()
plt.grid(True)
plt.show()

# 读取实验数据
url = "https://www.physics.upenn.edu/biophys/PMLS/Datasets/1HIVseries.csv"
data = pd.read_csv(url, header=None)
time_in_days = data[0]
viral_load_data = data[1]

# 绘制实验数据
plt.figure(figsize=(10, 6))
plt.scatter(time_in_days, viral_load_data, label='Experimental Data', color='red')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Experimental Viral Load Data')
plt.legend()
plt.grid(True)
plt.show()

# 拟合模型参数
from scipy.optimize import curve_fit

# 定义拟合函数
def fit_viral_load(t, A, alpha, beta):
    return viral_load(t, A, alpha, beta)

# 使用curve_fit进行拟合
params, covariance = curve_fit(fit_viral_load, time_in_days, viral_load_data)

# 打印拟合参数
A_fit, alpha_fit, beta_fit = params
print(f"Fitted Parameters: A={A_fit}, alpha={alpha_fit}, beta={beta_fit}")

# 绘制拟合结果
plt.figure(figsize=(10, 6))
plt.scatter(time_in_days, viral_load_data, label='Experimental Data', color='red')
plt.plot(time_in_days, fit_viral_load(time_in_days, *params), label='Fitted Model', color='blue')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Fitted Viral Load Model')
plt.legend()
plt.grid(True)
plt.show()

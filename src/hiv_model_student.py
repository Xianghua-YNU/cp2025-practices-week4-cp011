import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# 1.1 探索模型
# 生成时间序列
time = np.linspace(0, 10, 100)

# 定义模型参数
A = 1
a = 0.1
B = 0.5
beta = 0.05

# 定义病毒载量模型
def viral_load_model(t, A, a, B, beta):
    return A * np.exp(-a * t) + B * np.exp(-beta * t)

# 计算病毒载量
viral_load = viral_load_model(time, A, a, B, beta)

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(time, viral_load, label='Viral Load Model')
plt.title('Viral Load Over Time')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.legend()
plt.grid(True)
plt.show()

# 1.2 拟合实验数据
# 假设我们有实验数据
# 这里我们使用随机生成的数据来模拟实验数据
np.random.seed(0)
time_data = np.linspace(0, 10, 20)
viral_load_data = viral_load_model(time_data, A, a, B, beta) + np.random.normal(0, 0.1, size=time_data.shape)

# 使用curve_fit进行参数拟合
params, covariance = curve_fit(viral_load_model, time_data, viral_load_data, p0=[1, 0.1, 0.5, 0.05])

# 打印拟合参数
A_fit, a_fit, B_fit, beta_fit = params
print(f"Fitted Parameters: A={A_fit}, a={a_fit}, B={B_fit}, beta={beta_fit}")

# 绘制拟合曲线
viral_load_fit = viral_load_model(time_data, *params)
plt.figure(figsize=(10, 6))
plt.plot(time_data, viral_load_data, 'o', label='Data')
plt.plot(time_data, viral_load_fit, '-', label='Fit')
plt.title('Viral Load Data and Fit')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.legend()
plt.grid(True)
plt.show()

# 从文件中读取数据
# 假设数据文件名为HIVseries.csv
# HIVseries.csv文件包含两列：time_in_days和viral_load
data = pd.read_csv('HIVseries.csv')
time_data_file = data['time_in_days'].values
viral_load_data_file = data['viral_load'].values

# 使用curve_fit进行参数拟合
params_file, covariance_file = curve_fit(viral_load_model, time_data_file, viral_load_data_file, p0=[1, 0.1, 0.5, 0.05])

# 打印拟合参数
A_fit_file, a_fit_file, B_fit_file, beta_fit_file = params_file
print(f"Fitted Parameters from File: A={A_fit_file}, a={a_fit_file}, B={B_fit_file}, beta={beta_fit_file}")

# 绘制拟合曲线
viral_load_fit_file = viral_load_model(time_data_file, *params_file)
plt.figure(figsize=(10, 6))
plt.plot(time_data_file, viral_load_data_file, 'o', label='Data from File')
plt.plot(time_data_file, viral_load_fit_file, '-', label='Fit from File')
plt.title('Viral Load Data and Fit from File')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.legend()
plt.grid(True)
plt.show()

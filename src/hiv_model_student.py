import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1.1 探索模型
# 生成时间序列
time = np.linspace(0, 1, 11)

# 定义模型参数
A = 1
a = 0.1
B = 1
b = 0.1

# 计算病毒载量
viral_load = A * np.exp(-a * time) + B * np.exp(-b * time)

# 绘制图像
plt.plot(time, viral_load)
plt.xlabel('Time')
plt.ylabel('Viral Load')
plt.title('Viral Load Over Time')
plt.show()

# 1.2 拟合实验数据
# 读取数据
hiv_data = pd.read_csv('HIVseries.csv')

# 绘制数据点
plt.scatter(hiv_data['time_in_days'], hiv_data['viral_load'], label='Data Points')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Viral Load Over Time (Experimental Data)')
plt.legend()
plt.show()

# 定义拟合函数
def model(t, A, a, B, b):
    return A * np.exp(-a * t) + B * np.exp(-b * t)

# 使用scipy进行参数拟合
from scipy.optimize import curve_fit

# 拟合数据
params, covariance = curve_fit(model, hiv_data['time_in_days'], hiv_data['viral_load'])

# 打印拟合参数
A_fit, a_fit, B_fit, b_fit = params
print(f"Fitted Parameters: A={A_fit}, a={a_fit}, B={B_fit}, b={b_fit}")

# 绘制拟合曲线
plt.scatter(hiv_data['time_in_days'], hiv_data['viral_load'], label='Data Points')
plt.plot(hiv_data['time_in_days'], model(hiv_data['time_in_days'], *params), label='Fitted Curve', color='red')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Viral Load Over Time (Fitted Model)')
plt.legend()
plt.show()

# 作业
# a. 调整模型参数
# b. 进行误差分析
# c. 预测HIV潜伏期


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
B = 1
b = 0.1

# 定义病毒载量模型
def viral_load(t, A, a, B, b):
    return A * np.exp(-a * t) + B * np.exp(-b * t)

# 计算病毒载量
viral_load_values = viral_load(time, A, a, B, b)

# 绘制图像
plt.plot(time, viral_load_values)
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Viral Load Over Time')
plt.show()

# 1.2 拟合实验数据
# 读取数据
data_url = "http://www.physics.upenn.edu/biophysics/PMLS/Datasets/1HIVseries/HIVseries.csv"
hiv_data = pd.read_csv(data_url)

# 绘制实验数据
plt.scatter(hiv_data['time_in_days'], hiv_data['viral_load'], label='Experimental Data')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Experimental Viral Load Data')
plt.legend()
plt.show()

# 拟合模型参数
params, covariance = curve_fit(viral_load, hiv_data['time_in_days'], hiv_data['viral_load'])

# 打印拟合参数
A_fit, a_fit, B_fit, b_fit = params
print(f"Fitted Parameters: A={A_fit}, a={a_fit}, B={B_fit}, b={b_fit}")

# 绘制拟合曲线
plt.scatter(hiv_data['time_in_days'], hiv_data['viral_load'], label='Experimental Data')
plt.plot(hiv_data['time_in_days'], viral_load(hiv_data['time_in_days'], *params), label='Fitted Model', color='red')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Fitted Viral Load Model')
plt.legend()
plt.show()

# 作业
# a. 调整模型参数
# b. 进行误差分析
# c. 预测HIV潜伏期

# 假设潜伏期大约是10年，即3650天
latent_period = 3650

# 预测潜伏期的病毒载量
predicted_viral_load = viral_load(latent_period, *params)
print(f"Predicted viral load at latent period: {predicted_viral_load}")

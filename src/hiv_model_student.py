

import numpy as np
import matplotlib.pyplot as plt

# 1.1 探索模型
# 生成时间序列
time = np.linspace(0, 1, 11)

# 定义模型参数
A = 1
a = 0.1
B = 0.5
beta = 0.05

# 计算病毒载量
viral_load = A * np.exp(-a * time) + B * np.exp(-beta * time)

# 绘制图形
plt.plot(time, viral_load)
plt.title('Viral Load Over Time')
plt.xlabel('Time')
plt.ylabel('Viral Load')
plt.grid(True)
plt.show()

# 1.2 拟合实验数据
# 假设我们有实验数据
time_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
viral_load_data = np.array([0.1, 0.5, 1.2, 0.8, 0.3, 0.2, 0.15, 0.1, 0.08, 0.05, 0.03])

# 定义拟合函数
def model(t, A, a, B, beta):
    return A * np.exp(-a * t) + B * np.exp(-beta * t)

# 使用scipy进行参数拟合
from scipy.optimize import curve_fit

params, covariance = curve_fit(model, time_data, viral_load_data, p0=[1, 0.1, 0.5, 0.05])

# 打印拟合参数
A_fit, a_fit, B_fit, beta_fit = params
print(f"Fitted Parameters: A={A_fit}, a={a_fit}, B={B_fit}, beta={beta_fit}")

# 绘制拟合曲线
viral_load_fit = model(time_data, *params)
plt.plot(time_data, viral_load_data, 'o', label='Data')
plt.plot(time_data, viral_load_fit, '-', label='Fit')
plt.title('Viral Load Data and Fit')
plt.xlabel('Time')
plt.ylabel('Viral Load')
plt.legend()
plt.grid(True)
plt.show()

if __name__ == "__main__":
    main()

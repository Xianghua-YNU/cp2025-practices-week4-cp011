

import numpy as np
import matplotlib.pyplot as plt

# 1.1 探索模型
time = np.linspace(0, 1, 11)

# 定义不同的参数组合并绘制模型曲线
plt.figure(figsize=(10, 6))
params = [
    {'A': 1000, 'B': 500, 'alpha': 5, 'beta': 1},
    {'A': 800, 'B': 200, 'alpha': 2, 'beta': 0.5},
    {'A': 1500, 'B': 300, 'alpha': 10, 'beta': 0.1},
    {'A': 500, 'B': 100, 'alpha': 3, 'beta': 0.3}
]

for param in params:
    viral_load = param['A'] * np.exp(-param['alpha'] * time) + param['B'] * np.exp(-param['beta'] * time)
    plt.plot(time, viral_load, label=f"A={param['A']}, α={param['alpha']}\nB={param['B']}, β={param['beta']}")

plt.xlabel('Time')
plt.ylabel('Viral Load')
plt.title('Model Exploration with Different Parameters')
plt.legend()
plt.show()

# 1.2 导入实验数据并绘制散点图
# 假设数据文件为CSV格式
hiv_data = np.loadtxt('HIVseries.csv', delimiter=',')
time_days = hiv_data[:, 0]
viral_load_data = hiv_data[:, 1]

plt.figure(figsize=(10, 6))
plt.scatter(time_days, viral_load_data, marker='o', color='blue', label='Experimental Data')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Experimental HIV Viral Load Over Time')
plt.legend()
plt.show()

# 作业a: 手动调整参数并叠加模型
A = 150000
B = 50000
alpha = 0.8
beta = 0.05

model_time = np.linspace(0, max(time_days), 100)
model_viral = A * np.exp(-alpha * model_time) + B * np.exp(-beta * model_time)

plt.figure(figsize=(10, 6))
plt.scatter(time_days, viral_load_data, label='Experimental Data')
plt.plot(model_time, model_viral, 'r-', label=f'Model: A={A}, B={B}\nα={alpha}, β={beta}')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Manual Parameter Adjustment for Model Fitting')
plt.legend()
plt.show()

# 作业b: 通过长期数据估计参数并调整剩余参数
# 选择时间较大的数据点进行拟合
threshold = 7  # 根据数据分布调整阈值
mask = time_days > threshold
t_long = time_days[mask]
v_long = viral_load_data[mask]

# 对数线性回归拟合长期趋势
log_v = np.log(v_long)
coeffs = np.polyfit(t_long, log_v, 1)
beta_est = -coeffs[0]
B_est = np.exp(coeffs[1])

# 计算初始值A
A_est = viral_load_data[0] - B_est

# 调整alpha参数
alpha_est = 0.7  # 通过观察数据调整

model_viral_refined = A_est * np.exp(-alpha_est * model_time) + B_est * np.exp(-beta_est * model_time)

plt.figure(figsize=(10, 6))
plt.scatter(time_days, viral_load_data, label='Experimental Data')
plt.plot(model_time, model_viral_refined, 'g-', 
         label=f'Refined Model: A={A_est:.0f}, B={B_est:.0f}\nα={alpha_est}, β={beta_est:.3f}')
plt.xlabel('Time (days)')
plt.ylabel('Viral Load')
plt.title('Semi-Automated Parameter Estimation')
plt.legend()
plt.show()

# 作业c: 计算1/α并与潜伏期比较
latency_period = 10 * 365  # 十年潜伏期（天）
alpha_inverse = 1 / alpha_est

print(f"1/α = {alpha_inverse:.1f} days")
print(f"HIV潜伏期: {latency_period} days")
print("结论: T细胞感染率的倒数远小于潜伏期" if alpha_inverse < latency_period 
      else "结论: 1/α大于潜伏期（需要重新检查参数）")

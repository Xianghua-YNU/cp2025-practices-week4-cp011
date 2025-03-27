import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# 定义微分方程
def hiv_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]
 
# 初始条件
initial_conditions = [990, 10, 0]  # 易感者990，感染者10，移除者0
 
# 参数
beta = 0.00005  # 感染率
gamma = 0.01    # 康复率
 
# 时间点
t = np.linspace(0, 100, 100)  # 从0到100天，共100个时间点
 
# 解微分方程
solution = odeint(hiv_model, initial_conditions, t, args=(beta, gamma))
 
# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Susceptible')
plt.plot(t, solution[:, 1], label='Infected')
plt.plot(t, solution[:, 2], label='Recovered/Dead')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.legend()
plt.title('HIV Virus Load Model')
plt.grid(True)
plt.show()

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# 定义模型方程的函数
def hiv_model(y, t, beta, delta, mu, gamma):
    V, T = y
    dVdt = beta * V * T - delta * V  # 病毒复制和清除的动态平衡
    dTdt = -gamma * V * T + mu * T   # CD4细胞死亡和被病毒感染的动态平衡
    return [dVdt, dTdt]
 
# 参数设定
beta = 0.5  # 病毒复制速率
delta = 0.1 # 病毒清除速率
mu = 0.01   # CD4细胞自然死亡速率
gamma = 0.02 # CD4细胞被病毒杀死的速率
initial_conditions = [100, 1000]  # 初始病毒数量和CD4细胞数量
t = np.linspace(0, 100, 1000)  # 时间范围
 
# 解ODEs
solution = odeint(hiv_model, initial_conditions, t, args=(beta, delta, mu, gamma))
V, T = solution.T
 
# 绘图展示结果
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(t, V, label='Virus load')
plt.xlabel('Time')
plt.ylabel('Virus number')
plt.title('HIV Virus Load Over Time')
plt.legend()
 
plt.subplot(122)
plt.plot(t, T, label='CD4 Cells')
plt.xlabel('Time')
plt.ylabel('CD4 Cell number')
plt.title('CD4 Cell Count Over Time')
plt.legend()
 
plt.tight_layout()
plt.show()

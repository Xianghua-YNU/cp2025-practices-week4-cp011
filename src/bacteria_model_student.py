import numpy as np
import matplotlib.pyplot as plt

class BacteriaModel:
    def __init__(self, A, tau):
        """
        初始化细菌生长模型。
        
        参数:
        - A: 模型 W(t) 的幅度参数。
        - tau: 时间常数，控制模型的衰减速度。
        """
        self.A = A
        self.tau = tau

    def v_model(self, t):
        """
        计算 V(t) 模型的值：V(t) = 1 - e^{-t/τ}。
        
        参数:
        - t: 时间变量。
        
        返回值:
        - V(t) 的值。
        """
        return 1 - np.exp(-t/self.tau)

    def w_model(self, t):
        """
        计算 W(t) 模型的值：W(t) = A(e^{-t/τ} - 1 + t/τ)。
        
        参数:
        - t: 时间变量。
        
        返回值:
        - W(t) 的值。
        """
        return self.A * (np.exp(-t/self.tau) - 1 + t/self.tau)

    def plot_models(self, t):
        """
        绘制 V(t) 和 W(t) 的曲线。
        
        参数:
        - t: 时间序列。
        """
        # 计算 V(t) 和 W(t)
        v = self.v_model(t)
        w = self.w_model(t)
        
        # 绘制 V(t) 和 W(t) 曲线
        plt.plot(t, v, label='V(t)')
        plt.plot(t, w, label='W(t)')
        
        # 添加坐标轴标签和标题
        plt.xlabel('Time')
        plt.ylabel('Response')
        plt.title('Bacteria Growth Models')
        
        # 添加图例
        plt.legend()
        
        # 显示图像
        plt.show()

def load_bacteria_data(filepath):
    """
    加载实验数据文件。
    
    参数:
    - filepath: 数据文件的路径。
    
    返回值:
    - time: 时间数据。
    - response: 响应数据。
    """
    try:
        # 尝试加载结构化数据（如 CSV 文件）
        data = np.loadtxt(filepath, delimiter=',')
        return data['time'], data['response']
    except:
        # 如果加载失败，使用普通文本文件加载方式
        return np.loadtxt(filepath, delimiter=',', unpack=True)

def main():
    """
    主函数，用于运行细菌生长模型的模拟和实验数据分析。
    """
    # 初始化模型参数
    model = BacteriaModel(A=1.0, tau=2.0)
    
    # 生成时间序列，范围从 0 到 10，共 100 个点
    t = np.linspace(0, 10, 100)
    
    # 绘制模型曲线
    model.plot_models(t)
    
    # 加载实验数据
    time_data, response_data = load_bacteria_data('data/g149novickA.txt')
    
    # 绘制实验数据点
    plt.scatter(time_data, response_data, label='Experimental Data')
    
    # 添加图例
    plt.legend()
    
    # 显示图像
    plt.show()

if __name__ == "__main__":
    # 运行主函数
    main()





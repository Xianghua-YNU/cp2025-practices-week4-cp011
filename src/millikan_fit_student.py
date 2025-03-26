"""
最小二乘拟合和光电效应实验
"""

import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """
    加载数据文件
    
    参数:
        filename: 数据文件路径
        
    返回:
        x: 频率数据数组
        y: 电压数据数组
    """
    data = np.loadtxt(filename)
    x = data[:, 0]
    y = data[:, 1]
    return x, y
    

def calculate_parameters(x, y):
    """
    计算最小二乘拟合参数
    
    参数:
        x: x坐标数组
        y: y坐标数组
        
    返回:
        m: 斜率
        c: 截距
        Ex: x的平均值
        Ey: y的平均值
        Exx: x^2的平均值
        Exy: xy的平均值
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("输入数据为空，无法计算拟合参数")
    
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x ** 2)
    Exy = np.mean(x * y)
    
    if Exx - Ex ** 2 == 0:
        raise ValueError("除零错误，x 数据可能全相等")
    
    m = (Exy - Ex * Ey) / (Exx - Ex ** 2)
    c = (Ey * Exx - Ex * Exy) / (Exx - Ex ** 2)
    return m, c, Ex, Ey, Exx, Exy

def plot_data_and_fit(x, y, m, c):
    """
    绘制数据点和拟合直线
    
    参数:
        x: x坐标数组
        y: y坐标数组
        m: 斜率
        c: 截距
    
    返回:
        fig: matplotlib图像对象
    """
    if len(x) != len(y):
        raise ValueError("x 和 y 的长度必须相同")
    
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='experimental data')
    ax.plot(x, m * x + c, color='red', label='Least-squares fitting straight line')
    ax.set_xlabel('frequency(Hz)')
    ax.set_ylabel('voltage(V)')
    ax.legend()
    ax.grid()
    return fig

def calculate_planck_constant(m):
    """
    计算普朗克常量
    
    参数:
        m: 斜率
        
    返回:
        h: 计算得到的普朗克常量值
        relative_error: 与实际值的相对误差(%)
    """
    if m <= 0:
        raise ValueError("斜率必须为正值，计算无效")
    
    e = 1.602e-19  # 电子电荷
    h_calc = m * e
    h_actual = 6.626e-34  # 真实普朗克常量
    relative_error = abs((h_calc - h_actual) / h_actual) * 100
    return h_calc, relative_error

def main():
    """主函数"""
    filename = "millikan.txt"
    x, y = load_data(filename)
    
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
    
    print(f"Ex = {Ex:.6e}")
    print(f"Ey = {Ey:.6e}")
    print(f"Exx = {Exx:.6e}")
    print(f"Exy = {Exy:.6e}")
    print(f"斜率 m = {m:.6e}")
    print(f"截距 c = {c:.6e}")
    
    fig = plot_data_and_fit(x, y, m, c)
    
    h, relative_error = calculate_planck_constant(m)
    print(f"计算得到的普朗克常量 h = {h:.6e} J·s")
    print(f"与实际值的相对误差: {relative_error:.2f}%")
    
    fig.savefig("millikan_fit.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()

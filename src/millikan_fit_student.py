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
    data = np.loadtxt(filename)  # 用loadtxt()函数从文本文件“filename”中读取数据
                                 # 并加载到6行2列的NumPy数组data中
    x = data[:, 0]  # 遍历data数组的第一列（索引0）所有元素，存入列表x，表示频率(Hz)
    y = data[:, 1]  # 遍历data数组的第二列（索引1）所有元素，存入列表y，表示电压(V)
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
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x ** 2)
    Exy = np.mean(x * y)
    m = (Exy-Ex*Ey)/(Exx-Ex**2)  # 斜率
    c = (Ey*Exx-Ex*Exy)/(Exx-Ex**2)  # 截距
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
    fig, ax = plt.subplots()  # 创建一个图像和坐标轴
    ax.scatter(x, y, label='experimental data')  
    # 用散点图绘制实验数据点，横轴x表示频率(Hz)，纵轴y表示电压(V)，图例名称设置为"实验数据"
    ax.plot(x, m*x+c, color='red', label='Least-squares fitting straight line')  
    '''
    绘制自变量为x，方程为y=mx+c，颜色为红色，标注名称为“最小二乘拟合直线”的拟合直线
    '''
    ax.set_xlabel('frequency(Hz)')  # 设置x轴名称为"频率(Hz)"
    ax.set_ylabel('voltage(V)')   # 设置y轴名称为"电压(V)"
    ax.legend()  # 显示图例
    ax.grid()  # 添加网格
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
    # 电子电荷
    e = 1.602e-19  # C
    h_calc = m*e   # 计算普朗克常量(J·s)
    h_actual = 6.626e-34  # 真实普朗克常量(J·s)
    relative_error = abs((h_calc-h_actual)/h_actual)*100  
    # 计算相对误差的绝对值，后乘100可以转换为百分比数据
    return h_calc, relative_error

def main():
    """主函数"""
    # 数据文件路径
    filename = "millikan.txt"
    
    # 加载数据
    x, y = load_data(filename)
    
    # 计算拟合参数
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
    
    # 打印结果
    print(f"Ex = {Ex:.6e}")
    print(f"Ey = {Ey:.6e}")
    print(f"Exx = {Exx:.6e}")
    print(f"Exy = {Exy:.6e}")
    print(f"斜率 m = {m:.6e}")
    print(f"截距 c = {c:.6e}")
    
    # 绘制数据和拟合直线
    fig = plot_data_and_fit(x, y, m, c)
    
    # 计算普朗克常量
    h, relative_error = calculate_planck_constant(m)
    print(f"计算得到的普朗克常量 h = {h:.6e} J·s")
    print(f"与实际值的相对误差: {relative_error:.2f}%")
    
    # 保存图像
    fig.savefig("millikan_fit.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()

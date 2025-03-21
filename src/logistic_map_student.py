import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 添加字体配置（在函数外只需设置一次）
rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Zen Hei']  # 中文字体优先级列表
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    """
    绘制分岔图（修复中文显示版本）
    """
    r_values = np.linspace(r_min, r_max, n_r)
    keep = n_iterations - n_discard
    data = np.empty((n_r, keep))
    
    for i, r in enumerate(r_values):
        x = np.empty(n_iterations)
        x[0] = 0.5
        for j in range(1, n_iterations):
            x[j] = r * x[j-1] * (1 - x[j-1])
        data[i] = x[n_discard:]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 显式指定字体属性（双保险）
    font_prop = {'family': 'sans-serif',
                 'fontname': 'SimHei',
                 'size': 12}
    
    ax.plot(np.repeat(r_values, keep), data.ravel(), 
           ',', c='teal', alpha=0.15, markersize=0.8)
    ax.set(xlabel='r', ylabel='x', 
          title='Logistic映射分岔图', **font_prop)  # 应用字体设置
    ax.set_xlim(r_min, r_max)
    
    # 保存时确保字体嵌入
    fig.savefig("bifurcation.png", 
                dpi=300, 
                bbox_inches='tight', 
                facecolor='white')
    return fig



def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射

    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数

    返回:
        x: 迭代序列数组
    """
    x = np.empty(n)  # 改用empty提高初始化效率
    x[0] = x0
    prev = x0  # 使用局部变量减少数组访问
    for i in range(1, n):
        prev = r * prev * (1 - prev)
        x[i] = prev
    return x

def plot_time_series(r, x0, n):
    """
    绘制时间序列图

    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数

    返回:
        fig: matplotlib图像对象
    """
    x = iterate_logistic(r, x0, n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, 'navy', lw=1, alpha=0.8)  # 修改颜色和透明度
    ax.set(xlabel='迭代次数', ylabel='x', 
          title=f'Logistic映射时间序列 (r={r})')
    ax.grid(True, ls='--', alpha=0.6)  # 优化网格显示
    fig.tight_layout()
    return fig

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    """
    绘制分岔图

    参数:
        r_min: r的最小值
        r_max: r的最大值
        n_r: r的取值个数
        n_iterations: 每个r值的迭代次数
        n_discard: 每个r值丢弃的初始迭代点数

    返回:
        fig: matplotlib图像对象
    """
    r_values = np.linspace(r_min, r_max, n_r)
    keep = n_iterations - n_discard
    
    # 预分配数组提升性能
    data = np.empty((n_r, keep))
    
    # 向量化计算
    for i, r in enumerate(r_values):
        x = np.empty(n_iterations)
        x[0] = 0.5
        for j in range(1, n_iterations):
            x[j] = r * x[j-1] * (1 - x[j-1])
        data[i] = x[n_discard:]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(np.repeat(r_values, keep), data.ravel(), 
           ',', c='teal', alpha=0.15, markersize=0.8)  # 优化颜色和标记
    ax.set(xlabel='r', ylabel='x', 
          title='Logistic映射分岔图')
    ax.set_xlim(r_min, r_max)
    fig.tight_layout()
    return fig
def main():
    """主函数"""
    # 时间序列分析
    r_values = [2.0, 3.2, 3.45, 3.6]
    x0 = 0.5
    n = 100
    
    for r in r_values:
        fig = plot_time_series(r, x0, n)
        fig.savefig(f"logistic_r{r}.png", dpi=300)
        plt.close(fig)
    
    # 分岔图分析
    fig = plot_bifurcation(2.5, 4.0, 1000, 1000, 100)
    fig.savefig("bifurcation.png", dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    main()

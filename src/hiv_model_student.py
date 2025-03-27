import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def random_walk_2d(steps):
    """生成二维随机行走轨迹

    参数:
        steps (int): 随机行走的步数

    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    x_coords = np.cumsum(np.random.choice([-1, 1], size=steps))
    y_coords = np.cumsum(np.random.choice([-1, 1], size=steps))
    return (x_coords, y_coords)

def plot_single_walk(path):
    """绘制单个随机行走轨迹

    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    x_coords, y_coords = path
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, marker='o')
    plt.scatter(x_coords[0], y_coords[0], color='red', label='Start')
    plt.scatter(x_coords[-1], y_coords[-1], color='blue', label='End')
    plt.axis('equal')
    plt.legend()
    plt.show()

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    plt.figure(figsize=(10, 8))
    for i in range(1, 5):
        plt.subplot(2, 2, i)
        path = random_walk_2d(100)
        plot_single_walk(path)
        plt.title(f'Random Walk {i}')

def plot_viral_load(time, viral_load, alpha=0.5, beta=0.1):
    """绘制病毒载量随时间变化的图像"""
    plt.figure(figsize=(8, 6))
    plt.plot(time, viral_load, marker='o')
    plt.xlabel('Time')
    plt.ylabel('Viral Load')
    plt.title('Viral Load over Time')
    plt.show()

def load_data(file_path):
    """加载数据"""
    data = pd.read_csv(file_path)
    return data

def main():
    # 生成时间序列
    time = np.linspace(0, 1, 11)

    # 生成病毒载量数据
    viral_load = np.zeros_like(time)
    for i in range(1, len(time)):
        viral_load[i] = viral_load[i-1] + alpha * np.exp(-alpha * time[i-1]) + beta * np.exp(-beta * time[i-1])

    # 绘制病毒载量随时间变化的图像
    plot_viral_load(time, viral_load)

    # 加载实验数据
    hiv_data = load_data('HIVseries.csv')

    # 绘制实验数据
    plt.figure(figsize=(10, 6))
    plt.plot(hiv_data['time_in_days'], hiv_data['viral_load'], marker='o')
    plt.xlabel('Time (days)')
    plt.ylabel('Viral Load')
    plt.title('Experimental HIV Data')
    plt.show()

if __name__ == "__main__":
    main()

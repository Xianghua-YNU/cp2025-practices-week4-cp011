"""
测试最小二乘拟合和光电效应实验代码
"""

import os
import sys
import numpy as np
import pytest
import matplotlib.pyplot as plt

# 添加src目录到路径
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

#from solutions.millikan_fit_solution import load_data, calculate_parameters, calculate_planck_constant, plot_data_and_fit
from src.millikan_fit_student import load_data, calculate_parameters, calculate_planck_constant, plot_data_and_fit

# 测试数据文件路径
DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/millikan.txt')

def test_load_data():
    """测试数据加载函数"""
    x, y = load_data(DATA_FILE)
    
    # 检查数据类型
    assert isinstance(x, np.ndarray), "x应该是numpy数组"
    assert isinstance(y, np.ndarray), "y应该是numpy数组"
    
    # 检查数据长度
    assert len(x) > 0, "x数组不应为空"
    assert len(y) > 0, "y数组不应为空"
    assert len(x) == len(y), "x和y数组长度应相同"
    
    # 检查数据范围（根据millikan.txt的实际数据范围）
    assert np.min(x) > 0, "频率应为正值"
    assert np.max(x) < 1.5e15, "频率超出预期范围"
    assert np.min(y) > 0, "电压应为正值"
    assert np.max(y) < 10, "电压超出预期范围"

def test_calculate_parameters():
    """测试参数计算函数"""
    # 使用简单的测试数据
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
    
    # 检查计算结果
    assert abs(Ex - 3.0) < 1e-5, "Ex计算错误"
    assert abs(Ey - 6.0) < 1e-5, "Ey计算错误"
    assert abs(Exx - 11.0) < 1e-5, "Exx计算错误"
    assert abs(Exy - 22.0) < 1e-5, "Exy计算错误"
    assert abs(m - 2.0) < 1e-5, "斜率m计算错误"
    assert abs(c - 0.0) < 1e-5, "截距c计算错误"
    
    # 使用实际数据测试
    x, y = load_data(DATA_FILE)
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
    
    # 检查计算结果是否合理
    assert isinstance(m, float), "斜率m应为浮点数"
    assert isinstance(c, float), "截距c应为浮点数"
    assert m > 0, "对于millikan数据，斜率应为正值"

def test_calculate_planck_constant():
    """测试普朗克常量计算函数"""
    # 使用已知斜率测试
    known_slope = 4.124e-15  # 这是一个接近实际值的斜率
    h, relative_error = calculate_planck_constant(known_slope)
    
    # 检查计算结果
    assert abs(h - 6.626e-34) / 6.626e-34 < 0.1, "计算的普朗克常量与实际值相差过大"
    assert isinstance(relative_error, float), "相对误差应为浮点数"
    assert relative_error >= 0, "相对误差应为非负值"

def test_plot_data_and_fit():
    """测试绘图函数"""
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    m = 2.0
    c = 0.0
    
    fig = plot_data_and_fit(x, y, m, c)
    
    # 检查返回值是否为matplotlib图像对象
    assert isinstance(fig, plt.Figure), "应返回matplotlib Figure对象"
    
    # 检查图像是否包含两个元素（散点和直线）
    ax = fig.get_axes()[0]
    assert len(ax.get_lines()) >= 1, "图像应至少包含一条线"
    
    # 关闭图像以避免显示
    plt.close(fig)

def test_load_data_invalid_file():
    """测试加载不存在文件时的异常处理"""
    with pytest.raises(FileNotFoundError):
        load_data("nonexistent_file.txt")

def test_calculate_parameters_empty_data():
    """测试空数据时的异常处理"""
    x = np.array([])
    y = np.array([])
    with pytest.raises(ValueError):
        calculate_parameters(x, y)

def test_calculate_parameters_unequal_length():
    """测试x和y长度不匹配时的异常处理"""
    x = np.array([1, 2, 3])
    y = np.array([1, 2])
    with pytest.raises(ValueError):
        calculate_parameters(x, y)

def test_calculate_planck_constant_invalid_slope():
    """测试无效斜率时的异常处理"""
    with pytest.raises(ValueError):
        calculate_planck_constant(0)  # 斜率为0
    with pytest.raises(ValueError):
        calculate_planck_constant(-1)  # 斜率为负

if __name__ == "__main__":
    pytest.main(["-v", __file__])

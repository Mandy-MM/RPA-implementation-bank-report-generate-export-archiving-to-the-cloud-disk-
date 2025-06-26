from typing import *
try:
    from xbot.app.logging import trace as print
except:
    from xbot import print


def increment_variable(variable_value):
    """
    title: 变量自增1
    description: 对输入的变量值 % variable_value % 进行加1操作，返回自增后的结果。
    inputs: 
        - variable_value (int): 需要自增的变量值，eg: "5"
    outputs: 
        - incremented_value (int): 自增后的变量值，eg: "6"
    """
    
    # 检查输入有效性
    if not isinstance(variable_value, (int, float)):
        raise ValueError("输入的变量值必须是数字类型")
    
    # 执行自增操作
    incremented_value = variable_value + 1
    
    return incremented_value

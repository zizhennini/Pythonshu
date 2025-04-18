# 读取用户输入的长度和宽度
length_input = input()
width_input = input()

# 尝试将输入转换为整数，如果失败则转换为浮点数
try:
    # 尝试将长度转换为整数
    length = int(length_input)
except ValueError:
    # 如果转换整数失败，则尝试将长度转换为浮点数
    length = float(length_input)

try:
    # 尝试将宽度转换为整数
    width = int(width_input)
except ValueError:
    # 如果转换整数失败，则尝试将宽度转换为浮点数
    width = float(width_input)

# 计算矩形的面积
area = length * width

# 输出面积，根据输入的数据类型决定输出的格式（这里直接输出，因为Python会自动处理整数和浮点数的格式）
print(f"{area}")

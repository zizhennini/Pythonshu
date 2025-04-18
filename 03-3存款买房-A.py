"""
存款买房问题描述
你刚刚大学毕业，在北京找到了一份很好的工作，决定开始存钱买房。由于北京的房价很高，你要攒几年钱才能付得起房子的首付。

现根据以下假定来计算你需要多长时间才能攒够首付款：

将你想购买的房子的总价称为 total_cost。

将首付款占总房价的比例称为 portion_down_payment。为简单起见，假设 portion_down_payment = 0.30（30%）。

将存款金额称为 current_savings。你的存款从 0 元开始。

假设你的年薪是 annual_salary，按 12 个月平均发放，单位是元。

假设你每个月都要拿出一定百分比的工资来存首付。称为 portion_saved，此值为一个表示百分比的整数，例如 50 表示 50%。

写一个程序来计算你需要多少个月才能攒够钱付首付，不足一个月按一个月计算。
"""

import math


total_cost = float(input())           # '请输入总房价：'total_cost为当前房价
annual_salary = float(input())        # '请输入年薪：'
portion_saved = float(input()) / 100  # '请输入月存款比例：'月存款比例，输入30转为30%

# 根据首付款比例计算首付款金额和每个月需要存款数额
# 补充你的代码
portion_down_payment = 0.30
down_payment = total_cost * portion_down_payment
monthly_deposit = annual_salary / 12 * portion_saved



print(f'首付 {down_payment:.2f} 元', )
print(f'月存款 {monthly_deposit:.2f} 元')

# 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
# 补充你的代码

number_of_months = down_payment / monthly_deposit


print(f'需要{math.ceil(number_of_months)}个月可以存够首付')
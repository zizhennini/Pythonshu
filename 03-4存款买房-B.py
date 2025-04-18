"""
存款买房问题描述
你刚刚大学毕业，在北京找到了一份很好的工作，决定开始存钱买房。由于北京的房价很高，你要攒几年钱才能付得起房子的首付。

现根据以下假定来计算你需要多长时间才能攒够首付款：

将你想购买的房子的总价称为 total_cost。

将首付款占总房价的比例称为 portion_down_payment。为简单起见，假设 portion_down_payment = 0.30（30%）。

将存款金额称为 current_savings。你的存款从 0 元开始。

假设你的年薪是 annual_salary，按 12 个月平均发放，单位是元。

假设你每个月都要拿出一定百分比的工资来存首付。称为 portion_saved，此值为一个表示百分比的整数，例如 50 表示 50%。

假定你每 6 个月加一次工资，每半年加薪比例 semi_annual_raise 是一个表示百分比的整数，例如 7 表示 7%，即第 7 个月的月头涨一次工资，工资涨幅为 7%，以后每过 6 个月再涨一次工资。

写一个程序来计算你需要多少个月才能攒够钱付定金，不足一个月按一个月计算。
"""
total_cost = float(input())  # total_cost为当前房价
annual_salary = float(input())  # 年薪
portion_saved = float(input()) / 100  # 月存款比例，输入30转为30%
semi_annual_raise = float(input()) / 100  # 输入每半年加薪比例，输入7转化为7%

portion_down_payment = 0.30  # 首付比例，浮点数
# 补充你的代码，计算首付款*
down_payment = total_cost * portion_down_payment

print(f'首付 {down_payment:.2f} 元')

current_savings = 0  # 存款金额，从0开始
number_of_months = 0
monthly_salary = annual_salary / 12  # 月工资
monthly_deposit = monthly_salary * portion_saved  # 月存款
# 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
# 补充你的代码
while current_savings < down_payment:
    current_savings += monthly_deposit
    number_of_months += 1
    if number_of_months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)
        monthly_deposit = monthly_salary * portion_saved

    if number_of_months % 12 == 0:
        print("第{}个月月末有{:,.0f}元存款".format(number_of_months, current_savings))
print(f'需要{number_of_months}个月可以存够首付')
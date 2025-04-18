"""
目前我国个人所得税计算公式如下：
应纳个人所得税税额= (工资薪金所得 -五险一金 - 个税免征额)×适用税率-速算扣除数

个税免征额为5000元/月，2018年10月1日起调整后，也就是2018年实行的7级超额累进个人所得税税率表如下：

全月应纳税所得额 = 工资薪金所得 -五险一金 - 个税免征额

全月应纳税所得额（含税级距）  税率(%)   速算扣除数
不超过3,000元                           3                0
超过3,000元至12,000元的部分   10            210
超过12,000元至25,000元的部分 20         1,410
超过25,000元至35,000元的部分 25         2,660
超过35,000元至55,000元的部分 30         4,410
超过55,000元至80,000元的部分 35         7,160
超过80,000元的部分                   45         15,160

请编写一个个税计算器，用户输入为应发工资薪金所得扣除五险一金后的金额，
输出应缴税款和实发工资，结果保留小数点后两位。当输入数字小于0时，输出error。
"""
s = float(input())
taxable = s-5000
if s<0:
    print("error")
elif taxable<0:
    tax = 0
    print(f"应缴税款{tax:.2f}元，实发工资{s:.2f}元。")
else:
    if 0<=taxable <=3000:
        tax_rate=0.03
        deduction=0
    elif 3000<taxable <=12000:
        tax_rate=0.10
        deduction=210
    elif 12000<taxable <=25000:
        tax_rate=0.20
        deduction=1410
    elif 25000<taxable <=35000:
        tax_rate=0.25
        deduction=2660
    elif 35000<taxable <=55000:
        tax_rate=0.30
        deduction=4410
    elif 55000<taxable <=80000:
        tax_rate=0.35
        deduction=7160
    else:
        tax_rate=0.45
        deduction=15160
    tax = taxable * tax_rate - deduction
    n = s - tax
    print(f"应缴税款{tax:.2f}元，实发工资{n:.2f}元。")

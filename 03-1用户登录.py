"""
实现用户输入用户名和密码，
当用户名为admin或administrator且密码为012345时，显示登录成功，否则显示登录失败，
登录失败时允许重复输入3次。
"""
ci = 3
for _ in range(ci):
    name = input()
    mima = input()
    if (name=='admin' or name=='administrator') and mima=='012345':
        print("登录成功")
        break
    else:
        print("登录失败")
else:
    print("超过三次登录失败，程序结束")
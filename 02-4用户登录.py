"""
模拟用户登录行为，用户输入用户名和密码，
当用户名为 admin且密码为012345时，显示登录成功，否则显示登录失败。
"""
name = input()
m = input()
if name=='admin' and m=='012345':
    print('登录成功')
else:
    print('登录失败')
# ok_acc="188888888"#注意input输入的内容都是字符串类型，所以这里的账号也要用字符串类型来表示
# ok_key="666888"
# acc=input("请输入账号：")
# key=input("请输入密码：")
# if acc==ok_acc and key==ok_key:
#     print("登录成功！")
# if acc!=ok_acc or key!=ok_key:
#     print("账号或密码错误，请重新输入！")
a=int(input("请输入第一个边长："))
b=int(input("请输入第二个边长："))
c=int(input("请输入第三个边长："))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print("这是一个等边三角形")
    elif a==b or b==c or a==c:
        print("这是一个等腰三角形")
    else:
        print("这是一个普通三角形")    
else:
    print("输入的边长不能构成三角形，请重新输入！")

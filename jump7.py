print('Hello world!\n这是一个jump7小游戏')
a = 0
b=int(input('请输入100以内的数字'))#数字在100以内
while b > 100 :
    print('让你小于100呀小老弟')
    b=int(input('请输入100以内的数字'))#数字在100以内
    if b <= 100 :
        break
while a < b and b <= 100 :
    a = a+1     
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7 :
        continue   
    else:
        print(a)

num1 = int(input("please input first number: "))
num2 = int(input("please input second number: "))

if  num1>num2:
    x=num1-num2
    num1=num1-x
    num2=num2+x
else:
    x=num2-num1
    num2=num2-x
    num1=num1+x


print(num1,num2)
num = int(input("please input number of lines to print: "))
for i in range(1,(num+1)):
    x=(num-i)*" "
    y=i*"*"
    z=(i-1)*"*"
    print(x+y+z)
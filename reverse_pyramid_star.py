num = int(input("please input number of lines to print: "))
for i in range (1,num+1):
    x=(i-1)*" "
    y=(num+1-i)*"*"
    z=(num-i)*"*"
    print(x+y+z)
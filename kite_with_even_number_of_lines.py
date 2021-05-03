num = int(input("please input number of lines to print: "))
b   = num+1
g   =int(num/2)
for i in range(1,b):
    if (i<=g):
        x=(g-i)*" "
        y=i*"*"
        z=(i-1)*"*"
    else:
        x=(i-g-1)*" "
        y=(b-i)*"*"
        z=(b-1-i)*"*"
    print(x+y+z)

num = int(input("please input number of lines to print: "))
b   = num+1
d   =int(b/2)
# if b%2==0
for i in range(1,b):
   if (i<=d):
       x=(d-i)*" "
       y=i*"*"
       z=(i-1)*"*"
      #  print(x+y+z)
   else:
       x=(i-d)*" "
       y=(b-i)*"*"
       z=(b-1-i)*"*"
      
   print(x+y+z)

for i in range(1,10):
    if (i<=5):
       x=(6-i-1)*" "
       y=i*"*"
       z=(i-1)*"*"
       print(x+y+z)
    else :  
       x=(i-5)*" "
       y=(10-i)*"*"
       z=(9-i)*"*"
      
       print(x+y+z)

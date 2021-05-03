int_lines = int(input("please input number of lines to print: "))

int_middle_line = (int_lines + 1)/2 if int_lines % 2 == 1 else (int_lines)/2 
q = 1 if int_lines % 2 == 0 else 0

for i in range(1, int_lines+1):
   if (i<=int_middle_line):
      x=int(int_middle_line-i)*" "
      y=i*"*"
      z=(i-1)*"*"     
   else:
      x=int(i-int_middle_line - q)*" "
      y=(int_lines+1-i)*"*"
      z=(int_lines-i)*"*"

   print(f"{x}{y}{z}")
   
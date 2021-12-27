tempNumber = int(input("Please enter an integer: "))
factorList = []
for i in range(1, tempNumber+1):
    if tempNumber%i == 0:
        factorList.append(i)

if len(factorList) > 2:
    print("It is a composite number")
elif len(factorList) < 2:    
    print("It is not prime nor a composite number")
else:
    print("It is a prime number")
#this code prints the first two factors(other than one) of an input integer
tempNumber = int(input("Please enter a number: "))
factorList = []
for i in range(2, tempNumber+1):
    if tempNumber%i == 0:
        factorList.append(i)
if len(factorList) == 1:
    print("Number is prime")
else:
    print(factorList[0])
    print(factorList[1])
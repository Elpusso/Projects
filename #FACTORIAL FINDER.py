#FACTORIAL FINDER
fact=1
num= int(input("please enter a number: "))
if num<0:
    print ("factorial doesnt exist")
elif num==0:
    print ("factorial of 0 is 1")
else:
    for i in range (1, num+1):
        fact=fact*i
    print ("Factorial of", num, "is", fact)
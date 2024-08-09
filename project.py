import random

computernumber=random.randrange(1,201)
userinput=int(input(" Enter the number :"))
print("computer number is:" , computernumber)
if computernumber>userinput:
        print("computer won")
elif computernumber<userinput:
        print("you won")
else:
        print("Draw")
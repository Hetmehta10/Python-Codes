# Check whether given number is divisible by 3 and 5 both.
a=int(input("Enter number: "))
if a%3==0 and a%5==0:
        print(a,'Is divisible by 3 and 5 both')
else:
        print(a,'is not divisible by 3 and 5 both')
# Create a class to implement method Overriding.
class Bank:
        def getroi(self):
                return 10
class SBI(Bank):
        def getroi(self):
                return 7

b1 = Bank()
b2 = SBI()

print("Bank Rate of interest:",b1.getroi())
print("SBI Rate of interest:",b2.getroi())
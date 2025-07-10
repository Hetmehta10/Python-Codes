# Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
x2=int(input("Enter coefficient of x^2: "))
x1=int(input("Enter coefficient of x: "))
c=int(input("Enter constant: "))
if ((x1**2)-(4*x2*c))>0:
        print('the equation (%d)x^2 +(%d)x + (%d) has real roots'%(x2,x1,c))
        print("Roots = %f, %f"%((-x1-((x1*2)-(4*x2*c))(1/2))/2,(-x1+((x12)-(4*x2*c))*(1/2))/2))
        
else:
        print("No real roots")
# Write a program which takes any date as input and display next date of the calendar. e.g.
# 1. I/P: day=20 month=9 year=2005
# 2. O/P: day=21 month=9 year 2005
d=int(input("Enter date: "))
m=int(input("Enter month: "))
y=int(input("Enter year: "))
day31=[1,3,5,7,8,10]
if m in day31 and d==31:
        print('date = %d month = %d year = %d'%(1,m+1,y))
elif m==12 and d==31:
        print('date = %d month = %d year = %d'%(1,1,y+1))
elif m in day31 and d<=30:
        print('date = %d month = %d year = %d'%(d+1,m,y))
elif m==2 and d==28 and y%4==0:
        print('date = %d month = %d year = %d'%(d+1,m,y))
elif m==2 and d==28:
        print('date = %d month = %d year = %d'%(1,m+1,y))
elif m not in day31 and d<30:
        print('date = %d month = %d year = %d'%(d+1,m,y))
else:
        print('date = %d month = %d year = %d'%(1,m+1,y))
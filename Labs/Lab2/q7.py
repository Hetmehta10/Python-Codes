'''Write a program to convert given seconds into hours, minutes and
remaining seconds.
'''
a=int(input("Enter time in sec: "))
Min=0
hr=0
if a>=60:
        Min=a//60
        a=a%60
        if Min>=60:
                hr=Min//60
                Min=Min%60

print(hr,':',Min,':',a)
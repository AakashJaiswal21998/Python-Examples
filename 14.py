'''Program to find largest number among 3 number
Developer:Aakash
Date:21.02.2020
--------------------------------'''
a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
if(a>b):
    if(a>c):
        print("The first number you have entered is largest among all i.e.,",a)
    else:
        print("The third number you have entered is largest among all i.e.,",c)
elif(b>a):
     if(b>c):
        print("The second number you have entered is largest among all i.e.,",b)
     else:
        print("The third number you have entered is largest among all i.e.,",c)
else:
    print("The third number you have entered is largest among all i.e.,",c)

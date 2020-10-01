'''Program to print the sequence from lower to upper given by user and start
from odd if lower limit is odd otherwise start from even
Developer:Aakash
Date:22.02.2020
--------------------------------'''
l=int(input("Enter the Lower bound="))
u=int(input("Enter the Upper bound="))
i=l
if(i%2!=0):
    print("Your odd sequence is=")
    while(i<=u):
        print(i,"\t",end="")
        i=i+2
else:
    print("Your even sequence is=")
    while(i<=u):
        print(i,"\t",end="")
        i=i+2

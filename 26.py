'''Program to print the 1+2-3+4-5......+100
Developer:Aakash
Date:03.03.2020
--------------------------------'''
i=1
b=3
k=2
su=0;sm=0;s=0
while(b<=100):
    su=su+b
    b=b+2
while(k<=100):
    sm=sm+k
    k=k+2
s=1+sm-su    
print("The sum of number from 100 to 1=",s)

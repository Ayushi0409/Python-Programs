a=10
b=5
x,y=a,b
while b:
    a,b=b,a%b
gcd=a
lcm=(x*y)//gcd
print(lcm)
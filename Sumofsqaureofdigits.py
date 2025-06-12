n=145
sum=0
while(0<n):
    sum=sum+(n%10)*(n%10)
    n=n//10
print(sum)
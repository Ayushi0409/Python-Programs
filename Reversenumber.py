n=145
rev=0
while(0<n):
    rev=(rev*10)+n%10
    n=n//10
print(rev)
n=123
orig=n
sum=0
while(0<n):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if orig==sum:
    print("armstrome")
else:
    print("non-armstrome")
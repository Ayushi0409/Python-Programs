n=1331
orig=n
rev=0
while(0<n):
    rev=(rev*10)+n%10
    n=n//10
if orig==rev:
    print("palindrome")
else:
    print("non-palindrome")
# cook your dish here
def second_largest(arr):
    a=list(set(arr))
    a.sort()
    return a[-2]
print("second largest number:",second_largest([1,2,4,5,6,7,8]))
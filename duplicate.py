def find_duplicate(arr):
    seen = set()
    dupes = set()
    for num in arr:
        if num in seen:
            dupes.add(num)
        else:
            seen.add(num)
    return list(dupes)

print("Duplicate number:", find_duplicate([1, 2, 2, 3, 5, 4]))

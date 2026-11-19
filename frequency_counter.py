def frequency(arr):
    counts={}

    for num in arr:

        counts[num]= counts[num] +1 if num in counts else 1

    return counts

arr = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
result = frequency(arr)
print(result)
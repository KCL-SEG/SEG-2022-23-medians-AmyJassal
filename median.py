"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

"""Merge sort algorithm."""
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2= r - m
    """Creating arrays with n1 number of 0's"""
    Left = [0] * (n1)
    Right = [0] * (n2)
    
    for i in range(0,n1):
        Left[i] = arr[l+i]
        
    for j in range(0,n2):
        Right[j] = arr[m + 1 + j]
        
    i = 0
    j = 0
    k = l
    
    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = Left[i]
        i += 1
        k += 1
        
def mergeSort(arr, l, r):
    if l < r:

        m = l+(r-l)
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr
        
def median(arr):
    #Sort list first
    #arr = mergeSort(arr, 0, arr.length)
    arr.sort()
    if(len(arr) % 2 == 0):
        n1 = int(len(arr)/2)
        n2 = int((len(arr)/2) - 1)
        n3 = (arr[n1] + arr[n2]) / 2
        return n3
    else:
        n1 = (len(arr)/2) - 1
        return arr[int(n1)]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))
"""Program to sort two arrays in place without using extra space
@Phantom 26-07-2021
"""

def merge(arr1, arr2, n, m): 
    # code here
    i = n-1
    j = 0
    while j<m and i>=0:
        if arr1[i]>arr2[j]:
            arr1[i],arr2[j] = arr2[j], arr1[i]
        else:
            break
        j = j+1
        i = i-1
        print(arr1, arr2, i, j)
    arr1.sort()
    arr2.sort()
    print(arr1, arr2)

merge([1,3,5,7], [0,2,6,8,9], 4, 5)
<<<<<<< HEAD
<<<<<<< HEAD
import sys
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
def maxSubArraySum(a,size):
    max_so_far = 0
    max_ending_here = 0
   
    for i in range(size):
<<<<<<< HEAD
<<<<<<< HEAD
        #max_ending_here += a[i]
        if max_ending_here + a[i]<a[i]:
            max_ending_here = a[i]
        else:
        	max_ending_here+=a[i]
           
        if(max_so_far<max_ending_here):
            max_so_far = max_ending_here
    print(max_so_far)
           
    return max_so_far

def max_SubArray_Sum(a,size):    #Kadane algo
    ##Your code here
    output_arr = [0]*size
    output_arr[0]=a[0]
    max_sum = a[0]
    for i in range(1,size):
        output_arr[i] = max(a[i], output_arr[i-1]+a[i])
        #print(output_arr)
        max_sum = max(max_sum, output_arr[i])
        print(output_arr, max_sum)
    return max_sum


maxSubArraySum([2,3,-6,3,3,-6,1,-5], 5)
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
        max_ending_here += a[i]
        if max_ending_here<0:
            max_ending_here = 0
           
        elif(max_so_far<max_ending_here):
            max_so_far = max_ending_here
           
<<<<<<< HEAD
    return max_so_far
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
    return max_so_far
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
def minJump(n,array):
    element_position = 1
    jump_count = 0
    while(element_position<n):
        element_position += array[element_position-1]
        jump_count+=1
        if element_position>=n:
            return jump_count
       
   
   
if __name__ == "__main__":
    min_jump = minJump(6,[1, 4, 3, 2, 6, 7])
    print(min_jump)
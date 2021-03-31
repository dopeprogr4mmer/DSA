# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
class ZeroOneTwo:
    def __init__(self):
        pass
   
    def sort(self,array):
        index_of_zero = 0
        index_of_one = index_of_zero+1
        index_of_two = index_of_one+1
        for index in range(len(array)):
            if array[index] == 0:
                array.insert(index_of_zero,array[index])
                #print(array,index_of_zero,index)
                array.pop(index+1)
                index_of_zero+=1
            if array[index] == 1:
                if array[index] == array.index(1):
                    array.insert(index_of_zero,array[index])
                else:
                    array.insert(index_of_one,array[index])
                #print(array,index_of_one,index)
                array.pop(index+1)
       
                index_of_one+=1
               
        return array        
       
   
obj = ZeroOneTwo()
sorted_array = obj.sort([0,1,2,1,0,2,1,2,0,1,2,0,1,2,0,1,2,0,1,1,2,0,1,2,0])
print(sorted_array)
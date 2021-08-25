class Solution(object):
	def max_profit(self,prices_list):
		start = 0
		end = 0
		max_profit = 0
		for i in range(len(prices_list)-1):
			for j in range(i+1, len(prices_list)):
				profit = prices_list[j] - prices_list[i]
				if profit>max_profit:
					max_profit = profit
					#print(prices_list[i],prices_list[j],max_profit)
					start,end,max_profit = i,j,profit
					#print(start,end)
		
		return [start,end,max_profit]


<<<<<<< HEAD
<<<<<<< HEAD
#try:
#	sol = Solution()
#	return_value = sol.max_profit([7,6,4,3,1,10])
#	#print(return_value)
#	if return_value[2]>0:
#		print(f'buy on day {return_value[0]+1} and sell on day {return_value[1]+1} for a max profit of {return_value[2]}')
#	else:
#		print(return_value[2])
#except:
#	print('Invalid input. Pass Numeric values only!!')

def maxProfit(prices):					#O(n2) probably
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    l = [None]*n
    r = [None]*n
    o = [None]*n
    #l[0], r[-1] = prices[0], prices[-1]
    for i in range(n):
        l[i]=min(prices[:i+1])
        r[i]=max(prices[i:])
        o[i] = r[i]-l[i]
    #for j in range(n-2,-1,-1):
    #    r[j] = max(prices[j:])
    #for k in range(n):
    #    o[k] = r[k]-l[k]
    print(l,r,o)	
    #print(max(o))

def maxProfit(self, prices):			#O(nlogn)
    len_prices = len(prices)
    
    # base case
    if len_prices < 2:
        return 0
    
    left, right = 0, len_prices - 1
    mid = left + (right - left) // 2
    
    left_prices = prices[0:mid + 1]    # mind plus one
    right_prices = prices[mid + 1:]
    
    left_max_profit = self.maxProfit(left_prices)
    right_max_profit = self.maxProfit(right_prices)
    
    left_min = min(left_prices)
    right_max = max(right_prices)
    
    cross_max_profit = right_max - left_min
    
    return max(left_max_profit, right_max_profit, cross_max_profit)


maxProfit([7,1,5,3,6,4])
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
try:
	sol = Solution()
	return_value = sol.max_profit([7,6,4,3,1,10])
	#print(return_value)
	if return_value[2]>0:
		print(f'buy on day {return_value[0]+1} and sell on day {return_value[1]+1} for a max profit of {return_value[2]}')
	else:
		print(return_value[2])
except:
	print('Invalid input. Pass Numeric values only!!')
<<<<<<< HEAD
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05

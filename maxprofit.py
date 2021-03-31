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

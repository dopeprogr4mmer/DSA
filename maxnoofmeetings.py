class Solution:
    def maximumMeetings(self,n,start,end):
        # code here
        i = 0
        count=1
        meeting_schedule = list(zip(start,end))
        #print(meeting_schedule)
        meeting_schedule = list(sorted(meeting_schedule, key=lambda x: x[1]))
        print(meeting_schedule)
        while(i<len(meeting_schedule)-1):
            for j in range(i,len(meeting_schedule)):
                if meeting_schedule[j][0]>meeting_schedule[i][1]:
                    print(meeting_schedule[i],meeting_schedule[j])
                    
                    count+=1
                    break
            i = j
                
        return count

s = Solution()
count = s.maximumMeetings(30,[4,69,13],[50,74,49])
print(count)
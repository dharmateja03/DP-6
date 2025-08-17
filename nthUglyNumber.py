# TimeComplexity:O(n)
# SpaceComplexity:O(1)
# Approach:
# With brute foce use head and set to find nth number using heap is important beacuse we dont know contribution of each number i.e at kth level whcih number is gonna come first so using heap 
# keeps number ordered
# Optimized approach would be have pointer and numbers for ecah variable we go postion by postions and check min number adn add that to position now for that  number from which it got
# driven pointer would increse 

##########################
# Using pointers to find whose contribution while being smallest
##########################

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[1]
        p2,p3,p5=0,0,0
        n2,n3,n5=2,3,5 #always chain
        f2,f3,f5=2,3,5 #fixed
        while(len(nums)<n):
           
            x=min(n2,n3,n5)
            if x==n2:p2+=1
            if x==n3:p3+=1
            if x==n5:p5+=1
            nums.append(x) #this can optimized to O(1)
            n2=f2*nums[p2]
            n3=f3*nums[p3]
            n5=f5*nums[p5]
            # print(nums)
        return nums[-1]



##########################
# Using heap to find correct postions + set
##########################



class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s=set()
        fixed=[2,3,5]
        heap=[1]
        curr=1
        cnt=0
        heapq.heapify(heap)
        
        while(cnt<n):
            # print(heap)
            curr= heapq.heappop(heap)
            cnt+=1
            for f in fixed:
                
                if cnt==n:break
                
                if f*curr not in s:
                   
                    
                    # print(f*curr,cnt,curr)
                    s.add(f*curr)
                    heapq.heappush(heap,f*curr)
        return curr


            
            
     

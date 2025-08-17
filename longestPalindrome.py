# Time Complexity:O(n^2)
# SpaceComplexity:O(1)
# Approach:
# at each every point in string expand in two ways ,one for looking for odd and other for even , while expanding if chars didnot match break
# Use dp for common sub problems but it gonna cost us space




class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        doing by dp if s[i]==s[j]
        check for dp[i+1][j-1]
        """
        n=len(s)
        start=0
        mlength=1
        dp=[[False for ii in range(n+1)] for _ in range(n+1)]
        for  i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                start=i
                mlength=2
        #filling dp matrix based on length
        for length in range(3,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    start=i
                    mlength=length
        return s[start:start+mlength]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        check for odd and even 
        n^2 +n^2 = 2*n^2

        """
        def expand(l,r,s):
            while(l>=0 and r<len(s)):
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break
            return l+1,r-1
        
        #odd
        
        start, end = 0, 0
        for i in range(len(s)):

            #odd
            l1,r1=expand(i,i,s)
            #even
            l2,r2=expand(i,i+1,s)
            if r1-l1>end-start:
                start,end=l1,r1
            if r2-l2>end-start:
                start,end=l2,r2
        return s[start:end+1]
                


class Solution:
    def missingNum(self, arr):
        n=len(arr)+1
        total=0
        
        for i in range(1,n+1):
            total=total+i
        
        sum=0
        
        for i in arr:
            sum=sum+i
            
        return total-sum
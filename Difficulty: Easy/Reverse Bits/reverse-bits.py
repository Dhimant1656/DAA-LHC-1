class Solution:
    def reverseBits(self,n):
        
        result = 0
    
        while n>0:
            bit=n&1
            result=(result<<1)|bit
            n=n>>1
        
        return result
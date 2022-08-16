#User function Template for python3
from statistics import median
class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            final=array1+array2
            final.sort()
            res=(median(final))
            if(str(res)[-1])=='0':
                return(int(res))
            else:
                return(res)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

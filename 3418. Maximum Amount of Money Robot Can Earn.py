class Solution:
    def maximumAmount(self, cost: List[List[int]]) -> int:
        m=len(cost)
        n=len(cost[0])
        #Initializing DP array
        dp=[]
        for i in range(m):
            l=[]
            for j in range(n):
                y=[0]*3
                l.append(y)
            dp.append(l)
        
        #Constructing the DP array
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if k==0:
                        if i-1<0 and j-1<0:# Top-left corner of the grid
                            dp[i][j][k]=cost[i][j]
                        elif i-1<0: # First row (no cell above)
                            dp[i][j][k]=dp[i][j-1][k]+cost[i][j]
                        elif j-1<0: # First column (no cell to the left)
                            dp[i][j][k]=dp[i-1][j][k]+cost[i][j]
                        else:  # General case
                            dp[i][j][k]=max(dp[i][j-1][k]+cost[i][j],dp[i-1][j][k]+cost[i][j])
                    else:
                        if i-1<0 and j-1<0:# Top-left corner of the grid
                            dp[i][j][k]=max(cost[i][j],0)
                        elif i-1<0: # First row (no cell above)
                            dp[i][j][k]=max(dp[i][j-1][k]+cost[i][j],dp[i][j-1][k-1])
                        elif j-1<0: # First column (no cell to the left)
                            dp[i][j][k]=max(dp[i-1][j][k]+cost[i][j],dp[i-1][j][k-1])
                        else:  # General case
                            dp[i][j][k]=max(dp[i][j-1][k]+cost[i][j],dp[i-1][j][k]+cost[i][j],dp[i][j-1][k-1],dp[i-1][j][k-1])

                        
        return max(dp[m-1][n-1][0],dp[m-1][n-1][1],dp[m-1][n-1][2])

def edit(ip1, ip2, i, j,dp): 
    if i < 0:
        return j
    if j < 0:
        return i
    if dp[i][j] != None:
        #print(dp[i][j])
        return dp[i][j]
    #print(i,j)
    if ip1[i] == ip2[j]:
        dp[i][j] = edit(ip1, ip2, i-1, j-1,dp)
        #dp[i][j] = dp[i-1][j-1]
        return dp[i][j]
    #print(dp)
    #print(i,j)
    dp[i][j] =  min(edit(ip1, ip2, i, j-1,dp), min(edit(ip1, ip2, i-1, j,dp), edit(ip1, ip2, i-1, j-1,dp))) + 1
    #print(dp)
    #print(i,j)
    #print("=================")
    return dp[i][j]

ip1 = input()
ip2 = input()
#ip1 = "horse"
#ip2 = "ros"
#print(ip1,ip2) 
i = len(ip1) - 1
j = len(ip2) - 1
l = max(i,j) + 2
dp = []
for k in range(l):
    dp.append([None]*l)
#print(dp)
op = edit(ip1,ip2,i,j,dp)

print(op+1)
dp[3][1] = 2
#print(dp[3][0])
#print(dp)

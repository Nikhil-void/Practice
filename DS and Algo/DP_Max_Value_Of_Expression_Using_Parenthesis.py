
#expression = "5-8+7*4-8+9"
expression = input()

sign = []
num = []
for ind, i in enumerate(expression):
    if ind%2 == 0:
        num.append(int(i))
    else:
        sign.append(i)
#print(sign)
#print(num)
mat = []
n = len(num)
for i in range(n):
    mat.append([None]*n)

final = []
n = len(num)
for i in range(n):
    final.append([None]*n)

for gap in range(n):
    for i, j in zip(range(n), range(gap, n)):
        #print(i,j,gap)
        #continue
        if i>j:
            continue
        elif i==j:
            #print(num[i])
            mat[i][j] = (num[i], num[i])
        else:
            maxi = -1001
            mini = 1000000
            for cut in range(i,j):
                left_max = mat[i][cut][0]
                right_max = mat[cut+1][j][0]
                left_min = mat[i][cut][1]
                right_min = mat[cut+1][j][1]
                exp1 = str(left_max) + sign[cut] + str(right_max)
                exp2 = str(left_min) + sign[cut] + str(right_min)
                exp3 = str(left_max) + sign[cut] + str(right_min)
                exp4 = str(left_min) + sign[cut] + str(right_max)
                a1 = eval(exp1)
                a2 = eval(exp2)
                a3 = eval(exp3)
                a4 = eval(exp4)
                new_max = max(a1,a2,a3,a4)
                new_min = min(a1,a2,a3,a4)
                maxi = max(maxi, new_max)
                mini = min(mini, new_min)
            mat[i][j] = (maxi,mini)
            

print(mat[0][n-1][0])


#for i in (mat):
#    print(i)

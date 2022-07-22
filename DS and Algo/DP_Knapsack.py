


def create_matrix(arr, total):
    mat = []
    for i in range(len(arr)):
        mat.append([0]*(total+1))
    for i in range(len(arr)):
        for j in range(1, total+1):
            if arr[i] > j:
                if i == 0:
                    if arr[i] > j:
                        mat[i][j] = 0
                    else:
                        mat[i][j] = arr[i]
                else:
                    mat[i][j] = mat[i-1][j]
            else:
                #print(i, j , arr[i],  mat[i-1][arr[i]-j])
                
                mat[i][j] = max((arr[i] + mat[i-1][abs(arr[i]-j)]),  mat[i-1][j])
            #print(mat[i][j])
    return mat








total, n = input().split(' ')
total, n = int(total), int(n)
arr = input().split(' ')
arr = [int(i) for i in arr]
arr.sort()

if total == 0:
    print(0)
else:
    matrix = create_matrix(arr, total)

#for i in matrix:
#    print(i)

print(matrix[-1][-1])
#print(arr)


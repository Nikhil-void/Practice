def getlist(x):
    final_parent = [-1]*(x + 1)
    #for i in x:
    #    print(i)
    final_min_ops = [-1]*(x+1)
    final_min_ops[0] = 0 
    for i in range(1, x+1):
        new_parent = i-1
        min_ops = final_min_ops[new_parent] + 1
        if (i%3)==0:
            og_parent=i//3
            ops = final_min_ops[og_parent] + 1
            
            if ops<min_ops:
                new_parent, min_ops = og_parent, ops

        if (i%2) == 0:
            og_parent = i//2
            ops = final_min_ops[og_parent]+1
            if ops<min_ops:
                new_parent, min_ops = og_parent, ops

        final_parent[i], final_min_ops[i] = new_parent, min_ops

    return final_parent


x = int(input())
result = getlist(x)
op = []
while x > 0:
    op.append(x)
    x = result[x]
op.sort()

print(len(op) - 1)
for i in op:
    print(i,end=' ')

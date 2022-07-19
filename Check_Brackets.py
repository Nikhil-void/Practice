x = input()

dict1 = {"pppp":0, "qqqq":0, "jjjj":0}

map_dict = {"{":"pppp", "}":"pppp", "[":"qqqq", "]":"qqqq", "(":"jjjj", ")":"jjjj"}
open_val = {"pppp":"{", "qqqq":"[", "jjjj":"("}

"""
for index, i in enumerate(x):
    if i in map_dict:
        if i in ["{", "[", "("]:
            val = map_dict.get(i)
            dict1[val] += 1
        else:
            #print(dict1)
            val = map_dict.get(i)
            dict1[val] -= 1
            #print(dict1)
            if dict1[val] < 0:
                print(index+1)
                break
else:
    print(dict1)
    for key, val in dict1.items():
        if val > 0:
            open_key = open_val.get(key)
            print(x.rfind(open_key)+1)
            break
    else:
        print("Success")
"""


stack = []
pair = {"}":"{", "]":"[", ")":"("}
for index, i in enumerate(x):
    if i in map_dict:
        if i in ["{", "[", "("]:
            stack.append((i,index))
        else:
            if len(stack) < 1:
                print(index+1)
                break
            elif stack[-1][0] != pair.get(i):
                print(index+1)
                break
            else:
                stack.pop(-1)
else:
    if len(stack) > 0:
        print(stack[0][1]+1) 
    else:
        print("Success")

from itertools import permutations

div = [2,3,5,7,11,13,17]
def pans(n):
    counting = 0
    l = []
    for x in range(n+1):
        l.append(str(x))

    perm = permutations(l)

    for x in perm:
        if is_pan(x):
            # print(x)
            counting += int(''.join(x))

    return counting




def is_pan(lis):
    for i in range(2,len(lis)-1):
        x = int(''.join(lis[i-1:i+2]))
        if x % div[i-2] != 0:
            return False
    return True


p = int(input())
print(pans(p))
# count = 0
# list_pans = pans(p)
# # print(list_pans)
# for x in list_pans:
#     if is_pan(x):
#         # print(x)
#         count += int(''.join(x))
# print(count)















# def is_pan(value):
#     print(value)
#     str_val = str(value)
#     if len(str_val)<3:
#         return False
#     if len(str_val) == 3:
#         return value%2==0
#     for i in range(2,len(str_val)-1):
#         x = int(str_val[i-1:i+2])
#                 # (100*(int(str_val[i-1]))) + (10*(int(str_val[i]))) + (int(str_val[i+1]))
#         if x % div[i-2] != 0:
#             return False
#     return True
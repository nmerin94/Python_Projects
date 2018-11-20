# Write your code here
import math
T = int(input())
i = 0
op = []
while(i<T):
    j = 0
    ip_lst = input().split()
    #print(ip_lst)
    a = float(ip_lst[0])
    b = float(ip_lst[1])
    c = float(ip_lst[2])
    k = float(ip_lst[3])
    lim = int(math.sqrt(k))
    #print(lim)
    while(j<=lim) :
        y = a*j*j + b*j + c
        if( y >= k):
            op.append(j)
            break
        j = j + 1
    i = i + 1
for i in op :
    print(i)

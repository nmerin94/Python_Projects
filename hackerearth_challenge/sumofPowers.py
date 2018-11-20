'''


SAMPLE INPUT

3
4 4
5 3
6 1

SAMPLE OUTPUT

1
3
6

Explanation

Case 1. 4 can be expressed as 4^1. Case 2. 5 can be expressed as sum of 3^0 + 3^0 + 3^1. Case 3. 6 can be expressed as sum of 11 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1.


'''
def fun(a, b):
    if(int(a/b) == 0):
        return 0
    if(b == 1):
        a = a - 1
    elif(a%b == 0):
        a = int(a/b)
    else:
        a = a - 1
    return (1 + fun(a,b))


iterations = int(input())
#print(iterations)
while(iterations>0):
    li = input().split()
    a = int(li[0])
    b = int(li[1])
    op = fun(a, b)
    print(op)
    iterations = iterations - 1

# Write your code here
import math
import sys


def reverse(num, rev):
    if (num%10 == 0):
        return rev
    else :
        return reverse(int(num/10), rev*10 + num%10)



def odd_r(a,b) :
    no = 0
    tmp = a
    while (tmp <= b) :
        rev = reverse(tmp,0)
        if(rev==tmp):
            no = no + 1
            print(tmp)
        tmp = tmp + 1
    return no


print("Give the test cases number :")
count = int(sys.stdin.readline())
i=1
print("Give test cases (each case numbers seperate by spaces):")
while(i<=count) :
    print("Lower Upper")
    no = 0
    loo = 0
    ip = sys.stdin.readline().split()
    a = int(ip[0])
    b = int(ip[1])
    print("Palindromes are :")
    no = odd_r(a,b)
    print("Number of palindromes : ",no)
    i = i + 1

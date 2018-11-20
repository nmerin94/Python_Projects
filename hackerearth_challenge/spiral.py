'''


PROBLEM STATEMENT
Points: 30

Limelight is a technique that is used when all four users take
place in the cardinal directions. They will then join their
strength in the form of four connecting streams above the target
area. It will then create a massive ball of lightning powerful
enough to incinerate everything within the area of the four users.

The Leaf village is build in the shape of Spiral of integers. Spiral of integers, of an integer N, is an interesting spiral matrix which starts with 1 at the center. For example, for

, the spiral of integers is

16  15  14  13

5   4   3   12

6   1   2   11

7   8   9   10

Kitane, Nauma, Tōu and Seito are planning to destroy the whole Leaf village. The limelight spot will be the 4 corners of the village. Strength of the attack is equal to the sum of all the elements in the connecting streams as shown in the figure ( sum of diagonal elements of the spiral of integers of N ) .

Given the value of N, you need to compute the strength of the attack (mod

).

Input:

First line contains an integer T, denoting the number of testcases.
Each test case consists of a single integer N.

Output:

For each test case output a single integer denoting the strength of the attack (mod

).

Constraints:

SAMPLE INPUT

2
4
10000000

SAMPLE OUTPUT

56
679604006





'''




import time

n = int(input())

while (n > 0):
    sum = 0
    num = int(input())
    sq = num ** 2
    count = num-1
    while(sq > 0):
        x = 4
        while(x>0 and sq>0):
            sum = sum + sq
            sq = sq - count
            #time.sleep(2)
            #print(sq)
            x = x - 1
        count = count - 2
    print(sum)
    n = n - 1

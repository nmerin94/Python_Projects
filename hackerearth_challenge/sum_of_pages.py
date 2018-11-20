'''
He had two types of notebooks, when he was a kid.

problems could be solved in one page, in the first notebook.

    problems could be solved in one page, in the second notebook.

Little Jhool remembered how in order to maintain symmetry, if he was given with n problems in total to solve, he tore out pages from both notebooks, so no space was wasted. EVER!

But, now he's unable to solve his own problem because of his depression, and for the exercise of the week, he has to answer the queries asked by his psychologist.

Given n number of questions, print the minimum number of pages he needs to tear out from the combination of both the notebooks, so that no space is wasted.

Input Format:
The first line will contain t - number of test cases.

The second will contain an integer n - number of questions.

Output Format:
Corresponding to the input, print the minimum number of pages Little Jhool needs to tear out from the combination of both the notebooks. If it is NOT possible, print "1".

Constraints:

SAMPLE INPUT

2
23
32

SAMPLE OUTPUT

-1
3

Explanation

For
: 2 pages from the notebook, where can be solved; 1 page from the notebook, where can be solved.
'''
n = int(input())

while(n):

    num = int(input())
    c_num = 0;
    flag = 0
    c10 = 0
    c12 = 0
    lc12 = 0
    while(c_num <= num):
        c12 = c12 + 1
        c_num = c_num + 12
        if((num - c_num)%10 == 0 ):
            flag = flag + 1
            lc12= c12
            c10 = (num - c_num)/10
    if(flag == 0):
        print("-1")
    else:
        print(int(c10 + lc12))



    n = n - 1

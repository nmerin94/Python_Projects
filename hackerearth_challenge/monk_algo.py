'''

PROBLEM STATEMENT
Points: 50

Note: You can skip to BRIEF if you do not want to read the complete story.

Khaolin Temple is world's most famous algorithmic pilgrimage situated on Mount Kong in China. It is believed that human civilization has never seen better coders than Khaolin Coders and its well known about them that that they were so good at problem solving that they could even solve "NP-Complete" problems in constant amortized time. There are many folktales about Khaolin Coders, the most famous ones being about Monk Bosky who was incomparably the best Khaolin Coder. Following is a famous incident from Monk Bosky's early days at Khaolin Temple.

"During his early days at Khaolin Temple Bosky was the brightest and most notorious pupil at Khaolin. Once his master asked all his pupils to water the khaolin flowers[khaolin flowers are special flower which grow 1 meter tall on pouring 1 litre water to them]. Master wanted to keep everyone busy [specially Bosky] so that he could meditate in silence. He told his pupils where the flowers were and how tall they were at present and asked them to come back only when they are finished watering all the flowers assigned to them. He also told them that only those pupils will be allowed to enter the temple who will tell the correct heights of flowers after the watering process is complete.

Master knew that his pupils will cheat and calculate the height that will be achieved by flowers after pouring water to them if he asks them to water them one by one, hence he decided to make it difficult for them to calculate the height by asking them to follow certain rules while watering flowers.

He asked them to follow the following rules while watering flowers:

Rule 1: Every pupil will water all flowers assigned to him as an array of n khaolin flowers with heights [H1 H2 ... Hn].
Rule 2: When a pupil will be standing next to Kth flower he will have to go back to (K-1)th flower and inspect its height,if it is greater or equal to height of Kth flower he will have to note its index down,then he will have to go further back to (K-2)th flower and if its height is greater or equal to Kth flower he will again have to note down its index. And he must continue to do so till he reaches flower 1. After reaching flower 1 he has a list of indices of flowers with height>= Hk [i.e. height of Kth flower].Now he will have to bring sufficient water from river nearby and pour 1 litre water to each flower whose index he has noted down [NOTE: By pouring 1 litre water to the flowers he will be making them 1 meter taller].
Rule 3: Pupil can move to Kth flower only if he has applied Rule 2 standing next to (K-1)th flower. If (K+1)th flower exists he must continue to apply Rule 2 to (K+1)th flower after he has applied Rule 2 standing next to Kth flower.
Rule 4: Pupil must start watering process standing next to 1st flower

Master knew that if his pupils sincerely followed these rules while watering flowers they won't be able to water all flowers before a month's time span and in the meantime he could meditate in silence without being disturbed by anyone. Since this task was very boring, Master decided to reward the pupil who enters back into temple first,obviously by telling heights of all flowers correctly after the process of watering the plants was complete. As a reward Master will teach him secret algorithmic skills till the next pupil enters the temple and as soon as the next pupil enters the temple Master will stop teaching the first pupil. With that said,Master sent all his pupils to water Khaolin flowers and expected that no pupil will return before a month and also expected that he will have to teach secret algorithms as a reward only for few hours because if they follow same process they will complete the task in nearly equal time.

But to Master's utter surprise he heard a pupil on the gate of Khaolin Temple claiming that he has watered all the flowers in an hour and that pupil was Bosky who further astonished Master by reporting the correct heights of the flowers as expected by Master. Master refused to reward him as Bosky clearly cheated and did not follow his rules. But after Bosky explained Master the process he followed to water flowers which produced same height of flowers as Master expected,Master was so impressed that he taught him everything he knew for the next month and also declared him to be heir to his position in the Khaolin."

No one in today's world knows the algorithm Great Monk Bosky used to solve the problem given by his master but today we have at least been able to reconstruct such cases and time limits which can only be passed by using algorithm which is equivalent to Monk Bosky's algorithm or more efficient than it. You are thereby challenged to match Monk Bosky's efficiency and mightiness by telling the heights of flowers after watering them as stated in the question.

BRIEF
- An array A of N integers is given [a1, a2 … aN].
- Step 1: For every A[i] (1 <= i <= N), create an array B of size m which contains integers [b1, b2 … bm] where B[j] < i (for all 1 <= j <= m) and each A[B[j]] >= A[i].
- Step 2: Increment B[j]th element in A with 1 (i.e. do A[B[j]] = A[B[j]] + 1, where 1 <= j <= m).
- Step 3: If i < N, do i = i+1 and goto Step 1, otherwise print array A.

Your task is to print the transformed array A.

Input:
First line will contain an integer N, where N represents the number of flowers (integers). Next line will contain N space-separated integers H1 H2 ... HN representing heights of flowers in sequential order.

Output
Print N space separated integers that represent heights of flowers after all flowers have been watered.

Constrains
1 <= N <= 105
1 <= Hi <= 109
SAMPLE INPUT

5
7 5 2 1 8

SAMPLE OUTPUT

11 7 3 1 8

Explanation

7 5 2 1 8 (begin) -> 8 5 2 1 8 (A[1] >= A[2]) -> 9 6 2 1 8 (A[1], A[2] >= A[3]) -> 10 7 3 1 8 (A[1], A[2], A[3] >= A[4]) -> 11 7 3 1 8 (A[1] >= A[5])

'''
A = []
add = []

def merge(start, mid, end):
    if(start == mid):
        if(X[start]>X[end]):
            X[start]= X[start+1]
            add[start] = add[start] + 1
            tmp = X[start]
            X[start] = X[end]
            X[end] = tmp
            return
    i = start
    j = mid+1
    k = 0
    C = []

    while(i<=mid and j <= end):

        if(X[i]<=X[j]):
            C.append(X[i])
            k = k+1
            i = i+1
        else:
            X[i] = X[i] + 1

            C.append(X[j])
            add[i] = add[i] + 1
            j = j+1
            k = k+1
    while(i<=mid):
        X[i] = X[i] + 1
        C.append(X[i])
        add[i] = add[i] + 1
        k = k+1
        i = i+1
    while(j<=end):
        C.append(X[j])
        j = j+1
        k = k+1
    k = 0
    for i in range(start,end+1):
        X[i] = C[k]
        k = k + 1



def merge_sort(start, end) :
    mid = int((start + end)/2)
    if(start == end) :
         return
    merge_sort(start, mid)

    merge_sort(mid+1 , end)
    merge(start, mid, end)



# Write your code here
n = int(input())
str_list = input().split()

for i in str_list:
    A.append(int(i))
    add.append(0)
X = []
for i in range(0,n):
    X.append(A[i])
merge_sort(0, n-1)

for i in range(0,n):
    A[i] = A[i] + add[i]


'''B = [[]]
for i in range(0,n) :
    B.append([])
    for j in range(0,i):
        if ( j < i and A[j] >= A[i]) :
            B[i].append(j)
'''
print(add)
print(X)
for i in A :
    print(i , end = " ")

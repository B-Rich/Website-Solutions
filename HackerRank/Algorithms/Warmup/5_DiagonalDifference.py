'''

Hackerank Domains: https://www.hackerrank.com/domains

Algorithms https://www.hackerrank.com/domains/algorithms

Warmup: https://www.hackerrank.com/domains/algorithms/warmup/

Hackerrank - Algorithms - Diagonal Difference

Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, . The next  lines denote the matrix's rows, with each line containing  space-separated integers describing the columns.

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:
11
      5
            -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
            4
      5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

contact: bryce@brycefury.com

'''

#!/bin/python3

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)


def first_diagonal(a):
    return sum(a[i][i] for i in range(0, len(a)))

def second_diagonal(a):
    a.reverse()
    return sum(a[i][(i)] for i in range(0, len(a)))



print (abs(first_diagonal(a) - second_diagonal(a)))

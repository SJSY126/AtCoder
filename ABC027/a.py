"""
Input	script	結果
abcde	s = input()	s = 'abcde'
abcde	s = list(input())	s = ['a', 'b', 'c', 'd', 'e']
5(1つだけ)	a = int(input())	a = 5
1 2	x, y = map(int, input().split())	x = 1, y = 2
1 2 3 4 5 ... n 　	li = input().split()	li = ['1', '2', '3', ..., 'n']
1 2 3 4 5 ... n 　	li = list(map(int, input().split()))	li = [1, 2, 3, 4, 5, ..., n]
FFFTFTTFF 　	li = input().split('T')	li = ['FFF', 'F', '', 'FF']
"""
l1, l2, l3 = map(int, input().split())
if l1 == l2:
    print(l3)
elif l1 == l3:
    print(l2)
else:
    print(l1)

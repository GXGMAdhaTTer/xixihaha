# -*- coding: utf-8 -*-
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s,str)]
# # 期待输出: ['hello', 'world', 'apple']
# print(L2)
# g = (x * x for x in range(10))
# for n in g:
#     print(n)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n<max:
#         print(b)
#         a, b = b, a+b
#         n = n + 1
#     return 'done'

# fib(6)

def triangles():
    s = [1]
    while True:
        yield s
        s = [1]+[s[i-1] + s[i] for i in range(len(s)) if i >0]+[1]
n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
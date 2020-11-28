# def GuGu(n):
#     result = []
#     i=1
#     while i < 10:
#         result.append(n * i)
#         i += 1
#     return result

# print(GuGu(2))

# A = 0

# for n in range(1, 1000):
#     if n % 3 == 0 or n % 5 == 0:
#         A += n

# print(A)

# def getTotalPage(m, n):
#     if m % n == 0:
#         return m // n
#     else:
#         return m // n + 1

# print(getTotalPage(5, 10))
# print(getTotalPage(15, 10))
# print(getTotalPage(25, 10))
# print(getTotalPage(30, 10))

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
    
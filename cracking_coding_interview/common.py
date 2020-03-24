# Question: Given two sorted arrays, find the number of elements in common. The arrays are the same length an each has all distinct elements
#
# A: 13 27 25 40 49 55 59
# B: 17 35 39 40 55 58 60
from typing import List, Any


def get_common_elements(A: list, B: list) -> list:
    common: List[Any] = []
    index = 0
    for num1 in B:
        for i in range(index, len(A)):
            if num1 == A[i]:
                common.append(num1)

            if num1 < A[i]:
                index = i
                break
    return common


A = [13, 25, 27, 40, 49, 55, 59]
B = [17, 35, 39, 40, 55, 58, 60]

print(get_common_elements(A, B))
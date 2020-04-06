"""
1.1 Is Unique

Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Example:
    Input  : str = "aaabbccdaa"
    Output : No

    Input  : str = "abcd"
    Output : Yes

"""
import time


# This approach has Time Complexity of O(n^2)
def is_unique(input: str) -> bool:
    length = len(input)
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if input[i] == input[j]:
                return False

    return True


# This ORs checker with a value that has a 1 bit set only at position val, which turns the bit
# on. It's equivalent to setting the valth bit of the number to 1.
#
# This approach is much faster than yours. First, since the function starts off by checking
# the string has length greater than 26 (I'm assuming the 256 is a typo), the function never
# has to test any string of length 27 or greater. Therefore, the inner loop runs at most 26
# times. Each iteration does O(1) work in bitwise operations, so the overall work done is O(1)
# (O(1) iterations times O(1) work per iteration), which is significantly faster than your
# implementation.
# This approach has Time Complexity of O(n)
def is_unique_using_operator(s: str) -> bool:
    length = len(s)
    if length > 26:
        return False
    checker = 0
    for i in range(length):
        val = ord(s[i]) - ord('a')
        if checker & (1 << val):
            return False
        # bitwise OR operator with assignment
        checker |= (1 << val)

    return True


# This approach has Time Complexity of O(n)
def is_unique_using_datastructure(s: str) -> bool:
    length = len(s)
    if length > 256:
        return False
    checker = [0] * 256
    for i in range(length):
        val = ord(s[i]) - ord('a')
        if checker[val] != 0:
            return False

    return True

# This approach has Time Complexity of O(n)
def is_unique_using_sorting(s: str) -> bool:
    # Sorting takes O(log n)
    res = ''.join(sorted(s))
    for i in range(0, len(res) - 1):
        if res[i] == res[i + 1]:
            return False
    return True


print("First Input")
Input = "aaabbccdaa"
start = time.time()
print(is_unique(Input))
print(is_unique_using_operator(Input))
print(is_unique_using_operator(Input))
print(is_unique_using_sorting(Input))

print("Second Input")
Input = "abcd"
print(is_unique(Input))
print(is_unique_using_operator(Input))
print(is_unique_using_operator(Input))
print(is_unique_using_sorting(Input))

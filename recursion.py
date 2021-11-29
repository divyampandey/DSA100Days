### Recursion ######


"""
If we want to solve any problem using recursion we need to keep three things in mind
1. problem can be divided into smaller problems of same kind
2. problem has some base case
3. base case is reached before the stack size limit exceeds.

"""

"""
sample recursion program in python
"""


def recursive_hello():
    print("Hello Dear... !!!")

    a = input("enter 1 for recursion and any key to stop\n")
    if a=='1':
        recursive_hello()


recursive_hello()
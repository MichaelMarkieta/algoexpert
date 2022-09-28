# Solution 1
# def getNthFib(n):
    
#     prev = 0
#     next = 1
#     fibs = []
#     fibs.append(prev)
#     fibs.append(next)
    
#     for f in range(2, n):
#         temp = prev
#         prev = next
#         next = temp + next
#         fibs.append(next)

#     return fibs[n-1]

# Solution 2
def getNthFib(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
    return memoize[n]

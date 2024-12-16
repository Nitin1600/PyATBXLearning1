# deque - double-ended queue
# FIFO - bus stand queue, airport queue
# A list-like sequence optimized for data accesses near its endpoints.

from collections import deque

#creating a deque
d = deque()
print(d)
d = deque([1,2,3])
print(d)

d.append(4)
print(d)

d.appendleft(0)
print(d)

d.extend([5,6])
print(d)

print(d.pop())
print(d)
print(d.popleft())
print(d)

d.reverse()
print(d)


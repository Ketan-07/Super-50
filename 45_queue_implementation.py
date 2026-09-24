# Queue Implementation
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

print("Removed:", queue.popleft())
print(queue)
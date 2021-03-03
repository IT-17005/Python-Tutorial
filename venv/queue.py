from collections import deque
name = deque(["x","y","z"])
print(name)
name.popleft()
print(name)
name.popleft()
print(name)
name.popleft()
if not name:
    print("No person left")
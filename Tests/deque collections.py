from collections import deque

d = deque('hello', maxlen=5)

d.append('4')
d.append(4)
d.appendleft(2)
d.pop()
d.popleft()
d.clear()

d.extend(iter([1,2,3]))
print(d)
d.extendleft('hey')
print(d)
d.rotate(2) #useful
print(d)

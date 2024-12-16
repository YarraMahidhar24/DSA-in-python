# Stack implementation by using list
s=[]
s.append("hi")
s.append(1)
s.append("welcome")
print(s)
print(s.pop())
print(s)
# ..............................................
# Stack implementation by using collections.deque
from collections import deque
stack=deque()
stack.append("hello")
stack.append(1)
stack.append("welcome")
print(stack)
print(stack.pop())
print(stack)
# ..............................................
# Stack implementation by using queue.LifoQueue
from queue import LifoQueue
st=LifoQueue(maxsize=3)
print(st.empty())
st.put("hi")
st.put("mahi")
print(st.qsize())
st.put("LU")
print(st.queue)
print(st.full())
st.get()
print(st.queue)
print(st.full())
# ..............................................

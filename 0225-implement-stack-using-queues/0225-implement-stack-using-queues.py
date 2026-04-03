class MyStack:

    from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)            # Step 1: add new element
       # Step 2: move all old elements
        while self.q1:                
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1  # Step 3: swap

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
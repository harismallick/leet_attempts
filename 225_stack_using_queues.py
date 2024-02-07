## 225. Implement Stack using Queues
'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
'''
# Difficulty: Easy

class MyStack:

    def __init__(self, stack:list = []):
        self.stack = stack

    # def __repr__(self):
    #     for item in self.stack:
    #         print(item)
    #     return ""

    def push(self, x: int) -> None:
        self.stack.append(x)
        return

    def pop(self) -> int:
        if not self.stack:
            return None
        self.stack.reverse()
        item = self.stack.pop(0)
        self.stack.reverse()
        return item

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]
    
    def size(self) -> int:
        count = 0
        for item in self.stack:
            count += 1
        return count

    def empty(self) -> bool:
        if self.size() == 0:
            return True
        return False

# leetcode doesn't accept solution unless using dequeue()
# waste of time
    
if __name__ == '__main__':
    stack = MyStack()
    # ["MyStack", "push", "push", "top", "pop", "empty"]
    stack.push(1)
    stack.push(2)
    print(stack)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())



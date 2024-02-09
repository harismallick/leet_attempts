## 232. Implement Queue using Stacks
'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
'''
# Difficulty: Easy

class MyQueue:

    def __init__(self):
        from collections import deque
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        return

    def pop(self) -> int:
        self.stack.reverse()
        output = self.stack.pop()
        self.stack.reverse()
        return output

    def peek(self) -> int:
        self.stack.reverse()
        output = self.stack[-1]
        self.stack.reverse()
        return output

    def empty(self) -> bool:
        return len(self.stack) == 0

if __name__ == '__main__':
    stack = MyQueue()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    print(stack.pop())
    print(stack.empty())

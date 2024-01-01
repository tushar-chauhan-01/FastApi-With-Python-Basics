"""
Problem : N number of soldiers are trapped inside a cave and they decide to kill each other rather than surrendering.
They all stood in a circle facing each other and every person have to kill the k'th person to his left and the very last
person have to kill himself.
Josephus didnt wanna die so he need to figure out a position fast at which he can stand and survive till last. 
"""
"""
Deque:
A deque (pronounced "deck") in Python stands for a double-ended queue. It is a data structure that allows elements
to be added or removed from both ends with O(1) time complexity. A deque can be thought of as a hybrid between 
a stack and a queue.
"""
"""
Stack:
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
In simpler terms, the last element added to the stack is the first one to be removed. 
Think of it like a stack of plates where you can only add or remove plates from the top. 
Key operations associated with a stack are:

Push: Adding an element to the top of the stack.
Pop: Removing the element from the top of the stack.
Peek or Top: Examining the element at the top of the stack without removing it.
isEmpty: Checking if the stack is empty.
Stacks are used in various algorithms and applications, such as managing function calls in a program (call stack), 
parsing expressions, undo mechanisms in software, and more.

Queue:
A queue is another linear data structure, but it follows the First In, First Out (FIFO) principle. 
In a queue, the first element added is the first one to be removed. 
Think of it like a line of people waiting for a bus; the person who arrived first gets on the bus first. 
Key operations associated with a queue are:

Enqueue or Push: Adding an element to the rear or end of the queue.
Dequeue or Pop: Removing the element from the front or beginning of the queue.
Front: Examining the element at the front of the queue without removing it.
isEmpty: Checking if the queue is empty.
Queues are used in scenarios where tasks are processed in the order they arrive, such as task scheduling, 
managing resources like printers, breadth-first search algorithms, etc.

In summary:
Last In, First Out (LIFO) for stacks, and First In, First Out (FIFO) for queues.
"""
from collections import deque

def josephus(array,k):
    
    deque_array = deque(array)
    dead=[]
    while deque_array:
        deque_array.rotate(1-k)
        item = deque_array.popleft()
        dead.append(item)

    print( f"Survivor should stand at {dead[-1]} and dead people are at {dead[:-1]}" )
    
if __name__ == "__main__":
    
    import time
    soldiers = 41
    arr = [ s+1 for s in range(soldiers) ]
    k = 3
    start = time.perf_counter()
    josephus(arr,k)
    stop = time.perf_counter()
    
    print(stop-start)
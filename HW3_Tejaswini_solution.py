
############################################################
# Write code in file solution.py 
# Post� solution.py in Canvas along with 4 screen shots that shows Leetcode has passed. We will not use screen shot to give 100
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run solution.py file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    # NOTHING CAN BE CHANGED HERE
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

############################################################
#  class  Slist
###########################################################
class Slist():
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0

    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def append(self, x: 'int'):
        self._len += 1
        self._build_a_node(x, True)

    def prepend(self, x: 'int'):
        self._len += 1
        self._build_a_node(x, False)

    def _build_a_node(self, x, is_append):
        new_node = ListNode(x)
        if not self._first:
            self._first = new_node
            self._last = new_node
        else:
            if is_append:
                self._last.next = new_node
                self._last = new_node
            else:
                new_node.next = self._first
                self._first = new_node

    def is_empty(self):
        return self._len == 0

    def size(self):
        return self._len

    def pop_first(self):
        if self._first:
            node = self._first
            self._first = self._first.next
            self._len -= 1
            if self._len == 0:
                self._last = None
            return node.val
        return None

    def pop_last(self):
        if self._last:
            if self._len == 1:
                return self.pop_first()
            current = self._first
            while current.next != self._last:
                current = current.next
            value = self._last.val
            self._last = current
            self._last.next = None
            self._len -= 1
            return value
        return None

############################################################
#  class  MyStack
# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        return self._s.pop_last()

    def top(self) -> int:
        if not self._s.is_empty():
            return self._s._last.val
        return None

    def empty(self) -> bool:
        return self._s.is_empty()

############################################################
#  class  MyQueue
# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        return self._s.pop_first()

    def peek(self) -> int:
        if not self._s.is_empty():
            return self._s._first.val
        return None

    def empty(self) -> bool:
        return self._s.is_empty()

############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 
class MyCircularQueue:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()

    def enQueue(self, value: int) -> bool:
        if self._s.size() < self._K:
            self._s.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if not self._s.is_empty():
            self._s.pop_first()
            return True
        return False

    def Front(self) -> int:
        return self._s._first.val if not self._s.is_empty() else -1

    def Rear(self) -> int:
        return self._s._last.val if not self._s.is_empty() else -1

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s.size() == self._K

 #############################################################
#  MyCircularDeque
# 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque
###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()

    def insertFront(self, value: int) -> bool:
        if self._s.size() < self._K:
            self._s.prepend(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self._s.size() < self._K:
            self._s.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if not self._s.is_empty():
            self._s.pop_first()
            return True
        return False

    def deleteLast(self) -> bool:
        if not self._s.is_empty():
            self._s.pop_last()
            return True
        return False

    def getFront(self) -> int:
        return self._s._first.val if not self._s.is_empty() else -1

    def getRear(self) -> int:
        return self._s._last.val if not self._s.is_empty() else -1

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s.size() == self._K

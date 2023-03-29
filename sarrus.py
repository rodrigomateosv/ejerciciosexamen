class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = popped_node.next_node
        popped_node.next_node = None
        self.size -= 1
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size

def sarrus_det(matriz):
    stack = Stack()
    stack.push(matriz)
    det = 0
    
    while not stack.is_empty():
        submatriz = stack.pop()
        if len(submatriz) == 2: # base case
            det += submatriz[0][0] * submatriz[1][1] - submatriz[0][1] * submatriz[1][0]
        else:
            for j in range(len(submatriz)):
                submatriz_elements = [[submatriz[i][k] for k in range(len(submatriz)) if k != j] for i in range(1, len(submatriz))]
                submatriz = Stack()
                submatriz.push(submatriz_elements)
                subdet = sarrus_det(submatriz_elements)
                det += submatriz.peek()[0][j] * subdet * (-1) ** j
    
    return det

from math import *

class Node:
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    def __str__(self):
        return str(self.op) + " " + str(self.left) + " " + str(self.right)    


class Leaf:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return  self.value  

# Hardcode lisp code - code should be in brackets.
# Next step would be to handle outer and inner brackets in simple equations.

code = "- 10 5"

splitted_code = code.split()
head, *tail = splitted_code

#Operators: 
op = ["+", "-"]

def parse(splitted_code):
    head, *tail =splitted_code
    if head in op:
        (left, rest) = parse(tail)
        (right, rest2) = parse(rest)
        return (Node(left, right, head),rest2)
      
    else:
        return (Leaf(head),tail)  

print(parse(splitted_code))

(ast, rest) = parse(splitted_code)
print(ast)
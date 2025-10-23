# Stack class implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


# Function to define precedence of operators
def precedence(op):
    if op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0


# Function to convert INFIX → POSTFIX
def infix_to_postfix(expression):
    stack = Stack()
    result = [] 

    for char in expression:
        if char.isalnum():   # operand (single char)
            result.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                result.append(stack.pop())
            stack.pop()  # remove '('
        else:  # operator
            while (not stack.is_empty() and
                   precedence(char) <= precedence(stack.peek())):
                result.append(stack.pop())
            stack.push(char)

    # pop remaining operators
    while not stack.is_empty():
        result.append(stack.pop())

    return "".join(result)


# Function to evaluate POSTFIX expression
def evaluate_postfix(expression):
    stack = Stack()

    for char in expression:
        if char.isdigit():   # operand → push as int
            stack.push(int(char))
        else:  # operator → pop 2 operands
            val2 = stack.pop()
            val1 = stack.pop()
            if char == '+':
                stack.push(val1 + val2)
            elif char == '-':
                stack.push(val1 - val2)
            elif char == '*':
                stack.push(val1 * val2)
            elif char == '/':
                if val2 == 0:
                    raise ValueError("Division by zero")
                stack.push(val1 // val2)  
    return stack.pop()

infix_expr = "3+(2*5)-9"   
postfix_expr = infix_to_postfix(infix_expr)

print("Infix Expression:  ", infix_expr)
print("Postfix Expression:", postfix_expr)
print("Evaluation Result: ", evaluate_postfix(postfix_expr))
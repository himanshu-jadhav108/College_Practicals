#Stack

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
    
def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0

def is_operator(c):
    return c in ('+', '-', '*', '/', '^')

def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""
    for c in expression:
        if c.isalnum():  # operand (single character)
            postfix += c
        elif c == '(':
            stack.push(c)
        elif c == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # remove '('
        elif is_operator(c):
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(c)):
                postfix += stack.pop()
            stack.push(c)
        # Ignore any commas or spaces
        elif c in ', ':
            continue
        else:
            print(f"Invalid character '{c}' in expression")
            return None
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix

def evaluate_postfix(expression):
    stack = Stack()
    
    for c in expression:
        if c.isdigit():
            stack.push(int(c))
        elif is_operator(c):
            b = stack.pop()
            a = stack.pop()
            if a is None or b is None:
                print("Invalid postfix expression!")
                return None
            if c == '+': stack.push(a + b)
            elif c == '-': stack.push(a - b)
            elif c == '*': stack.push(a * b)
            elif c == '/': stack.push(a // b)  
            elif c == '^': stack.push(a ** b)
        else:
            print(f"Invalid character '{c}' in postfix expression")
            return None

    result = stack.pop()
    if not stack.is_empty():
        print("Invalid postfix expression!")
        return None
    return result

if __name__ == "__main__":
    infix_expr = input("Enter infix expression (single char operands) : ")
    postfix_expr = infix_to_postfix(infix_expr)
    if postfix_expr:
        print("Postfix Expression : ",postfix_expr)
        result = evaluate_postfix(postfix_expr)
        if result is not None:
            print("Evaluation Result : ",result)




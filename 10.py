class Stack:
    """Class to represent a stack."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pop an item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.items)


def precedence(op):
    """Return the precedence of the given operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expression):
    """Convert infix expression to postfix expression."""
    output = []
    stack = Stack()

    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':  # Opening parenthesis
            stack.push(char)
        elif char == ')':  # Closing parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from the stack
        else:  # Operator
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(char)):
                output.append(stack.pop())
            stack.push(char)

    # Pop remaining operators in the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)


def evaluate_postfix(postfix):
    """Evaluate the postfix expression."""
    stack = Stack()

    for char in postfix:
        if char.isdigit():  # Operand
            stack.push(int(char))
        else:  # Operator
            right = stack.pop()
            left = stack.pop()
            if char == '+':
                stack.push(left + right)
            elif char == '-':
                stack.push(left - right)
            elif char == '*':
                stack.push(left * right)
            elif char == '/':
                stack.push(left / right)

    return stack.pop()


# Example usage
if __name__ == "__main__":
    infix_expression = "3+(5*2)-8/4"
    
    # Convert infix to postfix
    postfix_expression = infix_to_postfix(infix_expression)
    print(f"Infix Expression: {infix_expression}")
    print(f"Postfix Expression: {postfix_expression}")
    
    # Evaluate the postfix expression
    result = evaluate_postfix(postfix_expression)
    print(f"Evaluation of Postfix Expression: {result}")

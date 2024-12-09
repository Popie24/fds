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


def is_well_parenthesized(expression):
    """Check if the given expression is well parenthesized."""
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matching = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matching[char]:
                return False

    return stack.is_empty()


# Example usage
if __name__ == "__main__":
    expressions = [
        "(a + b) * (c + d)",
        "{[a + b] * (c + d)}",
        "((a + b) * c)",
        "(a + b] * c)",
        "{(a + b) * (c + d)}]",
        "((a + b) * (c + d))"
    ]

    for expr in expressions:
        result = is_well_parenthesized(expr)
        print(f"Expression: {expr} -> Well Parenthesized: {result}")

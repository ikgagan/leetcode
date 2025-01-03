# Question: Valid Parentheses
# Description:
# Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

# A string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Example:
# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false

def isValid(s: str) -> bool:
    # Map to match closing brackets with their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []
    
    # Traverse each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop from stack or use a dummy value if the stack is empty
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the expected opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket; push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched
    return not stack

# Test cases
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False
print(isValid("({[]})"))  # Output: True
print(isValid("("))       # Output: False
print(isValid("]"))       # Output: False

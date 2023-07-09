"""Reverse letters but keep pattern in place"""
def reverse_letters(string: str) -> str:

    """Reverse letters in a string but keep the order of the non-letters the same"""
    stack = []
    result = ""
    for char in string:
        if char.isalpha():
            stack.append(char)

    while stack:
        for char in string:
            if char.isalpha():
                result += stack.pop()
            else:
                result += char
    return result
print(reverse_letters("ab5dEf"))


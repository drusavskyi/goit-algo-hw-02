from collections import deque

def is_palindrome(input_str):
    # Видаляємо пробіли та переводимо до нижнього регістру
    normalized_str = ''.join(input_str.lower().split())
    char_deque = deque(normalized_str)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Введите текст:').lower()
forbidden = (' ', '.', ',', '!', '?')

for symbol in something:
    for char in forbidden:
        if symbol == char:
            something = something.replace(symbol, '')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")

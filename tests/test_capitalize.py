from capitalize import capitalize

# Тесты для функции capitalize
assert capitalize("hello, hexlet!") == "Hello, hexlet!", "Should capitalize first letter"
assert capitalize("") == "", "Should handle empty string"
assert capitalize("a") == "A", "Should capitalize single letter"
assert capitalize("HELLO") == "Hello", "Should lowercase rest of string"

print("Все тесты пройдены!")
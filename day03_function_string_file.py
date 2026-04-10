def greet(name):
    print("こんにちは、" + name + "さん")

greet("Jun")

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

text = "  apple,banana,orange  "

print(text)
print(text.strip())
print(text.replace("banana", "grape"))

fruits = text.strip().split(",")
print(fruits)

name = "Jun"
age = 27
print(f"{name}さんは{age}歳です")

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("こんにちは\n")
    file.write("Python学習中です\n")

print("sample.txt に書き込みました")

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
str = "abcdefgh"
print(str[2])

print(str[2::-1])
lettersX = ["a", "b", "c"]
lettersY = ("a", "b", "c")
zeros = [0] * 5
combined = zeros + lettersX
#numbers = list(range(20))
chars = list("Hello world")
print(lettersX, lettersY, zeros, combined)
#print(numbers)
print(len(chars))
print(chars[::2])
numbmers = [1, 2, 3]
first, second, third = numbmers
print(first)
#finds, *other, last = numbers
#print(last)
lenders = ["a", "b", "c"]

for idx, lenders in enumerate(lenders):
    print(idx, lenders)

numibers = [3, 7, 9, 12]
def func(numibers):
    smal = numibers[0]
    for i in numibers:
        if i < smal:
            smal = i
    print(smal)
func(numibers)

letters = list(range(14532432))

letters.append("d") #dodaje na koniec
letters.insert(0, "-") #na miejsce 0 daje -
letters.pop(0)
#letters.remove("b")

numbers = [3, 78, 23, 754, 243, 6743, 21, 676, 354, 69]
numbers.sort(reverse=True)
print(numbers)

items = [("Product 1", 123), ("Product 2", 132), ("Product 3", 642), ("Product 4", 75)]
# def sort_item(items):
#   return items[1]
items.sort(key=lambda items:items[1])
print(items)

students = [{"imie": "Jan", "wiek": 20}, {"imie": "Koralina", "wiek": 37}, {"imie": "Brunhilda", "wiek": 189}]
students.sort(key=lambda students:students["wiek"])
print(students[0])

x = list(map(lambda items: items[1], items))

print(x)

from array import array:





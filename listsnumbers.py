numbers = [5,6,7,8,3,4]
numbers.append(10)
numbers.insert(0,20)
numbers.remove(7)
numbers.pop()
print(50 in numbers)
print(numbers)
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers.append(11)
print(numbers)
print(numbers2)

items = [2,3,4,5,2,6,7,4]
items1 = []
for item in items:
    if item not in items1:
        items1.append(item)
        print(items1)

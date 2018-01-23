fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting a position 4

print("\n", fruits)
fruits.reverse()
print("Reversed\n", fruits, "\n")

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
print("\n")

#do some queue work
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival


#two equivalent expressions
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs, "\n")



#more stuff
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

print("")

# call a method on each element, strip() gets ride of trailing whitespace
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

#transpose matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(list(zip(*matrix)))

#del
print()
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:] #just saying del a deletes the list a and so it can't be displayed
print(a)
print()


#tuples and sequences
t = 123, 456, 7890, 'sup'
print(t[0])
print(t)

u = t, (999, 000), 'yolo'
print(u)

#these don't work because tuples are immutable (can't be changed)
#t[0] = 'changed'
#print(u)
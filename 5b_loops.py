#containers are iterables (things that can be iterated over)
#this makes them ideal for a way to search
#searching our trivial lists of 2 or 3 times, but imagine a list holding all the words of a book
#or a library of books.  Imagine looking for a particular word in that book: bo'sun, calumny, syzygous
#or imagine looking for a series of numbers: 0221409, or 59265359 (avagondro, pi, respectively)
#looping over a list is tedious for humans; it is well suited for computers

#we will work with for loops for now

for target in "container":
    print(target)
print()
for target in range(5):
    print(target)

#the header has the "for" identifier, the target, in and the iterable (followed by a colon);
#the next line is indented and has the instruction.
#explain the mechanics of how a loop works

words=["cat", "calumny", "syzygy", "gnome"]

for word in words:
    print(word)

for word in words:
    words.clear()

print("this is words after being popped: ", words)
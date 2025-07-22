squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

new_squares = [i**2 for i in range(1, 11)]
print(new_squares)

evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)

pairs = [(x,y) for x in range(3) for y in range(2)]
print(pairs)







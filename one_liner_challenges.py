from functools import reduce

cubes = [i**3 for i in range(1, 11)]
print(cubes)

caps = list(map(str.capitalize, ['hello', 'world']))
print(caps)

sum = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(sum)

nums = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 == 1, nums))
print(odds)

primes = [i for i in range(2, 20) if all(i % j != 0 for j in range(2, i))]
print(primes)










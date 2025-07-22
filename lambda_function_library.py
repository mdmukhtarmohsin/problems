square = lambda x: x**2
print(square(5))

add = lambda x, y: x + y
print(add(5, 3))

is_even = lambda x: x % 2 == 0
print(is_even(4))

reverse = lambda s: s[::-1]
print(reverse("hello"))

filter_even = lambda nums: list(filter(lambda x: x % 2 == 0, nums))
print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

isPrime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))
print(isPrime(7))








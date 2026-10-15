# Exercise 9.11
# Create a set of odd numbers using set comprehension.

odd = {number for number in range(10) if number % 2 != 0}

print(odd)

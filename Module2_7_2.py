
# Exercise 7.2
# Use a while loop to find the correct number.

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break

    number += 1

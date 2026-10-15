
# Exercise 8.7
# Remove the disease from the list.

things = ["mozzarella", "cinderella", "salmonella"]

things[1] = things[1].capitalize()
things[0] = things[0].upper()

things.remove("salmonella")

print(things)

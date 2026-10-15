# Exercise 9.14
# Use zip to combine movie titles with their plots.

titles = ["Creature of Habit", "Crewel Fate", "Sharks On a Plane"]

plots = ["A nun turns into a monster", "A haunted yarn shop", "Check your exits"]

movies = dict(zip(titles, plots))

print(movies)

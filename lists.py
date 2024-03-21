import random

fruits = ["apple", "bannana", "cherry"]
fruits.append("date")
fruits.extend(["elderberry", "fig", "grape"])
fruits += ["honeydew", "kiwi", "lemon"]

print(fruits)

random_fruit = random.choice(fruits)

while True:
    fruit = random.choice(fruits)
    like = input(f"do you like {fruit}? (yes/no)")
    if like.lower() == "yes":
        new_fruit = input(f"name another fruit to add: ")
        fruit.append(new_fruit)
    elif like.lower() == "no":
        print(f"removing {fruit} from list")
        fruit.remove(fruit)
    elif like.lower() == "stop":
        break

with open("fruits.txt", "w") as fd:
    for fruit in fruits:
        fd.write(fruit + "\n")
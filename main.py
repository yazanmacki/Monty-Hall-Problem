import random
switch = True    # Decide whether to switch doors or not
score = 0

for i in range(0,100001):
    items = ["Car", "Goat", "Goat"]
    random.shuffle(items)

    choice = 0
    x = 0
    goatIndex = [-1,-1]

    for i in range(0,3):
        if items[i] == "Goat":
            goatIndex[x] = i
            x += 1

    removeChoice = random.choice(goatIndex)
    if removeChoice == choice:
        for i in range(0,2):
            if goatIndex[i] != choice:
                removeChoice = goatIndex[i]


    if switch:
        for i in range(0, 3):
            if i != choice and i != removeChoice:
                choice = i

    if items[choice] == "Car":
        score += 1


print(str(score/100000*100) + "%")

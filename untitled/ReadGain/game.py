locations = {0: "You are sitting in front of the computer",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at top of a hill",
             3: "You are in side a building",
             4: "You are in a vally beside a stream",
             5: "You are in a forest"}

exits = [{"Q": 0},
         {"W": 2, "N": 5, "E": 3, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
loc = 1

while True:
    avilable_exit = ""
    # for gateway in exits[loc].keys():
    #     avilable_exit += gateway
    print(",".join(exits[loc].keys()))

    print(locations[loc])

    if loc == 0:
        break
    path = input("Enter from the available exits "+avilable_exit)
    if path in exits[loc]:
        loc = exits[loc][path]
    else:
        print("Not a valid path")




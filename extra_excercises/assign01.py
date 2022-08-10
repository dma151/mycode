#!/usr/bin/env python3

favorites = []

food1 = ["Ramen", "Pho", "Naengmyun"]
food2 = ["Steak", "KBBQ", "Wings", "Ribs"]
food3 = ["Sushi", "Yakitori", "Bulgogi", "Katsu"]

favorites.append(food1)
favorites.append(food2)
favorites.append(food3)

print("Favorite list of lists")
print(favorites, "\n") 
print("My Favorite Food is: " + favorites[0][0], "\n")

champs = {
        "Sung Jinwoo": {
            "Rank": "S",
            "Ability": "Shadow Monarch",
            "Boo": "Cha Hae In"
            },
        "Saitama": {
            "Rank": "C",
            "Ability": "Superhuman",
            "Boo": "Fubuki"
            },
        "Han Yoojin": {
            "Rank": "F",
            "Ability": "Taming",
            "Boo": "Bak Yerim"
            }
        }

print("Super Heroes with shared qualities")
#print(champs, "\n")
#print(champs.keys())
#print(champs.values())
for i in range(3):
    print(list(champs.keys())[i], list(champs.values())[i])

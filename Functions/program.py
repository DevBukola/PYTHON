def fav_foods(**kwargs):
    for person, food in kwargs.items():
        print(f"{person}'s favorite food is {food}")
result = fav_foods(Dara="Potatoes and Eggs.", Daniel="Rice and Fish.", Simi="Beans.", Tony="Swallow and Vegetables Soup", Toyin="Rice and Chicken Stew.")
print(result)

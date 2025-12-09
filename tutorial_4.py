recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 3,
    "milk": 100,
    "vanilla": 5
}

pantry = {
    "flour": 400,       # We have some, but not enough (need 100 more)
    "eggs": 10,         # We have plenty (need 0)
    "milk": 100,        # We have exact amount (need 0)
    # sugar is missing completely (need 200)
    # vanilla is missing completely (need 5)
}

shopping_list={}
for ingredient in recipe:

    amount_have=pantry.get(ingredient, 0)
    amount_needed=recipe[ingredient]

    difference=amount_needed-amount_have

    if difference>0:
        shopping_list[ingredient]=difference

print("Shopping List:")
for name, amount in shopping_list.items():
    print(f"{name}: {amount}")

# print("Shopping List:")
# for ingredient in recipe:
#     if ingredient not in pantry:
#        amount=recipe[ingredient]
#        print(f'{ingredient}: {amount}')
#     else:
#         if recipe[ingredient]>pantry[ingredient]:
#           amount_needed=recipe[ingredient]-pantry[ingredient]
#           print(f"{ingredient}: {amount_needed}")

# Shopping List:
# flour: 100
# sugar: 200
# vanilla: 5

def findrecipes():
    user = set(ingredients)

    import random
    import json
    filepath = "C:/Users/katal/Documents/CODE University/food_recipes/data/epicurious-recipes.json"
    with open(filepath, encoding='utf-8') as f: 
        data = (line.strip() for line in f) #Erzeugt Generator Objekt 
        data_json = "[{0}]".format(','.join(data))
        data = json.loads(data_json)

    sample = random.sample(data,10000)

    matchingrecipes = [] # create an empty list where the matching recipes will be added
    matchcounterlist = [] # empty list to add the ingredientmatchcounter in

    for recipe in sample:    
        hed = recipe.get("hed", None)
        url = "www.epicurious.com" + recipe.get("url")
        ingredients = recipe.get("ingredients")
        if ingredients is not None:

            ingredients_text = " ".join(ingredients)
            ingredients_text
            ingredients_splitted = ingredients_text.split()
            ingredients_splitted
            unique_ingredients = set(ingredients_splitted)
            diff = user.difference(unique_ingredients)
            ingredientmatchcounter = len(user) - len(diff) #the higher the better
            note = str(ingredientmatchcounter) + " element out of your input used in this recipe"
            note

            recipe1 = {"hed": hed, "url": url, "note": note} #dictionary with all information

            matchingrecipes.append(recipe1)
            #print(matchingrecipes)
            matchcounterlist.append(ingredientmatchcounter)

    max_val = max(matchcounterlist)
    toprecipes = [matchingrecipes[e] for e, i in enumerate(matchcounterlist) if i == max_val]
    return toprecipes
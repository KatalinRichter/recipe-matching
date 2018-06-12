def findrecipes():
    user = set(ingredients)

    import random
    import json
    filepath = "C:/Users/XXX" #where to find the datasource
    with open(filepath, encoding='utf-8') as f: 
        data = (line.strip() for line in f)  
        data_json = "[{0}]".format(','.join(data))
        data = json.loads(data_json)

    sample = random.sample(data,10000)

    matchingrecipes = [] 
    matchcounterlist = []

    for recipe in sample:    
        hed = recipe.get("hed", None)
        url = "www.epicurious.com" + recipe.get("url") #website, which provided the recipe data set
        ingredients = recipe.get("ingredients")
        if ingredients is not None:

            ingredients_text = " ".join(ingredients)
            ingredients_text
            ingredients_splitted = ingredients_text.split()
            ingredients_splitted
            unique_ingredients = set(ingredients_splitted)
            diff = user.difference(unique_ingredients)
            ingredientmatchcounter = len(user) - len(diff) 
            note = str(ingredientmatchcounter) + " element out of your input used in this recipe"
            note

            recipe1 = {"hed": hed, "url": url, "note": note} 

            matchingrecipes.append(recipe1)
            #print(matchingrecipes)
            matchcounterlist.append(ingredientmatchcounter)

    max_val = max(matchcounterlist)
    toprecipes = [matchingrecipes[e] for e, i in enumerate(matchcounterlist) if i == max_val]
    return toprecipes

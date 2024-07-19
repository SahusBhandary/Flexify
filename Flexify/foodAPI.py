import requests

api_key = "clUgaUZjSTS0ReayoXNJbblmvM5zxYkUOymPpqM0"

# parameters for call to API
parameters = {
    "api_key": api_key 
}

food = {}

# store important nutrients into here
nutrients = {}

# finds nutrition of specific food using USDA API
def findNutrition(food):
    api = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + str(food) + ", raw"
    response = requests.get(api, params=parameters)
    for i in range (0,len(response.json()["foods"][0]["foodNutrients"])):
        nutrientName = response.json()["foods"][0]["foodNutrients"][i]["nutrientName"]
        value = str(response.json()["foods"][0]["foodNutrients"][i]["value"])
        unitName = response.json()["foods"][0]["foodNutrients"][i]["unitName"]
        if nutrientName == "Protein":
            nutrients["protein"] = str(value) + str(unitName)
        if nutrientName == "Total lipid (fat)":
            nutrients["fat"] = str(value) + str(unitName)
        if nutrientName == "Carbohydrate, by difference":
            nutrients["carbs"] = str(value) + str(unitName)
        if nutrientName == "Water":
            nutrients["water"] = str(value) + str(unitName)
        if nutrientName == "Energy":
            nutrients["energy"] = str(value) + str(unitName)
        if nutrientName == "Caffeine":
            nutrients["caffeine"] = str(value) + str(unitName)
        if nutrientName == "Sugars, total including NLEA":
            nutrients["sugar"] = str(value) + str(unitName)
        if nutrientName == "Fiber, total dietary":
            nutrients["fiber"] = str(value) + str(unitName)
        if nutrientName == "Calcium, Ca":
            nutrients["calcium"] = str(value) + str(unitName)
        if nutrientName == "Iron, Fe":
            nutrients["iron"] = str(value) + str(unitName)
        
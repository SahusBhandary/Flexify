import requests

api_key = "clUgaUZjSTS0ReayoXNJbblmvM5zxYkUOymPpqM0"

# parameters for call to API
parameters = {
    "api_key": api_key 
}

food = {

}

def findNutrition(food):
    api = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + str(food)
    response = requests.get(api, params=parameters)

    res = ""

    for i in range (0,5):
        nutrientName = response.json()["foods"][0]["foodNutrients"][i]["nutrientName"]
        value = str(response.json()["foods"][0]["foodNutrients"][i]["value"])
        unitName = response.json()["foods"][0]["foodNutrients"][i]["unitName"]
        res += nutrientName + value + unitName 

    return res
import requests



 #Función para obtener todos los cócteles con un ingrediente:
def search_by_ingredient(ingredient):
    response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}')
    if response.status_code == 200:
        data = response.json()
        return data['drinks']
    else:
        return None
    

#La función anterior utiliza el endpoint "Search by ingredient" para obtener la lista de categorías de cócteles. 

#Función para obtener un cóctel al azar:
def get_random_cocktail():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()
    cocktail = data['drinks'][0]

    cocktail_name = cocktail['strDrink']
    cocktail_ingredients = [cocktail[f'strIngredient{i}'] for i in range(1, 16) if cocktail[f'strIngredient{i}'] is not None]

    print("Cocktail Name:", cocktail_name)
    print("Ingredients:", ", ".join(cocktail_ingredients))



#La función anterior utiliza el endpoint "look up a random cocktail" para obtener un cóctel al azar. 

#Función para buscar cócteles por nombre:
def get_drink_by_name(drink_name):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}"
    response = requests.get(url)
    data = response.json()
    if data['drinks']:
        cocktail = data['drinks'][0]
        drink_details = {
            'name': cocktail['strDrink'],
            'category': cocktail['strCategory'],
            'instructions': cocktail['strInstructions'],
            'ingredients': []
        }

        for i in range(1, 16):
            ingredient_key = f'strIngredient{i}'
            measure_key = f'strMeasure{i}'
            if cocktail[ingredient_key]:
                ingredient = cocktail[ingredient_key]
                measure = cocktail[measure_key] or "to taste"
                drink_details['ingredients'].append(f"{measure} of {ingredient}")

        return drink_details
    else:
        return None


#La función utiliza el endpoint "Search by cocktail name" para buscar cócteles por nombre. 

#Funcion que muestra cocoteles con la letra inicial ingresada
def list_cocktails_by_letter(letter):
    url = f'http://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}'

    response = requests.get(url)
    data = response.json()

    if data['drinks']:
        cocktails = [drink['strDrink'] for drink in data['drinks']]
        return cocktails
    else:
        return []


#Esta función recibe una letra y con el endpoint"List all cocktails by first letter"" muestra los cocteles que inician con la letra ingresada.

# Función que muestra el menú de opciones al usuario
def show_menu():
    print("Menu options:")
    print("1. Get cockatils by name of ingredient ")
    print("2. Get a random cocktail")
    print("3. Look cocktail by name")
    print("4. See cocktails by initial letter")
    print("5. Exit")



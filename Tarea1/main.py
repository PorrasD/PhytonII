import API


if __name__ == "__main__":
    while True:
        API.show_menu()
        opcion = input("pick a number: ")
        if opcion == '1':
            ingredient = input(str.casefold("Enter an ingredient e.g. vodka, gin: "))
            API.search_by_ingredient(ingredient)
            result = API.search_by_ingredient(ingredient)
            if result is not None:
                for drink in result:
                    print(drink['strDrink'])
            else:
                print('No drinks found')
        elif opcion == '2':
            API.get_random_cocktail()

        elif opcion == '3':
            nombre=input("Enter a cocktail for all the details: ") 
            API.get_drink_by_name(nombre)
            cocktail = API.get_drink_by_name(nombre)
            if cocktail:
                print(f"Name: {cocktail['name']}")
                print(f"Category: {cocktail['category']}")
                print(f"Instructions: {cocktail['instructions']}")
                print("Ingredients:")
            for ingredient in cocktail['ingredients']:
                print(f"- {ingredient}")
            else:
                print("Drink not found")

        elif opcion == '4':
            letter = input("Enter a letter to look for cocktails:")
            API.list_cocktails_by_letter(letter)
            cocktails = API.list_cocktails_by_letter(letter)
            if cocktails:
                print(f"Cocktails starting with '{letter}':")
            for cocktail in cocktails:
                print(cocktail)
            else:
                print(f"No cocktails starting with '{letter}' found.")

        elif opcion == '5':
            print("¡See you later for more cockatils, Good bye!")
            break


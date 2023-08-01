import requests as req

# Función que obtiene un chiste aleatorio de Chuck Norris y lo muestra en pantalla
def chiste_aleatorio():
    response = req.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        chiste = response.json()['value']
        print(chiste)
    else:
        print("No se pudo obtener el chiste aleatorio")

# Función para obtener la lista de categorías de chistes y mostrarlas en pantalla
def obtener_categorias():
    response = req.get("https://api.chucknorris.io/jokes/categories")
    if response.status_code == 200:
        categorias = response.json()
        print("Categorías disponibles:")
        for categoria in categorias:
            print(categoria)
    else:
        print("No se pudo obtener la lista de categorías")

# Función para elegir un chiste de una categoría específica y mostrarlo en pantalla
def obtener_chiste_por_categoria(categoria):
    response = req.get(f"https://api.chucknorris.io/jokes/random?category={categoria}")
    if response.status_code == 200:
        chiste = response.json()['value']
        print(chiste)
    else:
        print(f"No se pudo obtener el chiste de la categoría {categoria}")

# Función que muestra el menú de opciones al usuario
def mostrar_menu():
    print("Menu de opciones:")
    print("1. Obtener chiste aleatorio")
    print("2. Obtener categorías de chistes")
    print("3. Obtener chiste de una categoría específica")
    print("4. Salir")


import API_Requests

# Menu de opciones
if __name__ == "__main__":
    while True:
        API_Requests.mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            API_Requests.chiste_aleatorio()
        elif opcion == '2':
            API_Requests.obtener_categorias()
        elif opcion == '3':
            categoria = input("Introduce la categoría: ")
            API_Requests.obtener_chiste_por_categoria(categoria)
        elif opcion == '4':
            break
        else:
            print("Opción no valida")

    print("¡Vuelve pronto por mas chistes,Hasta luego!")



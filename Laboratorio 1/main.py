import datetime
import Trig


def log_operation(operation, result):
    with open('log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'{timestamp} - Operation: {operation}, Result: {result}\n'
        log_file.write(log_entry)


def main():
    trig = Trig()

    while True:
        print("Seleccione una opción:")
        print("1. Seno")
        print("2. Coseno")
        print("3. Tangente")
        print("4. Salir")

        choice = input("Elija una opción: ")

        if choice == "1":
            sin = trig.sin()
            print("El seno de pi es:", sin)
            log_operation("Seno", sin)
        elif choice == "2":
            cos = trig.cos()
            print ("El coseno de pi es:" ,cos)
            log_operation("Coseno", cos)
        elif choice == "3":
            tan = trig.tan()
            print("La tangente de pi es: ",tan)
            log_operation("Tangente", tan)
        elif choice == "4":
            print("Hasta Pronto!")
            break
        else:
            print("Opción inválida. Por favor, elija nuevamente.")

if __name__ == "__main__":
    main()

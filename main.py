import datetime
from Trig import Trig

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
            sine = trig.get_sine()
            print(f"El seno de pi es: {sine}")
            log_operation("Seno", sine)
        elif choice == "2":
            cosine = trig.get_cosine()
            print(f"El coseno de pi es: {cosine}")
            log_operation("Coseno", cosine)
        elif choice == "3":
            tangent = trig.get_tangent()
            print(f"La tangente de pi es: {tangent}")
            log_operation("Tangente", tangent)
        elif choice == "4":
            print("Hasta Pronto!")
            break
        else:
            print("Opción inválida. Por favor, elija nuevamente.")

if __name__ == "__main__":
    main()

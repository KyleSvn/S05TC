# Creación de la lista 
agenda = []

def agregar_contacto(nombre, telefono):
    contacto = {"nombre": nombre, "telefono": telefono}
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado. ")

def mostrar_agenda():
    if not agenda:
        print("La agenda esta vacia. ")
    else:
        print("\n Agenda de Contactos: ")
        for i, contacto in enumerate(agenda, start=1):
            print(f"{i}. {contacto['nombre']} - {contacto['telefono']}")

# Menu simple
while True:
    print("\n--- Menu ---")
    print("1. Agregar contacto")
    print("2. Mostrar agenda")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif opcion == "2":
        mostrar_agenda()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("❌ Opción no válida.")

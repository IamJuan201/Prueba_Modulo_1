# • Actualizar la información de un estudiante.

# • ID (identificador único)

from funciones_gestion_estudiantes import main_options, registrar_estudiante, consultar_lista, buscar_estudiante, actualizar_estudiante, eliminar_estudiante

n = 70
Estudiantes = []

option = main_options()

while option != 6:
    if option == 1:
        registrar_estudiante(Estudiantes)

    elif option == 2:
        consultar_lista(Estudiantes)

    elif option == 3:
        nombre = input("Nombre del estudiante: ")
        Estudiante = buscar_estudiante(Estudiantes, nombre)
        if Estudiante:
            print("-"*n)
            print(f"ID: {Estudiante['Identificador_unico']}\nNombre: {Estudiante['Nombre_estudiante']}\nEdad: {Estudiante['Edad_estudiante']}\nPrograma: {Estudiante['Programa_estudiante']}\nEstado: {Estudiante['Estado_estudiante']}")
            print("-"*n)
            
        else:
            print('Estudiante no encontrado')
        input('\nPresione ENTER para volver al menu principal...')

    elif option == 4:
        nombre = input("Nombre del estudiante: ")
        actualizar_estudiante(Estudiantes)

    elif option == 5:
        nombre = input("Nombre del estudiante: ")
        eliminar_estudiante(Estudiantes)
    else:
        print("\nERROR! Esa opcion no existe. Intente de nuevo...\n")
        input('\nPresione ENTER para volver al menu principal...')

    option = main_options()

print("="*n)
print("\nThanks for use the program, See you later!".center(n))
print("="*n)
n = 70

def main_options():
    print('='*n)
    print('GESTION DE ESTUDIANTES'.center(n))
    print('='*n)
    print('1. Registrar nuevos estudiantes.')
    print('2. Consultar la lista de estudiantes.')
    print('3. Buscar estudiante')
    print('4. Actualizar información de estudiante.')
    print('5. Eliminar estudiantes.')
    print('6. Salir')
    print('='*n)

    try:
        option = int(input("Choose an option (1-6): "))
        return option
    except:
        return 0

def registrar_estudiante(Estudiantes):
    elecion = 'si'

    while elecion == 'si':
        print('='*n)
        # **Falta hacerlo unico
        ID_estudiante = int(input("ID del estudiante: "))
        if ID_estudiante < 0:
            print("ERROR! El ID el estudiante no puede ser negativo.")
            continue

        nombre = input("Nombre del estudiante: ").lower()

        edad = int(input("Edad del estudiante: "))
        if edad < 0:
            print("ERROR! La edad del estudiante no puede ser negativa.")
            continue

        curso = input("Programa del estudiante: ").lower()

        estado = input("Estado (activo/inactivo): ").strip().lower()

        if estado == "activo" or estado == "inactivo":
            estudiante = {
                            "Identificador_unico" : ID_estudiante,
                            "Nombre_estudiante" : nombre,
                            "Edad_estudiante" : edad,
                            "Programa_estudiante" : curso,
                            "Estado_estudiante" : estado
            }

            Estudiantes.append(estudiante)

            print('='*n)
            print(f"Estudiante '{nombre}' añadido con exito!")

            elecion = input('\nDesea registrar otro estudiante?(Si/No): ').lower()

        else:
            print("ERROR! Solo se puede escribir activo o inactivo.")
            continue

        print('='*n)


def consultar_lista(Estudiantes):
    print('='*n)
    print('LISTA DE ESTUDIANTES'.center(n))
    print('='*n)

    if not Estudiantes:
        print("La lista esta vacia. Necesita agregar estudiantes.")
        input('\nPresione ENTER para volver al menu principal...')
        return

    else:
        for Estudiante in Estudiantes:
            print(f"ID: {Estudiante['Identificador_unico']}\nNombre: {Estudiante['Nombre_estudiante']}\nEdad: {Estudiante['Edad_estudiante']}\nPrograma: {Estudiante['Programa_estudiante']}\nEstado: {Estudiante['Estado_estudiante']}")
            print('-'*n)

    input('\nPresione ENTER para volver al menu principal...')
    
def buscar_estudiante(Estudiantes, nombre):
    if not Estudiantes:
        print("La lista esta vacia. Necesita agregar estudiantes.")
        input('\nPresione ENTER para volver al menu principal...')
        return
    
    else:
        for Estudiante in Estudiantes:
            if Estudiante["Nombre_estudiante"] == nombre.strip().lower():
                return Estudiante
        return None

def actualizar_estudiante(Estudiantes, nombre):
    if not Estudiantes:
        print("La lista esta vacia. Necesita agregar estudiantes.")
        input('\nPresione ENTER para volver al menu principal...')
        return

    else:
        Estudiante = buscar_estudiante(Estudiantes, nombre)

        if not Estudiante:
            print(f"El estudiante '{nombre}' no se encontro en la lista.")
            return
        
        else:
            new_ID = (input("Nueva ID (ENTER para omitir): "))
            new_Name = input("Nuevo Nombre (ENTER para omitir): ")
            new_Age = int(input("Nuevo Nombre (ENTER para omitir): "))
            new_Program = input("Nuevo programa (ENTER para omitir): ")
            new_State = input("Nuevo estado (ENTER para omitir): ")

            if new_ID:
                Estudiante["Identificador_unico"] = int(new_ID)
            if new_Name:
                Estudiante["Nombre_estudiante"] = new_Name
            if new_Age:
                Estudiante["Edad_estudiante"] = int(new_Age)
            if new_Program:
                Estudiante["Programa_estudiante"] = new_Program
            if new_State:
                Estudiante["Estado_estudiante"] = new_State

            print("Datos del estudiante actualizados con éxito.")

def eliminar_estudiante(Estudiantes, nombre):
    if not Estudiantes:
        print("La lista esta vacia. Necesita agregar estudiantes.")
        input('\nPresione ENTER para volver al menu principal...')
        return
    else:
        Estudiante = buscar_estudiante(Estudiantes, nombre)

        if not Estudiante:
            print(f"El estudiante '{nombre}' no se encontro en la lista.")
            return

        Estudiantes.remove(Estudiante)
        print(f"El estudiante '{nombre}' ha sido eliminado de la lista.")
        input('\nPresione ENTER para volver al menu principal...')
        print("-"*n)
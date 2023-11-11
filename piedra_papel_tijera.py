import random

lista_opciones = ["Piedra", "Papel", "Tijera"]

def eleccion_ia():
    return random.randint(0, 2)

def eleccion_usuario(): # Esta eleccion se realiza ahora con numeros, se verifica que lo sean y esten dentro del dominio
    while True:
        eleccion_num = input("Elige una opción:\n1. Piedra\n2. Papel\n3. Tijera\n") 
        if eleccion_num.isdigit(): # se utiliza la propiedad del input para la validacion
            eleccion_num = int(eleccion_num) #Se hace el cast a entero para poder comparar con eleccion de la máquina posteriormente
            if 1 <= eleccion_num <= 3:
                return eleccion_num - 1
            else:
                print("Opción inválida. Por favor, elige un número entre 1 y 3.")
        else:
            print("Entrada no válida. Debes ingresar un número entre 1 y 3.")

def ganador_partida(user, IA):
    if user == IA:
        return "Empate"
    if (IA + 1) % len(lista_opciones) == user:
        return "Jugador"
    else:
        return "Máquina"
 
def jugar_partidas(num_partidas): # Nueva funcion que hace itera la cantidad de partidas ingresadas y acumula resultados  de cada una de las partidas

    resultados = {"Jugador": 0, "Máquina": 0, "Empate": 0}

    for _ in range(num_partidas):
        user = eleccion_usuario() #Estos llamados se realizaban antes desde la funcion jugar()
        IA = eleccion_ia()
        ganador = ganador_partida(user, IA)#Hasta aqui fueron movidas para ejecutarse dentro de este bucle
        if ganador == "Jugador":
            resultados["Jugador"] += 1
        elif ganador == "Máquina":
            resultados["Máquina"] += 1
        else:
            resultados["Empate"] += 1

        print(f"Jugador eligió: {lista_opciones[user]}")
        print(f"Máquina eligió: {lista_opciones[IA]}")
        print(f"Ganador: {ganador}")

    return resultados

def jugar(): #Se ha modificado la funcion para jugar varias veces, verifica opcion sea valida
    while True:
        num_partidas = input("¿Cuántas partidas deseas jugar? ")
        if num_partidas.isdigit():
            num_partidas = int(num_partidas)
            if num_partidas > 0: #Al validar numero de partidas a jugar, realiza el llamado a la funcion con el numero de partidas como parametro
                resultados = jugar_partidas(num_partidas)

                print("\nResultados finales:")
                print(f"Jugador: {resultados['Jugador']}")
                print(f"Máquina: {resultados['Máquina']}")
                print(f"Empate: {resultados['Empate']}")
                break
            else:
                print("Por favor, ingresa un número mayor que 0.")
        else:
            print("Entrada no válida. Debes ingresar un número entero mayor que 0.")


jugar()

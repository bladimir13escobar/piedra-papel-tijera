import random 


def jugar():
    usuario = input("Escoje una opcion 'PI' para piedra, 'PA' papel y 'TI' para tijera. \n").lower()

    computadora = random.choice(["piedra", "papel", "tijera"])


    if usuario == computadora:
        return f"la computadora escogio {computadora} ¡Empate."
    
    if gano_el_jugador(usuario, computadora):
        return f"la computadora escogio {computadora} ¡Ganaste."
    
    return f"La computadora escogio {computadora} ¡Perdiste!"


def gano_el_jugador(jugador, oponente):
    if ((jugador == "piedra" and oponente == "tijera")
        or (jugador == "papel" and oponente == "piedra")
        or (jugador == "tijera" and oponente == "papel")):
        return True
    else:
        return False


print(jugar())

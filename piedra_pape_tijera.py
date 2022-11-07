import random 


def jugar():
    print("""
        =========================
        || BIENVENIDO AL JUEGO ||
        =========================
        """)

    usuario = input("Escoje una opcion: piedra, papel o tijera. \n ==> ").lower()
    opciones = ("piedra", "papel", "tijera")
    computadora = random.choice(opciones)

    user_win = 0
    computer_win = 0
    if usuario in opciones:

        if usuario == computadora:
            return f"la computadora escogio {computadora} ¡Empate."
        elif gano_el_jugador(usuario, computadora):
            user_win += 1
            return f"la computadora escogio {computadora} ¡Ganaste."

        elif gano_el_jugador(usuario, computadora) == False:
            computer_win += 1
            return f"La computadora escogio {computadora} ¡Perdiste!"

    else:
        return "opcion no valida"

def gano_el_jugador(jugador, oponente):
    if ((jugador == "piedra" and oponente == "tijera")
        or (jugador == "papel" and oponente == "piedra")
        or (jugador == "tijera" and oponente == "papel")):
        return True
    else:
        return False



print(jugar())

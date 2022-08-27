import random 


def jugar():
    usuario = input("Escoje una opcion 'PI' para piedra, 'PA' papel y 'ti' para tijera. \n").lower()

    computadora = random.choice(["pi", "pa", "pi"])

    if usuario == computadora:
        return "¡Empate."
    
    if gano_el_jugador(usuario, computadora):
        return "¡Ganaste."
    
    return "¡Perdiste!"

def gano_el_jugador(jugador, oponente):
    if ((jugador == "pi" and oponente == "ti")
        or (jugador == "pa" and oponente == "pi")
        or (jugador == "ti" and oponente == "pa")):
        return True
    else:
        return False


print(jugar())
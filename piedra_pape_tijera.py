import random 


def jugar():
    usuario = input("Escoje una opcion 'PI' para piedra, 'PA' papel y 'ti' para tijera. /n").lower()

    computadora = random.choice("pi", "pa", "pi")
    
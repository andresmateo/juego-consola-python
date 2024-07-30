import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("¡Bienvenido a la aventura en el espacio! Por favor, ingresa tu nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Roboto", 30, 5),
        Enemigo("Monster", 70, 15)
    ]

    enemigos_derrotados = []

    print("¡Comienza la aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue

        print("=================================================================")
        print(f"Te encuentas con un enemigo {enemigo_actual.nombre} en tu camino.")

        while enemigo_actual.salud > 0:
            accion = input("¿Qué deseas hacer? (atacar/huir): ").lower()
            print("--------------------------------------------------------------")
            if accion == "atacar":
                danio_jugador = jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} y le has causado {danio_jugador} puntos de daño.")
                enemigo_actual.recibir_danio(danio_jugador)

                if enemigo_actual.salud > 0:
                    danio_enemigo = enemigo_actual.atacar()
                    print(f"{enemigo_actual.nombre} te atacó y te causó {danio_enemigo} puntos de daño")
                    jugador.recibir_danio(danio_enemigo)
            elif accion == "huir":
                print("Has decidido huir del combate.")
                print(f"{enemigo_actual.nombre} dice: ¡Vuelve aquí cobarde!")
                break
            print("--------------------------------------------------------------")
        if jugador.salud <= 0:
            print("¡Has perdido la guerra!")
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        if not enemigos:
            print("¡Felicidades, has derrotado a todos los enemigos!")
            break
        else:
            continuar = input("¿Quieres seguir explorando este planeta? (s/n): ").lower()

            if continuar != "s":
                print("¡Gracias por haber jugado Space Explorer!")
                break

if __name__ == "__main__": # Nos asegura que solo podremos ejecutar este script desde el programa principal
    main()
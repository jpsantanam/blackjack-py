from random import choice
from arte import logo


def sorteiaCartas():
    baralho = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(baralho)


def somaCartas(cartas):
    soma = sum(cartas)
    if soma == 21 and len(cartas) == 2:
        soma = 0
    if 11 in cartas and soma > 21:
        cartas.remove(11)
        cartas.append(1)
    return soma


def comparaPontos(pontosUsuario, pontosComputador):
    if pontosUsuario > 21 and pontosComputador > 21:
        return "Você perdeu, passou de 21..."
    if pontosUsuario == pontosComputador:
        return "Empate."
    if pontosComputador == 0:
        return "Você perdeu... Oponente tem um Blackjack!"
    if pontosUsuario == 0:
        return "Você ganhou com um Blackjack!"
    if pontosUsuario > 21:
        return "Você perdeu,  passou de 21..."
    if pontosComputador > 21:
        return "Você ganhou! Oponente passou de 21."
    if pontosUsuario > pontosComputador:
        return "Você ganhou!"
    else:
        return "Você perdeu..."


def main():
    print(logo)

    cartasUsuario = []
    cartasComputador = []
    deveContinuar = True

    for _ in range(2):
        cartasUsuario.append(sorteiaCartas())
        cartasComputador.append(sorteiaCartas())

    while deveContinuar:
        somaUsuario = somaCartas(cartasUsuario)
        somaComputador = somaCartas(cartasComputador)

        print(f"\nSua mão: {cartasUsuario}, pontuação total: {somaUsuario}")
        print(f"Primeira carta do computador: {cartasComputador[0]}")

        if 0 in [somaUsuario, somaComputador] or somaUsuario > 21:
            deveContinuar = False
        else:
            maisCarta = input("\n'sim' para mais uma carta e 'não' para parar: ").lower()
            if maisCarta == "sim":
                cartasUsuario.append(sorteiaCartas())
            else:
                deveContinuar = False

    while somaComputador != 0 and somaComputador < 17:
        cartasComputador.append(sorteiaCartas())
        somaComputador = somaCartas(cartasComputador)

    print(f"\nSua mão: {cartasUsuario}, pontuação total: {somaUsuario}")
    print(f"Mão do oponente: {cartasComputador}, pontuação total: {somaComputador}")
    print(comparaPontos(somaUsuario, somaComputador))

    outraPartida = input("\nDeseja jogar outra partida: 'sim' ou 'não'? ").lower()
    if outraPartida == "sim":
        main()


if __name__ == "__main__":
    main()

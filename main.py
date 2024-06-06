from Classi.Spese.CategoriaSpesa import *
from Classi.Spese.Spesa import *
from Classi.Squadra.Squadra import *
from Classi.utils import *
from Classi.Spese.SpeseRagruppate import *
from Classi.Squadra.SquadreRagruppate import *


boolD = False
squadreragruppate: Squadreragruppate = Squadreragruppate("Dati\\squadre.csv")
speseragruppate: ragruppaSpese = ragruppaSpese(
    squadreragruppate.squadreRagruppate)


def visualizza_info_squadra():

    print("Informazioni su tutte le squadre:")
    for squadra in squadreragruppate:
        print(squadra)


def seleziona_squadra_e_visualizza_info():  # non funziona
    # poter selezionare spese totali o altro
    nome_squadra = input("Inserisci il nome della squadra: ")

    squadra_selezionata = next(
        (squadra for squadra in squadreragruppate if squadra.nome == nome_squadra), None)
    if squadra_selezionata:
        print("\n\nEcco delle info: \n"+str(squadra_selezionata)+"\n")
    else:
        print("Squadra non trovata.")


def main_menu():

    print("MENU PRINCIPALE")

    print("1. Visualizza informazioni su tutte le squadre")

    print("2. Seleziona squadra e visualizza informazioni")

    print("3. Esci")

    choice = input("Scegli un'opzione: ")

    # Aggiungi una stampa di debug per verificare l'input dell'utente
    print(f"Scelta utente: {choice}")

    return choice


def printBoolD(frase: str) -> None:

    if boolD:
        print(frase)


def main():
    choice = -1
    while choice != 3:
        choice = main_menu()
        print(f"Hai scelto l'opzione: {choice}")
        if choice == "1":
            visualizza_info_squadra()
        elif choice == "2":

            seleziona_squadra_e_visualizza_info()

        elif choice == "3":

            print("Arrivederci PUTTANA!")

            choice = 3
        else:

            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

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

    print("Informazioni su tutte le squadre:\n")
    for squadra in squadreragruppate:
        print(squadra)
    print("\n")


def seleziona_squadra_e_visualizza_info():
    nome_squadra = input("Inserisci il nome della squadra: ")

    squadra_selezionata = next(
        (squadra for squadra in squadreragruppate if squadra.nome == nome_squadra), None)
    if squadra_selezionata:
        print("\n\nEcco delle info: \n"+str(squadra_selezionata)+"\n")
    else:
        print("Squadra non trovata.")


def seleziona_squadra_e_visualizza_spese():
    nome_squadra = input("Inserisci il nome della squadra: ").strip()
    squadra_selezionata = speseragruppate.ragruppaSpese.get(nome_squadra)
    if squadra_selezionata is not None:
        print("\n\nEcco delle spese effettuate \n" +
              str(squadra_selezionata)+"\n")
    else:
        print("Squadra non trovata.")


def seleziona_squadra_e_visualizza_spese_totali():
    nome_squadra = input("Inserisci il nome della squadra: ").strip()
    squadra_selezionata = speseragruppate.ragruppaSpese.get(nome_squadra)
    if squadra_selezionata is not None:
        totali = 0
        for n_info in range(0, len(squadra_selezionata)):
            squadra = squadra_selezionata[n_info]
            importo = squadra.importo
            totali += int(importo)
        print("Le totali spese che queste squadra ha avuto è "+str(totali))

    else:
        print("Squadra non trovata.")


def main_menu():

    print("\nMENU PRINCIPALE")

    print("0. Esci")

    print("1. Visualizza informazioni su tutte le squadre")

    print("2. Seleziona squadra e visualizza informazioni")

    print("3. Seleziona squadra e visualizza costi")

    print("4. Seleziona squadra e visualizza totali")

    print("\n")

    choice = input("Scegli un'opzione: ")

    # Aggiungi una stampa di debug per verificare l'input dell'utente
    print("Hai scelto l'opzione: "+choice+"\n")

    return choice


def printBoolD(frase: str) -> None:

    if boolD:
        print(frase)


def main():
    choice = -1
    while choice != 0:
        choice = main_menu()
        if choice == "1":
            visualizza_info_squadra()
        elif choice == "2":

            seleziona_squadra_e_visualizza_info()

        elif choice == "3":
            # ! non stanmpa in modo corretto le classi ma il codice funziona
            seleziona_squadra_e_visualizza_spese()

        elif choice == "4":
            seleziona_squadra_e_visualizza_spese_totali()

        elif choice == "0":

            print("Arrivederci PUTTANA!")

            choice = 0
        else:

            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

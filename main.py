from Classi.CategoriaSpesa import *
from Classi.Spesa import *
from Classi.Squadra import *
from Classi.StadioClass import *
from utils import *

boolD = False
path_file_csv = "Dati/squadre.csv"  # Percorso assoluto del file CSV

def visualizza_info_squadra(squadre):
    print("Informazioni su tutte le squadre:")
    for squadra in squadre:
        print(squadra)
        
        
def seleziona_squadra_e_visualizza_info():
    nome_squadra = input("Inserisci il nome della squadra: ")
    squadra_selezionata = next((squadra for squadra in squadre if squadra.nome == nome_squadra), None)
    if squadra_selezionata:
        print(squadra_selezionata)
        totale_spese = squadra_selezionata.calcola_totale_spese()
        print("Totale spese:", totale_spese, "euro")
    else:
        print("Squadra non trovata.")

def main_menu():
    print("MENU PRINCIPALE")
    print("1. Visualizza informazioni su tutte le squadre")
    print("2. Seleziona squadra e visualizza informazioni")
    print("3. Esci")
    choice = input("Scegli un'opzione: ")
    print(f"Scelta utente: {choice}")  # Aggiungi una stampa di debug per verificare l'input dell'utente
    return choice


def printBoolD(frase:str) -> None:
    if boolD:
        print(frase)

def main():
    
    printBoolD("Caricamento delle squadre...")
    squadre = carica_squadre_da_csv(path_file_csv)
    if not squadre:
        print("Nessuna squadra caricata. Controlla il file CSV.")
        return
    printBoolD("Squadre caricate correttamente.")
    printBoolD("Inizio del ciclo principale...")
    choice = -1
    while choice != 3:
        choice = main_menu()
        print(f"Hai scelto l'opzione: {choice}")
        if choice == "1":
            visualizza_info_squadra(squadre)
        elif choice == "2":
            seleziona_squadra_e_visualizza_info(squadre)
        elif choice == "3":
            print("Arrivederci!")
            choice = 3
        else:
            print("Opzione non valida. Riprova.")



if __name__ == "__main__":
    main()


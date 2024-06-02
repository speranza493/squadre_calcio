from Classi.CategoriaSpesa import *
from Classi.Spesa import *
from Classi.Squadra import *
from Classi.StadioClass import *
from utils import *

def visualizza_info_squadra(squadra):
    print("Informazioni sulla squadra:")
    print(squadra)
    print()

def main_menu():
    print("MENU PRINCIPALE")
    print("1. Visualizza informazioni su tutte le squadre")
    print("2. Seleziona squadra e visualizza informazioni")
    print("3. Esci")
    choice = input("Scegli un'opzione: ")
    print(f"Scelta utente: {choice}")  # Aggiungi una stampa di debug per verificare l'input dell'utente
    return choice

def main():
    file_path = "Dati/squadre.csv"  # Percorso assoluto del file CSV
    print("Caricamento delle squadre...")
    squadre = carica_squadre_da_csv(file_path)
    if not squadre:
        print("Nessuna squadra caricata. Controlla il file CSV.")
        return
    print("Squadre caricate correttamente.")
    
    print("Inizio del ciclo principale...")
    while True:
        choice = main_menu()
        print(f"Hai scelto l'opzione: {choice}")
        if choice == "1":
            print("Informazioni su tutte le squadre:")
            for squadra in squadre:
                visualizza_info_squadra(squadra)
        elif choice == "2":
            nome_squadra = input("Inserisci il nome della squadra: ")
            squadra_selezionata = next((squadra for squadra in squadre if squadra.nome == nome_squadra), None)
            if squadra_selezionata:
                visualizza_info_squadra(squadra_selezionata)
                totale_spese = squadra_selezionata.calcola_totale_spese()
                print("Totale spese:", totale_spese, "euro")
            else:
                print("Squadra non trovata.")
        elif choice == "3":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")
        
        # Aggiungi una pausa per dare il tempo di leggere i messaggi di debug
        input("Premi Invio per continuare...")



if __name__ == "__main__":
    main()


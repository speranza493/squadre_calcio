import pandas as pd
import copy

class CategoriaSpesa:
    STIPENDI_GIOCATORI = "Stipendi Giocatori"
    ACQUISTI_GIOCATORI = "Acquisti Giocatori"
    STIPENDI_ALLENATORI = "Stipendi Allenatori"
    STRUTTURE_SPORTIVE = "Strutture Sportive"
    VIAGGI_ALLOGGI = "Viaggi e Alloggi"
    ALTRO = "Altro"

class Stadio:
    def __init__(self, nome, capacita, citta, indirizzo):
        self.nome = nome
        self.capacita = capacita
        self.citta = citta
        self.indirizzo = indirizzo
        
    def __init__(self,nome):
        self.nome = nome
        

    def __str__(self):
        return f"Stadio: {self.nome}\nCittà: {self.citta}\nIndirizzo: {self.indirizzo}\nCapacità: {self.capacita}\n"

class Spesa:
    def __init__(self, categoria, importo):
        self.categoria = categoria
        self.importo = importo

    def __str__(self):
        return f"Categoria: {self.categoria}\nImporto: {self.importo} euro\n"

class Squadra:
    def __init__(self, nome, stadio):
        self.nome = nome
        self.stadio = stadio
        self.spese = []

    def aggiungi_spesa(self, spesa):
        self.spese.append(spesa)

    def calcola_totale_spese(self):
        return sum(spesa.importo for spesa in self.spese)

    def __str__(self):
        return f"Squadra: {self.nome}\n{self.stadio}"

def carica_squadre_da_csv(file_path):
    print(f"Tentativo di caricare il file CSV dal percorso: {file_path}")
    try:
        df = pd.read_csv(file_path)
        print("File CSV caricato correttamente.")
        squadre = []
        for index, row in df.iterrows():
            print(row["nome_squadra"])
            stadio = Stadio(row["nome_squadra"])
            squadra = Squadra(row["Squadra"], stadio)
            squadre.append(copy.copy(squadra))
        print(f"{len(squadre)} squadre caricate.")
        return squadre
    except FileNotFoundError:
        print(f"Errore: il file '{file_path}' non è stato trovato.")
        return []
    except pd.errors.EmptyDataError:
        print("Errore: il file è vuoto.")
        return []
    except Exception as e:
        print(f"Errore durante il caricamento delle squadre: {e}")
        print(e)
        return []

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
    file_path = "squadre.csv"  # Percorso assoluto del file CSV
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


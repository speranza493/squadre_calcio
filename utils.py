import pandas as pd
from Classi.Squadra import *
from Classi.StadioClass import *
import copy


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
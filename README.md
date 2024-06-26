Autori: Marin Angela, Speranza Marco e Scarpa Falce Elisa 

# squadre_calcio

## Descrizione del problema e degli obiettivi del progetto
Il progetto “squadre_calcio” affronta la problematica di gestione delle spese per le squadre di calcio della serie A italia.
Le spese possono includere gli stipendi dei giocatori e allenatori, acquisti dei giocatori, costi delle strutture sportive, viaggi, alloggi e altre categorie di spesa. 
Questo progetto ha l'obiettivo di sviluppare un software che permetta di visualizzare e monitorare le spese delle squadre. Il sistema deve, quindi, essere in grado di raggruppare le spese per categoria e associarle alle squadre corrispondenti, fornendo una visione dettagliata delle finanze delle squadre prese in visione.

## Analisi dei requisiti 
Abbiamo sviluppato il progetto nell’ambiente Visual Studio Code e GitHub.
È necessario che la libreria “pandas” sia stata installata precedentemente per garantire il corretto funzionamento del progetto.
In questa cartella c’è un file CSV contenente il nome della squadra, il suo allenatore e lo stadio in cui i giocatori abitualmente si allenano.


## Implementazione del progetto
Abbiamo implementato il programma in 2 fasi, la prima deve permette di visualizzare solo le informazioni delle squadre. La seconda fase che permetta di vedere le informazioni delle spese in modo più specifico.

Nella prima fase abbiamo creato le classi Squadra, e SquadreRaggruppate. La prima classe definisce la struttura in cui i dati di input dovranno essere salvati. Successivamente nella classe “SquadreRaggruppate” leggo il file di input e inserisco tutte le informazioni nel formato “Squadra” della classe precedente per poi inserire tutte le informazioni in un insieme. Perché in un insieme? non mi serve avere le informazioni indicizzate e ordinate come nella lista e rispetto al dictionary non mi serve una chiave.

Successivamente abbiamo creato un menu, in cui mettere le impostazioni che l’utente potrà usare. Noi attualmente abbiamo pensato a 4 impostazioni. Di queste 2 le classi sopra elencate, sono state necessarie. E per le altre 2 dovrò creare altri file.

Nella seconda parte del progetto si è creata una classe “CategoriaSpesa” in cui si definisce tutte le categorizzazioni possibili per le spese effettuate dall’utente. Abbiamo pensato di velocizzare il recupero di informazioni delle squadre utilizzando un dizionario, essendo ogni nome di una squadra unico. Si è messa, quindi, come chiave il nome della squadra, e come valori di riferimento una lista con contenuti oggetti “Spesa”. 
Abbiamo messo una lista perchè così in futuro potrebbero anche essere ordinati in più modi, invece di prendere i dati dalla funzione random.

Alla fine del progetto ci saranno 4 funzioni disponibili per il programma:
1- leggere tutte le info delle squadre
2- leggere le info di una squadra specifica
3- leggere le info di tutte le spese di una squadra
4- leggere il totale delle spese dentro la lista di una squadra scelta

## Test del progetto

Abbiamo eseguito un test per verificare il corretto caricamento del CSV: il progetto legge correttamente il file e crea oggetti “Squadra” per ogni riga del CSV.
Successivamente abbiamo verificato che si generassero delle spese fittizie per ogni squadra e che queste vengano aggiunte correttamente, controllando che il totale per ciascuna squadra si aggiornasse.
Per testare il progetto abbiamo anche creato una squadra "fittizia" di nome “1”, in cui quando il programma ti chiede di inserire un nome inserisco quel numero, per velocizzare i tempi dello sviluppo.
In conclusione abbiamo verificato che le informazioni e le spese delle squadre venissero visualizzate in modo corretto all’utente. 

## Conclusioni e valutazione dei risultati

Il progetto ha raggiunto i risultati prefissati, offrendo una soluzione efficace per la gestione delle spese delle squadre di calcio della serie A italiana.
Il progetto consente di visualizzare e gestire le spese delle squadre in modo dettagliato, fornendo anche una visualizzazione dettagliata delle varie spese affrontate dalle squadre. 

## Possibili sviluppi futuri e miglioramenti

Le possibili implementazioni future potrebbero essere le seguenti:
*   Aggiungere grafici e statistiche delle spese delle squadre
*   Le spese non dovranno più essere randomizzate ma bisognerà prendere dati veri da un csv, come capita per le squadre di calcio
*   Possibilità di escludere certi anni dalle statistiche, oppure certe categorie.

## Bibliografia e fonti utilizzate
*   Documentazione di pandas: https://pandas.pydata.org/docs/
*   Github: https://github.com/speranza493/squadre_calcio
*   Documentazione serie A italiana: https://www.legaseriea.it/it/serie-a/allenatori 
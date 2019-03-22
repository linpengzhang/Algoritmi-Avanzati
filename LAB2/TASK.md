# Lab. 2 - La rete dei trasporti pubblici

Il dominio applicativo di questo laboratorio è quello delle reti di trasporto pubblico. Il problema che vi si chiede di affrontare è quello di fornire informazioni sugli orari dei trasporti agli utenti della rete: più precisamente, di trovare un collegamento da una stazione di partenza a una stazione di arrivo e consenta all'utente di arrivare a destinazione il prima possibile. 

Il laboratorio va svolto a gruppi di massimo tre persone. E' sufficiente che uno solo dei componenti sottometta i risultati, specificando nel testo della risposta i nomi dei componenti del gruppo.

La rete dei trasporti pubblici
In questo laboratorio la rete di trasporti pubblici da analizzare è la rete dei treni ed autobus del Lussemburgo proveniente da [European Data Portal](https://www.europeandataportal.eu/data/en/dataset/horaires-et-arrets-des-transport-publics) e che potete trovare nel file allegato. La rete è composta 515 linee di autobus e treni locali, regionali ed internazionali. Ogni linea è descritta in un file con estensione .LIN e comprende più corse che percorrono la linea ad orari diversi. Ogni corsa è descritta nel file .LIN come mostrato qui sotto:

```
*Z 01884 C82---                                             % 01884 C82---
*A BH 120904002 120904002 000066  00945  00945              % 01884 C82---
*A BH 120604001 120604001 000066  00950  00949              % 01884 C82---
*R 1 120603002 120903018 120603002  00942  00956            % 01884 C82---
*G CRB 120903018 120603002  00942  00956                    % 01884 C82---
*A VE 120903018 120603002 000066  00942  00956              % 01884 C82---
120903018 Wiltz, Gare                  00942                % 01884 C82---
120904002 Paradiso, Gare        00945  00945                % 01884 C82---
120604001 Merkholtz, Gare       00949  00950                % 01884 C82---
120603002 Kautenbach, Op der G  00956                       % 01884 C82---
```

Le righe che iniziano con un asterisco formano l'intestazione. La riga che inizia con *Z riporta l'identificativo univoco della corsa, composto da un numero di corda a 5 cifre e un ID testuale della linea (nell'esempio, corsa 01884 della linea C82). Le altre righe che iniziano con un asterisco contengono informazioni aggiuntive sulla corsa che si possono ignorare. Dopo l'intestazione sono riportate in sequenza le stazioni che compongono la corsa. Ogni riga riporta il codice identificativo della stazione, il suo nome, l'orario di arrivo e l'orario di partenza dalla stazione. Gli orari sono in formato hh:mm (ore e minuti), con uno zero iniziale per portare la dimensione a 5 cifre. Orari successivi alle 24:00 si riferiscono al giorno successivo. La corsa descritta nell'esempio parte dalla stazione di Wiltz alle ore 9:42 e arriva alla stazione Kautenbach alle 9:56. Il carattere % identifica i commenti. I file sono tabulati con spaziatura fissa.

Il dataset contiene altri due file: il file bahnof con i nomi completi delle stazioni ed il file bfkoor con le coordinate geografiche delle stazioni (longitudine e latitudine).

### Il problema da risolvere
Data una stazione di partenza A, un orario di partenza e una stazione di arrivo B, il problema da risolvere è quello di trovare un percorso che parta da A non prima dell'orario prestabilito e consenta all'utente di arrivare a B il prima possibile. La soluzione deve tener conto degli eventuali tempi di attesa nelle stazioni. Per semplificare il problema assumete che i trasferimenti all'interno di una stazione richiedano tempi trascurabili.

### Domanda 1
Modellate il problema da risolvere usando un grafo orientato e pesato. Descrivete l'approccio che avete usato per creare il grafo, indicando cosa rappresentano i vertici del grafo, cosa rappresentano gli archi e quali pesi e valori avete associato agli archi.

### Domanda 2
Risolvete il problema utilizzando uno degli algoritmi per il problema dei cammini minimi visti a lezione. Indicate quale algoritmo avete utilizzato e se e come è stato modificato per poter risolvere il problema.

### Domanda 3
Testate la vostra implementazione con i seguenti viaggi:

* Da 200415016 a 200405005, partenza non prima delle 09:30
* Da 300000032 a 400000122, partenza non prima delle 05:30
* Da 210602003 a 300000030, partenza non prima delle 06:30
* Da 200417051 a 140701016, partenza non prima delle 12:00
* Da 200417051 a 140701016, partenza non prima delle 23:55
* Altre tre combinazioni di viaggio scelte a piacere
Per ogni viaggio, fornite l'elenco delle corse che lo compongono, le stazioni di cambio con gli orari di partenza e l'orario di arrivo a destinazione.

Per esempio, il viaggio più breve da 500000079 (CdT Trier, Hauptbahnhof) a 300000044 (CdT Namur, Gare) con partenza alle ore 13:00 è il seguente:

```
Viaggio da 500000079 a 300000044
Orario di partenza: 13:00
Orario di arrivo: 17:18
13:46 : corsa 06171 CFLBUS da 500000079 a 200405036
14:47 : corsa 06311 CFLBUS da 200405036 a 300000003
15:31 : corsa 02138 C82--- da 300000003 a 300000044
```
Le coordinate geografiche delle stazioni contenute nel file bfkoor possono essere utilizzate per rappresentare la soluzione in forma grafica.


### Domanda 4
Commentate la qualità delle soluzioni trovate dalla vostra implementazione: rappresentano soluzioni di viaggio ragionevoli oppure no? In caso negativo, quali sono i motivi che portano la vostra implementazione a generare soluzioni di viaggio irragionevoli? Ci sono dei modi per evitare che lo faccia?

### Domanda 5
Allegate il codice sorgente completo della soluzione come un unico file di archivio (.zip, .tar.gz, ecc)
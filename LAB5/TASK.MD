# Lab. 5 - Clustering k-means parallelo

In questo laboratorio confronteremo l'algoritmo di clustering k-means seriale sviluppato per il laboratorio 4 con la sua versione parallela. In particolare, analizzeremo come variano i tempi di calcolo dei due algoritmi rispetto a quattro parametri:

* Numero di punti 
* Numero di cluster
* Numero di iterazioni 
* Granularità del parallelismo


### Dataset
I metodi di clustering verranno applicati ad un dataset comprende [città e paesi degli Stati Uniti](https://public.opendatasoft.com/explore/dataset/cities-and-towns-of-the-united-states/table/). Ogni voce nel set di dati corrisponde a una città o paese include informazioni sulla popolazione e sulle coordinate geografiche (latitudine e logitudine).

Il dataset completo include 38183 città e paesi, ed è allegato alla pagina in formato CSV. Ogni riga dei file corrisponde ad una città o paese ed è composta da cinque campi in quest'ordine: codice, nome, popolazione, latitudine e longitudine. 

### Algoritmi
Implementate la versione seriale e la versione parallela dell'algoritmo di clustering k-means. Usate le k città con popolazione più alta come centroidi iniziali per l'algoritmo. Per calcolare la distanza tra i punti usate lo stesso modo che avete usato nel Laboratorio 3 per calcolare la distanza tra i punti di tipo GEO.

### Domanda 1
Confrontate i tempi di calcolo dell'algoritmo seriale e dell'algoritmo parallelo per il clustering k-means, al variare del **numero di punti**. 

Usate le soglie di popolazione minima 250, 2.000, 5.000, 15.000, 50.000, e 100.000 per eliminare città e paesi con bassa popolazione e ottenere dataset più piccoli con meno punti. 

Misurate i tempi di calcolo dell'algoritmo seriale e di quello parallelo sul dataset complessivo con 38183 punti e su quelli ridotti. Per tutti i dataset, fissate il numero di cluster a 50 ed il numero di iterazioni a 100.

Dopo aver misurato i tempi, create un grafico che mostri la variazione dei tempi di calcolo dei due algoritmi al variare del numero di punti. La figura dovrebbe includere due curve disegnate, una per l'algoritmo seriale e una per l'algoritmo parallelo. L'asse orizzontale indica il numero di punti mentre l'asse verticale indica la il tempo di calcolo. 

Calcolate lo speedup ottenuto dall'algoritmo parallelo. Come varia rispetto al numero dei punti?

### Domanda 2
Confrontate i tempi di calcolo dell'algoritmo seriale e dell'algoritmo parallelo per il clustering k-means, al variare del **numero di cluster**. 

Usando il dataset complessivo con 38183 punti, misurate i tempi di calcolo dell'algoritmo seriale e di quello parallelo variando il numero di cluster da 10 a 100. Mantenete costante il numero di iterazioni a 100.

Dopo aver misurato i tempi, create un grafico che mostri la variazione dei tempi di calcolo dei due algoritmi al variare del numero di cluster. In questo caso l'asse orizzontale indica il numero di cluster mentre l'asse verticale indica la il tempo di calcolo.


Calcolate lo speedup ottenuto dall'algoritmo parallelo. Come varia rispetto al numero dei cluster?

### Domanda 3
Confrontate i tempi di calcolo dell'algoritmo seriale e dell'algoritmo parallelo per il clustering k-means, al variare del **numero di iterazioni**. 

Usando il dataset complessivo con 38183 punti, misurate i tempi di calcolo dell'algoritmo seriale e di quello parallelo variando il numero di iterazioni da 10 a 1000. Mantenete costate il numero di cluster a 50.

Dopo aver misurato i tempi, create un grafico che mostri la variazione dei tempi di calcolo dei due algoritmi al variare del numero di iterazioni. In questo caso l'asse orizzontale indica il numero di iterazioni mentre l'asse verticale indica la il tempo di calcolo.


Calcolate lo speedup ottenuto dall'algoritmo parallelo. Come varia rispetto al numero di iterazioni?

### Domanda 4
Per migliorare i tempi di calcolo di un algoritmo risulta spesso utile limitare il parallelismo, passando ad una procedura seriale quando la dimensione dell'input scende sotto una certa soglia. Per esempio, in un algoritmo divide-et-impera si può stabilire una soglia di cutoff al di sotto della quale si utilizza un algoritmo seriale iterativo, invece di dividere ulteriormente l'input e procedere in parallelo.

Usando il dataset complessivo con 38183 punti, misurate i tempi di calcolo dell'algoritmo di clustering k-means parallelo utilizzando diverse soglie di cutoff per controllare la granularità del parallelismo.

Dopo aver misurato i tempi, create un grafico che mostri la variazione dei tempi di calcolo al variare del cutoff. Quale valore di cutoff vi permette di ottenere le prestazioni migliori?

### Domanda 5
Specificare le caratteristiche hardware del computer dove sono stati eseguiti i test, in particolare processore e numero di core disponibili.

### Domanda 6
Allegate il codice completo della vostra soluzione come un unico file di archivio (.zip, .tar.gz, ecc.)
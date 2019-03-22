# Lab. 1 - Resilienza di una rete di comunicazione

In questo laboratorio analizzeremo la connettività di una rete di calcolatori sottoposta ad un attacco. In particolare, simuleremo attacchi che disabilitano un numero crescente di server della rete per comprometterne l'operatività. In termini computazionali, la rete sarà modellata con un grafo non orientato da cui verranno eliminati man mano dei nodi secondo un certo ordine. Misureremo la resilienza della rete come la dimensione della componente connessa più grande rimasta nel grafo dopo l'eliminazione dei nodi.

Il laboratorio va svolto a gruppi di massimo tre persone. E' sufficiente che uno solo dei componenti sottometta i risultati, specificando nel testo della risposta i nomi dei componenti del gruppo.

## Grafi da analizzare

In questo laboratorio analizzeremo la resilienza di tre tipi di grafi diversi:

* Una rete di calcolatori reale, rappresentata nel file di testo allegato. La rete è composta da  6474 nodi e 13233 archi non orientati. Il file contiene l'elenco degli archi del grafo e non corrisponde esattamente alle assunzioni fatte a lezione: in particolare, include anche un certo numero di cappi (archi da un nodo verso se stesso), che vanno quindi ignorati.

* Un grafo ER, generato con il processo casuale ER visto a lezione, modificato per generare grafi non orientati anziché grafi orientati.

* Un grafo UPA. A lezione abbiamo visto la procedura DPA per generare grafi orientati (la D in DPA sta per "directed"). In questo laboratorio modificheremo il codice per generare grafi non orientati, ottenendo una procedura che chiameremo UPA. E' importante notare che in questo caso il grado dei nodi che vengono aggiunti al grafo non è più zero, e quindi che la loro probabilità di essere estratti nelle iterazioni successive diventa più alta. Il codice modificato deve tener conto di questo fatto.

### Domanda 1

Iniziamo la nostra analisi esaminando la resilienza della rete di calcolatori rispetto ad un attacco che sceglie i server da disattivare in modo casuale, e confrontandola con quella di un grafo ER e un grafo UPA di dimensioni simili.

Come prima cosa determinate dei valori di n, p e m tali che la procedura ER e la procedura UPA generino un grafo con lo stesso numero di nodi ed un numero di archi simile a quello della rete reale. Come valore del parametro m per la procedura UPA potete usare il numero intero più vicino al grado medio diviso 2 dei vertici della rete reale.

Quindi, per ognuno dei tre grafi (rete reale, ER, UPA), simulate un attacco che disabiliti i nodi della rete uno alla volta seguendo un ordine casuale, fino alla disattivazione di tutti i nodi del grafo, e calcolate la resilienza del grafo dopo ogni rimozione di un nodo.

Dopo aver calcolato la resilienza dei tre grafi, mostrate il risultato in un grafico con scala lineare che combini le tre curve ottenute. Usate un grafico a punti oppure a linea per ognuna delle curve. L'asse orizzontale del grafico deve corrispondere al numero di nodi disattivati dall'attacco (che variano da 0 a n), mentre l'asse verticale alla dimensione della componente connessa più grande rimasta dopo aver rimosso un certo numero di nodi. Aggiungete una legenda al grafico che permetta di distinguere le tre curve e che specifici i valori di p e m utilizzati. Allegate il file con la figura nell'apposito spazio.

### Domanda 2.

Considerate quello che succede quando si rimuove una frazione significativa dei nodi del grafo usando l'attacco con ordine casuale. Diremo che un grafo è resiliente a questo tipo di attacco quando la dimensione della componente connessa più grande è superiore al 75% del numero dei nodi ancora attivi. 

Esaminate l'andamento delle tre curve del grafico ottenuto nella Domanda 1, e dite quali dei tre grafi sono resilienti dopo che l'attacco in ordine casuale ha rimosso il 20% dei nodi della rete.

### Domanda 3.


Consideriamo ora un attacco che sceglie i nodi da rimuovere sulla base della struttura del grafo. In particolare, una strategia di attacco che ad ogni passo disattiva un nodo tra quelli di grado massimo rimasti nella rete. 

Per ognuno dei tre grafi (rete reale, ER, UPA), simulate un attacco di questo tipo fino alla disattivazione di tutti i nodi del grafo, e calcolate la resilienza dopo ogni rimozione di un nodo.

Mostrate il risultato in un grafico che combini le tre curve come nella Domanda 1e allegate il file con la figura nell'apposito spazio.

### Domanda 4.

Considerate quello che succede quando si rimuove una frazione significativa dei nodi del grafo usando l'attacco che sceglie i nodi con grado massimo.  Esaminate l'andamento delle tre curve del grafico ottenuto nella Domanda 3, e dite quali dei tre grafi sono resilienti dopo che l'attacco ha rimosso il 20% dei nodi della rete.
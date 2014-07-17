ANTONINO AMATO - 475928

PROGETTO FINALE
Il progetto è organizzato come segue:

-	Un file index.html, che è il file principale;
-	La cartella scripts che contiene tutte le librerie e varie funzioni utilizzate. In particolare:
- CreaBump.js contiene la funzione con cui ho creato il quadro di ingresso;
- CreateObj.js contiene la funzione che permette di importare i modelli .obj esterni, e tutti i modelli degli arredi che ho importato;
- FunctionLamp.js contiene la funzione che crea tutti i lampadari;
- FunctionMuri.js è stato creato per la gestione di tutte le shape che formano i muri interni ed esterni;
- FunctionPorteFinestre.js permette di importare con un unico comando finestre, porte e, per motivi di semplicità, anche i “sostegni” per tv e panorama esterno;
- luci.js gestisce tutte le luci dei vari lampadari e viene anche inserito un pannello per spegnere e  accendere le luci delle singole stanze;
- 	La cartella models contiene i file .obj e .mtl di tutti i modelli importati;
-	textures contiene tutte le immagini utilizzate come textures;
-	In movies sono presenti i due filmati usati per le textures video.

Le tecniche utilizzate in questo progetto sono:
-	TEXTURES per la creazione di muri, porte, finestre, parquet, ambiente esterno;
-	VIDEO TEXTURES per tv e panorama;
-	GUI CONTROLS per i controlli delle luci e della tv;
-	TWEEN per l’animazione della porta tra la cucina e il salone;
-	OBJECT PICKING per aprire le porte e le finestre e spostare la macchina e le scarpe;

La camera in prima persona è stata realizzata tramite la libreria KeyboardState.js, passando, in index.html, il tipo di movimento associato a ciascun tasto.

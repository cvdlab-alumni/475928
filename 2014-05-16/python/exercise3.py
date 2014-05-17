from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, '/Library/Python/2.7/site-packages/lar-cc/lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *



DRAW = COMP([VIEW,STRUCT,MKPOLS])

# 		Funzione che, dati in ingresso il master e
#		una cella divisa in blocchi, permette di scegliere il blocco da eliminare,
#		restituendo il master privo del blocco scelto.

def total_function (master,blocks,intervals):

    #variabili
    V,CV = master
    x,y,z = blocks
    iX,iY,iZ = intervals

    #creazione porta scelta nella cella
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1)
    VIEW(hpc)
    toMerge = input()
    diagram= assemblyDiagramInit(blocks)(intervals)
    master = diagram2cell(diagram,master,toMerge)   

    #rimozione porta scelta
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1)
    VIEW(hpc)
    toRemove = []
    choice = input()
    while(choice != -1):
        toRemove.append(choice)
        choice = input()
    master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    
    return master
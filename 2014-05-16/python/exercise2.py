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
from splines import *
from architectural import *

	######## importo l'intero codice dell'esercizio 1 per evitare problemi con gli import ########

DRAW = COMP([VIEW,STRUCT,MKPOLS])

# blocco unico
master = assemblyDiagramInit([7,9,2])([[.1,3.5,.1,1.5,.1,4,.1],[.1,2,.1,3,.1,1.75,.1,1.25,.1],[.1,2]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

# rimozione blocchi per le varie stanze e muri inutili
toRemove = [91,109,111,93,57,21,59,97,61,25,63,101,65,29,31,103,105,69,51,33,90,92,110,108]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


# creazione finestra 1
toMerge = 11
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[.75,.75,.25],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [105]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione finestra 2
toMerge = 7
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[1.25,.75,1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [112]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#creazione finestra 3
toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[.75,.75,.5],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [119]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione finestra 4
toMerge = 60
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[.75,.75,.5],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [126]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione finestra 5
toMerge = 87
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[1.25,.75,1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [133]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#creazione finestra 6
toMerge = 90
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[1,.75,1.25],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [143]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione finestra 7
toMerge = 83
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,3])([[1,1.75,1.25],[.1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [147]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazionne finestra 8
toMerge = 27
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([2,1,3])([[1.5,2],[.1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [154]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione porta 1
toMerge = 45
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,2])([[.25,1,.25],[.1],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [156]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione finestra 9
toMerge = 16
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,3])([[1.25,1,1.25],[.1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [162]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione finestra 10
toMerge = 72
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,3])([[1.25,1.5,1.25],[.1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [169]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione porta 2
toMerge = 33
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[1.25,.75,1],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [174]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione porta 3
toMerge = 59
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[1.25,.75,1],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [178]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione porta 4
toMerge = 29
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[.75,.75,.5],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [182]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione porta 5
toMerge = 35
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[.5,.75,.5],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [186]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creazione porta 6
toMerge = 60
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[.5,.75,.5],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
# blocchi finali numerati
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [190]

# abitazione complessiva
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

#DRAW(master)

								######## INIZIO ESERCIZIO 2 ########

master = (STRUCT(MKPOLS(master)))

# affianco 2 appartamenti uguali
t_master = T([1])(9.4) (master)

# creo una palazzina di sei piani
floor = STRUCT([master,t_master])
palazzina = STRUCT([floor, T(3)(3)(floor), T(3)(6)(floor), T(3)(9)(floor), T(3)(12)(floor), T(3)(15)(floor)])
#VIEW(palazzina)

#scala esterna
s = T([1,2])([1,-.6])(STRUCT(MKPOLS(spiralStair(0.1,1.8,1,.3,3,10,36))))

# pianerottoli
p1_1 = CUBOID([2.7,4,0.1])
p1_2 = T([1,2])([2.7,3])(CUBOID([2,1,0.1]))
p1 = STRUCT([p1_1,p1_2])
p1 = T([1,2,3])([-.8,-3,3])(p1)

p2_1 = CUBOID([2.7,4,0.1])
p2_2 = T([1,2])([2.7,3])(CUBOID([2,1,0.1]))
p2 = STRUCT([p2_1,p2_2])
p2 = T([1,2,3])([-.8,-3,6])(p2)

p3_1 = CUBOID([2.7,4,0.1])
p3_2 = T([1,2])([2.7,3])(CUBOID([2,1,0.1]))
p3 = STRUCT([p3_1,p3_2])
p3 = T([1,2,3])([-.8,-3,9])(p3)

p4_1 = CUBOID([2.7,4,0.1])
p4_2 = T([1,2])([2.7,3])(CUBOID([2,1,0.1]))
p4 = STRUCT([p4_1,p4_2])
p4 = T([1,2,3])([-.8,-3,12])(p4)

p5_1 = CUBOID([2.7,4,0.1])
p5_2 = T([1,2])([2.7,2.35])(CUBOID([2,1.65,0.1]))
p5 = STRUCT([p5_1,p5_2])
p5 = T([1,2,3])([-.8,-3,15])(p5)

# struttura totale
stair = STRUCT([s, p1, p2, p3, p4, p5])

scala1 = T([1,2])([-13.9,3])(stair)
scala2 = T([1,2])([-4.5,3])(stair)
scala = R([1,2])(-PI)(STRUCT([scala1,scala2]))


# creo il giardino con Bezier
c1 = larBezier(S1)([[0,0,0],[10,0,0]])
c2 = larBezier(S1)([[0,6,0],[2.5,9,3],[5,9,-3],[7.5,9,3],[9,9,2]])
c3 = larBezier(S2)([[0,0,0],[-2,0,3],[0,8,3],[0,9,0]])
c4 = larBezier(S2)([[8,0,0],[10,5,3],[8,10,-2]])
dom = larDomain([10])
dom2D = larModelProduct([dom, dom])
out = larMap(larCoonsPatch([c1,c2,c3,c4]))(dom2D)

giardino = T([1,2,3])([-5,18,-4.2])(R([1,2])(300)((COLOR(GREEN)(STRUCT(MKPOLS(out))))))

# struttura completa
struttura = STRUCT([palazzina,giardino,scala])
VIEW(struttura)
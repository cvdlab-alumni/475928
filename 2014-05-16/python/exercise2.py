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
diagram = assemblyDiagramInit([1,3,3])([[.1],[.75,.75,.5],[1,1,.4]])
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
diagram = assemblyDiagramInit([1,3,3])([[.1],[.75,.75,.5],[1,1,.4]])
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
diagram = assemblyDiagramInit([3,1,3])([[1.25,1.5,1.25],[.1],[.01,1.75,.24]])
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
hpc1 = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc1)
toRemove = [190]
# abitazione complessiva
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

# creo il balcone
b = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.1,2,.1],[.1,1]])
V,CV = b
hpc2 = SKEL_1(STRUCT(MKPOLS(b)))
hpc2 = T([1])([5.2])(cellNumbering (b,hpc2)(range(len(CV)),RED,2))
#VIEW(hpc2)
# totale blocchi numerati
#VIEW (STRUCT([hpc1, hpc2]))
toRemove = [9,11]
b = b[0], [cell for k,cell in enumerate(b[1]) if not (k in toRemove)]
b = T([1])([5.2])(STRUCT(MKPOLS(b)))
#VIEW(b)
master = (STRUCT(MKPOLS(master)))
completo = STRUCT([master, b])

VIEW(completo)

								######## INIZIO ESERCIZIO 2 ########

# affianco 2 appartamenti uguali
t_master = T([1])(9.3) (completo)
tetto = CUBOID ([18.7,10,1])
base = CUBOID ([18.7,8.5,2])

# creo una palazzina di sei piani
floor = STRUCT([completo,t_master])
palazzina = STRUCT([base, T(3)(2)(floor), T(3)(4)(floor), T(3)(6)(floor), T(3)(8)(floor), T(3)(10)(floor), T(3)(12)(floor), T([2,3])([-1.5,14])(tetto)])
#VIEW(palazzina)

#scala esterna
s1 = R([1,2])(-40.444)(R([2,3])(PI)(T([2,3])([-1.85,-12.05])(STRUCT(MKPOLS(spiralStair(0.1,1.3,.2,.3,2.5,1.65,28))))))
s = STRUCT ([s1, T(3)(-2)(s1), T(3)(-4)(s1), T(3)(-6)(s1), T(3)(-8)(s1), T(3)(-10)(s1)])

# pianerottoli
#lato ringhiera
ringh = assemblyDiagramInit([1,9,2])([[.1],[.1,.2,.1,.2,.1,.2,.1,.2,.1],[1,.1]])
V,CV = ringh
hpc = SKEL_1(STRUCT(MKPOLS(ringh)))
hpc = cellNumbering (ringh,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
# rimozione blocchi ringhiera
toRemove = [2,6,10,14]
ringh = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
ringh = STRUCT(MKPOLS(ringh))

p1 = STRUCT([T([1,2,3])([-.7,-3,2])(CUBOID([1.4,1.3,0.1])), T([1,2,3])([-.7,-3,2])(ringh)])
p2 = STRUCT([T([1,2,3])([-.7,-3,4])(CUBOID([1.4,1.3,0.1])), T([1,2,3])([-.7,-3,4])(ringh)])
p3 = STRUCT([T([1,2,3])([-.7,-3,6])(CUBOID([1.4,1.3,0.1])), T([1,2,3])([-.7,-3,6])(ringh)])
p4 = STRUCT([T([1,2,3])([-.7,-3,8])(CUBOID([1.4,1.3,0.1])), T([1,2,3])([-.7,-3,8])(ringh)])
p5 = STRUCT([T([1,2,3])([-.7,-3,10])(CUBOID([1.4,1.3,0.1])), T([1,2,3])([-.7,-3,10])(ringh)])
p6 = STRUCT([T([1,2,3])([-.7,-3,12])(CUBOID([1.4,1.3,0.1])), T([1,2,3])([.6,-3,12])(ringh), T([1,2,3])([-.7,-3,12])(ringh)])

# struttura totale
stair = STRUCT([s, p1, p2, p3, p4, p5, p6])

scala1 = T([1,2])([-13.9,3])(stair)
scala2 = T([1,2])([-4.5,3])(stair)
scala = R([1,2])(-PI)(STRUCT([scala1,scala2]))

# creo il giardino: una parte come semplice CUBOID, per far poggiare il palazzo, altre 2 parti con Bezier
c1 = larBezier(S1)([[0,0,0],[6,0,0]])
c2 = larBezier(S1)([[0,6,0],[1.5,6,3],[5,6,-3],[7.5,6,3],[6,6,2]])
c3 = larBezier(S2)([[0,0,0],[0,0,3],[0,8,3],[0,9,0]])
c4 = larBezier(S2)([[8,0,0],[7,5,3],[8,8,-2]])
dom = larDomain([6])
dom2D = larModelProduct([dom, dom])
out = larMap(larCoonsPatch([c1,c2,c3,c4]))(dom2D)
giardino1 = T([1,2,3])([-1,-2,-1])(COLOR(GREEN)(CUBOID([20.7,12,.5])))
giardino2 = T([1,2,3])([13,14,-4.5])(R([1,2])(300)((COLOR(GREEN)(STRUCT(MKPOLS(out))))))
giardino3 = T([1,2,3])([-13,14,-5])(R([1,2])(300)((COLOR(GREEN)(STRUCT(MKPOLS(out))))))
giardino = STRUCT([giardino1, giardino2, giardino3])

# struttura completa
struttura = STRUCT([palazzina,giardino,scala])
VIEW(struttura)
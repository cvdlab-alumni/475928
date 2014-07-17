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

DRAW = COMP([VIEW,STRUCT,MKPOLS])

def objExporter((V,FV), filePath):
    out_file = open(filePath,"w")
    out_file.write("# List of Vertices:\n")
    for v in V:
        out_file.write("v")
        for c in v:
            out_file.write(" " + str(c))
        out_file.write("\n")
    out_file.write("# Face Definitions:\n")
    for f in FV:
        out_file.write("f")
        for v in f:
            out_file.write(" " + str(v+1))
        out_file.write("\n")
    out_file.close()

# blocco unico
master = assemblyDiagramInit([7,9,2])([[.1,3.5,.1,1.5,.1,4,.1],[.1,2,.1,3,.1,1.75,.1,1.25,.1],[.1,2]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
# VIEW(hpc)

# creazione finestra 1
toMerge = 19
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,3])([[1,1.5,1],[.1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

#creazione finestra 2
toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[.75,.75,.5],[1,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazione finestra 3
toMerge = 6
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[1.25,.75,1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# # creazione finestra 4
toMerge = 9
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[.5,.75,.5],[1,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazionne finestra 5
toMerge = 31
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([2,1,3])([[1.5,2],[.1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazione finestra 6
toMerge = 102
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,3])([[1,2,1],[.1],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazione finestra 7
toMerge = 113
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[.25,.75,.25],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#creazione finestra 8
toMerge = 109
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[1.125,.75,1.125],[.6,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

# creazione porta 1
toMerge = 90
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,3])([[1.25,1.5,1.25],[.1],[.01,1.75,.24]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazione porta 2
toMerge = 50
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,2])([[.25,1,.25],[.1],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazione porta 3
toMerge = 34
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[.5,1,.5],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

# creazione porta 4
toMerge = 37
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[1,1,1],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

# creazione porta 5
toMerge = 40
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[.375,1,.375],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

# creazione porta 6
toMerge = 74
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[.375,1,.375],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

# creazione porta 7
toMerge = 70
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,2])([[.1],[1,1,1],[1.75,.25]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazione finestra 9
toMerge = 66
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.1],[.625,.75,.625],[1,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)

# creazione finestra 10
toMerge = 79
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,3])([[1.25,1.5,1.25],[.1],[1,1,.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

# #rimozione blocchi per le varie stanze e muri inutili
emptyChain = [17,21,25,27,29,43,48,50,52,54,56,60,80,83,87,89,91,113,122,131,140,149,155,164,173,182,189,195,201,207,213,219,236]


def extractFacets(master, emptyChain=[]):
    solidCV = [cell for k,cell in enumerate(master[1]) if not (k in emptyChain)]
    exteriorCV =  [cell for k,cell in enumerate(master[1]) if k in emptyChain]
    exteriorCV += exteriorCells(master)
    CV = solidCV + exteriorCV
    V = master[0]
    FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
    BF = boundaryCells(solidCV,FV)
    boundaryFaces = [FV[face] for face in BF]
    B_Rep = V,boundaryFaces
    return B_Rep

master_factes = extractFacets(master, emptyChain)
master_factes_tria = quads2tria(master_factes)

# # solidCV = [cell for k,cell in enumerate(master[1]) if not (k in emptyChain)]
# # DRAW((master[0],solidCV))
# # exteriorCV =  [cell for k,cell in enumerate(master[1]) if k in emptyChain]
# # exteriorCV += exteriorCells(master)
# # CV = solidCV + exteriorCV
# # V = master[0]
# # FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
# VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))

# # BF = boundaryCells(solidCV,FV)
# # boundaryFaces = [FV[face] for face in BF]
# # B_Rep = V,boundaryFaces
# # # VIEW(EXPLODE(1.1,1.1,1.1)(MKPOLS(B_Rep)))
# # # VIEW(STRUCT(MKPOLS(B_Rep)))

# # verts, triangles = quads2tria(B_Rep)
# # B_Rep = V,boundaryFaces
# # VIEW(EXPLODE(1.1,1.1,1.1)(MKPOLS((verts, triangles))))
# VIEW(STRUCT(MKPOLS((verts, triangles))))

objExporter(master_factes_tria,"/appartamento.obj")
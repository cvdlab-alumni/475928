from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, '/Library/Python/2.7/site-packages/lar-cc/lib/py/')
from larcc import *
from boolean import *
from sysml import *



		# All'interno della funzione da ottimizzare elimino i vertici doppi
		# usando la funzione vertexSieve della libreria Boolean


def diagram2cell(diagram,master,cell):
	mat = diagram2cellMatrix(diagram)(master,cell)
	diagram =larApply(mat)(diagram)

	#Eliminazione duplicati
	V1,CV1 = master
	CV1 = [c for k,c in enumerate(CV1) if k != cell]
	V,CV1,CV2,n12 = vertexSieve((V1,CV1),diagram)
	CV = CV1+CV2
	master = V, CV

	return master
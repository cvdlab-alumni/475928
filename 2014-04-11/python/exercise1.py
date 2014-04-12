from pyplasm import *

#scalini
x_scalino1=QUOTE([47.6]*10)
y_scalino1=QUOTE([24.8]*10)
scalino1=COLOR(RED)(T([1,2])([-5*10,-4*10])(INSR(PROD)([x_scalino1,y_scalino1,QUOTE([10])])))

x_scalino2=QUOTE([45.6]*10)
y_scalino2=QUOTE([22.8]*10)
scalino2=COLOR(RED)(T([1,2,3])([-4*10,-3*10,30])(INSR(PROD)([x_scalino2,y_scalino2,QUOTE([10])])))

x_scalino3=QUOTE([43.6]*10)
y_scalino3=QUOTE([20.8]*10)
scalino3=COLOR(RED)(T([1,2,3])([-3*10,-2*10,60])(INSR(PROD)([x_scalino3,y_scalino3,QUOTE([10])])))

x_scalino4=QUOTE([41.6]*10)
y_scalino4=QUOTE([18.8]*10)
scalino4=COLOR(RED)(T([1,2,3])([-2*10,-1*10,90])(INSR(PROD)([x_scalino4,y_scalino4,QUOTE([10])])))

base3D=STRUCT([scalino1,scalino2,scalino3,scalino4])
VIEW(base3D)

#colonna
c_sup=T(3)(70)(CIRCLE(5)([20,32]))
c_inf=CIRCLE(8)([20,32])
colonna=COLOR([1,0.65,0])(JOIN([c_sup,c_inf]))

#capitello
x_cap=QUOTE([20])
y_cap=QUOTE([20])
capitello=COLOR([1,0.65,0])(T([1,2])([-10,-10])(INSR(PROD)([x_cap,y_cap,QUOTE([-70,10])])))

colonna_completa=STRUCT([capitello,colonna])

#colonne esterne
pair_y=[T(2)(30),colonna_completa]
fila_corta1=T([1,2,3])([20,10,30])(STRUCT(NN(5)(pair_y)))

pair_x=[T(1)(30),colonna_completa]
fila_lunga1=T([1,2,3])([-10,10,30])(STRUCT(NN(13)(pair_x)))

pair_y=[T(2)(30),colonna_completa]
fila_corta2=T([1,2,3])([380,10,30])(STRUCT(NN(4)(pair_y)))

pair_x=[T(1)(30),colonna_completa]
fila_lunga2=T([1,2,3])([18,160,30])(STRUCT(NN(12)(pair_x)))

colonne_estrerne=STRUCT([fila_corta1,fila_corta2,fila_lunga1,fila_lunga2])

#colonne_interne
pair_y=[T(2)(30),colonna_completa]
col_int1=T([1,2,3])([80,40,10])(STRUCT(NN(2)(pair_y)))
col_int2=T([1,2,3])([330,40,10])(STRUCT(NN(2)(pair_y)))
colonne_interne=S(3)(1)(STRUCT([col_int1,col_int2]))

colonne3D=T(3)(120)(STRUCT([colonne_estrerne,colonne_interne]))

#muro_lungo 
x_muro=QUOTE([31*10])
y_muro=QUOTE([.4*10,-7.6*10,.4*10])
muro_lungo=T([1,2,3])([3.8*10,4*10,10])(INSR(PROD)([x_muro,y_muro,QUOTE([50])]))

#muro_corto
x_muro=QUOTE([.4*10,-17.4*10,.4*10])
y_muro=QUOTE([3.2*10,-1.6*10,3.2*10])
muro_corto=T([1,2,3])([10.6*10,4*10,10])(INSR(PROD)([x_muro,y_muro,QUOTE([50])]))

muro3D=T(3)(120)(COLOR([1,0.65,0])(STRUCT([muro_lungo,muro_corto])))
intermedio3D=STRUCT([colonne3D,muro3D])

VIEW(intermedio3D)


#muretto_superiore
x_muretto_o=QUOTE([42]*9)
z_muretto_o=QUOTE([10])
muretto_o=COLOR(YELLOW)(T([1,3])([5,200])(INSR(PROD)([x_muretto_o,QUOTE([10]),z_muretto_o])))

y_muretto_n=QUOTE([18.9]*9)
z_muretto_n=QUOTE([10])
muretto_n=COLOR(YELLOW)(T([3])([200])(INSR(PROD)([QUOTE([10]),y_muretto_n,z_muretto_n])))

x_muretto_e=QUOTE([42]*9)
z_muretto_e=QUOTE([10])
muretto_e=COLOR(YELLOW)(T([1,2,3])([5,160,200])(INSR(PROD)([x_muretto_e,QUOTE([10]),z_muretto_e])))

y_muretto_s=QUOTE([18.9]*9)
z_muretto_s=QUOTE([10])
muretto_s=COLOR(YELLOW)(T([1,3])([380,200])(INSR(PROD)([QUOTE([10]),y_muretto_s,z_muretto_s])))

muro_sup3D=T(3)(70)(STRUCT([muretto_o,muretto_n,muretto_e,muretto_s]))

#parte alta
p_punti=[[0,19*9,0],[0,-20,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta1=T(3)(220)(MKPOL([p_punti,p_celle,None]))
p_alta2=T([1,3])([6,220])(MKPOL([p_punti,p_celle,None]))
alto1=T(2)(10)(JOIN([p_alta1,p_alta2]))

p_punti=[[0,19*9,0],[0,-20,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta1=T(3)(220)(MKPOL([p_punti,p_celle,None]))
p_alta2=T([1,3])([6,220])(MKPOL([p_punti,p_celle,None]))
alto2=T([1,2])([384,10])(JOIN([p_alta1,p_alta2]))

p_alta3D=COLOR(YELLOW)(T(3)(80)(STRUCT([alto1,alto2])))

copertura3D=STRUCT([muro_sup3D,p_alta3D])

VIEW(copertura3D)

#//////////

#scalini
x_scalino1=QUOTE([47.6]*10)
y_scalino1=QUOTE([24.8]*10)
scalino1=COLOR(RED)(T([1,2])([-5*10,-4*10])(INSR(PROD)([x_scalino1,y_scalino1,QUOTE([10])])))

x_scalino2=QUOTE([45.6]*10)
y_scalino2=QUOTE([22.8]*10)
scalino2=COLOR(RED)(T([1,2,3])([-4*10,-3*10,10])(INSR(PROD)([x_scalino2,y_scalino2,QUOTE([10])])))

x_scalino3=QUOTE([43.6]*10)
y_scalino3=QUOTE([20.8]*10)
scalino3=COLOR(RED)(T([1,2,3])([-3*10,-2*10,20])(INSR(PROD)([x_scalino3,y_scalino3,QUOTE([10])])))

x_scalino4=QUOTE([41.6]*10)
y_scalino4=QUOTE([18.8]*10)
scalino4=COLOR(RED)(T([1,2,3])([-2*10,-1*10,30])(INSR(PROD)([x_scalino4,y_scalino4,QUOTE([10])])))

base=STRUCT([scalino1,scalino2,scalino3,scalino4])

#colonna
c_sup=T(3)(70)(CIRCLE(5)([20,32]))
c_inf=CIRCLE(8)([20,32])
colonna=COLOR([1,0.65,0])(JOIN([c_sup,c_inf]))

#capitello
x_cap=QUOTE([20])
y_cap=QUOTE([20])
capitello=COLOR([1,0.65,0])(T([1,2])([-10,-10])(INSR(PROD)([x_cap,y_cap,QUOTE([-70,10])])))

colonna_completa=STRUCT([capitello,colonna])

#colonne esterne
pair_y=[T(2)(30),colonna_completa]
fila_corta1=T([1,2,3])([20,10,40])(STRUCT(NN(5)(pair_y)))

pair_x=[T(1)(30),colonna_completa]
fila_lunga1=T([1,2,3])([-10,10,40])(STRUCT(NN(13)(pair_x)))

pair_y=[T(2)(30),colonna_completa]
fila_corta2=T([1,2,3])([380,10,40])(STRUCT(NN(4)(pair_y)))

pair_x=[T(1)(30),colonna_completa]
fila_lunga2=T([1,2,3])([18,160,40])(STRUCT(NN(12)(pair_x)))

colonne_estrerne=STRUCT([fila_corta1,fila_corta2,fila_lunga1,fila_lunga2])

#colonne_interne
pair_y=[T(2)(30),colonna_completa]
col_int1=T([1,2,3])([80,40,20])(STRUCT(NN(2)(pair_y)))
col_int2=T([1,2,3])([330,40,20])(STRUCT(NN(2)(pair_y)))
colonne_interne=S(3)(1)(STRUCT([col_int1,col_int2]))

colonne=STRUCT([colonne_estrerne,colonne_interne])

#muro_lungo 
x_muro=QUOTE([31*10])
y_muro=QUOTE([.4*10,-7.6*10,.4*10])
muro_lungo=T([1,2,3])([3.8*10,4*10,40])(INSR(PROD)([x_muro,y_muro,QUOTE([50])]))

#muro_corto
x_muro=QUOTE([.4*10,-17.4*10,.4*10])
y_muro=QUOTE([3.2*10,-1.6*10,3.2*10])
muro_corto=T([1,2,3])([10.6*10,4*10,40])(INSR(PROD)([x_muro,y_muro,QUOTE([50])]))

muro=T(2)(1.5)(COLOR([1,0.65,0])(STRUCT([muro_lungo,muro_corto])))

#muretto_superiore
x_muretto_o=QUOTE([42]*9)
z_muretto_o=QUOTE([10])
muretto_o=COLOR(YELLOW)(T([1,3])([5,120])(INSR(PROD)([x_muretto_o,QUOTE([10]),z_muretto_o])))

y_muretto_n=QUOTE([18.9]*9)
z_muretto_n=QUOTE([10])
muretto_n=COLOR(YELLOW)(T([3])([120])(INSR(PROD)([QUOTE([10]),y_muretto_n,z_muretto_n])))

x_muretto_e=QUOTE([42]*9)
z_muretto_e=QUOTE([10])
muretto_e=COLOR(YELLOW)(T([1,2,3])([5,160,120])(INSR(PROD)([x_muretto_e,QUOTE([10]),z_muretto_e])))

y_muretto_s=QUOTE([18.9]*9)
z_muretto_s=QUOTE([10])
muretto_s=COLOR(YELLOW)(T([1,3])([380,120])(INSR(PROD)([QUOTE([10]),y_muretto_s,z_muretto_s])))

muro_sup=STRUCT([muretto_o,muretto_n,muretto_e,muretto_s])

#parte alta
p_punti=[[0,19*9,0],[0,-20,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta1=T(3)(130)(MKPOL([p_punti,p_celle,None]))
p_alta2=T([1,3])([6,130])(MKPOL([p_punti,p_celle,None]))
alto1=T(2)(10)(JOIN([p_alta1,p_alta2]))

p_punti=[[0,19*9,0],[0,-20,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta1=T(3)(130)(MKPOL([p_punti,p_celle,None]))
p_alta2=T([1,3])([6,130])(MKPOL([p_punti,p_celle,None]))
alto2=T([1,2])([384,10])(JOIN([p_alta1,p_alta2]))
p_alta=COLOR(YELLOW)(STRUCT([alto1,alto2]))

copertura=STRUCT([muro_sup,p_alta])

elementi3D=STRUCT([base3D,colonne3D,muro3D,copertura3D])
completo=STRUCT([base,colonne,muro,copertura])

VIEW(elementi3D)
VIEW(completo)
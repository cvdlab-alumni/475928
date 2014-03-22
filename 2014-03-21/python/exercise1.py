from pyplasm import *

#scalino1
x_scalino1=QUOTE([47.6]*10)
y_scalino1=QUOTE([24.8]*10)
scalino1=COLOR(RED)(T([1,2])([-5*10,-4*10])(INSR(PROD)([x_scalino1,y_scalino1])))
VIEW(scalino1)

#scalino2
x_scalino2=QUOTE([45.6]*10)
y_scalino2=QUOTE([22.8]*10)
scalino2=COLOR(BLUE)(T([1,2,3])([-4*10,-3*10,10])(INSR(PROD)([x_scalino2,y_scalino2])))
VIEW(scalino2)

#scalino3
x_scalino3=QUOTE([43.6]*10)
y_scalino3=QUOTE([20.8]*10)
scalino3=COLOR(YELLOW)(T([1,2,3])([-3*10,-2*10,20])(INSR(PROD)([x_scalino3,y_scalino3])))
VIEW(scalino3)

#scalino4
x_scalino4=QUOTE([41.6]*10)
y_scalino4=QUOTE([18.8]*10)
scalino4=COLOR(GREEN)(T([1,2,3])([-2*10,-1*10,30])(INSR(PROD)([x_scalino4,y_scalino4])))
VIEW(scalino4)

#interno
#muro_lungo
x_muro=QUOTE([31]*10)
y_muro=QUOTE([.4*10,-7.6*10,.4*10])
muro_lungo=T([1,2,3])([3.8*10,4*10,50])(PROD([x_muro,y_muro]))

#muro_corto
x_muro=QUOTE([.4*10,-17.4*10,.4*10])
y_muro=QUOTE([3.2*10,-1.6*10,3.2*10])
muro_corto=T([1,2,3])([10.6*10,4*10,50])(PROD([x_muro,y_muro]))
muro=COLOR(MAGENTA)(STRUCT([muro_lungo,muro_corto]))
VIEW(muro)

#colonneesterne
x_cap=QUOTE([20])
y_cap=QUOTE([20])
capitello=PROD([x_cap,y_cap])

pair_y=[T(2)(30),capitello]
fila_corta1=(STRUCT(NN(5)(pair_y)))

pair_x=[T(1)(30),capitello]
fila_lunga1=T(1)(-30)(STRUCT(NN(13)(pair_x)))
insieme_cap1=T([1,2,3])([2.1,1.5,70])(STRUCT([fila_corta1,fila_lunga1]))
#VIEW(insieme_cap1)

pair_y=[T(2)(30),capitello]
fila_corta2=T(1)(360)(STRUCT(NN(5)(pair_y)))

pair_x=[T(1)(30),capitello]
fila_lunga2=T(2)(150)(STRUCT(NN(12)(pair_x)))
insieme_cap2=T([1,2,3])([2.1,1.5,70])(STRUCT([fila_corta2,fila_lunga2]))
#VIEW(insieme_cap2)

insieme_cap=STRUCT([insieme_cap1,insieme_cap2])
#VIEW(insieme_cap)

#colonneinterne
pair_y=[T(2)(30),capitello]
colonneinterne1=T([1,2])([55,30])(STRUCT(NN(2)(pair_y)))
colonneinterne2=T([1,2])([300,30])(STRUCT(NN(2)(pair_y)))
colonneinterne=T(3)(50)(STRUCT([colonneinterne1,colonneinterne2]))
#VIEW(colonneinterne)

colonne=COLOR([1,0.65,0])(STRUCT([insieme_cap,colonneinterne]))
VIEW(colonne)

building=STRUCT([scalino1,scalino2,scalino3,scalino4,muro,colonne])

VIEW(building)
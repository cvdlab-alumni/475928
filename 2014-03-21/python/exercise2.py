from pyplasm import *

#west

#scalino1
x_scalino1=QUOTE([47.6]*10)
z_scalino1=QUOTE([10])
scalino1=COLOR(RED)(T([1])([-5*10])(INSR(PROD)([x_scalino1,QUOTE([0]),z_scalino1])))
#VIEW(scalino1)

#scalino2
x_scalino2=QUOTE([45.6]*10)
z_scalino2=QUOTE([10])
scalino2=COLOR(BLUE)(T([1,3])([-4*10,10])(INSR(PROD)([x_scalino2,QUOTE([0]),z_scalino2])))
#VIEW(scalino2)

#scalino3
x_scalino3=QUOTE([43.6]*10)
z_scalino3=QUOTE([10])
scalino3=COLOR(YELLOW)(T([1,3])([-3*10,20])(INSR(PROD)([x_scalino3,QUOTE([0]),z_scalino3])))
#VIEW(scalino3)

#scalino4
x_scalino4=QUOTE([41.6]*10)
z_scalino4=QUOTE([10])
scalino4=COLOR(GREEN)(T([1,3])([-2*10,30])(INSR(PROD)([x_scalino4,QUOTE([0]),z_scalino4])))
#VIEW(scalino4)

scalini=STRUCT([scalino1,scalino2,scalino3,scalino4])
#VIEW(scalini)

#colonna
punti=[[6,0,0],[11,0,70],[26,0,0],[21,0,70],[6,0,70],[6,0,80],[26,0,70],[26,0,80]]
celle=[[1,2,3,4],[5,6,7,8]]
colonna=MKPOL([punti,celle,None])

pair_x=[T(1)(30),colonna]
colonne=COLOR([1,0.65,0])(T([1,3])([-4*10,40])(STRUCT(NN(13)(pair_x))))
#VIEW(colonne)

#muretto_superiore
x_muretto=QUOTE([43.5]*9)
z_muretto=QUOTE([10])
muretto=COLOR(PURPLE)(T([1,3])([-1*10,120])(INSR(PROD)([x_muretto,QUOTE([0]),z_muretto])))
#VIEW(muretto)

west=T(1)(45)(STRUCT([scalini,colonne,muretto]))

#east

#scalino1
x_scalino1=QUOTE([47.6]*10)
z_scalino1=QUOTE([10])
scalino1=COLOR(RED)(T([1])([-5*10])(INSR(PROD)([x_scalino1,QUOTE([0]),z_scalino1])))
#VIEW(scalino1)

#scalino2
x_scalino2=QUOTE([45.6]*10)
z_scalino2=QUOTE([10])
scalino2=COLOR(BLUE)(T([1,3])([-4*10,10])(INSR(PROD)([x_scalino2,QUOTE([0]),z_scalino2])))
#VIEW(scalino2)

#scalino3
x_scalino3=QUOTE([43.6]*10)
z_scalino3=QUOTE([10])
scalino3=COLOR(YELLOW)(T([1,3])([-3*10,20])(INSR(PROD)([x_scalino3,QUOTE([0]),z_scalino3])))
#VIEW(scalino3)

#scalino4
x_scalino4=QUOTE([41.6]*10)
z_scalino4=QUOTE([10])
scalino4=COLOR(GREEN)(T([1,3])([-2*10,30])(INSR(PROD)([x_scalino4,QUOTE([0]),z_scalino4])))
#VIEW(scalino4)

scalini=STRUCT([scalino1,scalino2,scalino3,scalino4])
#VIEW(scalini)

#colonna
punti=[[6,0,0],[11,0,70],[26,0,0],[21,0,70],[6,0,70],[6,0,80],[26,0,70],[26,0,80]]
celle=[[1,2,3,4],[5,6,7,8]]
colonna=MKPOL([punti,celle,None])

pair_x=[T(1)(30),colonna]
colonne=COLOR([1,0.65,0])(T([1,3])([-3*10,40])(STRUCT(NN(13)(pair_x))))
#VIEW(colonne)

#muretto_superiore
x_muretto=QUOTE([43.5]*9)
z_muretto=QUOTE([10])
muretto=COLOR(PURPLE)(T([3])([120])(INSR(PROD)([x_muretto,QUOTE([0]),z_muretto])))
#VIEW(muretto)

east=T([1,2])([45,28*9])(STRUCT([scalini,colonne,muretto]))


#north

#scalino1
y_scalino1=QUOTE([24.8]*10)
z_scalino1=QUOTE([10])
scalino1=COLOR(RED)(T([2])([-5*10])(INSR(PROD)([QUOTE([0]),y_scalino1,z_scalino1])))
#VIEW(scalino1)

#scalino2
y_scalino2=QUOTE([22.8]*10)
z_scalino2=QUOTE([10])
scalino2=COLOR(BLUE)(T([2,3])([-4*10,10])(INSR(PROD)([QUOTE([0]),y_scalino2,z_scalino2])))
#VIEW(scalino2)

#scalino3
y_scalino3=QUOTE([20.8]*10)
z_scalino3=QUOTE([10])
scalino3=COLOR(YELLOW)(T([2,3])([-3*10,20])(INSR(PROD)([QUOTE([0]),y_scalino3,z_scalino3])))
#VIEW(scalino3)

#scalino4
y_scalino4=QUOTE([18.8]*10)
z_scalino4=QUOTE([10])
scalino4=COLOR(GREEN)(T([2,3])([-2*10,30])(INSR(PROD)([QUOTE([0]),y_scalino4,z_scalino4])))
#VIEW(scalino4)

scalini=STRUCT([scalino1,scalino2,scalino3,scalino4])
#VIEW(scalini)

#colonna
punti=[[0,6,0],[0,11,70],[0,26,0],[0,21,70],[0,6,70],[0,6,80],[0,26,70],[0,26,80]]
celle=[[1,2,3,4],[5,6,7,8]]
colonna=MKPOL([punti,celle,None])

pair_y=[T(2)(30),colonna]
colonne=COLOR([1,0.65,0])(T([2,3])([-4.5*10,40])(STRUCT(NN(6)(pair_y))))
#VIEW(colonne)

#muretto_superiore
y_muretto=QUOTE([20]*9)
z_muretto=QUOTE([10])
muretto=COLOR(PURPLE)(T([2,3])([-14,120])(INSR(PROD)([QUOTE([0]),y_muretto,z_muretto])))
#VIEW(muretto)

#parte alta
p_punti=[[0,-20,0],[0,19*9,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta=T(3)(130)(MKPOL([p_punti,p_celle,None]))

north=T(2)(50)(STRUCT([scalini,colonne,muretto,p_alta]))

#south

#scalino1
y_scalino1=QUOTE([24.8]*10)
z_scalino1=QUOTE([10])
scalino1=COLOR(RED)(T([2])([-5*10])(INSR(PROD)([QUOTE([0]),y_scalino1,z_scalino1])))
#VIEW(scalino1)

#scalino2
y_scalino2=QUOTE([22.8]*10)
z_scalino2=QUOTE([10])
scalino2=COLOR(BLUE)(T([2,3])([-4*10,10])(INSR(PROD)([QUOTE([0]),y_scalino2,z_scalino2])))
#VIEW(scalino2)

#scalino3
y_scalino3=QUOTE([20.8]*10)
z_scalino3=QUOTE([10])
scalino3=COLOR(YELLOW)(T([2,3])([-3*10,20])(INSR(PROD)([QUOTE([0]),y_scalino3,z_scalino3])))
#VIEW(scalino3)

#scalino4
y_scalino4=QUOTE([18.8]*10)
z_scalino4=QUOTE([10])
scalino4=COLOR(GREEN)(T([2,3])([-2*10,30])(INSR(PROD)([QUOTE([0]),y_scalino4,z_scalino4])))
#VIEW(scalino4)

scalini=STRUCT([scalino1,scalino2,scalino3,scalino4])
#VIEW(scalini)

#colonna
punti=[[0,6,0],[0,11,70],[0,26,0],[0,21,70],[0,6,70],[0,6,80],[0,26,70],[0,26,80]]
celle=[[1,2,3,4],[5,6,7,8]]
colonna=MKPOL([punti,celle,None])

pair_y=[T(2)(30),colonna]
colonne=COLOR([1,0.65,0])(T([2,3])([-4.5*10,40])(STRUCT(NN(6)(pair_y))))
#VIEW(colonne)

#muretto_superiore
y_muretto=QUOTE([20]*9)
z_muretto=QUOTE([10])
muretto=COLOR(PURPLE)(T([2,3])([-14,120])(INSR(PROD)([QUOTE([0]),y_muretto,z_muretto])))
#VIEW(muretto)

#parte alta
p_punti=[[0,-20,0],[0,19*9,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta=T(3)(130)(MKPOL([p_punti,p_celle,None]))

south=T([1,2])([470,50])(STRUCT([scalini,colonne,muretto,p_alta]))

VIEW(south)
VIEW(east)
VIEW(north)
VIEW(west)

all=STRUCT([west,east,north,south])

VIEW(all)
from pyplasm import *

#colonna
c_sup=T(3)(70)(CIRCLE(5)([20,32]))
c_inf=CIRCLE(8)([20,32])
colonna=COLOR([1,0.65,0])(JOIN([c_sup,c_inf]))

#capitello
x_cap=QUOTE([20])
y_cap=QUOTE([20])
capitello=COLOR([1,0.65,0])(T([1,2])([-10,-10])(INSR(PROD)([x_cap,y_cap,QUOTE([-70,10])])))

colonna_completa=STRUCT([capitello,colonna])

#nord
pair_y=[T(2)(30),colonna_completa]
nord=T([1,2,3])([20,-20,30])(STRUCT(NN(6)(pair_y)))
y_muretto_n=QUOTE([18.9]*9)
z_muretto_n=QUOTE([10])
muretto_n=COLOR(YELLOW)(T([1,3])([10,110])(INSR(PROD)([QUOTE([10]),y_muretto_n,z_muretto_n])))

p_punti=[[0,19*9,0],[0,-20,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta1=T(3)(120)(MKPOL([p_punti,p_celle,None]))
p_alta2=T([1,3])([6,120])(MKPOL([p_punti,p_celle,None]))
alto1=COLOR(YELLOW)(T([1,2])([10,10])(JOIN([p_alta1,p_alta2])))

#scalini
a1=T([1,2,3])([7,-1*10,20])(CUBOID([10,(18.8)*10,10]))
b1=T([1,2,3])([2,-2*10,10])(CUBOID([10,(20.8)*10,10]))
c1=T([1,2])([-3,-3*10])(CUBOID([10,(22.8)*10,10]))
d1=T([1,2,3])([-8,-4*10,-10])(CUBOID([10,(24.8)*10,10]))
scalini_n=COLOR(RED)(STRUCT([a1,b1,c1,d1]))

t_nord=STRUCT([nord,muretto_n,alto1,scalini_n])

VIEW(t_nord)

#est
pair_x=[T(1)(30),colonna_completa]
est=T([1,2,3])([-10,10,30])(STRUCT(NN(13)(pair_x)))

x_muretto_e=QUOTE([42]*9)
z_muretto_e=QUOTE([10])
muretto_e=COLOR(YELLOW)(T([1,3])([11,110])(INSR(PROD)([x_muretto_e,QUOTE([10]),z_muretto_e])))

#scalini
a2=T([1,2,3])([-5,-5,20])(CUBOID([(41.6)*10,10,10]))
b2=T([1,2,3])([-15,-10,10])(CUBOID([(43.8)*10,10,10]))
c2=T([1,2])([-25,-15])(CUBOID([(45.8)*10,10,10]))
d2=T([1,2,3])([-35,-20,-10])(CUBOID([(47.8)*10,10,10]))
scalini_e=COLOR(RED)(STRUCT([a2,b2,c2,d2]))

t_est=STRUCT([est,muretto_e,scalini_e])

VIEW(t_est)

#sud
pair_y=[T(2)(30),colonna_completa]
sud=T([1,2,3])([380,-20,30])(STRUCT(NN(6)(pair_y)))

y_muretto_s=QUOTE([18.9]*9)
z_muretto_s=QUOTE([10])
muretto_s=COLOR(YELLOW)(T([1,3])([380,110])(INSR(PROD)([QUOTE([10]),y_muretto_s,z_muretto_s])))

#parte alta
p_punti=[[0,19*9,0],[0,-20,0],[0,75,20]]
p_celle=[[1,2,3]]
p_alta1=T(3)(120)(MKPOL([p_punti,p_celle,None]))
p_alta2=T([1,3])([6,120])(MKPOL([p_punti,p_celle,None]))
alto2=COLOR(YELLOW)(T([1,2])([384,10])(JOIN([p_alta1,p_alta2])))

#scalini
a3=T([1,2,3])([385,-1*10,20])(CUBOID([10,(18.8)*10,10]))
b3=T([1,2,3])([390,-2*10,10])(CUBOID([10,(20.8)*10,10]))
c3=T([1,2])([395,-3*10])(CUBOID([10,(22.8)*10,10]))
d3=T([1,2,3])([400,-4*10,-10])(CUBOID([10,(24.8)*10,10]))
scalini_s=COLOR(RED)(STRUCT([a3,b3,c3,d3]))

t_sud=STRUCT([sud,muretto_s,alto2,scalini_s])

VIEW(t_sud)

#ovest
pair_x=[T(1)(30),colonna_completa]
ovest=T([1,2,3])([-11,160,30])(STRUCT(NN(13)(pair_x)))

x_muretto_o=QUOTE([42]*9)
z_muretto_o=QUOTE([10])
muretto_o=COLOR(YELLOW)(T([1,2,3])([10,160,110])(INSR(PROD)([x_muretto_o,QUOTE([10]),z_muretto_o])))

#scalini
a4=T([1,2,3])([-5,165,20])(CUBOID([(41.6)*10,10,10]))
b4=T([1,2,3])([-15,170,10])(CUBOID([(43.8)*10,10,10]))
c4=T([1,2])([-25,175])(CUBOID([(45.8)*10,10,10]))
d4=T([1,2,3])([-35,180,-10])(CUBOID([(47.8)*10,10,10]))
scalini_o=COLOR(RED)(STRUCT([a4,b4,c4,d4]))

t_ovest=STRUCT([ovest,muretto_o,scalini_o])

VIEW(t_ovest)

completo=STRUCT([t_sud,t_nord,t_est,t_ovest])

VIEW(completo)
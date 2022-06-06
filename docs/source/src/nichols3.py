from control import tf, feedback
from control_plotly import bode,nichols, step

F = tf([1],[1,2,1])
fig = nichols(F,cm=[6,1,0,-1,-3,-6],show_phase=False,y_lim=[-25,30],x_lim=[-300,0])
fig.show()

K1dB = 14.2
K1 = 10**(K1dB/20)
fig = nichols([F,K1*F],cm=[6,1,0,-1,-3,-6],show_phase=False,y_lim=[-25,30],x_lim=[-300,0])
fig.show()

wr = 2
Ti = 1/(wr/5)
Cp = tf([K1*Ti,K1],[Ti,0])
fig = nichols([F,K1*F,Cp*F],cm=[6,1,0,-1,-3,-6],show_phase=False,y_lim=[-25,30],x_lim=[-300,0])
fig.show()

K2dB = -4
K2 = 10**(K2dB/20)
Ki = K1*K2
Cp2 = tf([Ki*Ti,Ki],[Ti,0])
fig = nichols([F,K1*F,Cp*F,Cp2*F],cm=[6,1,0,-1,-3,-6],show_phase=False,y_lim=[-25,30],x_lim=[-300,0])
fig.show()

H = feedback(Cp2*F,1)
fig = step(H)
fig.show()
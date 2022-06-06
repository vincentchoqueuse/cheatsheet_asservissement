from control import tf, feedback
from control_plotly import bode,nichols, step, rlocus

F = tf([1],[1,2,1])
fig = nichols(F,cm=[3, 0,-1.6, -2.6, -3, -6],show_phase=False,y_lim=[-25,30],x_lim=[-300,0])
fig.show()

K1 = 2.8
fig = nichols([F,K1*F],cm=[3, 0,-1.6, -2.6, -3, -6],show_phase=False,y_lim=[-25,30],x_lim=[-300,0])
fig.show()

H = feedback(K1*F,1)
fig = step(H)
fig.show()
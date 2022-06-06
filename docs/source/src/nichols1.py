import control as ctl 
from control_plotly import bode,nichols, step
import numpy as np

F = ctl.tf([3],[1,3,3,1])
w = np.logspace(-2,2,500)
fig = bode(F,w=w)
fig.show()

fig = nichols(F,w=w,show_grid=False,y_lim=[-80,30],x_lim=[-300,0])
fig.show()


H = ctl.feedback(F,1)
fig = bode(H,w=w)
fig.show()

fig = nichols(F,w=w,cm=[0,4,6,-2.5,-6,-12],show_phase=False,y_lim=[-80,30],x_lim=[-300,0])
fig.show()

fig = step(H)
fig.show()
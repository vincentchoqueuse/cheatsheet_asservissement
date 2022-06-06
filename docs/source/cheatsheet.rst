Cheatsheet
==========

Getting Started
---------------

* Install python control and python control plotly 

.. code ::

    pip install control control-plotly

The python control library provides several functions for the analysis of continuous time and discrete time systems.
The python control plotly library provides several function for plotting the time and frequency responses in the browser
using plotly.


Python control
--------------

System Creation
+++++++++++++++

.. code ::

    from control import tf

    sys = tf([1],[3,1])

.. note ::

    Documentation : https://python-control.readthedocs.io/en/latest/generated/control.tf.html

Pour obtenir les pôles et les zéros, nous pouvons utiliser les méthodes :code:`pole()` et :code:`zero()`. Il est également possible d'obtenir les informations sur l'amortissement associé à chaque pôle en utilisant la méthode 
:code:`damp()`.

.. code ::

    print(sys.pole())
    print(sys.zero())
    print(sys.damp())


Closed Loop 
+++++++++++

.. code ::

    from control import tf, feedback

    sys = tf([1],[3,1])
    sys_CL = feedback(sys,1)

.. note ::

    Documentation : https://python-control.readthedocs.io/en/latest/generated/control.feedback.html

Step Information 
++++++++++++++++

.. code ::

    from control import tf, step_info

    sys = tf([1],[3,1])
    step_info(sys,SettlingTimeThreshold=0.05,RiseTimeLimits=(0.1, 0.9))


Damping Factor 
++++++++++++++

.. code ::

    from control import tf, damp

    sys = tf([1],[3,1])
    damp(sys)

.. note ::

    Documentation : https://python-control.readthedocs.io/en/latest/generated/control.damp.html

Control Plotly
--------------

Poles Zeros Map 
+++++++++++++++

.. code ::

    from control import tf
    from control_plotly import pzmap

    sys = tf([1],[2,1,1])
    pzmap(sys)

.. note ::

    Documentation : https://python-control-plotly.readthedocs.io/en/latest/api/_autosummary/control_plotly.pzmap.html

Step Response 
+++++++++++++

.. code ::

    import numpy as np
    from control import tf
    from control_plotly import step

    sys = tf([1],[2,1,1])
    t = np.arange(0,20,0.01)
    step(sys,t=t) # t is optional 

.. note ::

    Documentation : https://python-control-plotly.readthedocs.io/en/latest/api/_autosummary/control_plotly.step.html

Impulse Response
++++++++++++++++

.. code ::

    import numpy as np
    from control import tf
    from control_plotly import impulse

    sys = tf([1],[2,1,1])
    t = np.arange(0,20,0.01)
    impulse(sys,t=t) # t is optional 

.. note ::

    Documentation : https://python-control-plotly.readthedocs.io/en/latest/api/_autosummary/control_plotly.impulse.html

Bode Diagram 
++++++++++++   

.. code ::

    import numpy as np
    from control import tf
    from control_plotly import bode

    sys = tf([1],[2,1,1])
    w = np.logspace(-1,1,100)
    bode(sys,w=w) # w is optional 

.. note ::

    Documentation : https://python-control-plotly.readthedocs.io/en/latest/api/_autosummary/control_plotly.bode.html


Nichols Chart 
+++++++++++++

.. code ::

    from control import tf
    from control_plotly import nichols

    sys = tf([1],[2,1,1])
    nichols(sys)

.. note ::

    Documentation : https://python-control-plotly.readthedocs.io/en/latest/api/_autosummary/control_plotly.nichols.html

Root Locus 
++++++++++

.. code ::

    import control as ctl
    from control_plotly import rlocus

    sys = tf([2,5,1],[1,2,3])
    rlocus(sys)


.. note ::

    Documentation : https://python-control-plotly.readthedocs.io/en/latest/api/_autosummary/control_plotly.rlocus.html
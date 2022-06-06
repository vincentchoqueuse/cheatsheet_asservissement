Liste des correcteurs
=====================

Contexte
--------

Considérons un système en boucle fermée avec un retour unitaire 

.. figure:: img/closed_loop_2.svg
  :width: 300
  :align: center
  :alt: Boucle Fermée avec Retour unitaire

  Boucle Fermée avec Retour Unitaire

* :math:`E(p)`: Transformée de Laplace de la consigne,
* :math:`C(p)`: Fonction de transfert du correcteur,
* :math:`F(p)`: Fonction de transfert du système + capteur,
* :math:`C(p)F(p)`: Fonction de transfert en boucle ouverte (FTBO).

Correcteurs Usuels 
------------------

Pour respecter les contraintes du cahier des charges, nous pouvons utiliser différents types de correcteurs :math:`C(p)`.
Ces correcteurs possèdent un ou plusieurs paramètres de liberté que nous pouvons ajuster en fonction des performances souhaitées. 

Proportionnel
+++++++++++++

La fonction de transfert du correcteur P est donnée par:

.. math ::

    C(p) = K_c

* Paramètre du correcteur: :math:`K_c`
* Réponse fréquentielle :


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K_c = 1
    sys = lti([K_c],[1])
    w, Hjw = sys.freqresp(w=np.logspace(-2,2,100))

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].semilogx(w, 20*np.log10(np.abs(Hjw)))
    axs[0].set_xlabel("w [rad/s]")
    axs[0].set_ylabel("Module [dB]")
    axs[0].set_yticks([20*np.log10(K_c)], ["$20\log(K_{c})$"])
    axs[0].grid()
    axs[0].set_xlim([0.01,100])
    axs[0].set_ylim([-20,20])
    axs[0].set_title("Module ")
    axs[1].semilogx(w, 180*np.angle(Hjw)/np.pi)
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("Argument [deg]")
    axs[1].set_title("Argument")
    axs[1].set_xlim([0.01,100])
    axs[1].set_ylim([-90,90])
    axs[1].grid()
    fig.tight_layout()

Proportionnel Intégral
++++++++++++++++++++++ 

La fonction de transfert du correcteur PI est donnée par:

.. math ::

    C(p) = K_c \left(1+ \frac{1}{T_ip}\right) = K_c \frac{T_i p+1}{T_ip}

* Paramètres du correcteur: :math:`K_c`, :math:`T_i`
* Réponse fréquentielle :


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K_c = 1
    T_i = 1
    sys = lti([K_c*T_i, K_c],[T_i, 0])
    w, Hjw = sys.freqresp(w=np.logspace(-2,2,100))

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].semilogx(w, 20*np.log10(np.abs(Hjw)))
    axs[0].set_xlabel("w [rad/s]")
    axs[0].set_ylabel("Module [dB]")
    axs[0].grid()
    axs[0].set_xlim([0.01,100])
    axs[0].set_ylim([-20,40])
    axs[0].set_yticks([20*np.log10(K_c),20*np.log10(K_c)+3], ["$20\log(K_{c})$","$20\log(K_{c})+3$"])
    axs[0].set_xticks([1/T_i], ["$\\frac{1}{T_i}$"])
    axs[0].set_title("Module ")
    axs[1].semilogx(w, 180*np.angle(Hjw)/np.pi)
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("Argument [deg]")
    axs[1].set_title("Argument")
    axs[1].set_xlim([0.01,100])
    axs[1].set_ylim([-90,90])
    axs[1].set_yticks([-90,-45,0,45,90], ["$-90^o$","$-45^o$","$0^o$","$45^o$","$90^o$"])
    axs[1].set_xticks([1/T_i], ["$\\frac{1}{T_i}$"])
    axs[1].grid()
    fig.tight_layout()


Proportionnel Dérivé
++++++++++++++++++++

La fonction de transfert du correcteur PD est donnée par:

.. math ::

    C(p) = K_c (1+T_d p)

* Paramètres du correcteur: :math:`K_c`, :math:`T_d`
* Réponse fréquentielle :

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K_c = 1
    T_d = 1
    sys = lti([K_c*T_d, K_c],[1])
    w, Hjw = sys.freqresp(w=np.logspace(-2,2,100))

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].semilogx(w, 20*np.log10(np.abs(Hjw)))
    axs[0].set_xlabel("w [rad/s]")
    axs[0].set_ylabel("Module [dB]")
    axs[0].grid()
    axs[0].set_xlim([0.01,100])
    axs[0].set_ylim([-20,40])
    axs[0].set_title("Module ")
    axs[0].set_yticks([20*np.log10(K_c),20*np.log10(K_c)+3], ["$20\log(K_{c})$","$20\log(K_{c})+3$"])
    axs[0].set_xticks([1/T_d], ["$\\frac{1}{T_d}$"])
    axs[1].semilogx(w, 180*np.angle(Hjw)/np.pi)
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("Argument [deg]")
    axs[1].set_title("Argument")
    axs[1].set_xlim([0.01,100])
    axs[1].set_ylim([-90,90])
    axs[1].set_yticks([-90,-45,0,45,90], ["$-90^o$","$-45^o$","$0^o$","$45^o$","$90^o$"])
    axs[1].set_xticks([1/T_d], ["$\\frac{1}{T_d}$"])
    axs[1].grid()
    fig.tight_layout()

Proportionnel Intégral Dérivé
+++++++++++++++++++++++++++++

La fonction de transfert du correcteur PID est donnée par:

.. math ::

    C(p) = K_c\left(1+\frac{1}{T_ip}+T_d p\right) = K_c \frac{T_iT_d p^2+T_i p+1}{T_ip}

* Paramètres du correcteur: :math:`K_c`, :math:`T_i`, :math:`T_d`
* Réponse fréquentielle :


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K_c = 1
    T_d = 0.1
    T_i = 10
    sys = lti([K_c*T_i*T_d, K_c*T_i, K_c],[T_i,0])
    w, Hjw = sys.freqresp(w=np.logspace(-2,2,100))

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].semilogx(w, 20*np.log10(np.abs(Hjw)))
    axs[0].set_xlabel("w [rad/s]")
    axs[0].set_ylabel("Module [dB]")
    axs[0].grid()
    axs[0].set_xlim([0.01,100])
    axs[0].set_ylim([-20,20])
    axs[0].set_title("Module ")
    axs[0].set_yticks([20*np.log10(K_c),20*np.log10(K_c)+3], ["$20\log(K_{c})$","$20\log(K_{c})+3$"])
    axs[0].set_xticks([1/T_i, 1/T_d], ["$\\frac{1}{T_i}$","$\\frac{1}{T_d}$"])
    axs[1].semilogx(w, 180*np.angle(Hjw)/np.pi)
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("Argument [deg]")
    axs[1].set_title("Argument")
    axs[1].set_xlim([0.01,100])
    axs[1].set_ylim([-90,90])
    axs[1].set_yticks([-90,-45,0,45,90], ["$-90^o$","$-45^o$","$0^o$","$45^o$","$90^o$"])
    axs[1].set_xticks([1/T_i, 1/T_d], ["$\\frac{1}{T_i}$","$\\frac{1}{T_d}$"])
    axs[1].grid()
    fig.tight_layout()

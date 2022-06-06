Systèmes Echantillonnés
=======================

Contexte
--------

Dans ce chapitre, nous montrons comment utiliser la transformée en Z pour analyser un système composé de CNA, d'un système continu et d'un CAN. Pour 
modéliser l'effet du CNA, nous introduisons le bloqueur d'ordre 0. Nous montrons ensuite qu'il est possible d'obtenir facilement la fonction de transfert en Z du système 
composé d'un CNA avec bloqueur d'ordre 0, d'un système analogique de fonction de transfert :math:`F(p)` et d'un CAN.

Modélisation CNA/CAN avec BOZ
-----------------------------

Même si la correction se fait en numérique, en pratique, le système à contrôler reste
le plus souvent analogique. Pour pouvoir mettre en place une stratégie de correction, il 
est alors nécessaire de modéliser l'influence des convertisseurs A/N et N/A.

Soit un système comportant

* un CNA de période d'échantillonnage :math:`T_e`,
* le système continu :math:`F(p)`,
* un CAN de période d'échantillonnage :math:`T_e` modélisé par un bloqueur d'ordre 0 (BOZ)

.. figure:: img/boz.svg
  :width: 350
  :align: center
  :alt: schema bloc

  CNA avec BOZ

Bloqueur d'ordre 0
++++++++++++++++++

Le bloqueur d'ordre 0 permet d'obtenir un signal analogique à partir d'un signal numérique. Spécifiquement, 
le bloqueur d'ordre 0 "bloque" la valeur du signal entre deux instants d'échantillonnage.

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    t = np.arange(0, 4, 0.01)
    t2 = np.arange(0, 4, 0.2)
    x = np.sin(2*np.pi*1*t) + 0.2*np.sin(2*np.pi*1.3*t) - 0.4*np.sin(2*np.pi*2.8*t)
    x_ech = np.sin(2*np.pi*1*t2) + 0.2*np.sin(2*np.pi*1.3*t2) - 0.4*np.sin(2*np.pi*2.8*t2)

    plt.plot(t, x, label="signal continu")
    plt.stem(t2, x_ech, label="signal échantillonné", basefmt="C1-", linefmt="C1*", markerfmt="C1o")
    plt.step(t2, x_ech, "C2-", where="post", label="signal après bloqueur")
    plt.legend()
    plt.grid()
    plt.tight_layout()


Un bloqueur d'ordre 0 peut être modélisé par un filtre analogique de réponse impulsionnelle 

.. math ::

  h(t) = u(t)-u(t-T_e) =\left\{\begin{array}{cl}1 & \text{ si }0\le t \le T_e \\
  0&\text{ ailleurs}\end{array}\right.

La fonction de transfert du bloqueur d'ordre 0 est alors donnée par 

.. math ::
  
  B_0(p) = \mathcal{L}[h(t)]=\frac{1}{p}-\frac{e^{-pT_e}}{p}=\frac{1-e^{-pT_e}}{p}

Fonction de transfert
+++++++++++++++++++++

La chaîne composée du CNA avec BOZ, du système continu et du CAN peut être modélisée par la fonction de transfert en Z suivante

.. math ::

    F(z)=\frac{z-1}{z}TZ\left[TL^{-1}\left[\frac{F(p)}{p}\right]\right]

Dans la plupart des cas, nous utiliserons par abus de notation la relation suivante :

.. math ::

    F(z)=\frac{z-1}{z}TZ\left[\frac{F(p)}{p}\right]

**Demonstration**

En utilisant directement l'abus de notation, la fonction de transfert d'une chaine CNA/CAN avec BOZ s'exprime sous la forme

.. math ::

    F(z)&= TZ\left[B_0(p)F(p)\right]\\
        &=TZ\left[\frac{F(p)}{p}\right]-TZ\left[\frac{(e^{-pT_e}F(p)}{p}\right]\\
        &=TZ\left[\frac{F(p)}{p}\right]-z^{-1}TZ\left[\frac{F(p)}{p}\right]\\
        &=(1-z^{-1}) TZ\left[\frac{F(p)}{p}\right]\\
        &=\frac{z-1}{z}TZ\left[\frac{F(p)}{p}\right]


Propriétés
++++++++++

* Les gains statiques de :math:`F(z)` et de :math:`F(p)` sont identiques.
* Les pôles de la fonction de transfert :math:`F(z)` sont liés aux pôles de :math:`F(p)` par la relation 

.. math ::

  z_k = e^{p_kT_e}



Exemple
+++++++

Considérons un système continu de premier ordre de fonction de transfert 

.. math ::

    F(p)=\frac{K}{1+\tau p}

Le pôle du système est donné par :math:`p=-\frac{1}{\tau}`.

La Fonction de transfert discrete du système composée du CNA avec BOZ, de :math:`F(p)` et d'un CAN est égale à 

.. math ::

  F(z)=K\left(\frac{1-e^{-\frac{T_e}{\tau}}}{z-e^{-\frac{T_e}{\tau}}} \right)

où :math:`T_e` désigne la période d'échantillonnage. Nous remarquons bien que le gain statique de :math:`F(z)` est égal à
:math:`F(1)=K`. De plus, nous observons que :math:`F(z)` possède un unique pôle en :math:`z=e^{p T_e}` où :math:`p=-\frac{1}{\tau}` correspond au pôle du système continu.
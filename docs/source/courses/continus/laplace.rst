Transformée de Laplace
======================

Définition
----------

La transformée de Laplace unilatérale d'un signal est donnée par

.. math ::

    X(p) = \mathcal{L}[x(t)]=\int_{0}^{\infty} x(t)e^{-pt}dt

Exemple
+++++++

Soit :math:`x(t)=u(t)`, l'échelon unité défini par :

.. math::

        u(t) =\left\{\begin{array}{cl} 1 & \text{ si }t\ge 0\\
        0&\text{ ailleurs}\\
        \end{array}\right.

La transformée de Laplace de :math: `u(t)` est alors égale à :

.. math ::

    U(p) = \mathcal{L}[u(t)]=\int_{0}^{\infty} e^{-pt}dt

Cette intégrale est une intégrale impropre au sens de Riemann. Cette intégrale est divergente pour :math:`p \le 0` et est convergente pour :math:`p > 0`. 
La transformée de Laplace n’est définie que pour :math:`p > 0`. Dans ce cas, nous obtenons

.. math ::

    U(p) = \frac{1}{p}.

Propriétés
----------

La transformée de Laplace possède les propriétés suivantes: 

* Linéarité :

.. math ::

    \mathcal{L}\left[\alpha_1 x_1(t)+\alpha_2 x_2(t)\right]=\alpha_1 X_1(p)+\alpha_2 X_2(p)

* Dérivation :

.. math ::

    \mathcal{L}\left[\frac{dx(t)}{dt}\right]=pX(p)-x(0^-)

* Théorème de la Valeur Initiale :

.. math ::

    x(0^+)=\lim_{p\to \infty} p X(p)

* Théorème de la Valeur Finale :

.. math ::

    x(\infty)=\lim_{p\to 0} p X(p)


Signaux Usuels
--------------

Impulsion de Dirac
++++++++++++++++++

* Définition : 

.. math :: 

    x(t) = \delta(t)=\left\{\begin{array}{cc}
    \infty,&t=0\\
    0,&t\ne 0
    \end{array}\right.~\text{s.t.}\int_{-\infty}^{\infty} \delta(t)dt = 1


* Transformée de Laplace : 

.. math :: 

    X(p) = 1


Echelon Unitaire 
++++++++++++++++

* Définition : 

.. math :: 

    u(t)=\left\{\begin{array}{cc}
    1,&t\ge 0\\
    0,&t< 0
    \end{array}\right.


* Transformée de Laplace : 

.. math :: 

    U(p) = \frac{1}{p}


Exponentielle Décroissante
+++++++++++++++++++++++++++

* Définition : 

.. math :: 

    x(t)=e^{-\alpha t}u(t)


* Transformée de Laplace : 

.. math :: 

    X(p) = \frac{1}{p+\alpha}


Sinusoide Amortie (Part 1)
++++++++++++++++++++++++++

* Définition : 

.. math :: 

    x(t)=e^{-\alpha t}\sin(\omega t) u(t)


* Transformée de Laplace : 

.. math :: 

    X(p) = \frac{\omega}{(p+\alpha)^2+\omega^2}

Sinusoide Amortie (Part 2)
++++++++++++++++++++++++++

* Définition : 

.. math :: 

    x(t)=e^{-\alpha t}\cos(\omega t) u(t)


* Transformée de Laplace : 

.. math :: 

    X(p) = \frac{p+\alpha}{(p+\alpha)^2+\omega^2}


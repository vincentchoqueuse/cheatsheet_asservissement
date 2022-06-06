Transformée en Z 
================

Définition
----------

La transformée en Z unilatérale d'une suite numérique :math:`x[n]` est définie par l'équation :

.. math ::

    X(z)= \mathcal{Z}[x[n]] = \sum_{n=0}^{\infty}x[n]z^{-n}

où :math:`z` est une variable complexe. 


La transformée de Z d'un signal ne converge pas nécessairement pour tout :math:`z`. Il est alors nécessaire de préciser la région de convergence (ROC) pour laquelle la série converge c-a-d les valeurs de :math:`z` telles que :math:`|X(z)|<\infty`.

Exemple
+++++++

Soit :math:`x[n]=u[n]`, l'échelon unité défini par :

.. math::

        u[n] =\left\{\begin{array}{cl} 1 & \text{ si }n\ge 0\\
        0&\text{ ailleurs}\\
        \end{array}\right.

La transformée en Z de :math:`x[n]=u[n]` est égale à :

.. math::

    X(z)&= \sum_{n=0}^{\infty}u[n]z^{-n}\\
    &=\sum_{n=0}^{\infty}z^{-n}\\
    &=\frac{1}{1-z^{-1}}\\
    &=\frac{z}{z-1}

où le passage de la deuxième à la troisième ligne s'obtient en remarquant le fait :math:`\sum_{n=0}^{\infty}z^{-n}` correspond à 
la somme des éléments d'une suite géométrique de raison :math:`z^{-1}`. La region de convergence est donnée par :math:`|z|>1`.


Propriétés
----------

La transformée en Z possède les propriétés suivantes : 

* Linéarité: Si :math:`y[n]=\alpha x_1[n]+\beta x_2[n]` où :math:`\alpha` et :math:`\beta` sont des constantes, alors 

.. math ::

    Y(z)=\alpha X_1(z)+\beta X_2(z)

* Décalage temporel: Si :math:`y[n]=x[n-k]` (:math:`k \in \mathbb{N}^{+}`), alors 

.. math ::
    
    Y(z)=X(z)z^{-k}

* Multiplication par une fonction exponentielle: Si :math:`y[n]= a^n x[n]`, alors 

.. math ::

    Y(z)=X(a^{-1}z)

* Convolution: Si :math:`y[n]= h[n]*x[n]`, alors 

.. math ::
    Y(z)=H(z)X(z)

* Théorème de la valeur initiale: Si la limite :math:`\lim_{z\to \infty}X(z)` existe, alors la valeur initiale s'obtient via l'expression

.. math ::

    x[0]=\lim_{z\to \infty} X(z)

* Théorème de la valeur finale: Si tous les pôles de :math:`X(z)` sont compris dans le cercle unité, alors la valeur finale s'obtient via l'expression

.. math ::

    \lim_{n\to \infty} x[n]=\lim_{z\to 1}(z-1)X(z)

Signaux Usuels
--------------

Impulsion unité
+++++++++++++++

* Définition : 

.. math :: 

    x[n] = \delta[n]=\left\{\begin{array}{cc}
    1,&n=0\\
    0,&n\ne 0
    \end{array}\right.


* Transformée en Z : 

.. math :: 

    X(z) = 1

Echelon unité
+++++++++++++

* Définition : 

.. math :: 

    x[n] = u[n]=\left\{\begin{array}{cc}
    1,&n\ge 0\\
    0,&n\ne 0
    \end{array}\right.


* Transformée en Z : 

.. math :: 

    X(z) = \frac{z}{z-1}

Rampe unité
+++++++++++

* Définition : 

.. math :: 

    x[n] = r[n]=\left\{\begin{array}{cc}
    nT_e,&n\ge 0\\
    0,&n\ne 0
    \end{array}\right.


* Transformée en Z : 

.. math :: 

    X(z) = \frac{zT_e}{(z-1)^2}
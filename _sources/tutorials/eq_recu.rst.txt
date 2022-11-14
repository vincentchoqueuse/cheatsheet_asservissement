Equation de récurrence 
======================

Objectif
--------

Dans ce tutorial, nous montrons comment obtenir l'équation de récurrence d'un système à temps discret décrit par une fonction de transfert :math:`F(z)`.
Pour illustrer ce tutoriel, nous allons considérer la fonction de transfert suivante :

.. math ::

    F(z) = \frac{S(z)}{E(z)} = \frac{2}{4z + 1}

Méthodologie
------------

Pour obtenir l'équation de récurrence, nous allons précéder en deux temps 

1. Obtention d'une équation impliquant la transformée en Z de la sortie, :math:`S(z)`, et la transformée en Z de l'entrée, :math:`E(z)`.
2. Ecriture de l'équation en puissances de z négatives. 
3. Passage à la transformée en Z inverse.


Transformée en Z 
++++++++++++++++

En utilisant l'expression de :math:`F(z)`, nous obtenons :

.. math ::

    S(z) (4z + 1) &= 2 E(z)\\
    4zS(z) + S(z) &= 2 E(z)

Puissances de z négatives 
+++++++++++++++++++++++++

Pour obtenir une écriture en puissance de z négatives, nous allons multiplier les deux parties de l'égalité par :math:`z^{-1}`.

.. math ::

    4S(z) + z^{-1}S(z) = 2 z^{-1}E(z)

Transformée en Z inverse 
++++++++++++++++++++++++

En utilisant la propriété de linéarité et du retard, nous obtenons :

.. math ::

    4s[n] + s[n-1] = 2 e[n-1]

Finalement, l'équation de récurrence est donnée par :

.. math ::

    s[n] = 0.5 e[n-1] - 0.25s[n-1]


Vérification 
------------

Pour vérifier notre équation, nous allons déterminer les premiers échantillons de sortie lorsque l'entrée est un échelon unitaire (:math:`e[n]=u[n]`). 
Ces échantillons en sortie seront comparés avec ceux obtenus en utilisant Python.

Lorsque l'entrée est un échelon unitaire, les premiers échantillons sont donnés par :

.. math ::

    s[0] &= 0.5 e[-1] - 0.25 s[-1] = 0 - 0 = 0\\
    s[1] &= 0.5 e[0] - 0.25s[0] = 0.5 - 0 = 0.5\\
    s[2] &= 0.5 e[1] - 0.25s[1] = 0.5 - 0.25 \times 0.5 = 0.375

En utilisant Python, nous obtenons la réponse indicielle suivante.

.. plot ::
    :context: close-figs
    :include-source:


    from control import tf, step_response
    import matplotlib.pyplot as plt

    Te = 1
    Fz = tf([2], [4, 1], Te)
    T, yout = step_response(Fz)

    plt.step(T, yout, where="post")
    plt.xlabel("Temps [s]")
    plt.ylabel("Reponse Indicielle")
    plt.grid()
    plt.tight_layout()

Nous pouvons constater que les deux réponses correspondent bien.
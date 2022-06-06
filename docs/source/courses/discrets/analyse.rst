Systèmes SLIT
=============

Equation de récurrence
----------------------

Dans ce cours, nous nous intéressons spécifiquement à l’analyse des SLITs modélisables par une équation de récurrence.

Expression
++++++++++

Lorsqu’un système est modélisable par une équation de récurrence, le lien entre l'entrée :math:`e[n]` et la sortie :math:`s[n]` est donné par :

.. math ::

    a_L s[n+L] + \cdots + a_0 s[n] = b_K e[n+K] + \cdots + b_0 e[n]

Lorsque le système est causal, :math:`K<L`. Sous l'hypothèse de causalité, l'équation de récurrence peut également s'exprimer
sous la forme 

.. math ::

    a_L s[n]  &= b_K e[n+K-L] + \cdots + b_0 e[n-L]\\
    &~-a_{L-1} s[n-1] -  \cdots - a_0 s[n-L]


Fonction de transfert
---------------------

Lorsque les conditions initiales sont nulles, la transformée en Z de la sortie s'exprime sous la forme 
:math:`S(z)=H(z)E(z)` où :math:`H(z)` correspond à la fonction de transfert en Z du système.

.. figure:: img/representation_d.svg
  :width: 250
  :align: center
  :alt: schema bloc

  Schéma Bloc

Forme polynomiale
+++++++++++++++++

Pour un système régit par une équation de récurrence, la fonction de transfert du système est donnée par : 

.. math ::

    H(z)=\frac{S(z)}{E(z)}=\frac{b_K z^{K} + \cdots + b_1 z + b_0}{a_L z^{L}+ \cdots + a_1z+ a_0}


Forme Factorisée
++++++++++++++++

Pour mettre en évidence les points singuliers de la fonction de transfert, il est possible de réexprimer la fonction de transfert sous une forme factorisée. 


.. math ::

    H(z)=G\frac{(z-z_1)(z-z_2)\cdots(z-z_K)}{(z-p_1)(z-p_2)\cdots(z-p_L)}

* les :math:`z_k` correspondent aux zéros de la fonction de transfert,
* les :math:`p_l` correspondent aux poles de la fonction de transfert).
* :math:`G=\frac{b_K}{a_L}` est un facteur d'amplification.

Propriétés
++++++++++

* Stabilité: Pour qu'un système à temps discret soit stable, il faut que tous les pôles de sa fonction de transfert sont inclus dans le cercle de rayon unité c-a-d si :math:`|p_l|\le 1``

* Valeur Initiale : 

.. math ::

    s[0]=\lim_{z\to \infty}H(z)E(z)

* Valeur Finale : Si la sortie converge,  

.. math ::

    s(\infty)=\lim_{z\to 1}(z-1)H(z)E(z)

Réponse Temporelle
------------------

Pour obtenir la réponse temporelle d'un système à une entrée :math:`e[n]`, deux solutions sont possibles.

Technique 1 (Décomposition en éléments simples)
+++++++++++++++++++++++++++++++++++++++++++++++

1. Calcul de la transformée en Z de la sortie du système c-à-d :math:`S(z) = H(z)E(z)` où :math:`E(z)` correspond à la transformée en Z de l'entrée. 
2. Décomposition en éléments simples de la sortie :math:`S(z)/z`, puis de :math:`S(z)`.
3. Retour à l'original en appliquant la transformée en Z inverse (utilisation des tables des transformées en Z).

Technique 2 (Equation de récurrence)
++++++++++++++++++++++++++++++++++++

1. Obtention de l'équation de récurrence donnant :math:`s[n]` en fonction de :math:`s[l]~(l<n)` et :math:`e[k]~(k\le n)`
2. Evaluation de la sortie :math:`s[n]` en remplaçant les :math:`e[k]` par leur valeur numérique.


Exemple
+++++++

Considérons un système de premier ordre défini par la fonction de transfert

.. math ::

    H(z) = \frac{S(z)}{E(z)} = \frac{1}{z-0.5}

Les paragraphes suivants montrent comment obtenir la réponse indicielle à un échelon d'amplitude :math:`E` du système en utilisant les deux techniques possibles.

**Technique 1**

1. Transformée en Z de la sortie :

.. math ::

    S(z) = \frac{1}{z-0.5}E(z) = \frac{z}{(z-0.5)(z-1)}E

2. Décomposition en éléments simples :

.. math ::

    \frac{S(z)}{z} =  -\frac{2}{z-0.5}E + \frac{2}{z-1}E \Rightarrow S(z) = -\frac{2z}{z-0.5}E+ \frac{2z}{z-1}E

3. Retour à l'original :

.. math ::

    s[n] &=  -2(0.5)^n Eu[n] + 2E u[n]\\
    &= 2 (1-(0.5)^n)E u[n]

A titre d'exemple pour :math:`E=1`, les premiers échantillons en sortie sont :

.. math ::

    s[0] &= 0\\ 
    s[1] &= 2 (1-0.5)=1\\
    s[2] &= 2 (1-0.25)=1.5\\
    s[3] &= 2 (1-0.125)=1.75

**Technique 2**

1. Equation de récurrence :

.. math ::

    S(z)(z-0.5) &= E(z)\\
    S(z) &=z^{-1} E(z) +0.5z^{-1}S(z)

Nous obtenons alors :

.. math ::

    s[n] =e[n-1] + 0.5s[n-1]

2. Evaluation de la sortie :math:`s[n]` :

.. math ::

    s[n] = Eu[n-1] + 0.5s[n-1]

A titre d'exemple pour :math:`E=1`, les premiers échantillons en sortie sont :

.. math ::

    s[0] &= u[-1] + 0.5s[-1] = 0\\ 
    s[1] &= u[0] + 0.5s[0] = 1\\
    s[2] &= u[1] + 0.5s[1] = 1.5\\
    s[3] &= u[2] + 0.5s[2] = 1.75

Réponse Fréquentielle
---------------------

Expression
++++++++++

Il est possible de montrer que si :math:`e[n]=e^{j\omega nT_e}`, la sortie s'exprime sous la forme :math:`s[n]=H\left(e^{j\omega T_e}\right)e^{j\omega nT_e}` où 
:math:`H\left(e^{j\omega T_e}\right)` désigne la réponse fréquentielle du système.  
Notons que la réponse fréquentielle peut s'obtenir directement à partir de la fonction de transfert en posant :

.. math ::

    z = e^{j\omega T_e}

Compte tenu des propriétés de périodicité et de symétrie, la réponse fréquentielle est le plus souvent déterminée pour :math:`0 \le \omega \le \omega_e/2`
où :math:`\omega_e=2\pi F_e` désigne la pulsation d'échantillonnage.

Représentation 
++++++++++++++

Comme la réponse fréquentielle est généralement complexe, nous représentons le plus souvent :

* son module :math:`|H\left(e^{j\omega T_e}\right)|`,
* son argument :math:`\arg[H\left(e^{j\omega T_e}\right)]`.


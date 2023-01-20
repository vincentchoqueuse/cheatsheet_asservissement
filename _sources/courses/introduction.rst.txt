Introduction
============

Objectif
--------

Dans ce cours, nous allons nous focaliser sur le contrôle et la commande des systèmes à une entrée / une sortie (SISO: Single Input Single Output).
Un système SISO peut être représenté un bloc prenant une entrée et renvoyant une sortie. 

.. figure:: img/representation3.svg
  :width: 250
  :align: center
  :alt: Modélisation Schéma Bloc

  Modélisation Schéma Bloc

En asservissement, notre objectif est de venir élaborer, synthétiser un signal de commande analogique ou numérique du processus que nous souhaitons contrôler.
Pour atteindre cet objectif, nous proposons :

* de mesurer la sortie du système au moyen d'un capteur,
* de mesurer la différence entre la consigne et la sortie du capteur au moyen d'un comparateur,
* d'élaborer un signal de commande à partir de la sortie du comparateur.

Cette structure correspond à un système bouclé puisque la sortie est combinée avec l'entrée via le comparateur.

.. figure:: img/representation4.svg
  :width: 450
  :align: center
  :alt: Modélisation Schéma Bloc

  Chaîne bouclée à retour non unitaire

Pour faciliter l'analyse des systèmes bouclés, nous travaillerons le plus souvent avec des systèmes bouclés à retour unitaire. En notant :math:`e(t)` et :math:`s(t)` le
signal de consigne et le signal en sortie de capteur, nous obtenons alors le schéma bloc suivant.

.. figure:: img/representation5.svg
  :width: 550
  :align: center
  :alt: Modélisation Schéma Bloc

  Chaîne bouclée à retour unitaire


Critères de Performance 
-----------------------

Pour élaborer un signal de commande, nous allons prendre en compte plusieurs contraintes portant sur l'allure du signal de sortie 
:math:`s(t)`. A titre d'illustration, la courbe suivante présente l'allure de la réponse d'un système à une entrée de type échelon (réponse indicielle). A 
partir de cette réponse, nous pouvons évaluer plusieurs critères permettant de critiquer les performances de l'asservissement.


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np
    from scipy.signal import lti
    

    w0 = 1
    m = 0.2
    t = np.arange(0,30,0.1)
    H = lti([0.8],[1/(w0**2),2*m/w0,1])
    t,s = H.step(T=t)
    t2 = np.insert(t,0,[-1,0])
    s2 = np.insert(s,0,[0,0])
    smax = max(s)
    tr = t[np.where((s>1.05*0.8) | (s<0.95*0.8))[-1]]

    plt.plot(t2,s2,label="s(t)")
    plt.plot([0,0,0,30],[0,0,1,1],color = 'r', label="Eu(t)")
    plt.xlabel("$t$ [rad/s]")
    plt.ylabel("$s(t)$")
    plt.xlim([-1,30])
    plt.ylim([0,1.25])
    plt.xticks([0,tr[-1]],["0","$t_r$"])
    plt.yticks([0,0.95*0.8,0.8,1.05*0.8,1,smax],["0","$0.95s(\infty)$","$s(\infty)$","$1.05s(\infty)$","$e(\infty)=E$","$\max(s(t))$"])
    plt.grid()
    plt.legend()


Stabilité
+++++++++

La première chose à évaluer est la stabilité du système. Un système est dit stable, au sens BIBO (Bounded Input Bounded Output),
si et seulement si pour tout :math:`t` 

.. math ::

    |e(t)|<\infty ~\Rightarrow~|s(t)|<\infty

En d'autres termes, une entrée bornée doit conduire à une sortie bornée.

Précision
+++++++++

Une autre caractéristique importante d'un asservissement est sa précision. Pour mesurer la précision, un critère possible consiste à mesurer l'écart statique entre l'entrée et la sortie c-à-d :math:`\epsilon = e(\infty)-s(\infty)`. En pratique, 
nous préférons utiliser l'écart statique relatif qui est une mesure généralement indépendante de l'amplitude de l'entrée. 

L'écart statique relatif est défini par :

.. math ::

    \epsilon_r (\%) = 100 \times \left(\frac{e(\infty)-s(\infty)}{e(\infty)}\right)

Pour un système précis, l'écart statique relatif doit être nul.

Rapidité
++++++++

En plus du comportement statique, il est souvent important de critiquer le comportement dynamique du système. Pour critiquer 
le comportement dynamique, il est courant d'analyser la rapidité du système via sa réponse indicielle. Pour mesurer la rapidité, un critère possible
est le temps de réponse à :math:`\pm 5\%`. 

Le temps de réponse à :math:`\pm 5\%` est défini par :

.. math ::

    \forall t>t_r,~0.95 s(\infty) \le s(t) \le 1.05 s(\infty)

En d'autres termes, le temps de réponse correspond au temps nécessaire pour rentrer **définitivement** dans une fourchette comprise entre 
:math:`-5\%` et :math:`+5\%` de la valeur finale. Plus un système est rapide, plus son temps de réponse est faible.

Dépassement
+++++++++++

Une autre caractéristique importante concerne la présence ou nom d'oscillation au niveau de la réponse indicielle.
Pour quantifier les oscillations, une critère possible consiste à mesurer le premier dépassement :math:`D = \max[s(t)]-s(\infty)`. Le plus souvent, nous préférons utiliser la valeur du premier dépassement 
relatif qui est une mesure généralement indépendante de la valeur finale. 

Le premier dépassement relatif est défini par 

.. math ::

    D_r(\%)=100 \times \frac{\max[s(t)]-s(\infty)}{s(\infty)}


Robustesse
++++++++++

Le plus souvent, l'analyse d'un système est réalisé sous l'hypothèse que nous connaissons exactement les comportements des différents
blocs. Le plus souvent, ces comportements sont modélisés par des équations différentielles ou par des équations aux différences. 
Cette modélisation est, dans le meilleur des cas, une approximation de la réalité. Dans ce contexte, il est important d'évaluer la robustesse des stratégies de 
commande en présence d'écart de modélisation.

Pour mesure la robustesse d'un asservissement, une approche couramment utilisée consiste à analyser l'influence de perturbations extérieures sur le 
comportement du système. Ces perturbations peuvent être déterministes ou aléatoires.

.. figure:: img/representation6.svg
  :width: 650
  :align: center
  :alt: Modélisation Schéma Bloc

  Influence des perturbations
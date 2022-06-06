Liste des correcteurs
=====================

Contexte
--------

Considérons un système en boucle fermée avec un retour unitaire 

.. figure:: img/closed_loop_2d.svg
  :width: 300
  :align: center
  :alt: Boucle Fermée avec Retour unitaire

  Boucle Fermée avec Retour Unitaire

* :math:`E(z)`: Transformée de Laplace de la consigne,
* :math:`C(z)`: Fonction de transfert du correcteur,
* :math:`F(z)`: Fonction de transfert du système + capteur avec BOZ,
* :math:`C(z)F(z)`: Fonction de transfert en boucle ouverte (FTBO).

Correcteurs Usuels 
------------------

Pour respecter les contraintes du cahier des charges, nous pouvons utiliser différents types de correcteurs :math:`C(z)` dont les 
expressions sont basés sur des correcteurs analogiques.

Proportionnel
+++++++++++++

La fonction de transfert du correcteur P est donnée par:

.. math ::

    C(z) = K_c

* Paramètre du correcteur: :math:`K_c`

Proportionnel Intégral
++++++++++++++++++++++ 

En "numérisant" l'intégration continue, la fonction de transfert d'un correcteur PI numérique est donnée par

.. math ::

  C(z)=K_p\left(1+\frac{T_e}{T_i}\frac{z}{z-1}\right)

* Paramètres du correcteur: :math:`K_c`, :math:`T_i`


Proportionnel Intégral Dérivé
+++++++++++++++++++++++++++++

La fonction de transfert du correcteur PID numérique est donnée par:

.. math ::

  C(z)=K_p\left(1+\frac{T_e}{T_i}\frac{z}{z-1}+\frac{T_d}{T_e}\frac{z-1}{z}\right)

* Paramètres du correcteur: :math:`K_c`, :math:`T_i`, :math:`T_d`

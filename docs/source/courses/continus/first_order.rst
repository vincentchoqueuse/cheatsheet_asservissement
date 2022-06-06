Systèmes de 1er ordre
=====================

Modélisation
------------

Equation Différentielle
+++++++++++++++++++++++

Un système LTI peut être décrit par une équation différentielle de liant l'entrée :math:`e(t)` et la sortie :math:`s(t)`.
Pour les systèmes passe-bas d'ordre 1, cette équation différentielle est donnée par: 

.. math ::

    \tau \frac{d s(t)}{dt} + s(t)= Ke(t)

* :math:`K` : gain statique,
* :math:`\tau` : constante de temps (s).

Fonction de Transfert
+++++++++++++++++++++

Pour faciliter l'analyse des systèmes LTI, il est courant de recourir à la notion de fonction de transfert. En utilisant les propriétés
de la transformée de Laplace, il est possible d'établir que la fonction de transfert d'un système LP d'ordre 1 est donnée par:

.. math ::

    H(p)=\frac{S(p)}{E(p)}=\frac{K}{\tau p +1}

Cette fonction de transfert possède:

* un unique pôle négatif en :math:`p=-\frac{1}{\tau}`,
* aucun zéro. 


Réponse indicielle
------------------

La réponse indicielle correspond à la réponse du système lorsque l'entrée est un échelon c-à-d 

.. math ::

    e(t)=Eu(t)=\left\{\begin{array}{cl} E &\text{ si }t\ge 0\\
    0&\text{ sinon}\\
    \end{array}\right.

Pour le cas d'un système LP d'ordre 1, la réponse indicielle est donnée par :

.. math ::

    s(t)=KE\left(1-e^{-\frac{1}{\tau}t}\right)u(t)

Exemple
+++++++

La figure suivante présente l'allure de la réponse indicielle à un échelon d'amplitude :math:E. Cette réponse suit une exponentielle croissante et se stabilise vers une valeur finie.

.. plot::
    :context: close-figs
    :include-source: false

    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K, tau = 2,3
    sys = lti([K],[tau,1])
    t,s = sys.step()

    # plot figure
    plt.plot(t,s)
    plt.grid()
    plt.axhline(y = 2, color = 'r', linestyle = '--')
    plt.axhline(y = 1.9, color = 'r', linestyle = '--')
    plt.axvline(x = 9, color = 'r', linestyle = '--')
    plt.xlabel("time [s]")
    plt.yticks([1.9,2], ["$0.95KE$","$KE$"])
    plt.xticks([9], ["$3\\tau$"])
    plt.ylabel("s(t)")
    plt.xlim([0,20])
    plt.ylim([0,2.2])

Propriétés
++++++++++

* Valeur initiale : :math:`s(0)=0`,
* Valeur finale : :math:`s(\infty)=KE`,
* Temps de réponse à :math:`\pm 5\%` : :math:`s(t_r)=0.95s(\infty)` avec :math:`t_r\approx 3\tau` s,
* Pas de dépassement : :math:`s(\infty)=\max(s(t))=KE`.

Identification
++++++++++++++

L'identification graphique des paramètres peut s'obtenir de la manière suivante:

* Gain statique: le gain statique s'obtient à partir de la valeur finale via la relation :math:`K = s(\infty)/E`.
* Constante de temps: la constante de temps peut s'obtenir à partir du temps de réponse via la relation :math:`t_r = 3\tau`.


Réponse Fréquentielle
---------------------

La réponse fréquentielle s'obtient en posant :math:`p=j\omega` où :math:`\omega` désigne la pulsation (en rad/s). La réponse fréquentielle d'un système LP de premier ordre est donnée par :

.. math ::

    H(j\omega)=\frac{K}{1+j\omega \tau}


La réponse fréquentielle est une fonction :math:`\mathbb{R} \to \mathbb{C}`. Pour représenter cette réponse, il est courant
de recourir à la représentation du module et de l'argument en fonction de :math:`\omega`.

Module 
++++++

.. plot::
    :context: close-figs
    :include-source: false

    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K, tau = 2,3
    sys = lti([K],[tau,1])
    w,Hjw = sys.freqresp(w=np.logspace(-2,1,100))
    wc = 1/tau
    Hjwc = K/np.sqrt(2)

    plt.loglog(w,np.abs(Hjw))
    plt.plot([0,wc,wc],[Hjwc,Hjwc,0],'r--')
    plt.plot([0,10],[K,K],'r--')
    plt.plot([0.01,10],[K*(wc/0.01),K*wc/10],'r--')
    plt.ylim([0.1,3])
    plt.xlim([0.01,10])
    plt.yticks([K,K/np.sqrt(2)], ["$G_0$","$G_0-3$"])
    plt.xticks([wc], ["$\omega_c = 1/\\tau$"])
    plt.grid()
    plt.xlabel("$w$ [rad/s]")
    plt.ylabel("$|H(j\omega)|_{dB}$");

Le module s'exprime sous la forme

.. math ::

    |H(j\omega)|=\frac{|K|}{\sqrt{1+(\omega\tau)^2}}

* Amplification basse-fréquence : :math:`\lim_{\omega\to 0}|H(j\omega)|=|K|`,
* Amplification haute-fréquence : :math:`\lim_{\omega\to \infty}|H(j\omega)|=0`.
* Pulsation de coupure à -3dB : :math:`|H(j\omega_c)|=|K|/\sqrt{2}` pour :math:`\omega_c=\frac{1}{\tau}` rad/s.
* Comportement asymptotique : Pour :math:`\omega \gg \omega_c`, :math:`|H(j\omega)|\approx K \left(\frac{\omega}{\omega_c}\right)^{-1}` (pente de -1)


Argument
++++++++

.. plot::
    :context: close-figs
    :include-source: false

    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K, tau = 2,3
    sys = lti([K],[tau,1])
    w,Hjw = sys.freqresp(w=np.logspace(-2,1,100))
    wc = 1/tau
    Hjwc = K/np.sqrt(2)

    plt.semilogx(w,180*np.angle(Hjw)/np.pi)
    plt.plot([0,wc,wc],[-45,-45,-90],'r--')
    plt.ylim([-90,0])
    plt.xlim([0.01,10])
    plt.xticks([wc], ["$\omega_c = 1/\\tau$"])
    plt.yticks([-45], ["$-45^o$"])
    plt.grid()
    plt.xlabel("$w$ [rad/s]")
    plt.ylabel("$\\arg[H(j\omega)]$");

Pour :math:`K>0`, l'argument s'exprime sous la forme :

.. math ::

    \arg[H(j\omega)]=-\arctan(\omega\tau)

Nous obtenons alors les propriétés suivantes :

* Déphasage basse-fréquences : :math:`\lim_{\omega\to 0}\arg[H(j\omega)]=0`,
* Déphasage haute-fréquences : :math:`\lim_{\omega\to \infty}\arg[H(j\omega)]=-90^o`.
* Déphasage à la pulsation de coupure à -3dB : :math:`\arg[H(j\omega_c)]=-45^o`.

Identification
++++++++++++++

L'identification graphique des paramètres s'obtient de la manière suivante:

* Gain statique: le gain statique correspond à la valeur du module en basse-fréquence. Si le module est affiché en dB, la valeur du module s'obtient via l'expression :math:`K = 10^{G_0/20}`. Attention à bien vérifier que la phase évolue de :math:`0` à :math:`-90^o`. Si ca n'est pas le cas, le gain est négatif. 
* Constante de temps: la constante de temps s'obtient à partir de la lecture de la pulsation de coupure via l'expression :math:`\omega_c = 1/\tau`.

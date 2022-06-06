Systèmes de 2nd ordre
=====================

Modélisation
------------

Equation Différentielle
+++++++++++++++++++++++

Pour un système passe-bas linéaire d'ordre 2, le lien entre l'entrée et la sortie peut être décrit par une équation différentielle de second ordre à coefficients constants.

.. math :: 

    \frac{1}{\omega_n^2}\frac{d^2 s(t)}{dt^2}+\frac{2m}{\omega_n}\frac{d s(t)}{dt}+s(t)=Ke(t)

* :math:`K` : gain statique,
* :math:`m \ge 0` : coefficient d'amortissement,
* :math:`\omega_n` : pulsation propre (en rad/s).

Notons que certains ouvrages préfèrent utiliser, au lieu du paramètre :math:`m`, le facteur de qualité 

* :math:`Q=\frac{1}{2m}` : facteur de qualité.



Fonction de Transfert 
+++++++++++++++++++++

La fonction de transfert d'un système passe-bas de second ordre est donnée par :

.. math :: 

    H(p)=\frac{K}{\frac{1}{\omega_n^2}p^2+\frac{2m}{\omega_n}p+1}

Pôles 
-----

Expression
++++++++++

Les pôles correspondent aux valeurs de :math:`p` pour lesquelles 

.. math ::

    \frac{1}{\omega_n^2}p^2+\frac{2m}{\omega_n}p+1 = 0

Le calcul des pôles s'obtient en recherchant les racines d'une équation du second degré. Le discriminant s'exprime sous la forme :

.. math ::

    \Delta =\frac{4}{\omega_n^2}(m^2-1)

Nous pouvons alors distinguer trois cas de figure :

- :math:`m>1`: deux pôles réels
    
  * :math:`p_{1}=-\omega_n(m-\sqrt{m^2-1})`
  * :math:`p_{2}=-\omega_n(m+\sqrt{m^2-1})`
   
- :math:`m=1`: un pôle double
    
  * :math:`p_1 = p_2 = -m\omega_n`

- :math:`m<1`: deux pôles complexe-conjugués
    
  * :math:`p_{1}=-\omega_n(m-j\sqrt{1-m^2})`
  * :math:`p_{2}=-\omega_n(m+j\sqrt{1-m^2})`

Exemple 
+++++++

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    import matplotlib.pyplot as plt


    m_vect = [0.5,1,1.25]
    w0 = 1

    fig = plt.figure(figsize=[7,4.8])

    for m in m_vect:
        poles = np.sort(np.roots([1/(w0**2),2*m/w0,1]))
        plt.plot(np.real(poles),np.imag(poles),'x',label="m={}".format(m))

    plt.xlabel("$\Re e(.)$")
    plt.ylabel("$\Im m(.)$")
    plt.legend()
    plt.grid()
    plt.axis("equal")
    plt.xlim([-4,2])


Identification
++++++++++++++

Lorsque :math:`0\le m<1`, l’identification de la pulsation propre et coefficient d'amortissement peut s’obtenir de la manière suivante:
    
* Pulsation propre: la pulsation propre correspond au module des pôles c-à-d :math:`\omega_n=|p_{k}|`,
* Coefficient d’amortissement: le coefficient d'amortissement s'obtient à partir de la partie réel des pôles via la relation :math:`m=-\Re e(p_{k})/|p_{k}|`.

Notons qu'il n'est pas possible d'identifier le gain statique en utilisant la position des pôles. 

Réponse Indicielle
-------------------

Cas où :math:`m>1`
++++++++++++++++++

La figure suivante présente l'allure de la réponse indicielle lorsque :math:`m>1`. Dans ce contexte, la réponse est monotone et ne présente pas de 
dépassement.

.. plot ::
    :context: close-figs
    :include-source: false

    from scipy.signal import lti
    import matplotlib.pyplot as plt

    K1, m1, wn1 = 10,2,100
    H1 = lti([K1],[1/(wn1**2),2*m1/wn1,1])
    E = 1
    t,s = H1.step(T=np.arange(0,0.25,0.001))  #E=1
    tr = 3/(-H1.poles[1])

    plt.plot(t,s)
    plt.plot([0,tr,tr],[0.95*K1*E,0.95*K1*E,0],'r--')
    plt.grid()
    plt.xticks([tr],["$t_r\approx -3/p_1$"])
    plt.yticks([K1*E,0.95*K1*E],["$s(\infty)=KE$","$0.95KE$"])
    plt.xlim([0,0.25])
    plt.ylim([0,11])
    plt.xlabel("temps [s]");

La réponse indicielle s'exprime sous la forme :

.. math ::

    s(t)=KE\left(1-\frac{1}{2\omega_n\sqrt{m^2-1}}\left(p_1 e^{p_2 t}-p_2 e^{p_1 t} \right)\right)u(t)

**Propriétés**

* Valeur initiale : :math:`s(0)=0`,
* Valeur finale : :math:`s(\infty)=KE`,
* Temps de réponse à :math:`\pm 5\%` : Pas de formule simple. Lorsque :math:`m\gg 1`, le temps de réponse est dicté par le pôle le plus lent c-a-d :math:`t_r\approx -\frac{3}{p_1}`,
* Pas de dépassement : :math:`s(\infty)=\max(s(t))=KE`.

Cas où :math:`m<1`
++++++++++++++++++

La figure suivante présente l'allure de la réponse indicielle lorsque :math:`m<1`. Dans ce contexte, la réponse présente un dépassement plus ou moins important 
et des oscillations de pseudo-pulsation :math:`\omega_p`. Pour analyser les performances d'un système de second ordre lorsque :math:`m<1`, nous utilisons principalement des abaques.


.. plot ::
    :context: close-figs
    :include-source: false

    K3, m3, wn3 = 10,0.05,100
    H3 = lti([K3],[1/(wn3**2),2*m3/wn3,1])
    E = 1
    t,s = H3.step(T=np.arange(0,0.7,0.001))  #E=1
    Dr = np.exp(-np.pi*m3/np.sqrt(1-m3**2))

    plt.plot(t,s)
    plt.plot(t,K3*E*(1+(1/np.sqrt(1-m3**2))*np.exp(-m3*wn3*t)),'r--')
    plt.plot(t,K3*E*(1-(1/np.sqrt(1-m3**2))*np.exp(-m3*wn3*t)),'r--')
    plt.plot([0,0.7],[K3*E,K3*E],'r--')
    plt.plot([0,0.7],[K3*E*(1+Dr),K3*E*(1+Dr)],'r--')
    plt.yticks([K3*E,K3*E*(1+Dr)],["$s(\infty)$","$\max[s(t)]$"])
    plt.grid()
    plt.xlim([0,0.7])
    plt.xlabel("temps [s]")

La réponse indicielle s'exprime sous la forme :

.. math ::

    s(t)=KE\left(1-\frac{1}{\sqrt{1-m^2}}e^{-m\omega_nt}\cos\left(\omega_n\sqrt{1-m^2}t-\arcsin(m)\right)\right)u(t)


**Propriétés**

* Valeur initiale : :math:`s(0)=0`,
* Valeur finale : :math:`s(\infty)=KE`,
* Temps de réponse à :math:`\pm 5\%` : Pas de formule simple, nous utiliserons des abaques. Lorsque :math:`m\to 0`, le temps de réponse est approximativement imposé par l'enveloppe c-a-d :math:`t_r\approx \frac{3}{\omega_n m}`,
* Présence d'oscillations à la pseudo-pulsation (rad/s):

.. math ::

    \omega_p = \omega_n\sqrt{1-m^2}

* Premier Dépassement relatif : 

.. math ::

    D_r(\%)=\frac{\max[s(t)]-s(\infty)}{s(\infty)} =e^{\frac{-\pi m}{\sqrt{1-m^2}}}


.. note ::
    
    En pratique, nous utiliserons des abaques pour déterminer le temps de réponse et le premier dépassement relatif : https://vincentchoqueuse.github.io/ENIB_tools/control_settling_time.html

Identification
++++++++++++++

Lorsque :math:`m<1`, l'identification graphique des paramètres peut s'obtenir de la manière suivante:

* Gain statique: le gain statique s'obtient à partir de la valeur finale via la relation :math:`K = s(\infty)/E`.
* Coefficient d'amortissement: le coefficient d'amortissement s'obtient en mesurant la valeur du premier dépassement relatif et en utilisant l'abaques donnant :math:`D_r(\%)` en fonction de :math:`m`.
* Pulsation propre: la pulsation propre s'obtient en mesurant la valeur du temps de réponse à :math:`\pm 5\%` et en utilisant la valeur de :math:`m` ainsi que l'abaque donnant :math:`\omega_n t_r = f(m)`.


Réponse Fréquentielle
---------------------

La réponse fréquentielle s'obtient en posant :math:`p=j\omega` où :math:`\omega` désigne la pulsation (en rad/s). La réponse fréquentielle d'un système passe-bas de premier ordre est donnée par :

.. math ::

    H(j\omega)=\frac{K}{1-\frac{\omega^2}{\omega_n^2}+j\frac{2m\omega }{\omega_n}}

Module
++++++

La figure suivante présente l'allure le module de la réponse fréquentielle. Lorsque :math:`m<0.7`, le module présente un maximum à la pulsation de 
résonance :math:`\omega_r`.

.. plot ::
    :context: close-figs
    :include-source: false

    w,H3jw = H3.freqresp(w=np.logspace(0,4,200))
    K3, m3, wn3 = 10,0.05,100
    H3 = lti([K3],[1/(wn3**2),2*m3/wn3,1])
    wr = wn3*np.sqrt(1-2*m3**2)
    Gm = K3/(2*m3*np.sqrt(1-m3**2))
    ax = plt.loglog(w,np.abs(H3jw))
    plt.plot([0,wr,wr],[K3/(2*m3*np.sqrt(1-m3**2)),K3/(2*m3*np.sqrt(1-m3**2)),0],'r--')
    plt.plot([1,100],[K3,K3],'r--')
    plt.plot([1,10000],[K3*(wn3/1)**2,K3*(wn3/10000)**2],'r--')
    plt.grid()
    plt.ylim([0.001,200])
    plt.xlim([1,10000])
    plt.yticks([K3,Gm],["$G_{0}$", "$G_{m}$"])
    plt.xticks([wr],["$\omega_r$"])
    plt.xlabel("$w$ [rad/s]")
    plt.ylabel("$|H(j\omega)|_{dB}$")

Le module s'exprime sous la forme

.. math ::

    |H(j\omega)|=\frac{|K|}{\sqrt{\left(1-\frac{\omega^2}{\omega_n^2}\right)^2+\frac{4m^2\omega^2}{\omega_n^2}}}


**Propriétés**

* Amplification basse-fréquence : :math:`\lim_{\omega\to 0}|H(j\omega)|=|K|`,
* Amplification haute-fréquence : :math:`\lim_{\omega\to \infty}|H(j\omega)|=0`,
* Comportement asymptotique : Pour :math:`\omega \gg \omega_n`, :math:`|H(j\omega)|\approx |K| \left(\frac{\omega}{\omega_n}\right)^{-2}` (pente de -2),

Si :math:`m<\frac{1}{\sqrt{2}}\approx 0.7`, il est possible de montrer que la dérivée du module présente un zéro. Dans ce contexte, le module présente un extremum nommé résonance.

* Pulsation de résonance : 

.. math ::

    \omega_r = \omega_n \sqrt{1-2m^2}

* Maximum du module : le maximum est égal à :math:`|H(j\omega_r)|=|K|/(2m\sqrt{1-m^2})`. En pratique, nous utiliserons essentiellement le facteur de resonance :math:`M` qui s'obtient en divisant le module à la pulsation de résonance par le module du gain statique c-à-d

.. math ::

    M=\frac{|H(j\omega_r)|}{|K|}=\frac{1}{2m\sqrt{1-m^2}}


En dB, le facteur de résonance s'exprime sous la forme 

.. math :: 

    M_{dB} = G_{m} - G_{0}

* :math:`G_{m} = 20 \log_{10}(|H(j\omega_r)|)` correspond au module à la pulsation de résonance en dB,
* :math:`G_{0} = 20 \log_{10}(|K|)` correspond au module du gain statique en dB.

.. note ::

    En pratique, nous utiliserons des abaques pour déterminer le facteur de résonance en dB : https://vincentchoqueuse.github.io/ENIB_tools/control_resonance.html

Argument
++++++++

.. plot ::
    :context: close-figs
    :include-source: false

    w,H3jw = H3.freqresp(w=np.logspace(0,4,200))
    K3, m3, wn3 = 10,0.05,100
    H3 = lti([K3],[1/(wn3**2),2*m3/wn3,1])
    wr = wn3*np.sqrt(1-2*m3**2)
    Gm = K3/(2*m3*np.sqrt(1-m3**2))
    ax = plt.semilogx(w,180*np.angle(H3jw)/np.pi)
    plt.plot([0,wn3,wn3],[-90,-90,-180],'r--')
    plt.grid()
    plt.ylim([-180,0])
    plt.xlim([1,10000])
    plt.xticks([wn3],["$\omega_n$"])
    plt.xlabel("$w$ [rad/s]")
    plt.ylabel("$\\arg[H(j\omega)]$ (deg)")


Lorsque :math:`K>0`, l'argument s'exprime sous la forme

.. math ::

    \arg[H(j\omega)]=-\textrm{arctan}\left(\frac{1}{2m} \left( \frac{\omega}{\omega_n} - \frac{\omega_n}{\omega}\right)  \right) - \frac{\pi}{2} 


**Propriétés**

Si :math:`K>0`, nous obtenons les propriétés suivantes.

* Déphasage basse-fréquence : :math:`\lim_{\omega\to 0}\arg[H(j\omega)]=0`,
* Déphasage haute-fréquence : :math:`\lim_{\omega\to \infty}\arg[H(j\omega)]=-180^o`.
* Déphasage à la pulsation propre : :math:`\arg[H(j\omega_n)]=-90^o`.

Identification
++++++++++++++

L'identification graphique des paramètres peut s'obtenir de la manière suivante:

- Gain statique: le gain statique correspond à la valeur du module en basse-fréquence. Si le module est affiché en dB, la valeur du module s'obtient via l'expression :math:`K = 10^{G_0/20}`. Attention à bien vérifier que la phase évolue de :math:`0` à :math:`-180^o`. Si ca n'est pas le cas, le gain est négatif. 
- Coefficient d'amortissement: le coefficient d'amortissement s'obtient en mesurant le facteur de résonance :math:`M_{dB}` et en utilisant l'abaque donnant le facteur de résonance en dB en fonction de :math:`m`.
- Pulsation propre: la pulsation propre peut s'obtenir de deux façons.

  - Si la phase est disponible, la pulsation propre s'obtient en déterminant la pulsation telle que :math:`\arg[H(j\omega)] = -90^o` (lorsque :math:`K` est positif).
  - Si la phase n'est pas disponible, la pulsation propre s'obtient à partir de la valeur de :math:`m` et de la mesure de la pulsation résonance :math:`\omega_r`, puis en utilisant la relation :math:`\omega_r = \omega_n \sqrt{1-2m^2}`.


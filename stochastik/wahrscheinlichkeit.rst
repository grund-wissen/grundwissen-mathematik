.. _Wahrscheinlichkeitsmaße:

Wahrscheinlichkeitsmaße
=======================

.. index::
    single: Häufigkeit
    single: Häufigkeit; absolute Häufigkeit
    single: Häufigkeit; relative Häufigkeit

.. _Relative Häufigkeit:

Die relative Häufigkeit
-----------------------

Um die relative Häufigkeit eines Ereignisses :math:`M` bei einem
Zufallsexperiment zu bestimmen, wird dieses :math:`n` mal durchgeführt und
gezählt, wie oft das Ereignis :math:`M` eintritt. Die relative Häufigkeit
:math:`h(M)` ist dabei folgendermaßen definiert:

.. math::

    h(M) = \frac{z(M)}{n}

Die Größe :math:`z(M)` wird dabei "absolute" Häufigkeit des Ereignisses
:math:`M` genannt und gibt an, wie häufig das Ereignis :math:`M` bei dem
Zufallsexperiment insgesamt eingetreten ist.

Bei großen Versuchszahlen gilt für die relative Häufigkeit das so genannte
Gesetz der großen Zahlen: Die relative Häufigkeit :math:`h(M)` eines
Ereignisses :math:`M`  weicht bei einem genügend großen Wert von :math:`n` nur
wenig von einem bestimmten, für das Ereignis charakteristischen Wert ab.

Besteht die Menge :math:`M` aus den Elementen :math:`\omega _1, \ldots,
\omega_m`, so gilt für die relative Häufigkeit bei einer Reihe von :math:`n`
Versuchen:

.. math::

    h(M) = \frac{z(M)}{n} = \frac{z(\{\omega_1\}) + z(\{\omega_2\}) + \ldots +
    z(\{\omega _{\rm{n}}\})}{n} = h(\{\omega_1\}) + h(\{\omega_2\}) + \ldots +
    h(\{\omega _{\rm{n}}\})

Die relative Häufigkeit von :math:`M` ist also gleich der Summe der relativen
Häufigkeiten aller Elementarereignisse, die in :math:`M` enthalten sind.

Allgemein gilt für die relative Häufigkeit stets :math:`0 \le h(M) \le 1`,
wobei :math:`h(M) = 0` für ein unmögliches und :math:`h(M) = 1` für ein
sicheres Ereignis gilt. Sind zudem zwei Ereignisse :math:`M_1` und :math:`M_2`
unvereinbar, d.h. gilt :math:`M_1 \cap M_2 = \emptyset`, so gilt :math:`h(M_1
\cup (M_2) = h(M_1) + h(M_2)`.

.. index:: Wahrscheinlichkeit
.. _Wahrscheinlichkeit:

Die Wahrscheinlichkeit
----------------------

Als Wahrscheinlichkeit bezeichnet man ein Maß für das Eintreten eines
Ereignisses :math:`M`.

Prinzipiell kann nach dem empirischen Gesetz der großen Zahlen
für die Wahrscheinlichkeit folgende Festsetzung genutzt werden:

.. math::

    P(M) = \lim _{n \rightarrow \infty} h(M)

In der Praxis lassen sich jedoch stets nur eine begrenzte Zahl :math:`n` an
Versuchen durchführen. Man definiert den Wahrscheinlichkeitsbegriff daher
über folgende Axiome:

*Definition:*

    Eine Abbildung der Form :math:`M \subset \mathcal{ P }(\Omega ) \rightarrow P(A) \in
    \mathbb{R}` heißt Wahrscheinlichkeitsmaß, wenn folgende Eigenschaften
    ("Axiome von Kolmogoroff") erfüllt sind:

    * Nichtnegativität: Für alle :math:`M \in \mathcal{ P }(\Omega)` gilt:

      .. math::

          P(M) \ge 0

    * Normiertheit: Ist :math:`M = \Omega`, so gilt:

      .. math::

          P(\Omega) = 1

    * Additivität: Für :math:`M_1 \cap M_2 = \emptyset` gilt:

      .. math::

          P(M_1 \cup M_2) = P(M_1) + P(M_2)

      Die Additivität gilt auch für mehrere Ereignisse :math:`M_1 ,\, M_2 ,\,
      \ldots`, wenn diese paarweise unvereinbar sind, d.h. wenn :math:`M_i \cap
      M_j = \emptyset` für :math:`i \ne j` gilt.

..  Insbesondere ist die Wahrscheinlichkeit eines Ereignisses :math:`M` somit gleich
..  der Summe der Wahrscheinlichkeiten aller jeweiligen Elementarereignisse:

..  ..  .. math::

..  ..  P(M) = \sum_{\omega \in M}^{} P(\{\omega\})

Die Zahl :math:`p(M)` wird dabei als Wahrscheinlichkeit des Ereignisses
:math:`M` bezeichnet.

Zu einem Zufallsexperiment sind beliebig viele unterschiedliche
Wahrscheinlichkeitsmaße denkbar. Welches Maß dabei das "Richtige" ist, hängt
von den physikalischen Gegebenheiten des Experiments ab. Bei einem "normalen"
Würfel erwartet man beispielsweise, dass die Wahrscheinlichkeit :math:`P` für
jede Augenzahl gleich :math:`\frac{1}{6}` ist; hat der Würfel jedoch kleine
Unregelmäßigkeiten, so können diese zur Folge haben, dass nicht mehr alle
Elementarereignisse gleich wahrscheinlich sind.

Zusätzlich zu den obigen Axiomen gelten als Folgerungen einige weitere
Eigenschaften für Wahrscheinlichkeitsmaße:

* Ist :math:`P(M)` die Wahrscheinlichkeit eines Ereignisses :math:`M`, so ist
  :math:`P(\bar{M}) = 1-P(M)` die Wahrscheinlichkeit des Gegenereignisses
  :math:`\bar{M}`. [#]_

* Ist :math:`M_1 \subset M_2`, so gilt :math:`P(M_1) \le P(M_2)`.
  Diese Eigenschaft wird auch "Monotonieregel" genannt. [#]_

* Es gilt stets: :math:`P(M_1 \cap \bar{M_2}) = P(M_1) - P(M_1 \cap M_2)`.
  Diese Eigenschaft wird auch "Zerlegungsregel" genannt. [#]_

* Es gilt stets: :math:`P(M_1 \cup M_2) = P(M_1) + P(M_2) - P(M_1 \cap M_2)`
  Diese Eigenschaft wird auch "Additionsregel" genannt. [#]_

.. rubric:: Wahrscheinlichkeit bei Laplace-Experimenten

Sind alle Elementarereignisse gleich wahrscheinlich, so bezeichnet man das
Zufallsexperiment als "Laplace-Experiment". Wahrscheinlichkeiten, die unter
dieser Annahme berechnet werden, nennt man entsprechend
"Laplace-Wahrscheinlichkeiten".

Hat ein Laplace-Experiment :math:`n` Elementarereignisse, d.h. ist
:math:`|\Omega| = n`, so gilt :math:`P = \frac{1}{n}` für jedes
Elementarereignis :math:`\{\omega\}`. Für ein Ereignis :math:`M = \{ \omega _1
,\, \omega _2 ,\, \ldots ,\, \omega _{\rm{k}}\}` mit :math:`k \le n` gilt
entsprechend:

.. math::

    P(M) = \frac{\text{Anzahl der günstigen Ergebnisse}}{\text{Anzahl der
    möglichen Ergebnisse}}= \frac{|M|}{|\Omega|}

Um die Anzahl der günstigen und der möglichen Ergebnisse zu bestimmen, werden
üblicherweise Methoden aus der Kombinatorik genutzt.


.. Wahrscheinlichkeitsverteilung: Wahrscheinlichkeitsmass für
.. Elementarereignisse (beschränkt auf Elementarereignisse)

.. Urliste, Stabdiagramm, Histogramm, Kreisdiagramm, Pictogramm

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Dass diese Gleichung gilt, folgt aus :math:`1 = P (\Omega) = P (M \cup
    \bar{M}) = P(M) + P(\bar{M})`.

.. [#] Dass diese Gleichung gilt, lässt sich wegen :math:`M_2 = (M_2 \cap
    \bar{M_1}) \cup M_1` zeigen:

    .. math::

        P(M_2) = P((M_2 \cap \bar{M_1}) \cup M_1) = P(M_2 \cap \bar{M_1}) +
        P(M_1)

    Wegen :math:`0 \le P(M_2 + \bar{M_1})` folgt :math:`P(M_1) \le P(M_2)`.

.. [#] Diese Eigenschaft ergibt sich aus :math:`M_1 = (M_1 \cap \bar{M_2}) +
    (M_1 \cap M_2)`. Damit gilt ebenfalls :math:`P(M_1 \cap \bar{M_2}) = P(M_1) -
    P(M_1 \cap M_2)`.

.. [#] Diese Eigenschaft gilt wegen :math:`P(M_1 \cup M_2) = P(M_1 \cup (M_2
    \cap \bar{M_1})) = P(M_1) + P(M_2 \cap \bar{M_1})`. Aufgrund der obigen
    Beziehung gilt zudem :math:`P(M_2 \cap \bar{(M_1)}) = P(M_2) - P(M_1 \cap
    M_2)`. Ein Einsetzen der zweiten Gleichung in die erste liefert die
    Additionsregel.




.. _Bernoulli-Experimente:

Bernoulli-Experimente
=====================

Als `Bernoulli <https://de.wikipedia.org/wiki/Jakob_I._Bernoulli>`_-Experiment
bezeichnet man ein Zufallsexperiment mit nur zwei möglichen Ergebnissen. Meist
verwendet man dabei als Ergebnismenge :math:`\Omega = \{ 0 ,\, 1 \}`, wobei
:math:`1` als Symbol für das Eintreten des Ereignisses ("Treffer") und :math:`0`
als Symbol für das Nichteintreten des Ereignisses ("Niete") benutzt wird.
Zusätzlich ist es üblich, mit :math:`p = P(\{ 1 \} )` die Wahrscheinlichkeit
für einen Treffer und mit :math:`q = P(\{ 0 \} )` die Wahrscheinlichkeit für
eine Niete zu bezeichnen.

Wird ein Bernoulli-Experiment mehrfach durchgeführt, wobei sich die einzelnen
Versuchen nicht beeinflussen und die Trefferwahrscheinlichkeiten bei allen
Versuchen gleich groß sind, so spricht man von einer Bernoulli-Kette. Eine
solche Bernoulli-Kette lässt sich ebenfalls durch einen Ergebnisbaum
veranschaulichen.

Betrachtet man ein Ereignis mit genau :math:`k` Treffern, so lassen sich mittels
des Ergebnisbaums folgende Gesetzmäßigkeiten herleiten:

* Jeder einzelne Weg im Ereignisbaum, der über :math:`k` Einsen und :math:`n-k`
  Nullen führt, setzt sich aus :math:`k` Teilstücken mit der Wahrscheinlichkeit
  :math:`p` sowie :math:`(n-k)` Teilstücken mit der Wahrscheinlichkeit
  :math:`q=(1-p)` zusammen.
  Nach der Multiplikationsregel für bedingte Wahrscheinlichkeiten ist somit die
  Wahrscheinlichkeit für jeden Weg mit genau :math:`k` Treffern gleich :math:`p
  ^k \cdot q ^{n-k}`.

* Um die Anzahl an Wegen mit genau :math:`k` Einsen zu ermitteln, muss bestimmt
  werden, auf wie viele verschiedene Arten es möglich ist, :math:`k` Einsen auf
  :math:`n` Stellen zu verteilen. Es handelt sich hierbei um Kombinationen ohne
  Wiederholung, da jeder Weg nur einmal gezählt werden darf und die Reihenfolge,
  in der die einzelnen Wege gezählt werden, ohne Bedeutung ist. Dies entspricht
  dem klassischen "Lotto-Problem", d.h. es gibt :math:`\binom{n}{k} =
  \frac{n!}{k! \cdot (n-k)!}` verschiedene Kombinationen.

Aus beiden Eigenschaften ergibt sich folgende Wahrscheinlichkeit, dass bei einer
Bernoulli-Kette mit einer Länge :math:`n` und einer Wahrscheinlichkeit
:math:`p` genau :math:`T=k` Treffer auftreten:

.. math::
    :label: eqn-bernoulli

    P(T=k) = \binom{n}{k} \cdot p^k \cdot q ^{n-k}

Diese Formel wird häufig als "Formel von Bernoulli" bezeichnet.

.. _Summenwahrscheinlichkeiten bei Bernoulli-Ketten:

.. rubric:: Summenwahrscheinlichkeiten bei Bernoulli-Ketten

Bezeichnet man bei einer Bernoulli-Kette mit einer Länge :math:`n` und einer
Trefferwahrscheinlichkeit :math:`p` das Ereignis "genau :math:`k` Treffer" mit
:math:`M _{\rm{k}}`, so gilt:

.. math::

    P (T \le k) = P (M _0 \cup M_1 \cup \ldots \cup M _{\rm{k}})

und

.. math::

    P (T \ge k) = P (M _k \cup M _{\rm{k+1}} \cup \ldots \cup M _{\rm{n}})

Alle Ereignisse :math:`M _{\rm{i}}`, die jeweils :math:`T=i` Treffer bedeuten,
sind paarweise stochastisch unabhängig; die einzelnen Wahrscheinlichkeiten
können also addiert werden.

Für ein Bernoulli-Experiment mit einer Länge :math:`n` und einer
Trefferwahrscheinlichkeit :math:`p` gelten somit folgende Regeln:

* Für mindestens :math:`k` Treffer:

  .. math::

      P (T \ge k) = \sum_{i=k}^{n}  \binom{n}{i} \cdot p^i \cdot q ^{n-i}


* Für höchstens :math:`k` Treffer:

  .. math::

      P(T \le k) = \sum_{i=0}^{k}  \binom{n}{i} \cdot p^i \cdot q ^{n-i}

* Für mindestens :math:`l` und höchstens :math:`k` Treffer:

  .. math::

      P (l \le T \le k) = \sum_{i=l}^{k}  \binom{n}{i} \cdot p^i \cdot q ^{n-i}

.. Häufig lässt sich der Rechenaufwand reduzieren, indem man die
.. Wahrscheinlichkeit für das Gegenereignis berechnet. Es gilt:

.. .. math::

..     P(T \ge k) = 1 - P (T \le (k-1)

.. und

.. .. math::

..     P(T \le k) = 1 - P (T \ge (k+1)





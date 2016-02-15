
.. _Bedingte Wahrscheinlichkeit:

Bedingte Wahrscheinlichkeit
===========================

*Definition:*

    Bei einem Zufallsexperiment mit der Ergebnismenge :math:`\Omega` werden zwei
    Ereignisse :math:`M_1` und :math:`M_2` mit :math:`P(M_1) > 0` betrachtet.
    Dann bezeichnet man folgenden Ausdruck als bedingte Wahrscheinlichkeit von
    :math:`M_2` unter der Bedingung :math:`M_1`:

    .. math::

        P _{M_1}(M_2) = \frac{P(M_1 \cap M_2)}{P(M_1)}

    Handelt es sich bei :math:`P(M_1)` und :math:`P(M_2)` um
    Laplace-Wahrscheinlichkeiten, so gilt:

    .. math::

        P _{M_1}(M_2) = \frac{P(M_1 \cap M_2)}{P(M_1)} = \frac{|M_1 \cap
        M_2|}{|M_1|}

Die obige Definition lässt sich auch, insbesondere bei der Nutzung von
Baumdiagrammen, als Produktsatz formulieren. Es gilt für die
Wahrscheinlichkeit, dass sowohl :math:`M_1` als auch :math:`M_2` eintreten:

.. math::

    P(M_1 \cap M_2) = P(M_1) \cdot P _{M_1}(M_2)


Für bedingte Wahrscheinlichkeiten gelten zudem folgende Regeln:

* Multiplikationsregel: In einem Ergebnisbaum stellt jeder Knoten ein
  Elementarereignis dar. Die Wahrscheinlichkeit eines bestimmten Ereignisses
  entspricht dabei dem Produkt der Wahrscheinlichkeiten aller
  Elementarereignisse längs des zugehörigen Weges.

* Additionsregel: Besteht ein Ereignis in einem Ereignisbaum aus mehreren Wegen,
  so ist die zugehörige Wahrscheinlichkeit gleich der Summe der
  Wahrscheinlichkeiten für die einzelnen Wege.

.. _Stochatisch unabhängige Ereignisse:

.. rubric:: Stochatisch unabhängige Ereignisse

Ein Ereignis :math:`M_2` ist von einem Ereignis :math:`M_1` unabhängig, wenn
:math:`M_1` auf die Wahrscheinlichkeit von :math:`M_2` keinen Einfluss hat.

*Definition:*

    Ist :math:`\Omega` die Ergebnismenge eines Zufallsexperiments und
    :math:`M_1` und :math:`M_2` zwei Ereignisse mit :math:`P(M_1) > 0`, so nennt
    man :math:`M_2` stochastisch unabhängig von :math:`M_1`, wenn gilt:

    .. math::

        P _{M_1}(M_2) = P(M_2)

    Andernfalls heißt :math:`M_2` stochastisch abhängig von :math:`M_1`.

Ist ein Ereignis :math:`M_2` stochastisch unabhängig vom Ereignis :math:`M_1`,
so ist umgekehrt auch :math:`M_1` stochastisch unabhängig von :math:`M_2`, denn
in diesem Fall gilt:

.. math::

    P _{M_2}(M_1) = \frac{P(M_1 \cap M_2)}{P(M_2)} = \frac{P(M_1)(M_2)
    \cdot P(M_1)}{P(M_2)} = \frac{P(M_2) \cdot P(M_1)}{P(M_2)} = P(M_1)

Als Sonderfall von stochastischer Unabhängigkeit gilt :math:`P(M_1 \cap M_2) =
P(M_1) \cdot P(M_2)` stets auch dann, wenn die Wahrscheinlichkeit von mindestens
einem der beiden Ereignisse gleich Null ist. Allgemein gilt für alle
stochastisch unabhängigen Ereignisse:

.. math::

    M_1 \text{ und } M_2 \text{ sind stochastisch unabhängig} \quad
    \Leftrightarrow \quad P(M_1 \cap M_2) = P(M_1) \cdot P(M_2)

Sind zwei Ereignisse :math:`M_1` und :math:`M_2` stochastisch unabhängig, so
gilt dies auch für die Gegenereignisse. In diesem Fall sind somit auch die
Ereignisse :math:`M_1 \cap \overline{M}_2`, :math:`\overline{M}_1 \cap M_2`
sowie :math:`\overline{M}_1 \cap \overline{M}_2` stochastisch unabhängig.


.. Olmscheid S. 49: Nachweis, dass  :math:`P _{M_1}(M_2)` ein W-Maß ist.
.. -> Übungsaufgabe?



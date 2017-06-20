.. _Eigenschaften von Gleichungen:

Eigenschaften von Gleichungen
=============================

Eine Gleichung entspricht einer :ref:`Aussageform <Aussageform>`, bei der zwei
Terme :math:`T_1` und :math:`T_2` durch die Gleichheits-Relation
:math:`=` miteinander verbunden sind:

.. math::
    :label: eqn-term

    T_1 = T_2

Als Aussageform ist eine Variablengleichung weder wahr noch falsch. Belegt man
allerdings die Variablen mit zulässigen Werten, so nehmen die einzelnen Terme
bestimmte Werte an -- die Gleichung wird hierbei zu einer wahren oder falschen
Aussage. [#]_ Ergibt sich eine wahre Aussage, so wird die Gleichung durch die
eingesetzten Zahlen erfüllt. Diese Zahlen werden als Lösungen der Gleichung
bezeichnet, die Gesamtheit aller Lösungen wird Lösungsmenge :math:`\mathbb{L}`
genannt.

Im einfachsten Fall entsprechen die beiden Terme :math:`T_1` und :math:`T_2`
zwei einzelnen Elementen :math:`x_1` und :math:`x_2` einer Menge
:math:`\mathbb{M}`. Diese können entweder gleich :math:`(x_1 = x_2)` oder
ungleich :math:`(x_1 \ne x_2)` sein. Im ersten Fall stehen die Variablen
:math:`x_1` und :math:`x_2` für das selbe Objekt.

.. _Lösbarkeit:
.. _Lösbarkeit von Gleichungen:

Lösbarkeit von Gleichungen
--------------------------

Ob eine Gleichung lösbar ist, hängt von der Gleichung selbst sowie von dem
vorgegebenen Variablenbereich ("Definitionsmenge" :math:`\mathbb{D}`) ab.

* Ist die Lösungsmenge leer :math:`(\mathbb{L} = \emptyset)`, so ist die
  Gleichung bezüglich :math:`\mathbb{D}` unerfüllbar.
* Ist die Lösungsmenge gleich der Definitionsmenge :math:`(\mathbb{L} =
  \mathbb{D})`, so ist die Gleichung bzgl. :math:`\mathbb{D}` stets erfüllt
  ("allgemeingültig").
* Grundsätzlich ist die Lösungsmenge eine Teilmenge der Definitionsmenge
  :math:`(\mathbb{L} \subseteq \mathbb{D})`.

.. index:: Identität, Gleichung; Identität
.. _Identität:

Allgemeingültige Gleichungen  (auch "Identitäten" genannt) werden oftmals als
Rechenregeln verwendet, da sie unabhängig vom Wert der Variablen stets wahr sind
und somit zur Vereinfachung einzelner Terme genutzt werden können. Gilt nämlich
:math:`a=b`, so kann in jeder Aussage nach Belieben :math:`a` durch :math:`b`
ersetzt werden (Ersetzbarkeits-Theorem von `Leibniz
<https://de.wikipedia.org/wiki/Leibniz>`_).

Ebenfalls können nach diesem Prinzip auch zwei Terme, die jeweils mit einem
dritten übereinstimmen, gleichgesetzt werden. Gilt nämlich :math:`a=b` und
:math:`b=c`, so folgt aus der :ref:`Äquivalenz <Äquivalenzrelation>` der
Gleichheitsrelation automatisch auch :math:`a=c`:


.. math::
    :label: eqn-drittengleichheit

    a = b \quad \text{und} \quad b = c \quad \Rightarrow \quad a = c

.. index:: Gleichung; Bestimmungsgleichung, Bestimmungsgleichung
.. _Bestimmungsgleichung:

Bei algebraischen Aufgaben muss die Lösungsmenge einer Gleichung meist erst
bestimmt werden. Als Unterscheidung zu den stets wahren Identitäten werden
derartige Gleichungen, deren Lösungsmenge erst gefunden werden muss, auch
"Bestimmungsgleichungen" genannt.


*Beispiele:*

* Folgende Gleichung ist für jede reelle Zahl :math:`x \in \mathbb{R}`
  unerfüllbar:

  .. math::

      x = x + 1

  Für die Lösungsmenge gilt somit :math:`\mathbb{L} = \emptyset`.

* Folgende Gleichung ist für jede reelle Zahl :math:`x \in \mathbb{R}`
  allgemeingültig:

  .. math::

      x - x = 0

  Für die Lösungsmenge gilt somit :math:`\mathbb{L} = \mathbb{R}`.

* Folgende Gleichung liefert nicht für jedes :math:`x \in \mathbb{R}`
  eine wahre Aussage:

  .. math::

      3 \cdot x = 2 \cdot x + 5

  Die Lösungsmenge ist somit eine Teilmenge des Definitionsbereichs. Konkret
  gilt :math:`\mathbb{L} = \{ 5 \}`.

Ist die Lösungsmenge einer Gleichung nicht unmittelbar erkennbar, so kann diese
durch entsprechende Umformungen in eine einfacher zu lösende Form gebracht
werden.

..
    Unterteilung in Gleichungen mit einer Variablen, mit mehreren Variablen.

.. index:: Äquivalente Umformung
.. _Umformen von Gleichungen:

Äquivalentes Umformen von Gleichungen
-------------------------------------

Manchmal lässt sich die Lösungsmenge einer Gleichung durch Einsetzen von
konkreten Werten in die Variablen ("Probieren") ermitteln. Im Allgemeinen jedoch
muss man eine Gleichung durch schrittweises Umformen lösen. Wesentlich hierfür
ist in diesem Zusammenhang die Äquivalenz von Gleichungen.

Eine Gleichung heißt äquivalent (gleichwertig) zu einer anderen Gleichung, wenn
beide die gleiche Lösungsmenge :math:`\mathbb{L}` bei gleicher Definitionsmenge
:math:`\mathbb{D}` besitzen. Eine Umformung, durch die eine Gleichung in eine zu
ihr äquivalente Gleichung übergeht, heißt äquivalente Umformung. Beispielsweise
dürfen aufgrund der Symmetrie der Gleichheits-Relation stets die linke und die
rechte Seite einer Gleichung vertauscht werden:

.. math::
    :label: eqn-umformung-links-rechts

    T_1 = T_2 \quad \Leftrightarrow \quad T_2 = T_1

Termumformungen, die sich nur auf eine Seite einer Gleichung auswirken,
beispielsweise :ref:`Zusammenfassen <Assoziativgesetz>` und
:ref:`Ausmultiplizieren beziehungsweise Ausklammern <Distributivgesetz>` von
Summentermen sowie :ref:`Kürzen und Erweitern <Erweitern und Vereinfachen>` von
Bruchtermen, dürfen ebenso jederzeit vorgenommen werden.

Addiert oder subtrahiert man auf beiden Seiten einen beliebigen Term :math:`T`,
so ist die neue Gleichung äquivalent zur ursprünglichen. Der Wahrheitswert einer
Gleichung bleibt auch unverändert, wenn beiden Seiten mit einem Term :math:`T
\ne 0` multipliziert oder durch einen solchen dividiert werden. Somit gilt:
[#]_

  .. math::
    :label: eqn-äquivalente-umformungen

      T_1  = T_2 \quad &\Leftrightarrow  \quad T_1 + T = T_2 + T \\[2pt]
      T_1  = T_2 \quad &\Leftrightarrow  \quad T_1 - T = T_2 - T \\[2pt]
      %\phantom{\qquad (T \ne 0) T + + T}
      T_1  = T_2  \quad &\Leftrightarrow \quad T_1 \, \cdot \; T = T_2 \, \cdot
      \; T \qquad (T \ne 0)\\[2pt]
      T_1  = T_2  \quad &\Leftrightarrow \quad T_1 \, : \, T = T_2 \, : \, T
      \qquad (T \ne 0)


Während eine Addition oder Subtraktion eines beliebigen Terms auf beiden Seiten
der Gleichung jederzeit problemlos möglich ist, ist bei der Multiplikation einer
Gleichung mit einem Term beziehungsweise der Division durch einen Term :math:`T`
stets Vorsicht geboten. Wird hierbei die Bedingung :math:`T \ne 0` nicht
beachtet, so können in der neuen Gleichung zusätzliche Lösungen hinzukommen
beziehungsweise ursprünglich gültige Lösung verschwinden.

*Beispiele:*

* Die Gleichung :math:`2 \cdot x - 3 = 4 \cdot x + 1` hat, wie man durch
  Einsetzen überprüfen kann, die Lösungsmenge :math:`\mathbb{L} = \{ -2 \}`.
  Multipliziert man beide Seiten mit :math:`x`, so erhält man folgende
  Gleichung:

  .. math::

      x \cdot (2 \cdot x -3) = x \cdot (4 \cdot x + 1)

  Die neue Gleichung hat neben der ursprünglichen Lösung :math:`(-2)` auch
  die Lösung :math:`x=0`; die Lösungsmenge der neuen Gleichung ist also
  :math:`\mathbb{L} = \{ -2;\, 0 \}`. Somit ist die neue Gleichung
  nicht äquivalent zur ursprünglichen Gleichung.

* Die Gleichung :math:`(3 \cdot x + 1) \cdot (x + 2) = (2 \cdot x - 6) \cdot (x
  +2)` hat, wie man durch Einsetzen überprüfen kann, die Lösungsmenge
  :math:`\mathbb{L} = \{ -7;\, -2 \}`. Teilt man beide Seiten der Gleichung
  durch den Term :math:`(x+2)`, so erhält man folgende Gleichung:

  .. math::

      3 \cdot x + 1 = 2 \cdot x - 6

  Die neue Gleichung hat die Lösungsmenge :math:`\mathbb{L} = \{ -7 \}`; bei der
  Division ist die zweite ursprüngliche Lösung :math:`x = -2` entfallen. Somit
  ist die neue Gleichung nicht äquivalent zur ursprünglichen Gleichung.


Die äquivalenten Umformungs-Verfahren von Gleichungen beziehen sich auf die
Anwendung der vier grundlegenden Rechenoperationen (Addition, Subtraktion,
Multiplikation und Division). Werden weitere Rechenoperationen (beispielsweise
Potenzieren, Wurzelziehen oder Logarithmieren) angewendet, sind oft zusätzliche
Überlegungen nötig.

Eine Kontrolle der Lösungsmenge kann durch Einsetzen der Elemente in die
Ausgangsgleichung ("Probe") erfolgen. Bei einer Probe ist jede Gleichungsseite
getrennt auszurechnen, es dürfen also keine Gleichungsumformungen vorgenommen
werden.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Tritt eine Variable in einem Term beziehungsweise in einer Gleichung
    mehrfach auf, so muss sie beim Ersetzen durch einen konkreten Wert an jeder
    Stelle durch ein und den selben Wert ersetzt werden. 
    
    In Termen oder Gleichungen mit mehreren Variablen können unterschiedliche
    Variablen mit beliebigen (gleichen oder verschiedenen) Werten belegt werden.

.. [#] :math:`T` ist eine Zahl oder ein Term, der für alle Elemente des
    Definitionsbereichs der Ausgangsgleichung :math:`T_1 = T_2` definiert sein
    muss.



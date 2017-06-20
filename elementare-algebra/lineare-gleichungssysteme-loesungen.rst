
.. _Lösungen Lineare Gleichungssysteme:

Lineare Gleichungssysteme
-------------------------

.. {{{

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Lineare Gleichungssysteme>` zum Abschnitt :ref:`Lineare Gleichungssysteme
<Lineare Gleichungssysteme>`.

----

.. _lgs01l:

* Multipliziert man die zweite Gleichung :math:`(\mathrm{II})` mit dem Faktor
  :math:`2`, so nehmen die Koeffizienten in der :math:`x_1`-Spalte die gleichen
  Werte an:

  .. math::

      (\mathrm{I}): \quad 4 \cdot x_1 + 2 \cdot x_2 &= \;\,-6 \\
      (\mathrm{II}): \quad 2 \cdot x_1 - 3 \cdot x_2 &= \;\,-7 \\[12pt]
      \Rightarrow (\mathrm{I}): \quad 4 \cdot x_1 + 2 \cdot x_2 &= \;\,-6 \\
      (2 \cdot \mathrm{II}): \quad 4 \cdot x_1 - 6 \cdot x_2 &= -14

  Subtrahiert man nun beide Gleichungen voneinander, so bleibt die erste Zeile
  unverändert, während die zweite Zeile durch die Differenz aus der ersten und
  zweiten Gleichung ersetzt wird.

  .. math::

      \Rightarrow (\mathrm{I}): \quad 4 \cdot x_1 + 2 \cdot x_2 &= -6 \\
      (\mathrm{I} - \mathrm{II}): \qquad \;\,\, 0 + 8 \cdot x_2 &= +8

  Die zweite Zeile stellt nun eine Gleichung mit nur *einer* Unbekannten dar;
  beim Auflösen dieser Gleichung erhält man das Ergebnis :math:`x_2 = 1`. Setzt
  man diesen Wert für :math:`x_2` in die Gleichung :math:`\mathrm{I}` ein, so
  erhält man für die andere Unbekannte:

  .. math::

      4 \cdot x_1 + 2 \cdot 2 = -6 \quad \Longleftrightarrow \quad 4 \cdot x_1 =
      -8 \quad \Longleftrightarrow \quad x_1 = -2

  Das Gleichungssystem hat somit die Lösung :math:`\mathbb{L} = \{ (-2 ;\; 1) \}`.

  :ref:`Zurück zur Aufgabe <lgs01>`

.. sy.solve( [ sy.Eq( 4*x + 2*y, -6 ), sy.Eq( 2*x - 3 *y, -7) ] )
.. {y: 1, x: -2}

----

.. _lgs02l:

* Bezeichnet man die Anzahl an Sätzen, die der erste Spieler gewonnen hat, mit
  :math:`x_1` und entsprechend die Anzahl der vom anderen Spieler gewonnenen
  Sätze mit :math:`x_2`, so entspricht das Rätsel folgendem linearen
  Gleichungssystem:

  .. math::

      x_1 + 1 &= 2 \cdot (x_2 - 1) \\
      x_1 - 1 &= x_2 + 1 \\

  Dieses Gleichungssystem kann beispielsweise dadurch gelöst werden, indem man
  die zweite Gleichung nach :math:`x_1` auflöst; man erhält dadurch :math:`x_1 =
  x_2 + 2`. Setzt man diesen Ausdruck für :math:`x_2` in die erste Gleichung
  ein, so erhält man:

  .. math::

      (x_2+2) + 1 &= 2 \cdot (x_2 - 1) \\
      x_2 + 3 &= 2  \cdot x_2 - 2) \\
      x_2 &= 5 \\

  Der zweite Spieler hat somit insgesamt :math:`5` Sätze gewonnen, der erste
  wegen der Beziehung :math:`x_1 = x_2 + 2` insgesamt :math:`7` Sätze.

  :ref:`Zurück zur Aufgabe <lgs02>`

----

.. _lgs03l:

* :math:`\text{a) }` Ein lineares Gleichungssystem mit drei Gleichungen und zwei
  Unbekannten hat genau dann eine Lösung, wenn es bei Betrachtung von nur zwei
  der drei Gleichungen eine Lösung hat und diese auch für die dritte Gleichung
  gilt.

  .. math::

      (\mathrm{I}): \qquad \phantom{+}2 \cdot x_1 + 8 \cdot x_2 &= \phantom{+2}4 \\[4pt]
      (\mathrm{II}): \qquad -5 \cdot x_1 + 4 \cdot x_2 &= \phantom{+}20 \\[4pt]
      (\mathrm{III}): \qquad \phantom{+}7 \cdot x_1 + 4 \cdot x_2 &= -16

  Es genügt also, zunächst beispielsweise folgendes Gleichungsystem zu
  betrachten:

  .. math::

      (\mathrm{I}): \qquad \phantom{+}2 \cdot x_1 + 8 \cdot x_2 &= \phantom{2}4 {\color{white}...}\\[4pt]
      (\mathrm{II}): \qquad -5 \cdot x_1 + 4 \cdot x_2 &= 20

  Multipliziert man die zweite Gleichung mit dem Faktor :math:`2`, so kann man
  diese von der ersten Gleichung subtrahieren, um das Gleichungssystem auf eine
  Gleichung mit nur noch einer Unbekannten zu reduzieren:

  .. math::

      (\mathrm{I}): \qquad  \phantom{+1}2 \cdot x_1 + 8 \cdot x_2 &= \phantom{2}4 {\color{white}\qquad \quad ...}\\[4pt]
      (2 \cdot \mathrm{II}): \qquad -10 \cdot x_1 + 8 \cdot x_2 &= 40 \\[12pt]
      (\mathrm{I} - 2 \cdot \mathrm{II}): \qquad \;\phantom{+}12 \cdot x_1 \phantom{+8 \cdot x_2} &= -36

  Diese Gleichung liefert :math:`x_1=-3` als Ergebnis. Setzt man diesen Wert für
  :math:`x_1` in die erste Gleichung ein, so erhält man für :math:`x_2`:

  .. math::

      2 \cdot (-3) + 8 \cdot x_2 &= \phantom{1}4 \\
      8 \cdot x_2 &= 10 \\
      x_2 &= \phantom{1}1,25 \\

  Nun ist zu prüfen, ob auch die dritte Gleichung durch die Variablen-Werte
  :math:`x_1 = -3` und :math:`x_2=1,25` erfüllt wird:

  .. math::

      \phantom{+}7 \cdot (-3 ) + 4 \cdot (1,25) &= -16\\[4pt]
      -21 + 5 &= -16 \quad \checkmark

  Die gefundene Lösung erfüllt auch die dritte Gleichung. Das Gleichungssystem
  hat somit eine eindeutige Lösung, und zwar :math:`\mathbb{L} = \{(-3;\,
  1,25)\}`.

.. sy.solve( [ sy.Eq(2*x + 8*y, 4), sy.Eq(-5*x + 4*y, 20), sy.Eq(7*x+4*y,-16) ])
.. [{x: -3, y: 5/4}]


* :math:`\text{b) }` Wiederum betrachtet man zunächst nur zwei der drei
  Gleichungen. Multipliziert man beispielsweise die dritte Gleichung mit
  :math:`4` und addiert sie zur zweiten, so erhält man eine neue Gleichung, die
  nur die Variable :math:`x_1` als Unbekannte hat:

  .. math::

      (\mathrm{II}): \quad \phantom{+}5 \cdot x_1 - 4 \cdot x_2  &= \;\,-2 \\[4pt]
      (\mathrm{4 \cdot III}): \quad -8 \cdot x_1 + 4 \cdot x_2 &= -16\\[20pt]
      (\mathrm{II} + 4 \cdot \mathrm{III}): \quad -3 \cdot x_1 \phantom{+ 4 \cdot x_2} &= -18

  Aus dieser Gleichung folgt :math:`x_1 = 6`. Setzt man diesen Wert für
  :math:`x_1` in Gleichung :math:`\mathrm{(II)}` ein, so erhält man für
  :math:`x_2`:

  .. math::

      5 \cdot 6 - 4 \cdot x_2 &= \;\;-2 \\
      - 4 \cdot x_2 &= -32 \\
      \Rightarrow \; x_2 &= \phantom{-3}8 \\

  Nun ist zu prüfen, ob auch Gleichung :math:`\mathrm{(I)}` durch die
  Variablen-Werte :math:`x_1 = 6` und :math:`x_2=8` erfüllt wird:

  .. math::

      -3 \cdot 6 + 7 \cdot 8 &  = 15 \\
      -18 + 56 &  = 15 \\
      38 &  = 15 \quad \text{\Lightning}

  Die gefundene Lösung erfüllt zwar die zweite und dritte, nicht jedoch die
  erste Gleichung. Das Gleichungssytem ist somit nicht lösbar, die Lösungsmenge
  ist also die leer: :math:`\mathbb{L} = \{  \}`.

  :ref:`Zurück zur Aufgabe <lgs03>`


----

.. _lgs04l:

* Bei einem Gleichungssystem mit drei Unbekannten und nur zwei Gleichungen
  stellt die dritte Variable einen frei wählbaren Parameter dar; das
  Gleichungssystem kann folglich nur in Abhängigkeit dieser Variablen gelöst
  werden.

  Im konkreten Fall soll das Gleichungssystem in Abhängigkeit von der Variablen
  :math:`x_3` gelöst werden. Hierzu sortiert man diese als erstes auf die rechte
  Seite des Gleichungssystems (so, als ob es sich dabei um einen gewöhnlichen
  Zahlenwert handeln würde). Man erhält:

  .. math::

      (\mathrm{I}): \quad \phantom{+}1 \cdot x_1 + 2 \cdot x_2 &= -6 -2 \cdot x_3 \\[4pt]
      (\mathrm{II}): \quad -1 \cdot x_1 + 2 \cdot x_2 &= \phantom{-}4 +1 \cdot x_3

  Dieses Gleichungssystem kann man beispielsweise lösen, indem man die zweite
  Gleichung von der ersten subtrahiert. Man erhält dann als Gleichung für :math:`x_1`:

  .. math::
  
      (\mathrm{I - II}): \quad \phantom{+}2 \cdot x_1 \phantom{+ 0 \cdot x_2 } &= -10 - 3 \cdot x_3 \\[4pt]
       \Rightarrow \qquad \phantom{2 \cdot }x_1 \phantom{+ 0 \cdot x_2 } &= -\phantom{1}5 - 1,5 \cdot x_3

  Somit ist :math:`x_1` in Abhängigkeit von :math:`x_3` bestimmt. Setzt man
  diesen Ausdruck für :math:`x_1` in die zweite Gleichung ein, so erhält man für
  :math:`x_2`:

  .. math::
  
      -1 \cdot (-5 - 1,5 \cdot x_3) + 2 \cdot x_2 & = \phantom{-}4  + 1 \cdot x_3 \\[4pt]
      +5 + 1,5 \cdot x_3 + 2 \cdot x_2 & = \phantom{-}4  + 1 \cdot x_3 \\[4pt]
      2 \cdot x_2 & = -1  - 0,5 \cdot x_3 \\[4pt]
      x_2 & = -0,5  - 0,25 \cdot x_3
  
  

  Die Lösungsmenge des Gleichungssystems in Abhängigkeit von :math:`x_3` lautet
  somit :math:`\mathbb{L}=\{-5 - 1,5 \cdot x_3;\, -0,5 - 0,25 \cdot x_3\}`.

  :ref:`Zurück zur Aufgabe <lgs04>`

.. sy.solve( [sy.Eq(1*x + 2*y + 2*z, -6), sy.Eq(-x +2*y - 1*z, 4) ] )
.. {x: -3*z/2 - 5, y: -z/4 - 1/2}

----

.. }}}

.. only:: html

    :ref:`Zurück zum Skript <Lineare Gleichungssysteme>`



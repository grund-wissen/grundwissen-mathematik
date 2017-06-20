
.. _Lösungen Lineare Algebra und analytische Geometrie:
.. _Lösungen zur Linearen Algebra und analytischen Geometrie:

Lösungen zur Linearen Algebra und analytischen Geometrie
========================================================

.. _Lösungen Determinanten:

Determinanten
-------------

.. {{{

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Determinanten>` zum Abschnitt :ref:`Determinanten <Determinanten>`.

----

.. _det01l:

* Um die Determinante mittels der Regel von Sarrus zu bestimmen, schreibt man
  die erste und zweite Spalte noch einmal hinter die dritte Spalte. Dann
  berechnet man zunächst die Produkte der Zahlen in jeder Hauptdiagonalen (von
  links oben nach rechts unten) und bildet ihren Summenwert:

  .. math::

      & \begin{matrix}
          1 & &3 & & \!\!\!\!-2 & & 1 & & 3\\
          & \searrow  & & \searrow  & & \searrow \\
          \!\!\!\!-1 & &  \!\!\!\!-5 & & 4 & & \!\!\!\!-1 & & \!\!\!\!-5 \\
          & & & \searrow  & & \searrow & & \searrow \\
          0 & & 7 & & \!\!\!\!-2 & & 0 & &7
      \end{matrix} \\[6pt]
      & = 10 + 0 + 14 = 24

  Anschließend bildet man die Summe der Produkte der in den Nebendiagonalen
  stehenden Zahlen (links unten nach rechts oben):

  .. math::

      & \begin{matrix}
          1 & &3 & & \!\!\!\!-2 & & 1 & & 3\\
          & & & \nearrow  & & \nearrow & & \nearrow \\
          \!\!\!\!-1 & &  \!\!\!\!-5 & & 4 & & \!\!\!\!-1 & & \!\!\!\!-5 \\
          & \nearrow  & & \nearrow  & & \nearrow \\
          0 & & 7 & & \!\!\!\!-2 & & 0 & &7
      \end{matrix} \\[6pt]
      & = 0 + 28 + 6 = 34

  Schließlich subtrahiert man beide Werte voneinander; das Ergebnis lautet somit
  :math:`24-34 = -10`.

  :ref:`Zurück zur Aufgabe <det01>`

.. np.linalg.det(np.array( [[1,3,-2],[-1,-5,4],[0,7,-2]] ))
.. -10


----

.. _det02l:

* :math:`\text{a) }` Zunächst kann man anhand der Koeffizienten-Determinate prüfen, ob das
  Gleichungssystem eindeutig lösbar ist:

  .. math::

      \begin{vmatrix} a_{\mathrm{11}} & a_{\mathrm{12}}  \\ a_{\mathrm{21}} & a_{\mathrm{22}} \end{vmatrix} =
      \begin{vmatrix}
      1 & \phantom{+}5  \\
      3 & -9
      \end{vmatrix} = -9 -15 = -24

  Der Wert der Determinante ist ungleich Null, das Gleichungssystem ist somit
  eindeutig lösbar.

  Zur Bestimmung der Unbekannten :math:`x_1` bildet man eine zweite
  Determinante, wobei die Koeffizienten von :math:`x_1` (die erste Spalte) durch
  die Werte auf der rechten Gleichungsseite ersetzt werden:

  .. math::

      \begin{vmatrix} b_1 & a_{\mathrm{12}} \\ b_2 &  a_{\mathrm{22}} \end{vmatrix}  =
      \begin{vmatrix} 8 & \phantom{+}5  \\ -24 & -9
      \end{vmatrix} = -72 - (-120) = 48

  Dividiert man den Wert dieser Determinante durch den Wert der
  Koeffizienten-Determinate, so erhält man als Wert für :math:`x_1`:

  .. math::

    x_1 = \frac{\begin{vmatrix} b_1 & a_{\mathrm{12}} \\ b_2 &  a_{\mathrm{22}}
    \end{vmatrix} }{\begin{vmatrix} a_{\mathrm{11}} & a_{\mathrm{12}}  \\ a_{\mathrm{21}}
    & a_{\mathrm{22}} \end{vmatrix} } = \frac{\phantom{+}48}{-24} = -2

  Zur Bestimmung der Unbekannten :math:`x_2` kann man entsprechend eine weitere
  Determinante bilden, bei der nun die Koeffizienten von :math:`x_2` (die zweite
  Spalte) durch die Werte auf der rechten Gleichungsseite ersetzt werden:

  .. math::

      \begin{vmatrix} a_{\mathrm{11}} & b_1 \\ a_{\mathrm{21}} &  b_2 \end{vmatrix}  =
      \begin{vmatrix} 1 & \phantom{+0}8  \\ 3 & -24
      \end{vmatrix} = -24 - 24 = -48

  Dividiert man den Wert dieser Determinante durch den Wert der
  Koeffizienten-Determinate, so erhält man als Wert für :math:`x_2`:

  .. math::

      x_2 = \frac{\begin{vmatrix}  a_{\mathrm{11}} & b_1 \\  a_{\mathrm{21}} &  b_2
      \end{vmatrix} }{\begin{vmatrix} a_{\mathrm{11}} & a_{\mathrm{12}}  \\ a_{\mathrm{21}}
      & a_{\mathrm{22}} \end{vmatrix} } = \frac{-48}{\phantom{+}24} = +2

  Das Gleichungssystem hat somit die Lösung :math:`\mathbb{L} = \{ (-2 ;\; 2) \}`.

.. sy.solve( [ sy.Eq(1*x + 5*y, 8), sy.Eq(3*x - 9*y, -24) ] )
.. {x: -2, y: 2}

* :math:`\text{b) }` Zunächst kann man wiederum anhand der
  Koeffizienten-Determinate prüfen, ob das Gleichungssystem eindeutig lösbar
  ist. Nach der Regel von Sarrus erhält man:

  .. math::

      \begin{vmatrix}
          a_{\mathrm{11}} & a_{\mathrm{12}} & a_{\mathrm{13}} \\
          a_{\mathrm{21}} & a_{\mathrm{22}} & a_{\mathrm{23}} \\
          a_{\mathrm{31}} & a_{\mathrm{32}} & a_{\mathrm{33}} \\
      \end{vmatrix} =
      \begin{vmatrix}
      \phantom{+}5 & \phantom{+}2 & -3 \\
      -2 & -7 & \phantom{+}3 \\
      \phantom{+}3 & -9 & \phantom{+}1
      \end{vmatrix} = -35 + 18 + (-54) - 63 - (-135) - (-4) = 5

  Der Wert der Determinante ist ungleich Null, das Gleichungssystem ist somit
  eindeutig lösbar.

  Zur Bestimmung der Unbekannten :math:`x_1` bildet man erneut eine
  Determinante, wobei die Koeffizienten von :math:`x_1` (die erste Spalte) durch
  die Werte auf der rechten Gleichungsseite ersetzt werden:

  .. math::

      \begin{vmatrix}
          b_1 & a_{\mathrm{12}} & a_{\mathrm{13}} \\
          b_2 & a_{\mathrm{22}} & a_{\mathrm{23}} \\
          b_3 & a_{\mathrm{32}} & a_{\mathrm{33}} \\
      \end{vmatrix} =
      \begin{vmatrix}
      11 & \phantom{+}2 & -3 \\
      \phantom{1}1 & -7 & \phantom{+}3 \\
      15 & -9 & \phantom{+}1
      \end{vmatrix} = -77 + 90 + 27 - 315 + 297 - 2 = 20

  Dividiert man den Wert dieser Determinante durch den Wert der
  Koeffizienten-Determinate, so erhält man als Wert für :math:`x_1`:

  .. math::

      x_1 = \frac{20}{5} = 4

  Zur Bestimmung der Unbekannten :math:`x_2` geht man wiederum von der
  ursprünglichen Determinante aus, ersetzt allerdings die Koeffizienten von
  :math:`x_2` (die zweite Spalte) durch die Werte auf der rechten
  Gleichungsseite:

  .. math::

      \begin{vmatrix}
          a_{\mathrm{11}} & b_1 & a_{\mathrm{13}} \\
          a_{\mathrm{21}} & b_2 & a_{\mathrm{23}} \\
          a_{\mathrm{31}} & b_3 & a_{\mathrm{33}} \\
      \end{vmatrix} =
      \begin{vmatrix}
      \phantom{+}5 & 11 & -3 \\
      -2 & \phantom{1}1 & \phantom{+}3 \\
      \phantom{+}3 & 15 & \phantom{+}1
      \end{vmatrix} = 5 + 99 + 90 - (-9) - 225 - (-22) = 0

  Der Wert dieser Determinante ist Null; somit ergibt auch eine Division durch
  den Wert :math:`5` der Koeffizienten-Determinante den Wert :math:`0`:

  .. math::

      x_2 = \frac{0}{5} = 0

  Zur Bestimmung der Unbekannten :math:`x_3` geht man erneut von der
  ursprünglichen Determinante aus, ersetzt allerdings die Koeffizienten von
  :math:`x_3` (die zweite Spalte) durch die Werte auf der rechten
  Gleichungsseite:

  .. math::

      \begin{vmatrix}
          a_{\mathrm{11}} & a_{\mathrm{12}} & b_1 \\
          a_{\mathrm{21}} & a_{\mathrm{22}} & b_2 \\
          a_{\mathrm{31}} & a_{\mathrm{32}} & b_3 \\
      \end{vmatrix} =
      \begin{vmatrix}
      \phantom{+}5 & \phantom{+}2 & 11 \\
      -2 & -7 & \phantom{1}1 \\
      \phantom{+}3 & -9 & 15
      \end{vmatrix} = -525 + 6 + 198 - (-231) - (-45) - (-60) = 15

  Dividiert man den Wert dieser Determinante durch den Wert der
  Koeffizienten-Determinate, so erhält man als Wert für :math:`x_3`:

  .. math::

      x_3 = \frac{15}{5} = 3

  Das Gleichungssystem hat somit die Lösung :math:`\mathbb{L} = \{ (4 ;\; 0 ;\; 3) \}`.

  :ref:`Zurück zur Aufgabe <det02>`

.. sy.solve( [ sy.Eq(5*x + 2*y - 3*z, 11), sy.Eq(-2*x + 7*y + 3*z,1), sy.Eq(3*x-9*y+1*z,15) ] )
.. {z: 3, x: 4, y: 0}

.. np.linalg.det( np.array( [[5,2,-3],[-2,-7,3],[3,-9,1]] ))
.. 5

.. -35+18-54-63+135+4
.. 5

.. np.linalg.det( np.array( [[11,2,-3],[1,-7,3],[15,-9,1]] ))
.. 20

.. 11*-7 + 2*3*15 + -3*1*-9 - 15*7*3 +9*3*11 - 2
.. 20



----


.. }}}


.. only:: html

    :ref:`Zurück zum Skript <Lineare Algebra>`




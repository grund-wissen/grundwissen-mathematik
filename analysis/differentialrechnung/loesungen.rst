
.. _Lösungen Differentialrechnung:

Differentialrechnung
====================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Differentialrechnung>` zum Abschnitt :ref:`Differentialrechnung
<Differentialrechnung>`.

----

.. _dif01l:

* Differenzierbarkeit setzt Stetigkeit voraus, jede an einer Stelle :math:`x_0`
  differenzierbare Funktion ist somit an dieser Stelle auch stetig.

  Die Umkehrung gilt jedoch nicht: Beispielsweise ist die Funktion :math:`y=|x|`
  an der Stelle :math:`x_0=0` zwar stetig (weil der linksseitige und rechtsseitige
  Grenzwert sowie der Funktionswert an dieser Stelle übereinstimmen), aber nicht
  differenzierbar (weil die Steigungen unmittelbar links und rechts von
  :math:`x_0` nicht übereinstimmen).

  :ref:`Zurück zur Aufgabe <dif01>`

----

.. _dif02l:

* Die Ableitung der Funktion :math:`f(x) = \frac{c \cdot x}{x^2 - c^2}` mit
  :math:`c \in \mathbb{R} ^{+}` kann mittels der Quotientenregel bestimmt werden.
  Mit :math:`f_1(x) = c \cdot x` und :math:`f_2(x) = x^2 - c^2` gilt:

  .. math::

      \left(\frac{f_1(x)}{f_2(x)} \right)' &= \frac{f_1'(x) \cdot f_2(x) -
      f_1(x) \cdot f_2'(x)}{\big(f_2(x)\big)^2} \\[4pt] &= \frac{(c \cdot 1)
      \cdot (x^2 - c^2) - c \cdot x \cdot (2 \cdot x - 0)}{(x^2 - c^2)^2}
      \\[4pt] 
      &= \frac{c \cdot x^2 - c^3 - 2 \cdot c \cdot x^2 }{(x^2 - c^2)^2} =
      \frac{-c \cdot x^2 - c^3}{(x^2 - c^2)^2} = \frac{-c \cdot (x^2 +
      c^2)}{(x^2 - c^2)^2}

  :ref:`Zurück zur Aufgabe <dif02>`

----

.. foo

.. only:: html

    :ref:`Zurück zum Skript <Differentialrechnung>`



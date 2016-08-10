
.. _Lösungen Eigenschaften von Funktionen:

Eigenschaften von Funktionen
============================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben zu
Eigenschaften von Funktionen>` zum Abschnitt :ref:`Eigenschaften von Funktionen
<Eigenschaften von Funktionen>`.

.. _Lösungen Stetigkeit:

.. rubric:: Stetigkeit

----

.. _fun01l:

* Eine Funktion :math:`f(x)` ist genau dann an einer Stelle :math:`x_0` stetig,
  wenn dort ihr linksseitiger und ihr rechtsseitiger Grenzwert übereinstimmen.
  Bei der stufenweise definierten Funktion gilt für den linksseitigen Grenzwert
  an der Stelle :math:`x_0 = 1`:

  .. math::

      \lim _{\substack{x \to x_0, \\ x < x_0}} f(x)
      = \lim _{\substack{x_0 \to 1, \\ x < 1}} \left(1 - x^2\right) = 0

  Für den rechtsseitigen Grenzwert gilt:

  .. math::

      \lim _{\substack{x \to x_0, \\ x > x_0}} f(x)
      = \lim _{\substack{x_0 \to 1, \\ x > 1}} \left(x - 1\right) = 0

  Beide Grenzwerte stimmen überein und sind mit dem Funktionswert
  :math:`f(x_0)` an der Stelle :math:`x_0` identisch. Damit ist die Funktion
  :math:`f(x)` an dieser Stelle stetig.

  :ref:`Zurück zur Aufgabe <fun01>`


----

.. _fun02l:

* Die Funktion :math:`f(x) = \frac{1}{x^2}` ist als :ref:`Hyperbelfunktion
  <Hyperbeln>` an jeder Stelle außer :math:`x_0 = 0` stetig. An dieser Stelle
  ist die Funktion nicht definiert, somit kann an dieser Stelle auch keine
  Aussage über ihre Stetigkeit getroffen werden.

  Die Funktion :math:`f(x)` ist also an jeder Stelle ihres Definitionsbereichs
  und somit global stetig.

  :ref:`Zurück zur Aufgabe <fun02>`


----

.. foo

.. only:: html

    :ref:`Zurück zum Skript <Eigenschaften von Funktionen>`


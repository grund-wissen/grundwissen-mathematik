
.. _Lösungen Gleichungen:
.. _Lösungen zu Gleichungen:

Lösungen zu Gleichungen
=======================

.. _Lösungen Bruchgleichungen:
.. _Lösungen Produktgleichungen:
.. _Lösungen Wurzelgleichungen:
.. _Lösungen Bruch-, Produkt- und Wurzelgleichungen:

Bruch-, Produkt- und Wurzelgleichungen
--------------------------------------

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Bruchgleichungen und Wurzelgleichungen>` zum Abschnitt :ref:`Bruch-, Produkt-
und Wurzelgleichungen <Bruchgleichungen und Wurzelgleichungen>`.

----

.. _pro01l:

* Bei der Gleichung handelt es sich um eine Produkt-Gleichung; für den
  Definitionsbereich gilt :math:`\mathbb{D} = \mathbb{R}`, es dürfen also alle
  reellen Zahlen für :math:`x` eingesetzt werden.

  Um die Gleichung zu lösen, ist es hilfreich, alle die Variable :math:`x`
  beinhaltende Terme auf die linke Seite zu sortieren. Dadurch erhält man:

  .. math::

      3 \cdot x \cdot (x - 5) &= 6 \cdot (x - 5) \\
      3 \cdot x \cdot (x - 5) - 6 \cdot (x - 5)&= 0

  Auf der linken Seite kann nun der Term :math:`(x-5)` ausgeklammert werden.
  Daraus ergibt sich:

  .. math::

      (3 \cdot x - 6) \cdot (x - 5) &= 0

  Ein Produkt hat genau dann den Wert Null, wenn einer der Faktoren Null ist.
  Die Gleichung ist somit in den folgenden beiden Fällen erfüllt:

  .. math::

      3 \cdot x - 6 &= 0 \quad \Longleftrightarrow \quad x = 2 \\
      x - 5 &= 0 \quad \Longleftrightarrow \quad x = 5

  Die Lösungsmenge der Gleichung ist somit :math:`\mathbb{L} = \{2;\,5\}`.


  :ref:`Zurück zur Aufgabe <pro01>`

----

.. _wurz01l:

* Betrachtet man (ohne jegliche algebraische Umformung) den Definitionsbereich
  der Gleichung, so stellt man fest, dass dieser leer ist. Es gibt nämlich
  keinen Wert für die Variable :math:`x`, so dass die beiden Bedingungen
  :math:`x-5 \ge 0` *und* :math:`2-x \ge 0` gleichzeitig erfüllt
  sind. Die Gleichung kann somit für keine reelle Zahl :math:`x \in \mathbb{R}`
  erfüllt werden.

  :ref:`Zurück zur Aufgabe <wurz01>`

----

.. _wurz02l:

* Die Definitionsmenge ergibt sich, da reellwertige Wurzeln nicht negativ sein
  dürfen, aus folgenden Ungleichungen:

  .. math::

      \sqrt{x + 1} \ge 0 \quad &\Longleftrightarrow \quad x \ge -1 \\
      x - 5 \ge 0 \quad &\Longleftrightarrow \quad x \ge 5 \\

  Da beide Bedingungen zugleich gelten müssen und die zweite Bedingung :math:`x
  \ge 5` die erste Bedingung :math:`x \ge -1` hinreichend mit einschließt, gilt
  für den Definitionsbereich der Gleichung :math:`\mathbb{D} = [5; \infty[`.

  Um die Gleichung zu lösen, können die Terme auf beiden Seiten in einem ersten
  Rechenschritt quadriert werden. Man erhält hierbei:

  .. math::

      x + 1 = (x - 5)^2

  Diese Gleichung entspricht nun einer quadratischen Gleichung. Um sie zu lösen,
  werden alle Terme auf die linke Seite sortiert und anschließend Klammer der
  quadratische Term :math:`(x-5)^2` ausgewertet:

  .. math::

      (x-5)^2 \quad - x - 1 &= 0 \\
      (x^2 - 10 \cdot x + 25) - x - 1 &= 0 \\

  Da in der resultierenden Gleichung alle Operatoren die gleiche Priorität haben
  und vor der Klammer kein Minuszeichen steht, können die Klammern weggelassen
  werden. Die :math:`x`-Terme sowie die Zahlenwerte können noch folgendermaßen
  zusammengefasst werden:

  .. math::

      x^2 - 11 \cdot x + 24 \quad  &= 0 \\

  Diese Gleichung kann beispielsweise mit der Lösungsformel für quadratische
  Gleichungen gelöst werden. Mit :math:`a=1`, :math:`b=-11` und :math:`c=24`
  erhält man:

  .. math::

      x_1 = \frac{-b - \sqrt{b^2 - 4 \cdot a \cdot c}}{2 \cdot a} = \frac{11 -
      \sqrt{121 - 4 \cdot 24}}{2 \cdot 1} = \frac{11 - \sqrt{25}}{2} = 3\\
      x_1 = \frac{-b + \sqrt{b^2 - 4 \cdot a \cdot c}}{2 \cdot a} = \frac{11 +
      \sqrt{121 - 4 \cdot 24}}{2 \cdot 1} = \frac{11 + \sqrt{25}}{2} = 8\\

  Man könnte nun annehmen, dass die Lösungsmenge gleich :math:`\mathbb{L} = \{
  3;\,5 \}` ist -- doch das ist ein Irrtum! Die Definitionsmenge
  :math:`\mathbb{D} = [5;\,\infty[` der ursprünglichen Gleichung schließt die
  Lösung :math:`x_1 = 3` der späteren quadratischen Gleichung aus. Der Grund für
  das Hinzukommen der "Scheinlösung" liegt im ersten Rechenschritt, nämlich dem
  Quadrieren beider Seiten der Gleichung. Da diese Umformung keine
  Äquivalenz-Umformung ist, können wie in diesem Beispiel weitere Lösungen
  hinzukommen.

  Neben einem Blick auf den Definitionsbereich hätte auch ein Einsetzen der
  erhaltenen Lösungen in die ursprüngliche Gleichung die Scheinlösung
  :math:`x_1=3` ausgeschlossen. Die Lösungsmenge lautet also :math:`\mathbb{L} =
  \{ 8 \}`.


  :ref:`Zurück zur Aufgabe <wurz02>`

----


.. _Lösungen Exponential- und Logarithmusgleichungen:

Exponential- und Logarithmusgleichungen
---------------------------------------

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Exponential- und Logarithmusgleichungen>` zum Abschnitt :ref:`Exponential- und
Logarithmusgleichungen <Exponential- und Logarithmusgleichungen>`.

----

.. _gel01l:

* Die Definitionsmenge der Gleichung ist :math:`\mathbb{D} = \{ x \,|\, x > 0,\;
  x \ne 1 \}`.

  Gemäß der Definition eines Logarithmus kann die Gleichung auch wie folgt
  geschrieben werden:

  .. math::

      \log_{x}{(125)} = 3 \quad \Longleftrightarrow \quad x^{3} = 125

  Zieht man bei der Gleichung auf der rechten Seite die dritte Wurzel, so erhält
  man:

  .. math::

      x = \sqrt[3]{125} = \pm 5

  Unter Berücksichtigung der Definitionsmenge lautet die Lösung somit
  :math:`\mathbb{L} = \{ 5 \}`.

  :ref:`Zurück zur Aufgabe <gel01>`

----

.. foo

.. only:: html

    :ref:`Zurück zum Skript <Exponential- und Logarithmusgleichungen>`



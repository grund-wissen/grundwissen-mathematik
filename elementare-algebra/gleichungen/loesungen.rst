
.. _Lösungen Gleichungen:
.. _Lösungen zu Gleichungen:

Gleichungen
===========

.. _Lösungen Lineare Gleichungen:

Lineare Gleichungen
-------------------

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Lineare Gleichungen>` zum Abschnitt :ref:`Lineare Gleichungen <Lineare
Gleichungen>`.

----

.. _ling01l:

* Zur Lösung der Gleichung empfiehlt es sich, beide Seiten der Gleichung mit dem
  Hauptnenner :math:`2 \cdot 3 = 6` der auftretenden Terme zu multiplizieren.

  .. math::

     \frac{10 \cdot x+3}{3} -5 &= 11 - \frac{3 \cdot x + 4}{2} - \frac{2 \cdot x
     +6}{3} \\[4pt]
     6 \cdot \left( \frac{10 \cdot x+3}{3} -5 \right) &= 6 \cdot \left( 11 -
     \frac{3 \cdot x + 4}{2} - \frac{2 \cdot x +6}{3} \right) \\[4pt]

  Multipliziert man die Klammern aus, so können die auftretenden Brüche durch
  Kürzen beseitigt werden. Man erhält dadurch:

  .. math::

     {\color{white}....}2 \cdot (10 \cdot x+3) \; - \; 30  = 66 - 3 \cdot (3
     \cdot x + 4) - 2 \cdot (2 \cdot x +6) \\[4pt]

  Die Gleichung kann durch ein Ausmultiplizieren der Klammern weiter vereinfacht
  werden:

  .. math::

     20 \cdot x+6 \; - \; 30  = 66 - 9 \cdot x - 12 - 4 \cdot x - 12 \\[4pt]

  Zum Auflösen werden alle :math:`x`-Terme auf eine Seite der Gleichung, alle
  anderen Terme auf die andere Seite der Gleichung gebracht. Damit folgt:

  .. math::

      20 \cdot x + 13 \cdot x &= 66 -24 + 24 \\
      33 \cdot x &= 66 \\ x &= 2 \\

  Die Lösung der Gleichung lautet somit :math:`x=2`.


  :ref:`Zurück zur Aufgabe <ling01>`

----

.. _Lösungen Quadratische Gleichungen:

Quadratische Gleichungen
------------------------

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Quadratische Gleichungen>` zum Abschnitt :ref:`Quadratische Gleichungen
<Quadratische Gleichungen>`.

----

.. _quag01l:

* :math:`\text{a) }` Die Lösungsformel für quadratische Gleichungen
  ("Mitternachtsformel") liefert für die gegebene Gleichung :math:`x^2 - 6 \cdot
  x + 8 = 0` mit :math:`a=1`, :math:`b=-6` und :math:`c=8`:

  .. math::

      x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4 \cdot a \cdot c}}{2 \cdot a} =
      \frac{+6 \pm \sqrt{36 - 4 \cdot 8}}{2} = \frac{6 \pm 2}{2}

  Somit ergeben sich folgende Lösungen:

  .. math::

      x_1 = \frac{6 - 2}{2} = 2 \qquad x_2 = \frac{6+2}{2} = 4

  Die Lösungsmenge der Gleichung lautet somit :math:`\mathbb{L} = \{ 2;\, 4 \}`.

* :math:`\text{b) }` Zum Lösen der Gleichung :math:`3 \cdot x^2 + 4 \cdot x - 15
  = 0` sind in die "Mitternachtsformel" die Werte :math:`a=3`, :math:`b=4` und
  :math:`c=-15` einzusetzen. Man erhält damit:

  .. math::

      x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4 \cdot a \cdot c}}{2 \cdot a} =
      \frac{-4 \pm \sqrt{16 - 4 \cdot 3 \cdot (-15)}}{6} = \frac{-4 \pm
      \sqrt{196}}{6}

  Die Wurzel :math:`\sqrt{196}` ergibt den Wert :math:`14`. Als Lösungen erhält
  man damit:

  .. math::

      x_1 = \frac{-4 - 14}{6} = -3 \qquad x_2 = \frac{-4+14}{6} = \frac{5}{3}

  Die Lösungsmenge der Gleichung lautet somit :math:`\mathbb{L} = \left\{ -3;\, \frac{5}{3} \right\}`.

  :ref:`Zurück zur Aufgabe <quag01>`

.. x = sy.S('x')
.. sy.solve( sy.Eq(3*x**2 + 4*x - 15, 0) )
.. [-3, 5/3]

.. x = sy.S('x')
.. sy.solve( sy.Eq(x**2 - 6*x + 8, 0) )
.. [2, 4]

----

.. _quag02l:

* Der Satz von Vieta ist insbesondere dann nützlich, wenn eine quadratische
  Gleichung der Form :math:`1 \cdot x^2 + b \cdot x + c = 0` vorliegt und
  :math:`b` sowie :math:`c` ganze Zahlen sind.

  Man prüft dann als erstes, durch welche Produkt zweier Zahlen sich die Zahl
  :math:`c` darstellen lässt. Im Fall :math:`c=20` ergeben sich folgende
  Möglichkeiten:

  .. math::

      20 &= 20 \cdot 1 \\
       &= 10 \cdot 2 \\
       &= 5 \cdot 4 \\

  Ebenfalls möglich sind die Produkte :math:`(-20) \cdot (-1)`, :math:`(-10)
  \cdot (-2)` und :math:`(-5) \cdot (-4)`. Eine dieser drei beziehungsweise
  sechs Möglichkeiten gibt die beiden Lösungen der Gleichung an.

  Um zu prüfen, welche der obigen Möglichkeiten die Gleichung löst, bildet man
  die Summen der einzelnen Wertepaare:

  .. math::

      20 + 1 &= 21 \\
      10 + 2 &= 12 \\
      5 + 4 &= 9 \\

  Das "richtige" Wertepaar erkennt man daran, dass die Summe einen Wert ergibt,
  der mit dem Wert von :math:`(-b)` identisch ist. In dieser Aufgabe ist
  :math:`b = -9`, also ist :math:`(-b) = 9`. Die Lösung der Gleichung lautet
  somit:

  .. math::

      x_1 = 4 \quad ; \quad x_2 = 5

  Als Produktform lässt sich die Gleichung damit wie folgt schreiben:

  .. math::

      x^2 - 9 \cdot x + 20 = 0 \quad \Longleftrightarrow \quad (x-4) \cdot (x-5) = 0

  :ref:`Zurück zur Aufgabe <quag02>`

----


.. _Lösungen Algebraische Gleichungen:

Algebraische Gleichungen
------------------------

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Algebraische Gleichungen>` zum Abschnitt :ref:`Algebraische Gleichungen höheren
Grades <Algebraische Gleichungen>`.

----

.. _alg01l:

* Existiert die Lösung :math:`x_1=3`, so kann der Gleichungsterm in ein Produkt
  aus dem Linearfaktor :math:`(x-3)` und einem Restterm zerlegt werden. Dieser
  kann mittels einer Polynom-Division ermittelt werden; es muss also folgende
  Rechnung durchgeführt werden:

  .. math::

      (x^3 - 6 \cdot x^2 - 1 \cdot x + 30) : (x - 3) = \; ?

  Als erstes prüft man, mit welchem Faktor :math:`x` zu multiplizieren ist, um
  :math:`x^3` zu erhalten; als Ergebnis kann man :math:`x^2` auf die rechte
  Seite schreiben. Das Produkt aus :math:`x^2 \cdot (x-3)` muss dann vom
  ursprünglichen Term abgezogen werden. Man erhält:

  .. math::

      \begin{array}{rlll}
      (x^3 &-  6 \cdot x^2 &-  1 \cdot x &+  30) : (x - 3) = x^2 \; + \; ?\\
      -(x^3 & - 3 \cdot x^2) \\ \cline{1-2} \\[-8pt]
      & -3 \cdot x^2 & - 1\cdot x &+ 30 \\
      \end{array}

  Als nächstes ist also zu prüfen, mit welchem Faktor :math:`x` zu
  multiplizieren ist, um :math:`-3 \cdot x^2` zu erhalten; als Ergebnis kann man
  wiederum :math:`-3 \cdot x` auf die rechte Seite schreiben. Das Produkt aus
  :math:`-3 \cdot x \cdot (x-3)` muss vom verbleibenden Term abgezogen werden.
  Man erhält:

  .. math::

      \begin{array}{rlll}
      (x^3 &-  6 \cdot x^2 &-  1 \cdot x &+  30) : (x - 3) = x^2 - 3 \cdot x \;
      + \; ?\\
      -(x^3 & - 3 \cdot x^2) \\ \cline{1-2} \\[-8pt]
      & -3 \cdot x^2 & - 1 \cdot x &+ 30 \\
      \qquad -(& -3 \cdot x^2 & + 9 \cdot x) \\\cline{1-3}\\[-8pt]
      && -10 \cdot x & + 30
      \end{array}

  Um den verbleibenden Term zu erhalten, muss :math:`(x-3)` mit dem Faktor
  :math:`(-10)` multipliziert werden. Man erhält also:

  .. math::

      \begin{array}{rllll}
      (x^3 &-  6 \cdot x^2 &-  1 \cdot x &+  30) & : (x - 3) = x^2 - 3 \cdot x - 10\\
      -(x^3 & - 3 \cdot x^2) \\ \cline{1-2} \\[-8pt]
      & -3 \cdot x^2 & - 1 \cdot x &+ 30 \\
      \qquad -(& -3 \cdot x^2 & + 9 \cdot x) \\\cline{1-3}\\[-8pt]
      &&-10 \cdot x & + 30 \\
      &\qquad -(&-10 \cdot x & + 30) \\\cline{1-4}\\[-8pt]
      &&& 0
      \end{array}

  Der bei der Polynomdivision verbleibende Rest-Term ist also :math:`x^2 - 3
  \cdot x - 10`. Setzt man diesen Term gleich Null, so kann man die
  verbleibenden Lösungen der ursprünglichen Gleichung berechnen:

  .. math::

      x^2 - 3 \cdot x - 10 = 0

  Diese quadratische Gleichung kann wahlweise mittels der Mitternachtsformel
  oder (in diesem Fall wohl einfacher) mittels des Satzes von Vieta gelöst
  werden. Man erhält:

  .. math::

      x_2 = -2 \qquad x_3 = 5

  Die Lösungsmenge der ursprünglichen Gleichung lautet somit
  :math:`\mathbb{L}=\{-2;\, 3;\, 5\}`.

  :ref:`Zurück zur Aufgabe <alg01>`

.. sy.expand( (x-3)*(x-5)*(x+2) )
.. x**3 - 6*x**2 - x + 30

----

.. _alg02l:

* :math:`\text{a) }` Die Gleichung :math:`2 \cdot x^3 - 5 \cdot x^2 - 12 \cdot x
  = 0` enthält auf der linken Gleichungs-Seite keinen Zahlenterm; es kann somit
  :math:`x` ausgeklammert werden:

  .. math::

      2 \cdot x^3 - 5 \cdot x^2 - 12 \cdot x &= 0 \\[4pt]
      \Rightarrow x \cdot (2 \cdot x^2 - 5 \cdot x - 12)  &= 0 \\[4pt]

  Man erhält damit unmittelbar :math:`x_1=0` als erste Lösung der Gleichung. Die
  übrigen Lösungen erhält man, wenn man den Restterm gleich Null setzt (denn ein
  Produkt ist stets dann Null, wenn einer der Faktoren gleich Null ist):

  .. math::

      2 \cdot x^2 - 5 \cdot x - 12 = 0

  Mittels der "Mitternachtsformel" erhält man mit :math:`a=2`, :math:`b=-5` und
  :math:`c=-12`:

  .. math::

      x_{2,3} = \frac{-b \pm \sqrt{b^2 - 4 \cdot a \cdot c}}{2 \cdot a} =
      \frac{+5 \pm \sqrt{25 - 4 \cdot 2 \cdot (-12)}}{4} = \frac{+5 \pm
      \sqrt{121}}{4}

  Die Wurzel :math:`\sqrt{121}` ergibt den Wert :math:`11`. Als Lösungen erhält
  man damit:

  .. math::

      x_2 = \frac{+5 - 11}{4} = -\frac{3}{2} \qquad x_3 = \frac{+5+11}{4} = 4

  Die Lösungsmenge der Gleichung lautet also :math:`\mathbb{L} = \{
  -\frac{3}{2};\, 0;\, 4 \}`.

* :math:`\text{b) }` Die Gleichung :math:`x^4 - 13 \cdot x^2 + 36 = 0` enthält
  auf der linken Seite nur :math:`x`-Terme mit geraden Exponenten; man kann
  daher :math:`x^2` durch eine neue Variable :math:`z` ersetzen
  ("Substitution"). Für diese neue Variable ergibt sich folgende Gleichung:

  .. math::

      z^2 - 13 \cdot z + 36 = 0

  Diese quadratische Gleichung kann wahlweise mittels der Mitternachtsformel
  oder (in diesem Fall wohl einfacher) mittels des Satzes von Vieta gelöst
  werden. Man erhält:

  .. math::

      z_1 = 4 \qquad z_2 = 9

  Die ursprüngliche Gleichung hat höchstens vier Lösungen, da der größte
  auftretende Exponent gleich vier ist. Diese Lösungen ergeben sich mit den
  obigen Lösungen für :math:`z` folgendermaßen:

  .. math::

      x_{1,2}^2 = 4 \quad \Longleftrightarrow \quad x_{1,2} = \pm \sqrt{4} \\
      x_{3,4}^2 = 9 \quad \Longleftrightarrow \quad x_{3,4} = \pm \sqrt{9} \\

  Man erhält damit als Lösungen :math:`x_1 = -2`, :math:`x_2 = +2`, :math:`x_3 =
  -3` und :math:`x_4 = +3`. Durch Einsetzen dieser Werte in die ursprüngliche
  Gleichung kann/muss geprüft werden, ob es sich tatsächlich um Lösungen der
  ursprünglichen Gleichung handelt, da durch das Quadrieren beziehungsweise
  Wurzelziehen (keine Äquivalenzumformung!) "Scheinlösungen" entstehen können.

  Da die obigen Werte tatsächlich die Gleichung erfüllen, ergibt sich als
  Lösungsmenge der Gleichung :math:`\mathbb{L} = \{ -3;\, -2;\, 2;\, 3 \}`.

  :ref:`Zurück zur Aufgabe <alg02>`

.. sy.solve( sy.Eq(2*x**3 - 5*x**2 -12*x, 0) )
.. [-3/2, 0, 4]

.. sy.expand( (x-2)*(x+2)*(x-3)*(x+3))
.. x**4 - 13*x**2 + 36

----





.. _Lösungen Bruch-, Produkt- und Wurzelgleichungen:

Bruch-, Produkt- und Wurzelgleichungen
--------------------------------------

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Bruchgleichungen und Wurzelgleichungen>` zum Abschnitt :ref:`Bruch-, Produkt-
und Wurzelgleichungen <Bruchgleichungen und Wurzelgleichungen>`.

.. _Lösungen Bruchgleichungen:
.. _Lösungen Produktgleichungen:

.. rubric:: Bruch- und Produktgleichungen

----

.. _prog01l:

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

  **Hinweis:** Würde man im ersten Schritt durch :math:`(x-5)` dividieren, so
  bliebe nur noch die Lösung :math:`x=2` übrig. Bei einer Division einer
  Gleichung durch einen Term muss also stets darauf geachtet werden, dass dieser
  Term ungleich Null ist; gegebenenfalls muss eine Fallunterscheidung
  vorgenommen und dieser Fall -- im obigen Beispiel :math:`x=5` -- separat
  untersucht werden.

  :ref:`Zurück zur Aufgabe <prog01>`

----

.. _bru01l:

* Bei Bruchgleichungen muss ausgeschlossen sein, dass die Nenner der
  auftretenden Terme gleich Null werden; es muss also gelten:

  .. math::

      2 \cdot x + 10 \ne 0 \quad &\Longleftrightarrow \quad x \ne -5 \text{ und }\\
      4 - 2 \cdot x \ne 0 \quad &\Longleftrightarrow \quad x \ne 2

  Um die Gleichung zu lösen, ist es empfehlenswert, beide Seiten der Gleichung
  mit dem Hauptnenner :math:`(2 \cdot x + 10) \cdot (4 - 2 \cdot x)` zu
  multiplizieren. Nach dem Kürzen entfallen dadurch die Nenner:

  .. math::

      \frac{3 \cdot x + 13}{2 \cdot x + 10} &= \frac{4 - 3 \cdot x}{4 - 2\cdot
      x} \\[8pt]
      \frac{\cancel{(2 \cdot x + 10)} \cdot (4 - 2 \cdot x) \cdot (3 \cdot x +
      13)}{\cancel{2 \cdot x + 10}} &= \frac{(4 - 3 \cdot x) \cdot (2 \cdot x +
      10) \cdot \cancel{(4 - 2 \cdot x)}}{\cancel{4 - 2\cdot x}} \\[8pt]
      \Rightarrow (4 - 2 \cdot x) \cdot (3 \cdot x + 13) &= (4 - 3 \cdot x)
      \cdot (2 \cdot x + 10)

  Um diese Gleichung weiter zu vereinfachen, müssen die Terme auf beiden Seiten
  ausmultipliziert werden, denn ansonsten wäre ein Sortieren der Gleichung in
  Variablen-Terme und reine Zahlen-Terme nicht möglich. Man erhält:

  .. math::

      12 \cdot x + 52 - 6 \cdot x^2 - 26 \cdot x &= 8 \cdot x + 40 - 6 \cdot x^2
      - 30 \cdot x \\
      - 6 \cdot x^2 -14 \cdot x + 52 &= -6 \cdot x^2 -22 \cdot x + 40 \\

  Sortiert man nun alle :math:`x`-Terme auf die linke und alle übrigen Terme auf
  die rechte Seite, so entfällt der quadratische Term. Übrig bleibt eine lineare
  Gleichung mit folgender Lösung:

  .. math::

      8 \cdot x \; &= -12 \\
      x \; &= -\frac{3}{2} \\

  Die Lösungsmenge der Gleichung ist somit :math:`\mathbb{L} = \{ -\frac{3}{2} \}`.

  :ref:`Zurück zur Aufgabe <bru01>`

----

.. _Lösungen Wurzelgleichungen:

.. rubric:: Wurzelgleichungen

----

.. _wurz01l:

* Betrachtet man (ohne jegliche algebraische Umformung) den Definitionsbereich
  der Gleichung, so stellt man fest, dass dieser der leeren Menge
  :math:`\emptyset` entspricht: Es gibt nämlich keinen Wert für die Variable
  :math:`x`, so dass die beiden Bedingungen :math:`x-5 \ge 0` und :math:`2-x \ge
  0` gleichzeitig erfüllt sind. Da dies nicht möglich ist, kann die Gleichung
  folglich für keine reelle Zahl :math:`x \in \mathbb{R}` erfüllt werden.

  :ref:`Zurück zur Aufgabe <wurz01>`

----

.. _wurz02l:

* :math:`\text{a) }` Die Definitionsmenge ergibt sich, da reellwertige Wurzeln
  nicht negativ sein dürfen, aus folgenden Ungleichungen:

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
  3;\,8 \}` ist -- doch das ist falsch! Die Definitionsmenge :math:`\mathbb{D} =
  [5;\,\infty[` der ursprünglichen Gleichung schließt die Lösung :math:`x_1 = 3`
  der späteren quadratischen Gleichung aus. Der Grund für das Hinzukommen der
  "Scheinlösung" liegt im ersten Rechenschritt, nämlich dem Quadrieren beider
  Seiten der Gleichung. Da diese Umformung keine Äquivalenz-Umformung ist,
  können -- wie in diesem Beispiel -- weitere Lösungen hinzukommen.

  Neben einem Blick auf den Definitionsbereich schließt auch ein Einsetzen der
  erhaltenen Lösungen in die ursprüngliche Gleichung die Scheinlösung
  :math:`x_1=3` aus. Die Lösungsmenge lautet also :math:`\mathbb{L} = \{ 8 \}`.

* :math:`\text{b) }` Der Definitionsbereich dieser Gleichung muss folgende beide
  Bedingungen erfüllen:

  .. math::

      3 \cdot x + 7 \ge 0 \quad &\Longleftrightarrow \quad x \ge -2\tfrac{1}{3} \\
      2 - 2 \cdot x \ge 0 \quad &\Longleftrightarrow \quad x \le 1\\

  Der Definitionsbereich :math:`\mathbb{D}` der Gleichung entspricht somit dem
  Intervall :math:`[-2\tfrac{1}{3};\; 1]`. Durch ein Quadrieren der Gleichung
  ergibt sich:

  .. math::

      \left( \sqrt{3 \cdot x + 7} \right)^2 = \left( 2 - 2 \cdot x \right)^2 \\[4pt]
      3 \cdot x + 7 = 4 - 8 \cdot x +  4 \cdot x^2 \\[4pt]

  Durch das Quadrieren wird die Wurzelgleichung somit zu einer quadratischen
  Gleichung. Durch ein Sortieren der einzelnen Terme auf die linke
  Gleichungsseite kann diese auf Normalform gebracht werden:

  .. math::

      4 \cdot x^2 - 11 \cdot x - 3 = 0

  Mittels der "Mitternachtsformel" kann diese Gleichung gelöst werden, wenn man
  für :math:`a=4`, :math:`b=-11` und :math:`c=-3` setzt:

  .. math::

      x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4 \cdot a \cdot c}}{2 \cdot a} =
      \frac{+11 \pm \sqrt{121 - 4 \cdot 4 \cdot (-3)}}{8} = \frac{11 \pm
      \sqrt{169}}{8}

  Die Wurzel :math:`\sqrt{169}` ergibt den Wert :math:`13`. Als Lösungen erhält
  man damit:

  .. math::

      x_1 = \frac{11 - 13}{8} = -\frac{1}{4} \qquad x_2 = \frac{11+13}{8} = 3

  Nur die Lösung :math:`x_1` ist im Definitionsbereich :math:`\mathbb{D}` der
  Gleichung enthalten, :math:`x_2` hingegen stellt eine durch das Quadrieren der
  Gleichung entstandene Scheinlösung dar. Die Lösungsmenge der Gleichung lautet
  somit :math:`\mathbb{L} = \{ -\frac{1}{4} \}`.

  :ref:`Zurück zur Aufgabe <wurz02>`

.. sy.solve( sy.Eq( sy.sqrt(3*x + 7), 2 - 2*x ) )
.. [-1/4]
.. sy.solve( sy.Eq( 4*x**2 - 11*x -3, 0 ) )
.. [-1/4, 3]


----


.. _Lösungen Exponential- und Logarithmusgleichungen:

Exponential- und Logarithmusgleichungen
---------------------------------------

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Exponential- und Logarithmusgleichungen>` zum Abschnitt :ref:`Exponential- und
Logarithmusgleichungen <Exponential- und Logarithmusgleichungen>`.

----

.. _gel01l:

* :math:`\text{a) }` Die Gleichung kann gelöst werden, indem beide Seiten
  logarithmiert werden:

  .. math::

      3^{x} &= 12 \\[4pt]
      \Rightarrow \; \log{\left(3^{x}\right)} &= \log{(12)}

  Die Wahl des :math:`10`-er-Logarithmus war/ist hierbei willkürlich. Nun kann
  allerdings die Rechenregel :math:`\log_{a}{\left( b^c \right)} = c \cdot
  \log_{a}{b}` genutzt werden (siehe :ref:`Rechenregeln für Logarithmen <Summen und
  Differenzen von Logarithmen>`), so dass sich folgende Gleichung ergibt:

  .. math::

      x \cdot \log{(3)} &= \log{12} \\
      \Rightarrow \; x &= \frac{\log{(12)}}{\log_{}{(3)}} \approx 2,262

  Die Gleichung gilt also für :math:`x \approx 2,262`.

.. sy.solve( sy.Eq( sy.log(3**x), sy.log(12) ) )
.. [log(12)/log(3)]

.. sy.N(sy.solve( sy.Eq( sy.log(3**x), sy.log(12) ) )[0] )
.. 2.26185950714292

* :math:`\text{b) }` Die Gleichung kann gelöst werden, indem beide Seiten
  auf die gleiche Basis gebracht werden. Auf der rechten Seite der Gleichung
  nämlich :math:`4 = 2^2` gesetzt werden:

  .. math::

      2^{2 \cdot x + 2} &= 4^{3 \cdot x - 15} \\
      2^{2 \cdot x + 2} &= \left(2^2\right)^{3 \cdot x - 15} \\

  Diese Umformung hat den Vorteil, dass nun die Rechenregel :math:`\left( a^b
  \right)^c = a^{b \cdot c}` angewendet werden kann:

  .. math::

      2^{2 \cdot x + 2} &= 2^{2 \cdot (3 \cdot x - 15)} \\
      2^{2 \cdot x + 2} &= 2^{6 \cdot x - 30} \\

  Sind die Basen auf beiden Seiten der Gleichung identisch, so müssen auch die
  Exponenten gleich sein. Es muss also gelten:

  .. math::

      2 \cdot x + 2 &= 6 \cdot x - 30 \\
      4 \cdot x &= 32 \\
      x &= 8 \\

  Die Gleichung hat somit die Lösung :math:`x=8`.

  :ref:`Zurück zur Aufgabe <gel01>`

.. sy.solve( sy.Eq( 2**(2*x+2), 4**(3*x-15) ) )
.. 8

----

.. _gel02l:

* :math:`\text{a) }` Die Definitionsmenge der Gleichung ist :math:`\mathbb{D} = \{ x \,|\, x > 0,\;
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


* :math:`\text{b) }` Um die Gleichung zu lösen, werden zunächst beide Seiten der
  Gleichung als Exponenten zur Basis :math:`5` geschrieben. Auf der linken Seite
  entfällt dabei wegen :math:`5^{\log_{\mathrm{5}}{x}} = x` der Logarithmus:

  .. math::

      \log_{5}{(3 \cdot x - 2)} &= 4 \\[4pt]
      \Rightarrow \; 3 \cdot x - 2 &= 5^4 \\
       3 \cdot x - 2 &= 625 \\
       3 \cdot x &= 627 \\
       x &= 209

  Die Gleichung hat somit die Lösung :math:`x=209`.

  :ref:`Zurück zur Aufgabe <gel02>`

.. sy.N(sy.solve( sy.Eq( sy.log(3*x-2, 5), 4 ) )[0] )
.. 209.000000000000

----

.. .

.. only:: html

    :ref:`Zurück zum Skript <Exponential- und Logarithmusgleichungen>`



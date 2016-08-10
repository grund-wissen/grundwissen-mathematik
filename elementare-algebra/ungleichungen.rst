.. index:: Ungleichung
.. _Ungleichungen:

Ungleichungen
=============

Sind zwei Terme :math:`T_1` und :math:`T_2` durch die Kleiner-als-Relation
:math:`<` oder die Größer-als-Relation :math:`>` miteinander verbunden, so
spricht man von einer Ungleichung. [#]_

.. math::
    :label: eqn-ungleichung:

    T_1 < T_2  \quad \text{oder} \quad  T_1 > T_2

Für Ungleichungen gilt ebenso wie für :ref:`Gleichungen <Eigenschaften von
Gleichungen>`, dass man durch Belegung der Variablen mit konkreten Werten eine
wahre oder falsche Aussage erhält. Die Definitionsmenge :math:`\mathbb{D}` einer
Ungleichung ist, sofern durch die Terme :math:`T_1` und :math:`T_2` keine
Einschränkung vorgegeben ist, gleich der Menge :math:`\mathbb{R}` der reellen
Zahlen.

.. index:: Intervall

Ungleichungen können keine, eine, mehrere oder unendlich viele Lösungen haben.
Im Allgemeinen besteht die zu bestimmende Lösungsmenge :math:`\mathbb{L}` aus so
genannten Intervallen, d.h. aus Teilbereichen von :math:`\mathbb{R}`. Jedes
Intervall hat eine untere Grenze :math:`a` und eine obere Grenze :math:`b` und
umfasst somit alle Zahlen :math:`a < b`, die zwischen diesen Grenzen liegen.

Intervalle lassen sich auf einfache Weise durch eckige Klammern angeben. Je
nachdem, ob die Grenzen eines Intervalls noch zum Intervall gehören sollen oder
nicht, unterscheidet man folgende Fälle:

* | Für ein geschlossenes Intervall gilt :math:`a \le x \le b`.
  | Man schreibt dafür :math:`[a \,;\, b]`.
* | Für ein halboffenes Intervall gilt entweder :math:`a \le x < b` oder
    :math:`a < x \le b`.
  | Man schreibt dafür :math:`[a \,;\, b[` beziehungsweise :math:`]a \,;\, b]`.
* | Für ein offenes Intervall gilt :math:`a < x < b`.
  | Man schreibt dafür :math:`]a \,;\, b[`.


.. _Lösen von Ungleichungen:

.. rubric:: Lösen von Ungleichungen

Ungleichungen lassen sich ebenso wie Gleichungen durch schrittweises Umformen
lösen. Auch hierfür spielen :ref:`äquivalente Umformungen <Umformen von
Gleichungen>` eine wesentliche Rolle. Beispielsweise lassen sich die linke und
die rechte Seite einer Ungleichung vertauschen, wenn gleichzeitig auch das
Relationszeichen "umgedreht" wird:

.. math::

    T_1 < T_2 \quad \Leftrightarrow \quad T_2 > T1

Termumformungen, die sich nur auf eine Seite einer Gleichung auswirken,
beispielsweise :ref:`Zusammenfassen <Assoziativgesetz>` und
:ref:`Ausmultiplizieren bzw. Ausklammern <Distributivgesetz>` von
Summentermen sowie :ref:`Kürzen und Erweitern <Erweitern und Vereinfachen>` von
Bruchtermen, dürfen ohne Änderung des Relationszeichens jederzeit vorgenommen werden.

Eine Ungleichung bleibt zudem unverändert, wenn man auf beiden Seiten einen
beliebigen Term :math:`T` addiert oder subtrahiert.

.. math::

      T_1 < T_2 \quad &\Leftrightarrow  \quad T_1 + T < T_2 + T \\[2pt]
      T_1 < T_2 \quad &\Leftrightarrow  \quad T_1 - T < T_2 - T \\[2pt]

Multipliziert oder dividiert man eine Gleichung mit bzw. durch einen Term
:math:`T`, so muss zum einen -- wie bei Gleichungen -- auf die Bedingung
:math:`T \ne 0` geachtet werden, da ansonsten zusätzliche Lösungen hinzukommen
bzw. ursprünglich gültige Lösung verschwinden können. Zum anderen ist zu
beachten, dass das Relationszeichen umgedreht werden muss, wenn :math:`T < 0`
ist. Somit gilt:

.. math::

      T_1  < T_2  \quad &\Leftrightarrow \quad T_1 \, \cdot \; T < T_2 \, \cdot
      \; T \qquad (T > 0)\\[2pt]
      T_1  < T_2  \quad &\Leftrightarrow \quad T_1 \, : \, T < T_2 \, : \, T
      \qquad (T > 0)

bzw.

.. math::

      T_1  < T_2  \quad &\Leftrightarrow \quad T_1 \, \cdot \; T > T_2 \, \cdot
      \; T \qquad (T < 0)\\[2pt]
      T_1  < T_2  \quad &\Leftrightarrow \quad T_1 \, : \, T > T_2 \, : \, T
      \qquad (T < 0)

Werden neben den vier grundlegenden Rechenoperationen (Addition, Subtraktion,
Multiplikation und Division) weitere Rechenoperationen (z.B. Potenzieren,
Wurzelziehen oder Logarithmieren) angewendet, so sind wiederum zusätzliche
Überlegungen nötig.


..  Eine Kontrolle der Lösungsmenge kann auch bei Ungleichungen durch Einsetzen der
..  Elemente in die Ausgangsgleichung ("Probe") erfolgen. Bei einer Probe ist jede
..  Gleichungsseite getrennt auszurechnen, d.h. es dürfen keine
..  Gleichungsumformungen vorgenommen werden.

.. _Lineare Ungleichungen:

Lineare Ungleichungen
---------------------

Eine Ungleichung heißt linear, wenn sie in folgender allgemeiner Form
dargestellt werden kann:

.. math::
    :label: eqn-lineare-ungleichung

    a \cdot x + b < 0

| Die Lösung einer linearen Ungleichung ist :math:`x < - \frac{b}{a}`, falls
  :math:`a > 0` ist. Wenn andernfalls :math:`a < 0` gilt, so ist die Lösung
  :math:`x > - \frac{b}{a}`.
| (Die Division durch eine negative Zahl dreht das Ungleichungszeichen um.)

*Beispiel*:

* Für welche :math:`x`-Werte gilt die folgende Ungleichung?

  .. math::

      3 \cdot x -4 < -5 \cdot x + 9

  Zunächst wird die Gleichung in die allgemeine Form :math:`a \cdot x + b < 0`
  gebracht:

  .. math::

      8 \cdot x - 13 < 0

  Da in diesem Fall der Koeffizient :math:`a=8` positiv ist, folgt mit :math:`b
  = -13` für die Lösung :math:`x < -\frac{b}{a}`:

  .. math::

      x < \frac{13}{8}

  Die Ungleichung ist somit für alle  :math:`x`-Werte kleiner als
  :math:`\frac{13}{8} = 1,625` erfüllt.

Löst man eine lineare Ungleichung mit Papier und Bleistift, so kann es einfacher
sein, alle :math:`x`-Terme auf die eine Seite und alle anderen Terme auf die
andere Seite zu sortieren und anschließend die Ungleichung durch den
Koeffizienten des :math:`x`-Terms zu teilen. Dies funktioniert jedoch einerseits
nur bei linearen Ungleichungen, andererseits verlangen auch
Computer-Algebra-Systeme wie :ref:`Sympy <gwip:Sympy>` teilweise explizit
die in Gleichung :eq:`eqn-lineare-ungleichung` angegebene Darstellung.

Quadratische Ungleichungen
--------------------------

Eine Ungleichung heißt quadratisch, wenn sie in folgender allgemeiner Form
dargestellt werden kann:

.. math::
    :label: eqn-quadratische-ungleichung

    a \cdot x^2 + b \cdot x + c < 0

Um eine quadratische Ungleichung zu lösen, zerlegt man den Term auf der linken
Seite, sofern möglich, in ein Produkt aus zwei Linearfaktoren. Dieses Produkt
kann nur dann negativ sein, wenn beide Faktoren unterschiedliche Vorzeichen
haben. Mittels zweier Fallunterscheidung wird also geprüft, für welche
:math:`x`-Werte jeweils ein Linearfaktor positiv und der andere negativ ist; die
Lösung der quadratischen Ungleichung ist dann die Vereinigungsmenge beider
Teillösungen.

.. todo *Beispiel*:

Lässt sich der Term auf der linken Seite nicht in Linearfaktoren zerlegen, so
ist die Ungleichung entweder für alle :math:`x`-Werte wahr oder für alle
:math:`x`-Werte falsch. Welcher Fall zutrifft, lässt sich durch ein probeweises
Einsetzen eines beliebigen :math:`x`-Wertes leicht ermitteln.


.. _Betragsungleichungen:

Betragsungleichungen
--------------------

Ungleichungen, die einen in Betragszeichen stehenden Term :math:`T` enthalten,
erfordern eine Fallunterscheidung hinsichtlich dieses Terms:

* Für alle :math:`x`-Werte, die als Bedingung :math:`T \ge 0` erfüllen,
  können die Betragsstriche durch runde Klammern ersetzt werden.

* Für alle :math:`x`-Werte, die :math:`T<0` zur Folge haben, werden die
  Betragsstriche durch runde Klammern ersetzt und mit :math:`(-1)`
  multipliziert.

Nach dieser Fallunterscheidung wird die verbleibende Ungleichung gelöst. In
beiden Fällen ist die Teil-Lösungsmenge gleich der Schnittmenge aus der Menge an
:math:`x`-Werten, für die :math:`T \ge 0` beziehungsweise :math:`T <0` ergibt,
und der jeweiligen Lösung der resultierenden Ungleichung. Die
Gesamt-Lösungsmenge ist schließlich gleich der Vereinigungsmenge beider
Teil-Lösungsmengen.

..  todo *Beispiel*:

.. _Bruchungleichungen:

Bruchungleichungen
------------------

Jede Bruchungleichung kann in eine der zwei folgenden Formen gebracht werden:

.. math::
    :label: eqn-bruchungleichung

    \frac{a}{b} > 0 \quad \text{oder} \quad \frac{a}{b} < 0

Im ersten Fall ist nur dann eine Lösung möglich, wenn :math:`a` und
:math:`b` beide positiv oder beide negativ sind. Im zweiten Fall muss entweder
:math:`a` negativ und :math:`b` positiv sein, oder umgekehrt :math:`a` positiv
und :math:`b` negativ. Führen die sich ergebenden Fallunterscheidungen
zu keinem Ergebnis, so ist die Ungleichung nicht lösbar.

*Beispiel*:

* Für welche :math:`x`-Werte gilt die folgende Ungleichung?

  .. math::

      \frac{x-2}{x+3} < 6

  Zunächst wird die Gleichung in die allgemeine Form :eq:`eqn-bruchungleichung`
  gebracht:

  .. math::

      \frac{x-2}{x+3} - 6 &< 0 {\color{white}\qquad 1}\\[3pt]
      \frac{x-2}{x+3} - \frac{6 \cdot (x+3)}{x+3} &<0 \\[3pt]
      \frac{x-2-6\cdot x-18}{x+3} &<0 \\[3pt]
      \frac{-5 \cdot x -20}{x+3} &< 0

  Die erste Möglichkeit, dass die Ungleichung erfüllt wird, besteht darin, dass
  der Zähler positiv und der Nenner negativ ist. Dabei muss gelten:

  .. math::

      -5 \cdot x - 20 > 0 \quad &\text{und} \quad x + 3 < 0 \\
      -5 \cdot x > 20 \quad & \text{und} \quad x < -3 \\
      x < -4 \quad & \text{und} \quad x < -3

  Die erste Teillösung lautet somit :math:`x < -4`, da nur diese
  :math:`x`-Werte beide Bedingungen gleichzeitig erfüllen.

  Die zweite Möglichkeit, dass die Ungleichung erfüllt wird, besteht darin, dass
  der Zähler negativ und der Nenner positiv ist. Dabei muss gelten:

  .. math::

      -5 \cdot x - 20 < 0 \quad &\text{und} \quad x + 3 > 0 \\
      -5 \cdot x < 20 \quad & \text{und} \quad x > -3 \\
      x > -4 \quad & \text{und} \quad x > -3

  Die zweite Teillösung lautet somit :math:`x > -3`, da nur diese
  :math:`x`-Werte beide Bedingungen gleichzeitig erfüllen.

  Die Gesamt-Lösung ist gleich der Vereinigungsmenge beider Teillösungen, also
  :math:`]\!-\!\infty \,;\, -4[ \;\; \cup \;\; ]\! -\!3 \,;\, +\!\infty[`.

Ebenso wäre es möglich, die ursprüngliche Gleichung :math:`\frac{a}{b} < c` mit
dem Nenner des Bruchterms zu multiplizieren; hierbei muss jedoch ebenso mittels
einer Fallunterscheidung geprüft werden, für welche :math:`x`-Werte der Nenner
positiv bzw. negativ ist; anschließend muss die sich ergebende Ungleichung
mittels weiterer Fallunterscheidungen gelöst werden. Der insgesamte
Rechenaufwand wird durch dieses Verfahren also meist nicht verringert.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Eine Ungleichung der Form :math:`T_1 \le T_2` stellt eine Vereinigung
    der Fälle :math:`T_1 < T_2` und :math:`T_1 = T_2` dar. Entsprechendes gilt
    für Ungleichungen mit der Größer-als-Relation :math:`\ge`.



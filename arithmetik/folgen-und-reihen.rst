.. _Folgen und Reihen:

Folgen und Reihen
=================


.. index:: Folge

.. _Folgen und ihre Eigenschaften:

Folgen und ihre Eigenschaften
-----------------------------

Ordnet man jeder natürlichen Zahl :math:`n \in \mathbb{N}`  eine reelle Zahl
:math:`a_{\mathrm{n}}` eindeutig zu, so entsteht eine unendliche (reelle) Folge
:math:`(a_{\mathrm{n}})`. Die einzelnen Werte der Folge heißen Folgenglieder und
werden mit Indizes durchnummeriert:

.. math::

    ( a_{\mathrm{n}} ) = a_1 ,\,  a_2 ,\, a_3 ,\, \ldots
    ,\, a_{\mathrm{n}} ,\, \ldots

Im Unterschied zu einer Menge kann bei einer Folge ein und das selbe Glied
mehrere Male auftreten. Die Definition einer Folge kann auf zweierlei Arten
erfolgen:

* Viele Folgen lassen sich nach einem Bildungsgesetz mittels eines Terms
  aufstellen. Das Bildungsgesetz wird hierzu in runde Klammern geschrieben.
  Beispiel:

  .. math::

    (a_{\mathrm{n}}) = (2 \cdot n^2) = 2 ,\,  8 ,\,  18 ,\, 32 ,\, \ldots

.. index:: Rekursion, Fibonacci-Folge

* Ist (mindestens) das erste Folgenglied bekannt und besteht eine
  Rechenvorschrift, wie sich ein Folgenglied aus einem vorhergehenden berechnen
  lässt, so sind alle Glieder einer Folge ebenfalls eindeutig festgelegt.
  Dieses Vorgehen wird als "Rekursion" bezeichnet. Beispiel:

   .. math::

    a_{\mathrm{n}} = 0 ,\, 1 ,\, 2 ,\, 3 ,\, 5 ,\, 8 ,\, 13 ,\, 21 ,\, \ldots

  Die obige Zahlenfolge wird auch zu Ehren von `Leonardo Fibonacci
  <https://de.wikipedia.org/wiki/Fibonacci>`_ als "Fibonacci-Folge" bezeichnet.
  Die Folgenglieder lassen sich dadurch berechnen, indem jeweils die Summe der
  beiden vorangehenden Folgenglieder gebildet wird. Das Bildungsgesetz der Folge
  lautet somit für :math:`n \ge 2`:

  .. math::

      a_{\mathrm{n}} = a_{\mathrm{n-2}} + a_{\mathrm{n-1}}

Beschränkt man die Definitionsmenge auf die ersten :math:`n` natürlichen Zahlen
:math:`(n \ne 0)`, so erhält man eine endliche Folge mit dem Anfangsglied
:math:`a_1` und dem Endglied :math:`a_{\mathrm{n}}`.


.. index::
    single: Monotonie einer Zahlenfolge

.. _Monotonie einer Zahlenfolge:

Monotonie einer Zahlenfolge
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ein wichtiges Kriterium bei der Unterscheidung von Zahlenfolgen ist ihre so
genannte Monotonie. Werden die Werte der Folgenglieder mit zunehmendem Index
kontinuierlich (wenn möglicherweise auch in unterschiedlichem Maß) größer, so
nennt man die Folge monoton wachsend zunehmend. Nehmen die Werte der
Folgenglieder im umgekehrten Fall kontinuierlich (möglicherweise unterschiedlich
stark) ab, so spricht man von einer monoton fallenden Folge. Bei einer
konstanten Folge bleiben die Werte im Verlauf der Folge konstant.

Es gilt somit für jede Folge :math:`(a_{\mathrm{n}})`:

.. math::

    a_{\mathrm{n + 1}} &\ge a_{\mathrm{n}} \text{\;\; für alle $n$} \quad
    \Rightarrow \quad \text{$(a_{\mathrm{n}})$ ist monoton zunehmend. } \\
    a_{\mathrm{n + 1}} &\le a_{\mathrm{n}} \text{\;\; für alle $n$} \quad
    \Rightarrow \quad \text{$(a_{\mathrm{n}})$ ist monoton abnehmend. } \\
    a_{\mathrm{n + 1}} &= a_{\mathrm{n}} \text{\;\; für alle $n$} \quad
    \Rightarrow \quad \text{$(a_{\mathrm{n}})$ ist konstant. }

Gilt bei der obigen Unterscheidung anstelle der Kleiner-Gleich-Relation
:math:`\le` die Kleiner-Relation :math:`<` bzw. anstelle der Größer-Gleich-Relation
:math:`\ge` die Größer-Relation :math:`>`, so nennt man die Folge *streng*
monoton ab- bzw. zunehmend.

.. index::
    single: Beschränktheit einer Zahlenfolge

.. _Beschränktheit einer Zahlenfolge:

Beschränktheit einer Zahlenfolge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eine Folge :math:`(a_{\mathrm{n}})` wird beschränkt genannt, wenn es zwei reelle
Zahlen :math:`s` und :math:`S` gibt, so dass die Werte aller Folgenglieder
zwischen beiden begrenzenden Zahlen liegen, d.h. wenn gilt:

.. math::

    s \le a_{\mathrm{n}} \le S \text{\;\; für alle $n$}

Hierbei wird :math:`s` als untere Schranke und :math:`S` als obere Schranke
bezeichnet.

.. index::
    single: Grenzwert einer Zahlenfolge
    single: Konvergenz
    single: Divergenz

.. _Grenzwert einer Zahlenfolge:

Grenzwert einer Zahlenfolge
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eine Folge :math:`(a_{\mathrm{n}})` hat einen Grenzwert :math:`a`, wenn sich
außerhalb einer beliebig großen Umgebung von :math:`a` nur endlich viele Glieder
der Folge befinden. Besitzt eine Folge einen Grenzwert, so nennt man sie
konvergent, andernfalls divergent.

.. Limes, \lim, \rightarrow

Bezüglich des Grenzwerts einer Folge gilt:

* Der Grenzwert einer Folge ist stets eindeutig bestimmt; insbesondere ist
  :math:`\infty` kein zulässiger Grenzwert.
* Jede monotone und beschränkte Folge ist konvergent, besitzt also einen
  (eindeutigen) Grenzwert.
* Jede konvergente Folge ist beschränkt.

*Beispiele:*

* Die Folge :math:`\left( \frac{1}{n} \right)`  ist konvergent zum Grenzwert
  :math:`0`, also gilt:

  .. math::

      \lim_{n \rightarrow \infty } \frac{1}{n} = 0

* Die Folge :math:`\left( \frac{n}{n+1} \right)` ist konvergent zum Grenzwert
  :math:`1`, also gilt:

  .. math::

      \lim_{n \rightarrow \infty } \frac{n}{n + 1} = 1

* Die Folge :math:`(n^2)` ist divergent, sie hat keinen Grenzwert.

.. index:: Nullfolge, Cauchy-Kriterium
.. _Konvergenzkriterium:

Folgen, die den Wert Null als Grenzwert haben, nennt man Nullfolgen. Ihnen kommt
eine besondere Bedeutung zu, denn allgemein gilt die Aussage, dass eine Folge
:math:`(a_{\mathrm{n}})` den Grenzwert :math:`a` hat, wenn die Folge
:math:`(a_{\mathrm{n}} - a)` eine Nullfolge ist.

Dieses Konvergenzkriterium wurde von `Augustin-Louis Cauchy
<https://de.wikipedia.org/wiki/Augustin-Louis_Cauchy>`_ in eine noch nützlichere
Form gefasst, mittels derer sich die Konvergenz einer Folge auch dann nachweisen
lässt, wenn der Grenzwert :math:`a` nicht schon von vornherein bekannt ist. Das
so genannte "Cauchy-Kriterium" besagt, dass jede Folge genau dann konvergiert,
wenn sich zu jedem beliebig kleinen Wert :math:`\varepsilon` eine Zahl
:math:`n_0 > n` finden lässt, so dass für alle Folgenglieder
:math:`a_{\mathrm{i}}, a_{\mathrm{j}}` ab :math:`a_{\mathrm{n_0}}` gilt, dass
:math:`|a_{\mathrm{i}} - a_{\mathrm{j}} | < \varepsilon` ist.


.. index::
    single: Arithmetische Folge
    single: Folge; arithmetische Folge

.. _Arithmetische Folgen:

Arithmetische Folgen
^^^^^^^^^^^^^^^^^^^^

Eine Folge heißt arithmetisch, wenn die Differenz :math:`d` zweier aufeinander
folgender Glieder stets konstant ist. Für eine arithmetische Folge gilt also:

.. math::

    a_{\mathrm{n + 1}} - a_{\mathrm{n}} = d

Als Bildungsgesetz gilt:

.. math::
    :label: eqn-arithmetische-folge-bildungsgesetz

    a_{\mathrm{n}} =  a_1 + (n - 1) \cdot d

Ist :math:`d > 0`, so ist die Folge (streng) monoton steigend, bei :math:`d < 0`
ist die Folge (streng) monoton fallend. Gilt :math:`d=0`, so ist die Folge
konstant.

Da die einzelnen Folgenglieder immer um den gleichen Betrag zu- bzw. abnehmen,
ist das mittlere dreier Folgenglieder stets gleich dem arithmetischen Mittel der
beiden benachbarten Folgenglieder. Es gilt also: [#]_

.. math::

    a_{\mathrm{n}} = \frac{a_{\mathrm{n + 1}} + a_{\mathrm{n-1}}}{2}

Wichtige arithmetische Folgen sind beispielsweise die natürlichen Zahlen
:math:`1 ,\, 2 ,\, 3 ,\, 4 ,\, \ldots`, die geraden Zahlen :math:`2 ,\, 4 ,\, 6
,\, 8 ,\, \ldots`, die ungeraden Zahlen :math:`1 ,\, 3 ,\, 5 ,\, 7 ,\,
\ldots`, usw.

Will man zwischen zwei Werten :math:`a_1` und :math:`a_2` insgesamt :math:`n`
weitere Zahlen als eine arithmetische Folge einfügen, so gilt dabei für alle
Differenzen der einzelnen Folgenglieder:

.. math::

    d_{\mathrm{i}} = \frac{a_2 - a_1}{n + 1}

.. LUM1 S.186.

Diese Formel kann beispielsweise hilfreich sein, um fehlende Werte in
Wertetabellen (näherungsweise) zu ergänzen. Eine ähnliche Anwendung kann darin
bestehen, :math:`n` Objekte (z.B. Holzbalken) in jeweils gleichem Abstand
voneinander zwischen zwei festen Grenzen :math:`a_1` und :math:`a_2` einzufügen;
dabei gibt :math:`d_{\mathrm{i}}` an, in welchem Abstand die Mittelpunkte der
Objekte jeweils eingefügt werden müssen.

..
    Arithmetische Folgen höheren Grades, lineare Funktion bzw. Potenzfunktion


.. index::
    single: Geometrische Folge
    single: Folge; geometrische Folge
.. _Geometrische Folgen:

Geometrische Folgen
^^^^^^^^^^^^^^^^^^^

Eine Folge heißt geometrisch, wenn der Quotient :math:`q` zweier aufeinander
folgender Glieder stets konstant ist. Für eine jede geometrische Folge gilt
also:

.. math::

    \frac{a_{\mathrm{n + 1}}}{ a_{\mathrm{n}} } = q

Als Bildungsgesetz gilt:

.. math::
    :label: eqn-geometrische-folge-bildungsgesetz

    a_{\mathrm{n}} =  a_1 \cdot q ^{n-1}

Ist :math:`q > 1`, so ist die Folge (streng) monoton zunehmend, bei :math:`0 < q
< 1` ist die Folge (streng) monoton abnehmend und konvergiert gegen Null. Gilt
:math:`q=0`, so ist die Folge konstant, im Fall  :math:`- \infty < q < 0` ist
die Folge "alternierend", d.h. die Werte der Folgenglieder sind abwechselnd
positiv und negativ.

Da die einzelnen Folgenglieder immer um den gleichen Faktor zu- bzw. abnehmen,
ist das mittlere dreier Folgenglieder stets gleich dem geometrischen Mittel der
beiden benachbarten Folgenglieder. Es gilt also: [#]_

.. math::

    | a_{\mathrm{n}} | = \sqrt{a_{\mathrm{n+1}} \cdot a_{\mathrm{n-1}}}

Will man zwischen zwei Werten :math:`a_1` und :math:`a_2` insgesamt :math:`n`
weitere Zahlen als eine geometrische Folge einfügen, so gilt dabei für alle
Quotienten der einzelnen Folgenglieder:

.. math::

    q_{\mathrm{i}} = \sqrt[n+1]{\frac{ a_2}{ a_1}}

.. LUM1 193.

..  todo Harmonische Folgen

.. Beispiel :math:`(a_{\mathrm{n}})` mit :math:`a_{\mathrm{n}} = \frac{1}{n}`


.. index:: Reihe, Summenzeichen
.. _Reihen und ihre Eigenschaften:

Reihen und ihre Eigenschaften
-----------------------------

Die Summe der Glieder einer Folge (oder eines Teils der Folgenglieder) wird als
Reihe bezeichnet. Mathematisch wird die Summe :math:`s_{\mathrm{n}}` der Glieder
einer Folge :math:`(a_{\mathrm{n}})` durch das Summen-Symbol :math:`\Sigma`
ausgedrückt:

.. math::
    :label: eqn-reihe

    s_{\mathrm{n}} = \sum_{i=1}^{n} a_{\mathrm{i}} = a_1 + a_2 + a_3 +
    \ldots + a_{\mathrm{n}}

Hierbei wird unterhalb des Summenzeichens die Untergrenze und oberhalb die
Obergrenze des Index :math:`i` angegeben, wobei die Summengrenzen jeweils ganze
Zahlen sind. Im obigen Fall werden alle Folgenglieder :math:`a_{\mathrm{i}}` somit
von :math:`i=1` bis :math:`i=n` aufsummiert.

..  [#]_

Ist die untere Summationsgrenze :math:`i=k` gleich der oberen, so bedeutet dies,
dass die Summe aus einer einzigen Zahl :math:`a_{\mathrm{k}}` besteht:

.. math::

    \sum_{i=k}^{k} a_{\mathrm{i}} =  a_{\mathrm{k}}

Ist die untere Summationsgrenze größer als die obere Summationsgrenze, wird das
Ergebnis der Summe als Null definiert. Weitere wichtige Rechenregeln für das
Summenzeichen sind:

.. math::
    :label: eqn-reihe-rechenregeln

    \sum_{i=1}^{n} ( a_{\mathrm{i}} +  b_{\mathrm{i}} ) &= \sum_{i=1}^{n}   a_{\mathrm{i}}
    +  \sum_{i=1}^{n}   b_{\mathrm{i}} \\[4pt]
    \sum_{i=1}^{n} ( a_{\mathrm{i}} -  b_{\mathrm{i}} ) &= \sum_{i=1}^{n}   a
    _{\mathrm{i}} -  \sum_{i=1}^{n}   b_{\mathrm{i}} \\[4pt]
    \sum_{i=i}^{n} c  \cdot   a_{\mathrm{i}} &= c  \cdot  \sum_{i=1}^{n}   a
    _{\mathrm{i}} \\[4pt]

Die oberen beiden dieser Rechenregeln entsprechen einem Umsortieren der
Summanden, das letzte einem Ausklammern des Faktors :math:`c` aus jedem
Summanden. Diese Regel findet auch Anwendung, wenn man :math:`n` Folgenglieder
mit konstantem Wert aufsummiert:

.. math::
    :label: eqn-reihe-konstant

    \sum_{i=1}^{n} c = c  \cdot  \sum_{i=1}^{n} 1 = c \cdot \underbrace{(1 + 1 +
    \ldots + 1)}_{\text{$n$-mal}} = n \cdot c

Nach der obigen Gleichung funktionieren auch digitale Zählmaschinen, die eine
Reihe von (meist elektrischen) "Eins"-Signalen aufaddieren und den
entsprechenden Wert :math:`n` anzeigen.

Zwei weitere Rechentricks werden im Umgang mit Reihen oftmals nutzvoll
eingesetzt:

.. index:: Teilsumme
.. _Teilsumme:

* Eine Reihe lässt sich in zwei (oder mehrere) Teilsummen zerlegen. Werden in
  der ursprünglichen Reihe Folgenglieder von  :math:`1` bis :math:`n`
  aufsummiert, so können in äquivalenter Weise zunächst nur die Folgenglieder
  bis zu einem zwischen beiden Grenzen liegenden Wert :math:`k` summiert werden,
  und anschließend die restlichen Folgenglieder von :math:`k+1` bis :math:`n`
  addiert werden. [#]_ Es gilt also:

  .. math::
      :label: eqn-reihe-teilsummen

      \sum_{i=1}^{n} a_{\mathrm{i}} = \sum_{i=1}^{k} a_{\mathrm{i}} + \sum_{i=k+1}^{n}
      a_{\mathrm{i}}

.. index:: Indexverschiebung
.. _Indexverschiebung:

* Der Wert einer Reihe bleibt durch eine Indexverschiebung unverändert.
  Hierunter versteht man ein Verfahren folgender Art:

  .. math::

      \sum_{i=1}^{2} a_{\mathrm{i} } =  a_1 +  a_2 = a_{\mathrm{3-2}}
      + a_{\mathrm{4-2}} = \sum_{i=3}^{4} a_{\mathrm{i-2}}

  Wird der Index der Summationsgrenzen im allgemeinen Fall um :math:`+k`
  angehoben, so muss der Index der Folgenglieder auf :math:`i-k` reduziert
  werden. [#]_ Es gilt somit:

  .. math::
      :label: eqn-reihe-indexverschiebung-plus

      \sum_{i=1}^{n} a_{\mathrm{i} } = \sum_{i=1+k}^{n+k} a_{\mathrm{i-k}}

  Eine Verminderung der Summationsgrenze um :math:`-k` bewirkt in entsprechender
  Weise eine Anhebung des Index der Folgenglieder auf :math:`i+k`:

  .. math::
      :label: eqn-reihe-indexverschiebung-minus

      \sum_{i=1}^{n} a_{\mathrm{i} } = \sum_{i=1-k}^{n-k} a_{\mathrm{i+k}}


.. index::
    single: Arithmetische Reihe
    single: Reihe; arithmetische Reihe
.. _Arithmetische Reihen:

Arithmetische Reihen
^^^^^^^^^^^^^^^^^^^^

Addiert man alle Glieder einer :ref:`arithmetischen Folge <Arithmetische
Folgen>`, d.h. eine Folge von Zahlen, die sich untereinander stets um den
gleichen Wert :math:`d` unterscheiden, so ergibt sich eine arithmetische Reihe.
Für den Wert der wohl bekanntesten arithmetischen Reihe, bei der alle
natürlichen Zahlen von :math:`1` bis :math:`n` addiert werden, hat `Carl
Friedrich Gauss <https://de.wikipedia.org/wiki/Gauss>`_ bereits in jungem Alter
die folgende Formel gefunden, die bisweilen auch "Kleiner Gauss" genannt wird:
[#]_ [#]_

.. math::
    :label: eqn-arithmetische-reihe-gauss

    s_{\mathrm{n}} = \sum_{i=1}^{n} i =  \frac{n \cdot (n+1)}{2}

Im allgemeinen Fall lässt sich der Wert einer arithmetischen Reihe
folgendermaßen berechnen: [#]_

.. math::
    :label: eqn-arithmetische-reihe

    s_{\mathrm{n}} = \sum_{i=1}^{n} a_{\mathrm{i}} = \sum_{i=1}^{n} \big( a_1 +
    (i-1) \cdot d \big)  = n \cdot  a_1 + \frac{n \cdot (n-1)}{2} \cdot d


.. index::
    single: Geometrische Reihe
    single: Reihe; geometrische Reihe
.. _Geometrische Reihen:

Geometrische Reihen
^^^^^^^^^^^^^^^^^^^

Addiert man alle Glieder einer :ref:`geometrischen Folge <Geometrische Folgen>`,
d.h. eine Folge von Zahlen, die sich untereinander stets um den gleichen Faktor
:math:`q` unterscheiden, so ergibt sich eine geometrische Reihe. Der Wert
:math:`s_{\mathrm{n}}` einer geometrischen Reihe lässt sich folgendermaßen
berechnen: [#]_

.. math::
    :label: eqn-geometrische-reihe

    s_{\mathrm{n}} = \sum_{i=1}^{\infty } a_1 \cdot q ^{i-1} =  a_1 \cdot
    \frac{q ^n -1}{q-1}

Mittels geometrischen Reihen können beispielsweise :ref:`Zinseszinsen
<Zinseszinsrechnung>` berechnet werden.

.. todo Harmonische Reihen

.. index:: Produktfolge
.. _Produktfolgen:

Produktfolgen
^^^^^^^^^^^^^

Neben gewöhnlichen Reihen als Summenfolgen können auch Produktfolgen gebildet
werden. In der Praxis sind jedoch meist nur so genannte Partialproduktfolgen von
Bedeutung, deren Ergebnis das Produkt von :math:`n` Folgengliedern ist.
Mathematisch wird ein solches Produkt :math:`p_{\mathrm{n}}` der Glieder einer
Folge :math:`(a_{\mathrm{n}})` durch das Produkt-Symbol :math:`\Pi` ausgedrückt:

.. math::

    p(n) = \prod_{i=1}^{n}a_{\mathrm{i}} = a_1  \cdot a_2  \cdot a_3  \cdot  \ldots
    a_{\mathrm{n}}

Hierbei wird unterhalb des Produktzeichens die Untergrenze und oberhalb die
Obergrenze des Index :math:`i` angegeben, wobei die Produktgrenzen jeweils ganze
Zahlen sind.

.. index:: Fakultät
.. _Fakultät:

Für die insbesondere in der :ref:`Kombinatorik <Kombinatorik>` häufig
auftretende Partialproduktfolge der natürlichen Zahlen ist eine besondere
Notation üblich:

.. math::

    p_1 &= 1! = 1 \\
    p_2 &= 2! = 1 \cdot 2 \\
    p_3 &= 3! = 1 \cdot 2 \cdot 3\\ \vdots \\
    p_{\mathrm{n}} &= n! = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot n \\

Der Ausdruck :math:`n!` wird dabei als ":math:`n` Fakultät" gelesen; für den
Sonderfall :math:`n=0` ist dabei :math:`0! = 1` definiert.

.. .. [#] Bei dem Summenzeichen handelt es sich letztlich nur um eine abkürzende
..     Schreibweise. In ähnlicher Form gibt es auch ein Produktzeichen, das mehrere
..     Faktoren eines Produkts zusammenfasst:

..     .. math::

..         \prod_{i=1}^{n} a_{\mathrm{i}} = a_1 \cdot a_2 \cdot a_3 \cdot \ldots
..         \cdot a_{\mathrm{n}}


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Bei einer arithmetischen Folge gilt:

    .. math::

        a_{\mathrm{n+1}} - a_{\mathrm{n}} = d = a_{\mathrm{n}} - a_{\mathrm{n-1}}

    Setzt man in der obigen Gleichung die linke und die rechte Seite gleich und
    löst diese Gleichung nach :math:`a_{\mathrm{n}}` auf, so erhält man die
    Rechenregel zur Berechnung des arithmetischen Mittels.

.. [#] Bei einer geometrischen Folge gilt:

    .. math::

        \frac{ a_{\mathrm{n+1}} }{ a_{\mathrm{n}}   } = q =
        \frac{ a_{\mathrm{n}}   }{ a_{\mathrm{n-1}} }

    Setzt man in der obigen Gleichung die linke und die rechte Seite gleich und
    löst diese Gleichung nach :math:`a_{\mathrm{n}}` auf, so erhält man die
    Rechenregel zur Berechnung des geometrischen Mittels.


.. [#] Im umgekehrten Fall lässt sich eine Zerlegung in Teilsummen auch
    nutzen, um den Wert einer Reihe zu berechnen, deren Glieder von :math:`k >
    1` bis :math:`n` aufsummiert werden. Hierbei gilt stets:

    .. math::

        \sum_{i=k}^{n}  a_{\mathrm{i}} = \sum_{i=1}^{n}  a_{\mathrm{i}} -
        \sum_{i=1}^{k-1} a_{\mathrm{i}}

.. [#] Diese Ersetzung ist vorzunehmen, bevor irgendeine weitere Auswertung
    erfolgt. Darauf ist insbesondere dann zu achten, wenn sich vor dem Index
    :math:`i` einer Reihe ein Minuszeichen befindet. Durch eine Verschiebung der
    Summationsgrenzen um :math:`+k` wird beispielsweise :math:`1-i` zu :math:`1
    - (i+k) = 1-i-k`.

.. [#] Die Gültigkeit von Gleichung :eq:`eqn-arithmetische-reihe-gauss` wurde
    bereits als Beispiel im Abschnitt :ref:`Die vollständige Induktion
    <Vollständige Induktion>` gezeigt.

.. [#] Ähnliche Sonderfälle arithmetischer Reihen sind die Reihen der
    geraden und ungeraden Zahlen:

    * Die Folge der geraden Zahlen :math:`2 ,\, 4 ,\, 6 ,\, 8 ,\, \ldots`
      lässt sich als :math:`(a_{\mathrm{n}}) = 2 \cdot n` ausdrücken. Für die
      entsprechende Reihe :math:`s_{\mathrm{n}}` gilt:

      .. math::

          s_{\mathrm{n}} = \sum_{i=1}^{n} 2 \cdot i = n \cdot (n+1)

    * Die Folge der ungeraden Zahlen :math:`1 ,\, 3 ,\, 5 ,\, 7 ,\, \ldots`
      lässt sich als :math:`(a_{\mathrm{n}}) = 2 \cdot n - 1` ausdrücken. Für die
      entsprechende Reihe :math:`s_{\mathrm{n}}` gilt:

      .. math::

          s_{\mathrm{n}} = \sum_{i=1}^{n} 2 \cdot i -1 = n ^2

    Nach der obigen Gleichung lässt sich somit jede Quadratzahl als
    arithmetische Reihe darstellen:

    .. math::

        1^2 &= 1 \\
        2^2 &= 1 + 3 \\
        3^2 &= 1 + 3 + 5 \\
        4^2 &= 1 + 3 + 5 + 7 \\
        &\ldots \\
        n^2 &= 1 + 3 + 5 + 7 + \ldots + (2 \cdot n - 1) \\


.. [#] Hierfür muss die Reihe zunächst aufgeteilt werden:

    .. math::

        \sum_{i=1}^{n} \big( a_1 + (i-1) \cdot d \big) = \sum_{i=1}^{n}
        a_1 + \sum_{i=1}^{n} (i-1) \cdot d

    In der ersten Teilreihe wird der konstante Wert :math:`a_1`
    aufsummiert; ihr Wert ist nach Gleichung :eq:`eqn-reihe-konstant` gleich
    :math:`n \cdot  a_1`. Bei der zweiten Teilreihe kann der konstante
    Faktor :math:`d` nach Gleichung :eq:`eqn-reihe-rechenregeln` ausgeklammert
    werden. Somit gilt:

    .. math::

        \sum_{i=1}^{n} \big( a_1 + (i-1) \cdot d \big) = n \cdot  a_1 + d \cdot
        \sum_{i=1}^{n} (i-1)

    Die zweite Teilreihe kann mittels einer Indexverschiebung gemäß Gleichung
    :eq:`eqn-reihe-indexverschiebung-minus` umgeschrieben werden. Es gilt:

    .. math::

       \sum_{i=1}^{n} (i-1) = \sum_{i = 0}^{n-1} i

    Nach Gleichung :eq:`eqn-arithmetische-reihe-gauss` gilt für den Wert dieser
    Reihe

    .. math::

       \sum_{i = 0}^{n-1} i = \frac{(n-1) \cdot (n-1+1)}{2} = \frac{n \cdot
       (n-1)}{2}

    Addiert man beide Teilreihen  und berücksichtigt dabei den Faktor :math:`d`
    (zweite Gleichung dieser Anmerkung), so erhält man Gleichung
    :eq:`eqn-arithmetische-reihe`.

.. [#] Die Formel :eq:`eqn-geometrische-reihe` zur Berechnung einer
    geometrischen Reihe kann auf zweierlei Arten dargestellt werden, denn es
    gilt:

    .. math::

          \frac{q^n -1}{q-1} = \frac{-(q^n -1)}{-(q-1)} =
          \frac{1-q^n}{1-q\phantom{^n}}

    Die erste Darstellung wird im Fall :math:`q > 1`, die zweite im Fall
    :math:`q<1` genutzt.

    Um die Gültigkeit von Formel :eq:`eqn-geometrische-reihe` zu demonstrieren,
    wird die Differenz von :math:`s_{\mathrm{n}}` und :math:`q \cdot s_{\mathrm{n}}`
    betrachtet. Es gilt:

    .. math::

        s_{\mathrm{n}} &=  a_1 \cdot (1 + q + q^2 + q^3 + \ldots + q ^{n-1})
        \\[2pt]
        q \cdot s_{\mathrm{n}} &=  a_1 \cdot (q + q^2 + q^3 + q^4 + \ldots + q
        ^{n}) \\[5pt]
        \Rightarrow s_{\mathrm{n}} - q \cdot s_{\mathrm{n}}  &=  a_1 \cdot ( 1 +
        q + q^2 + q^3 + \ldots + q ^{n-1} \\ & \phantom{ = a_1 \cdot ( 1 \,} - q
        - q^2 - q^3 - \ldots - q ^{n-1} - q^n) \\

    Auf der linken Seite kann :math:`s_{\mathrm{n}}` ausgeklammert werden, auf der
    rechten Seite heben sich alle Summanden bis auf :math:`1` und :math:`-q^n`
    auf. Folglich gilt:

    .. math::

        s_{\mathrm{n}} \cdot (1-q) =  a_1 \cdot (1 - q^n)

    Löst man diese Gleichung nach :math:`s_{\mathrm{n}}` auf, so erhält man als
    Ergebnis :math:`s_{\mathrm{n}} = a_1 \cdot \frac{1-q^n}{1-q\phantom{^n}}`,
    was nach der ersten Gleichung dieser Anmerkung mit Formel
    :eq:`eqn-geometrische-reihe` übereinstimmt.





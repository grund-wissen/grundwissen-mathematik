.. _Zahlensysteme:

Exkurs: Zahlensysteme
=====================

Zahlen lassen sich in unterschiedlichen "Zahlensystemen" in verschiedener Form
darstellen, ohne dass sich ihre mathematische Bedeutung verändert.


.. _Historische Zahlensysteme:

.. rubric:: Historische Zahlensysteme

Die Kunst des Zählens begann wohl mit der Verwendung von
Strichen zur Darstellung von Zahlen:

.. math::

    \large \mathrm{I ,\, II ,\, III ,\, IIII ,\, IIIII ,\, IIIIII ,\, \ldots }

Offensichtlich ist diese Darstellungsart für größere Zahlen sehr aufwendig und
unübersichtlich. Ein Ziel der verschiedenen Zahlensysteme, die sich im Lauf der
Zeit entwickelten, war es somit, die jeweiligen Ziffern so miteinander zu
verbinden, dass eine möglichst einfache, übersichtliche und/oder zweckmäßige
Darstellung der Zahlen ergibt. Hierbei gibt es zwei Möglichkeiten:

* Additionssysteme:
    Bei Additionssystemen werden die Werte der hintereinander gestellten
    Ziffern durch Addition (und gegebenenfalls durch Subtraktion) verknüpft.
    Hierbei ist die Wahl bestimmter Symbole als Grundziffern von grundlegender
    Bedeutung,

    *Beispiele:*

    * Beim "Kerbholz"-System aus mittelalterlicher Zeit wurden Symbole in ein
      Stück Holz eingeritzt, beispielsweise in folgender Form:

      .. math::

         \cancel{\mathrm{IIII}} \;\cancel{\mathrm{IIII}} \;
         \cancel{\mathrm{IIII}} \; \cancel{\mathrm{IIII}} \; \mathrm{III} = 23

    * Im römischen Additionssystem wurden folgende Grundziffern definiert:

      .. math::

         \mathrm{I} = 1 ,\; \mathrm{V} = 5 ,\; \mathrm{X} = 10 ,\; \mathrm{L} =
         50 ,\; \mathrm{C} = 100 ,\; \mathrm{D} = 500 ,\; \mathrm{M} = 1000

      Die einzelnen Ziffern einer Zahl werden in dieser Notationsweise
      hintereinander geschrieben, wobei die größte Ziffer üblicherweise am
      Anfang steht. Ihre Werte werden addiert. Steht jedoch :math:`\mathrm{I}`
      vor :math:`\mathrm{V}` oder :math:`\mathrm{X}`, :math:`\mathrm{X}` vor
      :math:`\mathrm{L}` oder :math:`\mathrm{C}`, :math:`\mathrm{C}` vor
      :math:`\mathrm{D}` oder :math:`\mathrm{M}`, so wird der voranstehende
      kleinere Wert vom nachfolgenden größeren subtrahiert, beispielsweise:
      [#]_

      .. math::

          \mathrm{MCMLXIX} = 1969

    Additionssysteme haben allgemein den Nachteil, bei großen Zahlen schnell
    unleserlich zu werden.

* Bei *Positionssystemen* werden die mit einem sich durch die Position
  ergebenden Stellenwert multiplizierten Werte der Ziffern addiert. Hierbei ist
  die Wahl der Basis und somit die Anzahl der Ziffern von grundlegender
  Bedeutung,

   *Beispiele:*

   * Die Babylonier nutzten bevorzugt ein Zahlensystem, das auf der Zahl 60 beruhte
     ("Sexagesimalsystem"). Noch heute wird es für Zeit- und Winkelangaben
     genutzt.
   * An das nicht mehr verwendete "Duodezimalsystem" erinnern heute
     noch im Warenhandel gebräuchliche Begriffe wie "Dutzend" :math:`(12)` oder
     "Gros" :math:`(144 = 12 \cdot 12)`.
   * In der Mathematik sind weltweit Zahlensysteme mit der Basis
     :math:`10` und ihren Potenzen am weitesten verbreitet. In der Informatik
     spielt die Basis :math:`2` und ihre Potenzen eine entscheidende Rolle.

Praktisch werden heutzutage fast ausschließlich Positionssysteme verwendet, da
sich hiermit auch große Zahlen sowie Bruchzahlen mit großer Genauigkeit
darstellen lassen.


.. _Römisches Additionssystem:


.. _Dezimalsystem:

.. rubric:: Das Dezimalsystem

Das Dezimalsystem ist ein Positionssystem mit der Basis :math:`10`. Daraus
ergeben sich als Positionsfaktoren folgende Werte:

.. math::

    1 = 10^0 ,\; 10 = 10^1 ,\; 100 = 10^2 ,\; 1000 = 10^3 ,\; \ldots

Mit diesen Positionsfaktoren ("Stellenwerten") werden die einzelnen Ziffern
einer Zahl von rechts beginnend multipliziert.

*Beispiel:*

.. math::

    4\,538 = 4 \cdot 10^3 + 5 \cdot 10^2 + 3 \cdot 10^1 + 8 \cdot 10^0

Im umgekehrten Fall kann man eine Zahl durch wiederholte Division durch die
Basis in Form ihrer Divisionsreste darstellen:

*Beispiel:*

.. math::

    4\,538 &= 453 \cdot 10 + 8 \\
    453  &= \phantom{3}45 \cdot 10 + 3  \\
    45 &= \phantom{53}4 \cdot 10 + 5 \\
    4 &=  \phantom{53}0 \cdot 10 + 4 \\

Die Dezimalziffern der darzustellenden Zahl entsprechen den Divisionsresten,
sofern diese von unten nach oben abgelesen werden. Diese Darstellungsweise wird
insbesondere bei der Konvertierung angewendet, d.h. der Übertragung einer Zahl
aus einem Zahlensystem in ein anderes.


.. _Binärsystem:

.. rubric:: Das Binärsystem

Das Binärsystem (auch "Dualsystem" genannt) ist ein Positionssystem mit der
Basis :math:`2`. Daraus ergeben sich als Positionsfaktoren folgende Werte:

.. math::

    1 = 2^0 ,\; 2 = 2^1 ,\; 4 = 2^2 ,\; 8 = 2^3 ,\; 16 = 2^4 ,\; \ldots

Um eine Dezimalzahl in eine Binärzahl umzuwandeln, wird die im vorherigen
Abschnitt beschriebene Methode der Division mit Rest angewendet. Die Binärzahl
ergibt sich aus der Dezimalzahl durch wiederholte Division mit :math:`2`, wobei
das Ergebnis an den Divisionsresten von unten nach oben abgelesen werden kann.

*Beispiel:*

.. math::

    4\,538 &= 2\,269 \cdot 2 + 0 \\
    2\,269 &= 1\,134 \cdot 2 + 1 \\
    1\,134 &= \phantom{1\,}567 \cdot 2 + 0 \\
    567 &= \phantom{1\,}283 \cdot 2 + 1 \\
    283 &= \phantom{1\,}141 \cdot 2 + 1 \\
    141 &= \phantom{1\,1}70 \cdot 2 + 1 \\
    70 &= \phantom{1\,1}35 \cdot 2 + 0 \\
    35 &= \phantom{1\,1}17 \cdot 2 + 1 \\
    17 &= \phantom{1\,11}8 \cdot 2 + 1 \\
    8 &= \phantom{1\,11}4 \cdot 2 + 0 \\
    4 &= \phantom{1\,11}2 \cdot 2 + 0 \\
    2 &= \phantom{1\,11}1 \cdot 2 + 0 \\
    1 &= \phantom{1\,11}0 \cdot 2 + 1 \\[8pt]
    \quad \Rightarrow \quad 4\,538_{10} &= 1000110111010_{2}

Um den Wechsel des Zahlensystems klar erkennbar zu machen, wird häufig die
jeweilige Zahlenbasis :math:`(2 \text{ bzw. } 10)` über einen entsprechenden
Index angedeutet.

Soll im umgekehrten Fall eine Binärzahl in eine Dezimalzahl konvertiert werden,
so müssen die auftretenden Ziffern mit ihren jeweiligen Positionsfaktoren
multipliziert und die Ergebnisse anschließend aufsummiert werden.

*Beispiel:*

.. math::

    1000110111010_{2} &= 1 \cdot 2^{12} + 0 \cdot 2^{11} + 0 \cdot 2^{10} + 0
    \cdot 2^9 + 1 \cdot 2^8 + 1 \cdot 2^7 \\ &\phantom{=} + 0 \cdot 2^6 + 1
    \cdot 2^5 + 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot
    2^0 \\[2pt] &= (4096 + 256 + 128 + 32 + 16 + 8 + 2)_{10} \\[2pt]
    &= 4\,538_{10}

Auch wenn die langen Abfolgen von Einsen und Nullen im ersten Moment als
ungewöhnlich erscheinen, so haben sie sich insbesondere bei der Entwicklung von
Computer-Systemen als fundamental wichtig erwiesen. Auch nach dem heutigen Stand
der Technik erleichtern Binärzahlen das Speichern und Übertragen von Daten
erheblich und machen ihre Verarbeitung mit Hilfe von Microcontrollern überhaupt
erst möglich.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die "Hilfsziffern" :math:`\mathrm{V ,\, L} \text{ und } \mathrm{D}` werden
    niemals größeren vorangestellt und kommen auch höchstens einmal je Zahl vor.


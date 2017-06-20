.. index:: Bruchrechnung
.. _Bruchrechnung:

Bruchrechnung
=============

Für das Rechnen mit Bruchtermen gelten prinzipiell die gleichen Regeln wie für
das Rechnen mit Bruchzahlen. Als Besonderheit ist allerdings stets darauf zu
achten, dass der Nenner des Bruchs nicht den Wert Null annehmen darf, da eine
Division durch Null nicht definiert ist. Diese Bedingung lässt sich
gegebenenfalls durch eine Beschränkung des Definitionsbereichs der im Nenner
auftretenden Variablen erreichen.

.. index:: Bruchrechnung; Erweitern und Vereinfachen
.. _Erweitern und Vereinfachen:

Erweitern und Vereinfachen
--------------------------

Ein Bruchterm :math:`\frac{z}{n}` lässt sich jederzeit erweitern, indem sowohl
der Zähler :math:`z` wie auch der Nenner :math:`n` mit dem gleichen Faktor
:math:`c \ne 0` multipliziert werden. Es gilt somit:

..  :label: eqn-bruchterm-erweitern
.. math::

    \frac{z}{n} = \frac{c \cdot z}{c \cdot n}

Ein Bruchterm lässt sich ebenso in umgekehrter Weise vereinfachen ("kürzen"),
wenn sowohl der Zählerterm wie auch der Nennerterm einen gleichen Faktor
:math:`c` (oder mehrere gleiche Faktoren :math:`c_1`, :math:`c_2` usw.)
beinhalten.

*Beispiele:*

.. math::

    \frac{3 \cdot a^2 \cdot b }{9 \cdot b^3 }
    = \frac{3 \cdot b \cdot \;\; a^2 \phantom{\;\;}}{3
    \cdot b \cdot 3 \cdot b^2} = \frac{a^2}{3 \cdot b^2}

.. math::

    \frac{a^2 -1}{(a + 1)^2 } = \frac{(a+1) \cdot (a-1)}{(a+1) \cdot (a+1)} =
    \frac{(a-1)}{(a+1)}

Besteht der Zähler und/oder der Nenner eines Bruchterms aus einer Summe von
Termen, so ist ein Kürzen nicht unmittelbar möglich; vielmehr müssen der Zähler
wie auch der Nenner jeweils vollständig in einzelne Faktoren zerlegt werden.
Hierbei können insbesondere das :ref:`Distributivgesetzes <Distributivgesetz>`
sowie :ref:`binomische Formeln <Binomische Formeln>`
hilfreich sein:

* Nach dem Distributivgesetz kann ein in allen Summanden des Zählers und/oder
  des Nenners auftretender Faktor ausgeklammert werden. Eine Summe kann damit
  als Produkt zweier Faktoren geschrieben werden.
* Jede Summe :math:`a + b` kann, sofern man sie in Klammern setzt, ebenfalls als
  einzelner Faktor :math:`1 \cdot (a+b)` angesehen werden. [#]_ Somit gilt
  beispielsweise:

  .. math::

      \frac{x+1}{2 \cdot x + 2} = \frac{1 \cdot (x+1)}{2 \cdot (x + 1)} =
      \frac{1}{2}

* Entspricht der Zähler und/oder Nenner eines Bruches (oder zumindest einer der
  auftretenden Faktoren) dem Ergebnis einer binomischen Formel, so kann diese
  angewendet werden, um eine weitere Faktorisierung zu erreichen.

Ein Bruchterm, der zum Schluss einer Rechnung ein Endergebnis darstellt, wird
üblicherweise in einer so weit wie möglich gekürzten Form angegeben.


.. _Rechenregeln für Bruchterme:

Rechenregeln für Bruchterme
---------------------------

Da bei der Rechnung mit Bruchtermen üblicherweise mit reellen Zahlen oder
entsprechenden Variablen gerechnet wird, gelten die drei :ref:`Rechengesetze für
Grundrechenarten <Rechengesetze für die Grundrechenarten>` in gleicher Form auch
für Bruchterme. Als Besonderheit muss dabei stets darauf geachtet werden, dass der
Nennerterm nicht den Wert Null annehmen darf.

Für :math:`n_1 ,\, n_2 ,\, n_3 \ne 0` gilt:

* Kommutativgesetz:

  .. math::

      \frac{z_1}{n_1} + \frac{z_2}{n_2} &=
      \frac{z_2}{n_2} + \frac{z_1}{n_1} {\color{white} \qquad \! \ldots}
      \\[2pt]
      \frac{z_1}{n_1} \, \cdot \; \frac{z_2}{n_2} &=
      \frac{z_2}{n_2} \; \cdot \, \frac{z_1}{n_1}


* Assoziativgesetz:

  .. math::

      \frac{z_1}{n_1} + \left( \frac{z_2}{n_2} + \frac{z_3}{n_3} \right)
      &= \left( \frac{z_1}{n_1} + \frac{z_2}{n_2}\right) + \frac{z_3}{n_3}
      {\color{white} \qquad \ldots} \\[2pt]
      \frac{z_1}{n_1} \, \cdot \; \left( \frac{z_2}{n_2} \, \cdot \;
      \frac{z_3}{n_3} \right) &= \left( \frac{z_ 1}{n_1} \, \cdot \;
      \frac{z_2}{n_2}\right) \; \cdot \, \frac{z_3}{n_3}

* Distributivgesetz:

  .. math::

      \frac{z_1}{n_1} \cdot \left( \frac{z_2}{n_2} + \frac{z_3}{n_3}
      \right) = \frac{z_1}{n_1} \cdot \frac{z_2}{n_2} + \frac{z_1}{n_1}
      \cdot \frac{z_3}{n_3} = \left(\frac{z_2}{n_2} + \frac{z_3}{n_3}
      \right) \cdot \frac{z_1}{n_1}{\color{white} \qquad \ldots}

Auf weitere Besonderheiten, die sich bei der Verknüpfung von Bruchtermen durch
die vier Grundrechenarten ergeben, wird in den folgenden Abschnitten näher
eingegangen.


.. index::
    single: Bruchrechnung; Addition
.. _Addition und Subtraktion von Bruchtermen:

.. rubric:: Addition und Subtraktion von Bruchtermen

Zwei Brüche lassen sich bei einer Addition oder Subtraktion nur dann direkt
zusammenfassen, wenn sie "gleichnamig" sind, d.h. den gleichen Nenner besitzen.
Dabei werden die Zählerterme addiert, der Nennerterm bleibt unverändert:

.. math::
    :label: eqn-bruch-addition

    \frac{z_1}{n} + \frac{z_2}{n} = \frac{z_1 + z_2}{n} \\[2pt]
    \frac{z_1}{n} - \frac{z_2}{n} = \frac{z_1 - z_2}{n}


..  Durch das Plus-Minus-Zeichen :math:`\pm` kann die obige Gleichung sowohl die
..  Addition wie auch die Subtraktion von gleichnamigen Brüchen beschrieben.

.. index:: Hauptnenner, Kleinstes gemeinsame Vielfache

Haben Brüche unterschiedliche Nennerterme, so müssen alle Brüche zunächst auf
einen gemeinsamen Nenner gebracht werden, bevor eine Addition beziehungsweise
Subtraktion möglich ist. Hierzu empfiehlt es sich, zunächst die Nennerterme
vollständig in einzelne Faktoren zu zerlegen. Von jedem Faktor, der in
mindestens einem der Nenner vorkommt, wählt man anschließend die jeweils höchste
Potenz aus und multipliziert diese Faktoren miteinander. Auf diese Weise erhält
man das kleinste gemeinsame Vielfache der Nennerterme :math:`(\mathrm{kgV})`,
das auch als "Hauptnenner" bezeichnet wird.

*Beispiele:*

* Entsprechen die Nenner dreier Brüche den Zahlen :math:`20`, :math:`30` und
  :math:`45` so lautet der Hauptnenner:

  .. math::

      20 &= 2^2 \; \phantom{\cdot \; 3^2 \cdot \; } \, \cdot \; 5
      {\color{white} \qquad \qquad \ldots}\\
      30 &= 2\phantom{^2} \; \cdot \; 3 \phantom{^2}\; \cdot \; 5 \\
      45 &= \phantom{2^2} \; \cdot \; 3^{2} \; \cdot \; 5 \\
      \mathrm{kgV} &= 2^2 \; \cdot \; 3^2 \; \cdot \; 5 \; =  \; 180

  Bei einem Ausmultiplizieren der einzelnen Zahlen ohne Faktorisierung und
  Bildung des kleinsten gemeinsamen Vielfachen würde sich ein gemeinsamer
  Nenner von :math:`20 \cdot 30 \cdot 45 = 27\;000` ergeben.

* Entsprechen die Nenner den Termen :math:`(2 \cdot a - 3)`, :math:`(4 \cdot a^2
  - 6 \cdot a)` und :math:`(4 \cdot a^2 - 9)` so lautet der Hauptnenner:

  .. math::

      {\color{white}\ldots \qquad \qquad \quad }(2 \cdot a - 3) &= \phantom{ 2
      \cdot a \cdot \;\; } (2 \cdot a - 3) \\
      (4 \cdot a^2 - 6 \cdot a) &= \, 2 \cdot a \cdot  (2 \cdot a - 3) \\
      (4 \cdot a^2 - 9 ) &= \phantom{ 2 \cdot a \cdot \;\;} (2 \cdot a - 3) \cdot
      (2 \cdot a + 3)\\
      \mathrm{kgV} & = \, 2 \cdot a \cdot (2 \cdot a - 3) \cdot (2 \cdot a + 3) = 8 \cdot
      a^3 - 18 \cdot a

  Bei einem Ausmultiplizieren der einzelnen Terme ohne Faktorisierung und
  Bildung des kleinsten gemeinsamen Vielfachen würde sich ein gemeinsamer Nenner
  von :math:`32 \cdot a^5 - 96 \cdot a^4  + 216 \cdot a^2  - 162 \cdot a`
  ergeben.

Die zu addierenden Brüche können anschließend um die fehlenden Faktoren
erweitert und die Zählerterme nach obiger Gleichung addiert werden.

.. index:: Bruchrechnung; Multiplikation, Größter gemeinsamer Teiler
.. _Größter gemeinsamer Teiler:
.. _Multiplikation und Division von Brüchen:

.. rubric:: Multiplikation und Division von Bruchtermen

Bruchterme lassen sich miteinander multiplizieren, indem man sowohl ihre Zähler
als auch ihre Nenner miteinander multipliziert: [#]_

.. math::
    :label: eqn-bruch-multiplikation

    \frac{z_1}{n_1} \cdot \frac{z_2}{n_2} =
    \frac{z_1 \cdot z_2}{n_1 \cdot n_2}

Um das Ergebnis in einer möglichst vereinfachten Form vorliegen zu haben, ist
es (vor dem Ausmultiplizieren) sinnvoll, sowohl die Zähler wie auch die Nenner
beider Brüche vollständig in Faktoren zu zerlegen. Kürzt man im Zähler und
Nenner anschließend alle gemeinsamen Teiler, so erhält man als Endergebnis
einen nicht weiter zu vereinfachenden Bruch.

Das Produkt aller gemeinsamen Teiler wird oftmals als "größter gemeinsamer
Teiler" :math:`(\mathrm{ggT})` bezeichnet. Die explizite Berechnung des
:math:`\mathrm{ggT}` ist meist nicht erforderlich; die Aussage, dass sich durch
Kürzen des größten gemeinsamen Teilers von Zähler und Nenner ein nicht weiter zu
vereinfachender Bruch ergibt, gilt jedoch allgemein.

Bruchterme lassen sich durcheinander dividieren, indem man -- durch Vertauschen
von Zähler und Nenner -- den Kehrbruch des Divisors bildet und eine
Multiplikation nach obigem Schema durchführt:

.. math::
    :label: eqn-bruch-division

    \frac{z_1}{n_1} : \frac{z_2}{n_2} =
    \frac{z_1}{n_1} \cdot  \frac{n_2}{z_2} =
    \frac{z_1 \cdot n_2}{n_1 \cdot z_2}

Auch hierbei ist eine Faktorisierung von Zähler und Nenner hilfreich, um das
Endergebnis in einer möglichst vereinfachten Form zu erhalten. Das gleiche
Verfahren kann genutzt werden, um so genannte Doppelbrüche aufzulösen:

.. math::

    \frac{\frac{z_1}{n_1}}{\frac{z_2}{n_2}} = \frac{z_1}{n_1} : \frac{z_2}{n_2}
    = \frac{z_1}{n_1} \cdot \frac{n_2}{z_2}

Bereits in der Antike fand `Euklid <https://de.wikipedia.org/wiki/Euklid>`_
einen Algorithmus zur Berechnung des :math:`\mathrm{ggT}`; dieser ist auf der
Grund-Wissen-Seite im Rahmen des :ref:`Python-Tutorials
<gwip:Euklid-Algorithmus>` näher beschrieben.


.. todo Doppelbrüche

.. todo Dezimalbrüche?


.. _Prozentrechnung:

Prozentrechnung
---------------

Bruchzahlen können auch verwendet werden, um Größenvergleiche anzugeben. Eine
Bruchzahl beschreibt dabei das Verhältnis zweier Größen, d.h. welchen Bruchteil
die eine Zahl (der Nenner) von der anderen Zahl (dem Zähler) ausmacht.

Um Zahlenverhältnisse vergleichen zu können, ist es oftmals hilfreich die
Bruchteile auf den selben Nenner zu bringen. Haben zwei Zahlen unterschiedliche
Zähler :math:`a` und :math:`b`, aber einen gleichen Nenner :math:`n`, so gilt
stets:

.. math::

    a < b \quad \Leftrightarrow \quad \frac{a}{n} < \frac{b}{n}

Als gemeinsamer Nenner wird in der Praxis meist die Zahl :math:`100` verwendet
und statt von Hundertsteln von Prozenten gesprochen. Für :math:`1` Prozent
schreibt man wahlweise :math:`\frac{1}{100}` oder :math:`0,01` oder :math:`1
\%`.

Die Anzahl der Prozente wird üblicherweise als Prozentsatz :math:`p`
bezeichnet. Hierbei ist allerdings stets darauf zu achten, auf welchen Grundwert
:math:`G` sich die Prozentangabe bezieht.

*Beispiel:*

* Werden zu einem Grundwert von :math:`G = 1` Liter Wasser ein Bruchteil von
  :math:`p = 10 \%` hinzu gegeben, so ergibt sich eine neue Menge :math:`G + 0,1
  \cdot G = 1,1` Liter.

  Werden von dieser Menge (:math:`G = 1,1` Liter) hingegen :math:`p = 10 \%`
  abgezogen, so bleiben nicht ein Liter, sondern "nur" :math:`G - 0,1 \cdot G =
  0,99` Liter übrig.

Der tatsächliche Wert, den eine Prozentangabe wiedergibt, wird Prozentwert
:math:`W` genannt. Er lässt sich als Produkt aus dem Prozentsatz :math:`p` und
dem basierenden Grundwert :math:`G` berechnen:

.. math::
    :label: eqn-prozentformel

    W = p \, \% \cdot G


Im obigen Beispiel wurde die Prozentformel :eq:`eqn-prozentformel` bereits
unmittelbar angewendet:

* Bezogen auf den Grundwert :math:`1` entspricht ein Prozentsatz von :math:`10
  \%{\color{white} .}` einem Prozentwert von :math:`\frac{10}{100} \cdot 1 = 0,1`.
* Bezogen auf den Grundwert :math:`1,1` entspricht der gleiche Prozentsatz
  einem Prozentwert von :math:`\frac{10}{100} \cdot 1,1 = 0,11`.

Wird der sich resultierende Prozentwert zum jeweiligen Grundwert addiert
beziehungsweise von diesem abgezogen, so ergeben sich folglich auch
unterschiedliche Ergebnisse.

Kleinere Mengenangaben werden häufig in Tausendstel (Promille) oder Millionstel
(Pars per Million) angegeben. Für :math:`1` Promille schreibt man
:math:`1 \,\permil` und für ein Millionstel  :math:`\unit[1]{ppm}`.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:


.. [#] Hier wird wiederum das Distributivgesetz genutzt: Da für jede reelle
    Zahl :math:`a` die Beziehung :math:`a = 1 \cdot a` gilt, kann die :math:`1`
    jederzeit als gemeinsamer Faktor einer beliebigen Summe ausgeklammert
    werden.

.. [#] Insbesondere kann ein Bruch :math:`\frac{z}{n}` mit einer ganzen Zahl :math:`a`
    multipliziert werden, indem der Zähler :math:`z` mit dieser Zahl
    multiplizert wird:

    .. math::

        a \cdot \frac{z}{n} = \frac{a}{1} \cdot \frac{z}{n} = \frac{a \cdot z}{1
        \cdot n} = \frac{a \cdot z}{n}

   Hierbei wird berücksichtigt, dass ein Zahlenwert unverändert bleibt, wenn man
   ihn durch :math:`1` dividiert. Wendet man dann die Rechenregel für die
   Multiplikation zweier Brüche an, so bleibt der Nenner gleich, da auch
   eine Multiplikation mit :math:`1` den Wert einer Zahl nicht ändert.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Bruchrechnung>`.






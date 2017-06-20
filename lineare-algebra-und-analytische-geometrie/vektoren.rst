
.. index:: Vektor
.. _Vektor:
.. _Vektoren:

Vektoren
========


.. _Komponente:
.. _Komponente eines Vektors:
.. _Darstellung von Vektoren:

Darstellung von Vektoren
------------------------

Bei Vektoren handelt es sich aus geometrischer Sicht um :ref:`Strecken
<Strecke>` mit einer bestimmten Länge, die sowohl eine bestimmte Richtung, wie
auch einen bestimmten Richtungssinn haben; dieser wird in Zeichnungen durch
Pfeil am Ende der Strecke hervorgehoben. In der Formelschreibweise werden
Vektoren meist mit kleinen lateinischen Buchstaben bezeichnet und durch einen
Pfeil über der Vektorgröße markiert.

.. figure:: ../pics/geometrie/vektor.png
    :width: 50%
    :align: center
    :name: fig-vektor
    :alt:  fig-vektor

    Darstellung eines Vektors.

    .. only:: html

        :download:`SVG: Vektor
        <../pics/geometrie/vektor.svg>`

Je nachdem, ob zwei- oder dreidimensionale geometrische Formen untersucht
werden, reicht ein geordnetes Paar aus zwei oder ein Tupel aus drei
Koordinatenwerten -- also :math:`(a_{\mathrm{x}} \,,\, a_{\mathrm{y}})`
beziehungsweise :math:`(a_{\mathrm{x}} \,,\, a_{\mathrm{y}} \,,\,
a_{\mathrm{z}})` -- aus,  um einen Vektor :math:`\vec{a}` vollständig zu
charakterisieren. [#]_ Die einzelnen Koordinatenwerte ("Komponenten") geben
dabei an, um wie viele Längeneinheiten die Spitze des Vektors entlang der
jeweiligen Raumrichtung vom Anfangspunkt des Vektors entfernt liegt.

.. math::
    :label: eqn-vektor

    \vec{a} = (a_{\mathrm{x}} \,,\, a_{\mathrm{y}} \,,\, a_{\mathrm{z}}) = \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix}

.. index:: Ortsvektor
.. _Ortsvektor:

.. figure:: ../pics/geometrie/ortsvektor.png
    :width: 50%
    :align: center
    :name: fig-ortsvektor
    :alt:  fig-ortsvektor

    Darstellung eines (dreidimensionalen) Ortsvektors in einem
    Koordinatensystem.

    .. only:: html

        :download:`SVG: Ortsvektor
        <../pics/geometrie/ortsvektor.svg>`

Ein Vektor, dessen Anfangspunkt dem Ursprung des Koordinatensystems
:math:`\vec{0} = (0 \,,\, 0 \,,\, 0)` entspricht, wird als Ortsvektor
bezeichnet. Jeder Punkt eines Raumes kann durch einen zugehörigen Ortsvektor
eindeutig charakterisiert werden.


.. index:: Betrag eines Vektors, Vektor; Betrag
.. _Betrag eines Vektors:

.. rubric:: Betrag eines Vektors

Die Länge der Verbindungsstrecke vom Anfangspunkt eines Vektors :math:`\vec{a}`
zu seinem Endpunkt wird Betrag des Vektors genannt. In Kurzform schreibt man
dafür :math:`| \vec{a} |` oder :math:`a` (ohne Vektorpfeil).

.. figure:: ../pics/geometrie/vektor-betrag.png
    :width: 50%
    :align: center
    :name: fig-vektor-betrag
    :alt:  fig-vektor-betrag

    Betrag eines (zweidimensionalen) Vektors.

    .. only:: html

        :download:`SVG: Betrag eines Vektors
        <../pics/geometrie/vektor-betrag.svg>`

Der Betrag eines Vektors kann mit Hilfe des Satzes von Pythagoras folgendermaßen
anhand seiner Komponenten :math:`a_{\mathrm{x}}` und :math:`a_{\mathrm{y}}` (und
:math:`a_{\mathrm{z}}` bei dreidimensionalen Vektoren) berechnet werden:

.. math::
    :label: eqn-vektor-betrag

    a = | \vec{a } \, | &= \sqrt{a_{\mathrm{x}}^2 + a_{\mathrm{y}}^2}
    \phantom{+ a_{\mathrm{z}}^2} \; \quad \text{für zweidimeinsionale
    Vektoren} \\[4pt]
    a = | \vec{a } \, | &= \sqrt{a_{\mathrm{x}}^2 + a_{\mathrm{y}}^2 +
    a_{\mathrm{z}}^2} \quad \text{für dreidimeinsionale Vektoren}

*Beispiele:*

* Der zweidimensionale Vektor :math:`\vec{a} = \begin{pmatrix} 4 \\ 3
  \end{pmatrix}` hat folgenden Betrag:

  .. math::

      \left| \vec{a} \right| = \sqrt{a_{\mathrm{x}}^2 + a_{\mathrm{y}}^2} =
      \sqrt{4^2 + 3^2} = \sqrt{25} = 5{\color{white} \; \; \qquad \quad \ldots}

* Der dreidimensionale Vektor :math:`\vec{b} = \begin{pmatrix} 4 \\ 5 \\ 2
  \end{pmatrix}` hat folgenden Betrag:

  .. math::

      \left| \vec{b} \right| = \sqrt{b_{\mathrm{x}}^2 + b_{\mathrm{y}}^2 +
      b_{\mathrm{z}}^2} = \sqrt{4^2 + 5^2 + 2^2} = \sqrt{45}


.. index:: Vektor; Gegenvektor
.. _Vektor und Gegenvektor:

.. rubric:: Vektor und Gegenvektor

Zwei Vektoren :math:`\vec{a}` und :math:`\vec{a}` sind gleich, wenn sie in allen
Koordinaten übereinstimmen. Beide Vektoren haben dann den gleichen Betrag, die
gleiche Richtung und den gleichen Richtungssinn. Sie können allerdings von
unterschiedlichen Anfangspunkten ausgehen und daher parallel zueinander im Raum
verschoben sein, da für Vektoren stets nur die Differenz der Koordinatenwerte
von Anfangspunkt und Endpunkt von Bedeutung ist.

.. figure:: ../pics/geometrie/vektor-gleichheit.png
    :width: 50%
    :align: center
    :name: fig-vektor-gleichheit
    :alt:  fig-vektor-gleichheit

    Zwei identische Vektoren.

    .. only:: html

        :download:`SVG: Gleichheit zweier Vektoren
        <../pics/geometrie/vektor-gleichheit.svg>`

Das Negative :math:`- \vec{a}` eines Vektors :math:`a`, auch "Gegenvektor"
genannt, ist ein Vektor mit gleichem Betrag und gleicher Richtung wie
:math:`\vec{a}`, jedoch mit umgekehrtem Richtungssinn.

.. figure:: ../pics/geometrie/vektor-gegenvektor.png
    :width: 50%
    :align: center
    :name: fig-vektor-gegenvektor
    :alt:  fig-vektor-gegenvektor

    Vektor und Gegenvektor.

    .. only:: html

        :download:`SVG: Vektor und Gegenvektor
        <../pics/geometrie/vektor-gegenvektor.svg>`

In der Komponentenschreibweise kann der zu einem Vektor :math:`\vec{a}`
gehörende Gegenvektor :math:`- \vec{a}` gebildet werden, indem man alle
Komponenten von :math:`\vec{a}` mit einem Minuszeichen versieht:

.. math::
    :label: eqn-vektor-gegenvektor

    {\color{white}+}\vec{a} = \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix} \quad \Leftrightarrow \quad
    - \vec{a} = \begin{pmatrix}
    - a_{\mathrm{x}} \\
    - a_{\mathrm{y}} \\
    - a_{\mathrm{z}} \\
    \end{pmatrix}

Bei zweidimensionalen Vektoren wird die dritte Komponente :math:`a_{\mathrm{z}}
= 0` weggelassen.


.. index:: Vektor; Normvektor
.. _Normvektor und Nullvektor:

.. rubric:: Normvektor und Nullvektor

Ein Vektor, dessen Länge genau einer Längeneinheit :math:`(\unit[1]{LE})`
entspricht, wird "normierter" Vektor :math:`\vec{a}_0` genannt.

.. figure:: ../pics/geometrie/vektor-normvektor.png
    :name: fig-vektor-normvektor
    :alt:  fig-vektor-normvektor
    :align: center
    :width: 50%

    Normvektor :math:`\vec{a} _{\mathrm{0}}` eines Vektors :math:`\vec{a}`

    .. only:: html

        :download:`SVG: Vektor und Normvektor
        <../pics/geometrie/vektor-normvektor.svg>`

Ein Vektor mit Betrag Null wird als Nullvektor :math:`\vec{0}` bezeichnet. Bei
einem Nullvektor sind Anfangs- und Endpunkt identisch.


.. _Addition und Subtraktion von Vektoren:

Addition und Subtraktion von Vektoren
-------------------------------------

Ein Vektor kann durch Beibehalten seiner Richtung und seines Richtungssinns,
also parallel im Raum verschoben werden, ohne dass sich die Werte seiner
Komponenten ändern. Dies kann genutzt werden, um zwei Vektoren zeichnerisch zu
addieren beziehungsweise subtrahieren.

.. index:: Vektor; Summenvektor
.. _Summenvektor:

.. rubric:: Der Summenvektor

Fügt man an einen Vektor :math:`\vec{a}` einen zweiten Vektor :math:`\vec{b}`
durch eine passende Verschiebung (Translation) so an, dass der Anfangspunkt des
zweiten Vektors mit dem Endpunkt des ersten Vektors übereinstimmt, dann erhält
man den Summenvektor :math:`\overrightarrow{a + b}`, indem man den Anfangspunkt
des ersten Vektors mit dem Endpunkt des zweiten Vektors verbindet.

.. figure:: ../pics/geometrie/vektor-addition.png
    :name: fig-vektor-addition
    :alt:  fig-vektor-addition
    :align: center
    :width: 70%

    Summenvektor der beiden Vektoren :math:`\vec{a}_{\mathrm{1}}` und
    :math:`\vec{a}_{\mathrm{2}}`.

    .. only:: html

        :download:`SVG: Vektor-Addition
        <../pics/geometrie/vektor-addition.svg>`

Rechnerisch erhält man den Summenvektor, indem man die einzelnen Komponenten
beider Vektoren addiert:

.. math::
    :label: eqn-vektor-addition

    \overrightarrow{a + b\;}  = \vec{a} + \vec{b} = \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix} + \begin{pmatrix}
    b_{\mathrm{x}} \\
    b_{\mathrm{y}} \\
    b_{\mathrm{z}} \\
    \end{pmatrix} = \begin{pmatrix}
    a_{\mathrm{x}} + b_{\mathrm{x}} \\
    a_{\mathrm{y}} + b_{\mathrm{y}} \\
    a_{\mathrm{z}} + b_{\mathrm{z}} \\
    \end{pmatrix}

Eine Addition von Vektoren mit unterschiedlicher Dimension ist nicht definiert.

..  Additionen von Vektoren haben unmittelbar zahlreiche Anwendungen in der
..  Physik, beispielsweise beim Zusammenwirken mehrerer Kräfte.

.. index:: Vektor; Differenzvektor
.. _Differenzvektor:

.. rubric:: Der Differenzvektor

Die Differenz :math:`\vec{a} - \vec{b}` zweier Vektoren lässt sich zeichnerisch
auf ähnliche Weise bestimmen, indem man den Gegenvektor :math:`- \vec{b}` des
zweiten Vektors zum ersten Vektor addiert.

.. figure:: ../pics/geometrie/vektor-subtraktion.png
    :name: fig-vektor-subtraktion
    :alt:  fig-vektor-subtraktion
    :align: center
    :width: 70%

    Differenzvektor der beiden Vektoren :math:`\vec{a}_1` und :math:`\vec{a}_2`.

    .. only:: html

        :download:`SVG: Vektor-Subtraktion
        <../pics/geometrie/vektor-subtraktion.svg>`

Rechnerisch erhält man den Differenzvektor, indem man die einzelnen Komponenten
beider Vektoren subtrahiert:

.. math::
    :label: eqn-vektor-subtraktion

    \overrightarrow{a - b\;}  = \vec{a} - \vec{b} = \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix} - \begin{pmatrix}
    b_{\mathrm{x}} \\
    b_{\mathrm{y}} \\
    b_{\mathrm{z}} \\
    \end{pmatrix} = \begin{pmatrix}
    a_{\mathrm{x}} - b_{\mathrm{x}} \\
    a_{\mathrm{y}} - b_{\mathrm{y}} \\
    a_{\mathrm{z}} - b_{\mathrm{z}} \\
    \end{pmatrix}

.. index:: Vektormultiplikation
.. _Multiplikation von Vektoren:

Multiplikation von Vektoren
---------------------------

Vektoren können entweder mit einer reellen Zahl (einem so genannten "Skalar")
als auch mit anderen Vektoren multipliziert werden.


.. index:: Vektormultiplikation; S-Multiplikation
.. _Multiplikation eines Vektors mit einer reellen Zahl:

.. rubric:: Multiplikation eines Vektors mit einer reellen Zahl

Multipliziert man einen Vektor :math:`\vec{a}` mit einer reellen Zahl :math:`c`,
so ergibt sich ein Vektor, der die gleiche Richtung und den gleichen
Richtungssinn hat, dessen Betrag jedoch um den Faktor :math:`c` verändert ist.

* Ist :math:`c > 1`, so wird der Vektor gestreckt.
* Ist :math:`0 < c < 1`, so wird der Vektor gestaucht.
* Ist :math:`c < 0`, so wird zusätzlich zur Streckung beziehungsweise Stauchung
  des Vektors der Richtungssinn umgedreht.

Diese Form der Vektor-Multiplikation wird oftmals auch "S-Multiplikation"
genannt.

.. figure:: ../pics/geometrie/vektor-produkt-mit-skalar.png
    :name: fig-vektor-produkt-mit-skalar
    :alt:  fig-vektor-produkt-mit-skalar
    :align: center
    :width: 50%

    Produkt eines Vektors mit einem Skalar (Faktoren: :math:`c = \frac{1}{2}`
    beziehungsweise :math:`c = 2`).

    .. only:: html

        :download:`SVG: Produkt eines Vektors mit einem Skalar
        <../pics/geometrie/vektor-produkt-mit-skalar.svg>`

Rechnerisch lässt sich ein Vektor :math:`\vec{a}` mit einer reellen Zahl
:math:`c` multiplizieren, indem jede Komponente des Vektors mit dieser Zahl
multipliziert wird:

.. math::
    :label: eqn-produkt-vektor-mit-skalar

    c \cdot \vec{a} = c \cdot \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix} = \begin{pmatrix}
    c \cdot a_{\mathrm{x}} \\
    c \cdot a_{\mathrm{y}} \\
    c \cdot a_{\mathrm{z}} \\
    \end{pmatrix}

Multipliziert man einen Vektor :math:`\vec{a}` mit der Zahl :math:`1`, so bleibt
er unverändert; es gilt also stets:

.. math::
    :label: eqn-produkt-vektor-mit-skalar-unitaritaetsgesetz

    1 \cdot \vec{a} = \vec{a}


Multipliziert man einen Vektor :math:`\vec{a}` hingegen mit dem Kehrwert seines
Betrags :math:`\frac{1}{| \vec{a} |}`, so erhält man den zugehörigen, auf
eine Längeneinheit :math:`(\unit[1]{LE})` normierten Vektor :math:`\vec{a}_0`:

.. math::
    :label: eqn-produkt-vektor-normierung

    \vec{a}_0 = \frac{\vec{a}}{\left|\vec{a}\right|}

.. _Distributivgesetz für Vektoren:
.. _Assoziativgesetz für Vektoren:

Zusätzlich gelten bezüglich der Multiplikation von Skalaren mit Vektoren das
:ref:`Assoziativ <Assoziativgesetz>`- und :ref:`Distributivgesetz
<Distributivgesetz>`:

.. math::
    :label: eqn-produkt-vektor-mit-skalar-assoziativgesetz

    (c_1 \cdot c_2) \cdot \vec{a} = c_1 \cdot (c_2 \cdot \vec{a})


.. math::
    :label: eqn-produkt-vektor-mit-skalar-distributivgesetz

    {\color{white}\ldots\,\!}(c_1 + c_2) \cdot \vec{a} &= c_1 \cdot \vec{a} + c_2 \cdot \vec{a} \\
    c \cdot (\vec{a} + \vec{b}) &= c \cdot \vec{a} + c \cdot \vec{b}



.. index:: Skalarprodukt, Vektormultiplikation; Skalarprodukt
.. _Skalarprodukt:

.. rubric:: Das Skalarprodukt

Das Skalarprodukt zweier Vektoren :math:`\vec{a}` und :math:`\vec{a}` ist
definiert als das Produkt ihrer Beträge :math:`|\vec{a}|` und
:math:`|\vec{b}|`, multipliziert mit dem Cosinus des zwischen ihnen
eingeschlossenen Winkels :math:`\alpha`:

.. math::
    :label: eqn-skalarprodukt-winkel

    {\color{white}.\;}\vec{a} \cdot \vec{b} =  |\vec{a}| \cdot |\vec{b}| \cdot
    \cos{(\alpha)}

.. figure:: ../pics/geometrie/vektor-skalarprodukt.png
    :width: 50%
    :align: center
    :name: fig-skalarprodukt
    :alt:  fig-skalarprodukt

    Anschauliche Interpretation eines Skalarprodukts.

    .. only:: html

        :download:`SVG: Skalarprodukt
        <../pics/geometrie/vektor-skalarprodukt.svg>`

.. Für Vektoren mit unterschiedlicher Dimension ist das Skalarprodukt nicht
.. definiert. 

Schreibt man die beiden Vektoren :math:`\vec{a}` und :math:`\vec{b}`
in Spaltenform, so kann das Skalarprodukt komponentenweise nach folgender Formel
berechnet werden:

.. math::
    :label: eqn-skalarprodukt

    {\color{white}\ldots \qquad \qquad \quad  }\vec{a} \cdot \vec{b} &=
    \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix} \cdot \begin{pmatrix}
    b_{\mathrm{x}} \\
    b_{\mathrm{y}} \\
    b_{\mathrm{z}} \\
    \end{pmatrix} \\[4pt]
    &= a_{\mathrm{x}} \cdot b_{\mathrm{x}} + a_{\mathrm{y}} \cdot
    b_{\mathrm{y}}+ a_{\mathrm{z}} \cdot b_{\mathrm{z}}

Das Ergebnis ist ein skalarer Wert, also eine Zahl. Die Bedeutung des
Skalarprodukts wird schnell deutlich, wenn man sich einige Sonderfälle
betrachtet:

* Stehen die beiden Vektoren :math:`\vec{a}` und :math:`\vec{b}` senkrecht
  zueinander, so ist :math:`\cos{(\alpha)} = \cos{(90 \degree)} = 0`. Somit ergibt
  das Skalarprodukt in diesem Fall den Wert Null:

  .. math::

      \vec{a} \perp \vec{b}  \quad \Leftrightarrow \quad
      \vec{a} \cdot \vec{b} = 0

  Mit Hilfe dieser Beziehung kann einerseits leicht gepüeft werden, *ob* zwei
  Vektoren :math:`\vec{a}` und :math:`\vec{b}` senkrecht aufeinander stehen.
  Andererseits kann bei einem Vektor :math:`\vec{a}` mit nur zwei gegebenen
  Komponenten unter Verwendung der komponentenweisen Darstellung die dritte
  Komponente so bestimmt werden, dass der Vektor auf dem zweiten Vektor
  :math:`\vec{b}` senkrecht steht.

  *Beispiel:*

    Die dritte Komponente des Vektors :math:`\vec{a} = (2,6,?)` soll so
    bestimmt werden, dass er auf dem Vektor :math:`\vec{b} = (3,-5,6)`
    senkrecht steht. Somit muss gelten:

    .. math::

        \vec{a} \cdot \vec{b} &= 0 \\ 2 \cdot 3 + 6 \cdot (-5) +\; ? \cdot 6
        &= 0 {\color{white}\qquad \qquad \qquad \qquad \ldots}\\ \Rightarrow 6
        \cdot \; ? &= 24 \\  ? &= 4

    Ist die gesuchte Komponente somit gleich :math:`4`, so stehen beide Vektoren
    senkrecht aufeinander.


* Stehen die beiden Vektoren :math:`\vec{a}` und :math:`\vec{b}` parallel
  zueinander, so ist :math:`\cos{(\alpha)} = \cos{(0\degree)} = 1`. Das
  Skalarprodukt ist in diesem Fall gleich dem Produkt der Beträge beider
  Vektoren.

  .. math::

      {\color{white}\ldots \qquad \;\; }\vec{a} \parallel \vec{b} \quad
      \Leftrightarrow \quad \vec{a} \cdot \vec{b} = | \vec{a} | \cdot |
      \vec{b} |

  Dieser Zusammenhang wurde implizit bereits verwendet, um den Betrag eines
  bestimmten Vektors :math:`\vec{a}` zu berechnen. Setzt man nämlich
  :math:`\vec{a} = \vec{b}`, so gilt:

  .. math::

      a = | \vec{a} | = \sqrt{ | \vec{a} | ^2 } = \sqrt{ \vec{a} \cdot \vec{a}}

  Der Betrag :math:`|\vec{a}|` des Vektors kann somit bestimmt werden, indem man
  das Skalarprodukt des Vektors mit sich selbst bildet und aus dem Ergebnis die
  Quadratwurzel zieht. Schreibt man die obige Gleichung komponentenweise, so
  erhält man die übliche Betrags-Gleichung :eq:`eqn-vektor-betrag`.

* Für beliebige Winkel :math:`\alpha` lässt sich das Produkt :math:`b \cdot
  \cos{(\alpha)}` geometrisch als "Projektion" des Vektors :math:`b` auf den
  Vektor :math:`a` deuten. Die Projektion entspricht dabei anschaulich dem
  "Schattenwurf" des Vektors :math:`\vec{b}`, der sich bei einer senkrecht auf
  :math:`\vec{a}` einfallenden Beleuchtung ergeben würde.

  Der Wert des Skalarprodukts ist damit im Allgemeinen gleich dem Betrag des
  ersten Vektors, multipliziert mit der senkrechten Projektion des zweiten
  Vektors auf den ersten.

Da das Skalarprodukt komponentenweise einfach zu berechnen ist, kann es auch
genutzt werden, um den Winkel zwischen zwei Vektoren oder einem Vektor und einer
der Achsen eines (kartesischen) Koordinatensystems zu berechnen. Für den Winkel
zwischen zwei Vektoren gilt nämlich aufgrund von Gleichung
:eq:`eqn-skalarprodukt-winkel`:

.. math::

    \cos{\left(\alpha\right)} &= \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot
    |\vec{b}|} \\[4pt]
    \Rightarrow \alpha &= \text{acos}\left(\frac{\vec{a} \cdot \vec{b}}{|\vec{a}|
    \cdot |\vec{b}|}\right)

Um den Winkel zu berechnen, muss man somit nur das Skalarprodukt berechnen und
dieses durch das Produkt beider Vektor-Beträge dividieren; der Arcus-Cosinus
dieses Werts ergibt den gesuchten Winkel.

Um den Winkel zwischen eines Vektors und den einzelnen Raumachsen zu berechnen,
kann man diese ebenfalls durch Vektoren der Länge :math:`1` und mit je nur einer
einzigen Vektorkomponente dargestellt werden kann, beispielsweise die
:math:`x`-Achse durch den Vektor :math:`e_{\mathrm{x}} = (1,0,0)`. Man erhält
damit:

.. math::

    {\color{white}\ldots \qquad \quad  }\vec{a} \cdot \vec{e}_{\mathrm{x}} &=
    \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix} \cdot \begin{pmatrix}
    1 \\
    0 \\
    0 \\
    \end{pmatrix} \\[4pt]
    &= a_{\mathrm{x}} \cdot 1 + a_{\mathrm{y}} \cdot 0 + a_{\mathrm{z}} \cdot 0
    = a_{\mathrm{x}}

Gleiches gilt auch für die Skalarprodukte von :math:`\vec{a}` mit den beiden
anderen Raumachsen. Die allgemeine Formel :eq:`eqn-skalarprodukt-winkel` des
Skalarprodukts kann damit nach dem gesuchten Winkel :math:`\alpha` aufgelöst
werden:

.. math::

    \vec{a} \cdot \vec{e}_{\mathrm{x}} = | \vec{a} | \cdot | \vec{e}_{\mathrm{x}} |
    \cdot \cos{(\alpha)} \quad \Leftrightarrow \quad \cos{(\alpha)} = \frac{\vec{a}
    \cdot \vec{e}_{\mathrm{x}}}{ | \vec{a} | \cdot |\vec{e}_{\mathrm{x}}| }

Setzt man :math:`\vec{a} \cdot \vec{e}_{\mathrm{x}} = a_{\mathrm{x}}` und
:math:`|\vec{e}_{\mathrm{x}}| = 1` in die obige Gleichung ein, so folgt: [#]_

.. math::

    \cos{(\alpha)} = \frac{\vec{a} \cdot \vec{e}_{\mathrm{x}}}{ | \vec{a} | \cdot
    |\vec{e}_{\mathrm{x}}| } = \frac{a_{\mathrm{x}}}{| \vec{a} |}

Für die Winkel :math:`\alpha ,\, \beta ,\, \gamma` zwischen :math:`\vec{a}` und
den :math:`x ,\, y ,\, z`-Achsen gilt somit:

.. math::
    :label: eqn-winkel-zwischen-vektor-und-raumachsen

    \alpha = \text{acos}\left( \frac{a_{\mathrm{x}}}{|\vec{a}|} \right) \quad ; \quad
    \beta  = \text{acos}\left( \frac{a_{\mathrm{y}}}{|\vec{a}|} \right) \quad ; \quad
    \gamma = \text{acos}\left( \frac{a_{\mathrm{z}}}{|\vec{a}|} \right) \quad

..  Todo Beispiel?


.. index:: Vektormultiplikation; Vektorprodukt
.. _Vektorprodukt:

.. rubric:: Das Vektorprodukt

Das Vektorprodukt zweier Vektoren :math:`\vec{a}` und :math:`\vec{b}` ergibt
einen Vektor, der auf jedem der beiden Vektoren und senkrecht steht. Diese
Definition ist erst ab einem dreidimensionalen Raum sinnvoll.

.. figure:: ../pics/geometrie/vektor-vektorprodukt.png
    :width: 50%
    :align: center
    :name: fig-vektorprodukt
    :alt:  fig-vektorprodukt

    Anschauliche Interpretation eines Vektorprodukts.

    .. only:: html

        :download:`SVG: Vektorprodukt
        <../pics/geometrie/vektor-vektorprodukt.svg>`

Der Betrag des Vektorprodukts zweier Vektoren :math:`\vec{a}` und
:math:`\vec{b}` ist gleich dem Produkt ihrer Beträge :math:`|\vec{a}|` und
:math:`|\vec{b}|`, multipliziert mit dem Sinus des zwischen ihnen
eingeschlossenen Winkels :math:`\alpha`:

.. math::
    :label: eqn-vektorprodukt-winkel

    |\vec{a} \times  \vec{a}| =  |\vec{a}| \cdot |\vec{b}| \cdot \sin{\alpha}

Schreibt man die beiden Vektoren :math:`\vec{a}` und :math:`\vec{a}` in
Spaltenform, so kann das Vektorprodukt komponentenweise nach folgender Formel
berechnet werden:

.. math::
    :label: eqn-vektorprodukt

    \vec{a} \times \vec{b} = \begin{pmatrix}
    a_{\mathrm{x}} \\
    a_{\mathrm{y}} \\
    a_{\mathrm{z}} \\
    \end{pmatrix} \times \begin{pmatrix}
    b_{\mathrm{x}} \\
    b_{\mathrm{y}} \\
    b_{\mathrm{z}} \\
    \end{pmatrix} = \begin{pmatrix}
    a_{\mathrm{y}} \cdot b_{\mathrm{z}} - a_{\mathrm{z}} \cdot b_{\mathrm{y}} \\
    a_{\mathrm{z}} \cdot b_{\mathrm{x}} - a_{\mathrm{x}} \cdot b_{\mathrm{z}} \\
    a_{\mathrm{x}} \cdot b_{\mathrm{y}} - a_{\mathrm{y}} \cdot b_{\mathrm{x}} \\
    \end{pmatrix}

Das Vektorprodukt findet Anwendung in der analytischen Geometrie und in der
Technik. Beispielsweise kann zu zwei gegebenen Richtungsvektoren, die eine Ebene
beschreiben, mit Hilfe des Vektorprodukts ein dritter "Normvektor" gefunden
werden, der auf der Ebene senkrecht steht. In der Physik wird das Vektorprodukt
beispielsweise bei der Berechnung von :ref:`Drehmomenten <gwp:Drehmoment>` und
:ref:`Drehimpulsen <gwp:Drehimpuls>` genutzt.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Vektoreigenschaften lassen sich so verallgemeinern, dass in der
    algebraischen Geometrie allgemein auch Vektoren mit :math:`n` Dimensionen
    behandelt werden können.

.. [#] Der Betrag des Vektors :math:`\vec{e}_{\mathrm{x}}` ist gleich Eins, da
    :math:`|\vec{e}_{\mathrm{x}}| = \sqrt{1^2 + 0^2 + 0^2} = 1` gilt.


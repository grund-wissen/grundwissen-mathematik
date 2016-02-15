
.. index:: Matrix
.. _Matrizen:

Matrizen
========

Bei einer Matrix handelt es sich, ebenso wie bei einer Determinante, um eine
rechteckige Anordnungen mehrerer Zahlen. Hat eine Matrix :math:`m` Zeilen und
:math:`n` Spalten, so sagt man, die Matrix sei vom Typ :math:`(m;n)`. Eine
solche Matrix hat allgemein folgende Gestalt:

.. math::

    \underline{A}_{\;(m;\,n)} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n}\\ a_{21} &
    a_{22} & \cdots & a_{2n}\\ \vdots & \vdots & & \vdots\\ a_{m1} & a_{m2} &
    \cdots & a_{mn}\\ \end{pmatrix}

In der Literatur werden Matrizen häufig auch durch fettgedruckte Großbuchstaben
bezeichnet, in der Praxis werden die Großbuchstaben hingegen üblicherweise
unterstrichen. Die in einer Matrix :math:`\underline{A}` stehenden Zahlen werden
allgemein Elemente oder Komponenten :math:`a _{\mathrm{ij}}` der Matrix genannt,
wobei :math:`i` den Zeilenindex (eine Zahl zwischen :math:`1` und :math:`n`) und
:math:`j` den Spaltenindex (eine Zahl zwischen :math:`1` und :math:`n`)
bezeichnet. Schreibt man :math:`(a _{\mathrm{ij}})` in runden Klammern, so ist
damit die Gesamtheit aller Komponenten, also wiederum die ganze Matrix gemeint.

.. _Spezielle Matrizen:

.. rubric:: Spezielle Matrizen

Matrizen können sowohl hinsichtlich der Zahlenwerte ihrer Komponenten als auch
hinsichtlich ihrer Form Besonderheiten aufweisen: Beispielsweise werden
Matrizen, die ausschließlich Nullen als Werte enthalten, Nullmatrizen genannt.
Andererseits können auch gewöhnliche Vektoren als spezielle Matrizen mit einer
Spaltenzahl von :math:`n=1` aufgefasst werden:

.. math::

    \vec{a} := \underline{A}_{\;(m;\,1)} = \begin{pmatrix}
        a_1 \\ a_2 \\ \vdots \\ a_m
    \end{pmatrix}

Matrizen, die hingegen nur eine Zeilenzahl von :math:`m=1` haben, werden
entsprechend Zeilenvektoren genannt:

.. math::

    {\color{white}\vec{a}:=\quad}\underline{A}_{\;(1;\,n)} = \begin{pmatrix} a_1 \;
    \ldots \; a_n \end{pmatrix}

Ein Zeilenvektor, der die gleichen Elemente hat wie ein Spaltenvektor
:math:`\vec{a}`, wird häufig auch mit :math:`\vec{a}^{\;\mathrm{T}}` bezeichnet. Das
hochgestellte :math:`\mathrm{T}` bedeutet dabei "transponiert". Allgemein kann zu jeder
Matrix :math:`\underline{A}` eine transponierte Matrix :math:`\underline{A}^{\mathrm{T}}`
gebildet werden, indem man die Zeilen und Spalten der Matrix vertauscht:

.. math::

    \underline{A}_{\;(m;\,n)} = \begin{pmatrix} a_{11} & a_{12} & \cdots\; \cdots\; \cdots & a_{1n}\\ a_{21} &
    a_{22} & \cdots\; \cdots \; \cdots & a_{2n}\\ \vdots  & \vdots & & \vdots \\ a_{m1} & a_{m2} &
    \cdots\; \cdots \; \cdots & a_{mn}\\ \end{pmatrix}
    \quad \Longleftrightarrow \quad
    \underline{A}^{\mathrm{T}}_{\;(n;\,m)} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1m}\\ a_{21} &
    a_{22} & \cdots & a_{2m}\\ \vdots & \vdots & & \vdots \\ \vdots & \vdots \\ \vdots & \vdots & &
    \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nm}\\
    \end{pmatrix}

Beim Transponieren einer Matrix bleiben also nur diejenigen Komponenten
unverändert, die auf der von links oben nach rechts unten verlaufenden
"Hauptdiagonalen" liegen; alle anderen Einträge werden an dieser Diagonalen
gespiegelt.

.. index:: Matrix; Diagonalmatrix, Matrix; Einheitsmatrix

Eine weitere Sonderstellung haben quadratische Matrizen, für deren Zeilen- wie
auch Spaltenanzahl :math:`m=n` gilt. Für jede derartige Matrix
:math:`\underline{A}_{\;(n;\,n)}` lässt sich eine so genannte Diagonalmatrix
:math:`\underline{D}_{\;(n;\,n)}` angeben, bei der alle Komponenten, die nicht
auf der Hauptdiagonalen liegen, gleich Null sind:

.. math::

    \underline{A}_{\;(n;\,n)} = \begin{pmatrix} a_{11} & a_{12} & \cdots &
    a_{1n}\\ a_{21} & a_{22} & \cdots & a_{2n}\\ \vdots & \vdots & & \vdots\\
    a_{n1} & a_{n2} & \cdots & a_{nn}\\ \end{pmatrix}
    \quad \Longleftrightarrow \quad
    \underline{D}_{\;(n;\,n)} = \begin{pmatrix} a_{11} & 0 & \cdots & 0\\ 0 &
    a_{22} & \cdots & 0\\ \vdots & \vdots & & \vdots\\ 0 & 0 &
    \cdots & a_{nn}\\ \end{pmatrix}

Eine Sonderform einer Diagonalmatrix ist eine so genannte Einheitsmatrix, bei
der alle Elemente auf der Hauptdiagonalen den Wert :math:`1` haben.

.. math::

    \underline{E}_{\;(n;\,n)} = \begin{pmatrix} 1 & 0 & \cdots & 0\\ 0 &
        1 & \cdots & 0\\ \vdots & \vdots & & \vdots\\ 0 & 0 &
        \cdots & 1 \\ \end{pmatrix}

Eine Gleichheit zweier Matrizen liegt nur dann vor, wenn beide die gleiche Form
haben und die Werte aller ihrer Komponenten identisch sind. Es muss also gelten:

.. math::

    \underline{A}_{\;(m;\,n)} = \underline{B}_{\;(m;\,n)} \quad \Longleftrightarrow
    \quad a_{ij} = b_{ij} \; \text{für alle $i,\,j$}


.. _Rechenregeln für Matrizen:

Rechenregeln für Matrizen
-------------------------

Für Matrizen lassen sich ebenso wie für Zahlen und Vektoren grundlegende
Rechenregeln definieren.

.. index:: Matrixaddition

.. rubric:: Addition und Skalarmultiplikation

Haben zwei Matrizen die gleiche Form, so können sie
addiert beziehungsweise subtrahiert werden, indem die jeweils an gleicher Stelle
stehenden Komponenten addiert beziehungsweise subtrahiert werden:

.. math::

    \underline{A}_{\;(m;\,n)} + \underline{B}_{\;(m;\,n)} = (a_{ij} +
    b_{ij})_{\;(m;\,n)} \; \text{für alle $i,\,j$}

Das Resultat einer Addition beziehungsweise Subtraktion ist wiederum eine
Matrix, welche die gleiche Form hat wie die beiden ursprünglichen Matrizen.
Da die Addition beziehungsweise Subtraktion komponentenweise nach den gleichen
Rechenregeln wie mit gewöhnlichen Zahlen erfolgt, gilt auch für die Addition
beziehungsweise Subtraktion das :ref:`Kommutativ- <Kommutativgesetz>` und
:ref:`Assoziativgesetz <Assoziativgesetz>` :

.. math::
    :label: eqn-kommutativgesetz-matrixaddition

    \underline{A} + \underline{B} = \underline{B} + \underline{A}

.. math::
    :label: eqn-assoziativgesetz-matrixaddition

    (\underline{A} + \underline{B}) + \underline{C} = \underline{A} +
    (\underline{B} + \underline{C}) = \underline{A} + \underline{B} +
    \underline{C}

Ebenso komponentenweise erfolgt die Multiplikation einer Matrix mit einer
reellen Zahl (einem so genannten "Skalar"). Bei einer solchen
Skalarmultiplikation wird jedes Element der Matrix :math:`\underline{A}` mit dem
Wert des Skalars :math:`c` multipliziert.

.. math::

    c \cdot \underline{A}_{\;(m;\,n)} = (c \cdot a_{ij} )_{\;(m;\,n)} \; \text{für alle $i,\,j$}

Das Resultat einer ist wiederum eine Matrix, welche die gleiche Form hat wie die
ursprüngliche Matrix. Auch für die Multiplikation einer Matrix mit einem Skalar
gelten das :ref:`Kommutativ- <Kommutativgesetz>`, :ref:`Assoziativgesetz
<Assoziativgesetz>`:

.. math::
    :label: eqn-kommutativgesetz-matrix-skalarmultiplikation

    c \cdot \underline{A} = \underline{A} \cdot c

.. math::
    :label: eqn-assoziativgesetz-matrix-skalarmultiplikation

    c_1 \cdot (c_2 \cdot \underline{A}) = (c_1 \cdot c_2) \cdot \underline{A} = c_1 \cdot c_2 \cdot \underline{A}

Zudem gilt das :ref:`Distributivgesetz <Distributivgesetz>` in gewohnter Form:

.. math::
    :label: eqn-distributivgesetz-matrix-skalarmultiplikation

    (c_1 + c_2) \cdot \underline{A}) = c_1 \cdot \underline{A} + c_2 \cdot \underline{A} \\
    c \cdot (\underline{A}) + \underline{B}) = c \cdot \underline{A} + c \cdot \underline{B} \\

.. index:: Matrixmultiplikation

.. _Multiplikation zweier Matrizen:

.. rubric:: Multiplikation zweier Matrizen

Zur Herleitung einer Rechenregel für die Multiplikation zweier Matrizen wird
zunächst von der skalaren Multiplikation eines Zeilenvektors mit einem
Spaltenvektor ausgegangen. Wie bei einem gewöhnlichen :ref:`Skalarprodukt zweier
Vektoren <Skalarprodukt>` werden dabei die einzelnen Komponenten des Zeilen- und
des Spaltenvektors miteinander multipliziert, und die sich dabei ergebenden
Teilergebnisse schließlich summiert.

.. math::
    :label: eqn-skalarprodukt-zeilenvektor-spaltenvektor

    \vec{a} ^{\;\mathrm{T}} _{(1;\,n)} \cdot \vec{b}_{(n,1)} = (a_1,\, a_2,\, \ldots,\,
    a_n) \cdot \begin{pmatrix}
        b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix} = a_1 \cdot b_1 + a_2 \cdot b_2 + \ldots +
        a_n \cdot b_n = \sum_{i=1}^{n} a_i \cdot b_i

Damit eines solches Produkt möglich ist, muss der Zeilenvektor ebenso viele
Komponenten haben wie der Spaltenvektor. Das Ergebnis des Produkts ist dann eine
gewöhnliche Zahl (ein Skalar).

*Beispiel:*

* Welches Ergebnis erhält man, wenn man den Zeilenvektor :math:`\vec{a}
  ^{\;\mathrm{T}} = (3,\, -5,\, 4)` skalar mit dem Spaltenvektor :math:`\vec{b} =
  \begin{pmatrix} -1 \\ \phantom{+}2 \\ \phantom{+}1 \end{pmatrix}` multipliziert?

  .. math::

      \vec{a} ^{\;\mathrm{T}}\cdot \vec{b} = (3,\, -5,\, 4) \cdot
      \begin{pmatrix} -1 \\ \phantom{+}2 \\ \phantom{+}1 \end{pmatrix} = 3 \cdot (-1) + (-5) \cdot 2 +
      4 \cdot 1 = -9

  Das Produkt liefert somit den Wert :math:`\vec{a} ^{\;\mathrm{T}}\cdot \vec{b} = -9`

.. index:: Falk-Schema

Multipliziert man nun nicht nur einen Zeilenvektor mit :math:`n` Komponenten,
sondern eine :math:`n`-spaltige Matrix mit einem Spaltenvektor der Länge
:math:`n`, so wird nach der obigen Regel
:eq:`eqn-skalarprodukt-zeilenvektor-spaltenvektor` für jede Zeile der Matrix ein
Skalarprodukt mit dem Spaltenvektor gebildet. Hat die Matrix :math:`m` Zeilen,
so erhält man folglich :math:`m` einzelne Ergebnisse. Diese werden als
Komponenten in einen neuen Spaltenvektor der Länge :math:`m` geschrieben.

.. figure:: ../pics/algebra/matrix-multiplikation-falk-schema-1.png
    :name: fig-matrix-multiplikation-falk-schema
    :alt:  fig-matrix-multiplikation-falk-schema
    :align: center
    :width: 75%

    Multiplikation einer Matrix mit einem Spaltenvektor ("Falk-Schema")

    .. only:: html

        :download:`SVG: Matrix-Multiplikation (Falk-Schema) 1 <../pics/algebra/matrix-multiplikation-falk-schema-1.svg>`

Ein solches Produkt kann nur dann gebildet werden, wenn die Anzahl an Spalten
der Matrix mit der Anzahl an Zeilen des Vektors übereinstimmt; andernfalls ist
die Multiplikation nicht definiert.

Das "Falk-Schema", wie es in der obigen Abbildung dargestellt ist, bei dem die
zu multiplizierenden Matrizen beziehungsweise Vektoren tabellenartig aufgelistet
werden, kann auch auf die Multiplikation zweier Matrizen ausgeweitet werden.
Hierbei wird jeweils an der Stelle, wo sich eine Zeile der linken Matrix mit
einer Spalte der rechten Matrix überkreuzt, das entsprechende Skalarprodukt
eingetragen.

.. figure:: ../pics/algebra/matrix-multiplikation-falk-schema-2.png
    :name: fig-matrix-multiplikation-falk-schema2
    :alt:  fig-matrix-multiplikation-falk-schema2
    :align: center
    :width: 75%

    Multiplikation einer Matrix mit einer zweiten Matrix ("Falk-Schema").

    .. only:: html

        :download:`SVG: Matrix-Multiplikation (Falk-Schema) 2 <../pics/algebra/matrix-multiplikation-falk-schema-2.svg>`

Auch in diesem Fall ist das Produkt nur dann definiert, wenn die die Anzahl an
Spalten der linken Matrix mit der Anzahl an Zeilen des Vektors übereinstimmt.
Hat die linke Matrix die Form :math:`(m;\,n)` und die rechte Matrix die Form
:math:`(n;\,p)`, so erhält man als Ergebnis eine neue Matrix der Form
:math:`(m;\,p)`. Multipliziert man zwei quadratische Matrizen mit gleicher
Zeilen- beziehungsweise Spaltenanzahl, so ist die Form der resultierenden Matrix
mit der Form der beiden ursprünglichen Matrizen identisch.

Die Bedingung, dass bei der Multiplikation zweier Matrizen auf zueinander
passende Spalten- und Zeilenanzahlen geachtet werden muss, zeigt bereits, dass
bei diesem Rechenvorgang die Reihenfolge der Faktoren von Bedeutung ist:

* Multipliziert man eine Matrix der Form :math:`(3;\,2)` mit einer Matrix der
  Form :math:`(2;\,3)`, so ergibt sich eine Matrix der Form :math:`(3;\,3)`.
* Multipliziert man eine Matrix der Form :math:`(2;\,3)` mit einer Matrix der
  Form :math:`(3;\,2)`, so ergibt sich eine Matrix der Form :math:`(2;\,2)`.

Für die Multiplikation zweier Matrizen gilt folglich im Allgemeinen
Kommutativgesetz der Multiplikation *nicht* :

.. math::
    :label: eqn-kommutativgesetz-matrix-multiplikation

    \underline{A} \cdot \underline{B} \ne \underline{B} \cdot \underline{A}

Für die Multiplikation zweier Matrizen gilt allerdings das Distributivgesetz in
folgender Form:

.. math::
    :label: eqn-distributivgesetz-matrix-multiplikation

    \underline{A} \cdot (\underline{B} + \underline{C}) = \underline{A} \cdot
    \underline{B} + \underline{A} \cdot \underline{C}

Zusätzlich gilt, dass bei jedem Produkt einer Matrix :math:`\underline{A}` mit
einer entsprechenden Nullmatrix :math:`\underline{0}` wiederum eine Nullmatrix
entsteht (da jedes einzelnen Skalarprodukt den Wert Null hat). Multipliziert man
hingegen eine beliebige Matrix :math:`\underline{A}` mit einer Einheitsmatrix
:math:`\underline{E}`, so erhält man die ursprüngliche Matrix
:math:`\underline{A}` als Ergebnis. Es gilt also stets:

.. math::

    \underline{A} \cdot \underline{0} = \underline{0} \cdot \underline{A} &= \underline{0} \\[4pt]
    \underline{A} \cdot \underline{E} = \underline{E} \cdot \underline{A} &= \underline{E} \\[4pt]

In diesen beiden Sonderfällen spielt die Reihenfolge der Faktoren keine Rolle.

.. Matrizengleichungen
.. -------------------

... to be continued ...


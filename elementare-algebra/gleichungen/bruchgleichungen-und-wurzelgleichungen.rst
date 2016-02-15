.. _Bruchgleichungen und Wurzelgleichungen:

Bruch-, Produkt- und Wurzelgleichungen
======================================

Bruchgleichungen und Wurzelgleichungen stellen Gleichungstypen dar, die durch
entsprechende Umformungen in eine algebraische Gleichung umgewandelt werden
können.

.. index:: Bruchgleichung
.. _Bruchgleichungen:

Bruchgleichungen
----------------

Als Bruchgleichung wird eine Gleichung bezeichnet, in der die Variable :math:`x`
mindestens einmal im Nenner steht. Hierbei ist auf den Definitionsbereich der
Gleichung zu achten, da der Nenner eines Bruches niemals den Wert Null annehmen
darf ("Definitionslücke"). Allgemein ist der Definitionsbereich einer
Bruchgleichung gleich den reellen Zahlen ohne die Lösungen der Gleichungen, die
sich ergeben, wenn man den im Nenner stehenden :math:`x`-Term bzw. die im Nenner
stehende :math:`x`-Terme jeweils gleich Null setzt.

Um eine Bruchgleichung zu lösen, wendet man folgende Methode an:

1. Zunächst werden die einzelnen Bruchterme durch passende Erweiterungen auf
   den Hauptnenner gebracht -- wahlweise durch Multiplikation aller
   Nennerterme oder durch Bildung des kleinsten gemeinsamen Vielfachen der
   Nennerterme. [#BGL]_
2. Multipliziert man dann die Gleichung mit dem Hauptnenner :math:`N \ne 0`, so
   entfallen alle Brüche (da der Hauptnenner in allen Bruchtermen gekürzt
   werden kann beziehungsweise :math:`0 \cdot N = 0` gilt).

Die übrig bleibenden Terme stellen oftmals eine algebraische Gleichung dar,
häufig ersten oder zweiten Grades, die mit Hilfe der in den vorherigen
Abschnitten beschriebenen Verfahren gelöst werden kann.

*Beispiel:*


*   Die Lösungsmenge folgender Gleichung soll bestimmt werden:

    .. math::

        {\color{white}xx}\frac{4 \cdot x - 2}{x-5} = \frac{3 \cdot x +8}{x+2}

    Damit keiner der beiden Nenner gleich Null ist, muss :math:`x \ne 5` und
    :math:`x \ne -2` gelten.
    Zur Lösung der Gleichung werden die Terme auf beiden Seiten mit dem
    Hauptnenner :math:`(x-5) \cdot (x+2)` multipliziert. Beide Brüche können
    anschließend gekürzt werden:

    .. math::

        \frac{(4 \cdot x - 2\phantom{x}) \cdot (x-5) \cdot
        (x+2)\phantom{.}}{\phantom{\ldots\,}(x-5)} &= \; \frac{(3 \cdot x + 8)
        \cdot (x-5) \cdot (x+2)}{\phantom{xx}(x+2)} \\[8pt]
        \Rightarrow \quad  (4 \cdot x - 2) \cdot (x+2) \; &= \; (3 \cdot x + 8)
        \cdot (x-5)

    Die so gekürzte Gleichung entspricht einer algebraischen Gleichung zweiten
    Grades. Nach dem Ausmultiplizieren kann sie wie üblich umgeformt und gelöst
    werden:

    .. math::

        {\color{white}\ldots\;\;}4 \cdot x^2 + 8 \cdot x - 2 \cdot x -4 &= 3
        \cdot x^2  - 15 \cdot x + 8 \cdot x - 40 \\[6pt]
        \Rightarrow \quad 1 \cdot x^2 + 13 \cdot x + 36 &= 0

    Nach der :ref:`Mitternachtsformel <Quadratische Gleichungen>` gilt:

    .. math::

        {\color{white}\ldots\;\;\;}D = b^2 - 4 \cdot a \cdot c &= 13^2 - 4 \cdot
        1 \cdot 36 = 25\\[8pt]
        x _{\rm{1,2}} = \frac{-b \pm \sqrt{D}}{2 \cdot a} &= \frac{-13 \pm 5}{2}
        \\[6pt]
        \Rightarrow \quad x _{\rm{1}} = -9 \quad &\text{und} \quad x _{\rm{2}} =
        -4{\color{white}\;\;  \ldots \quad \qquad}

    Die Lösungsmenge der Bruchgleichung lautet somit :math:`\mathbb{L} = \{ -9,\; -4 \}`.


.. index:: Verhältnisgleichung
.. _Verhältnisgleichungen:

Verhältnisgleichungen
^^^^^^^^^^^^^^^^^^^^^^

Ein (vergleichsweise) einfacher Sonderfall einer Bruchgleichung liegt vor, wenn
die Variable :math:`x` nur ein einziges Mal auf einer Seite der Gleichung im
Nenner oder Zähler vorkommt, beispielsweise bei :math:`\frac{9}{4} =
\frac{x}{6}` oder allgemein :math:`\frac{a}{x} = \frac{b}{c}`, wobei :math:`a,\,
b` und :math:`c` beliebige, aber bekannte Werte bezeichnen. Derartige
Gleichungen werden als Verhältnisgleichungen bezeichnet und können genutzt
werden, um eine unbekannte Größe zu berechnen, wenn drei andere Größen bekannt
sind und sich die Zahlenverhältnisse zwischen den Größen nicht ändern, die
Größen also zueinander "proportional" sind.

Steht die Variable :math:`x` bei einer Verhältnisgleichung im Zähler eines
Terms, so genügt es, beide Seiten der Gleichung mit dem entsprechenden Nenner zu
multiplizieren, um den gesuchten Wert zu erhalten.

*Beispiel:*

* Für ein Brotrezept werden :math:`\unit[500]{g}` Mehl für :math:`\unit[800]{g}`
  Brot benötigt. Wieviel Gramm Mehl würde man (theoretisch) benötigen, um
  :math:`\unit[3000]{g}` Brot zu backen?

  Die gesuchte Mengenangabe :math:`x` steht hierbei im gleichen Verhältnis zur
  Zahl :math:`3000` wie :math:`500` zu :math:`800`, also:

  .. math::

      \frac{500}{800} = \frac{x}{3\,000}

  Multipliziert man beide Seiten der Gleichung mit :math:`3000`, so lässt sich
  der gesuchte Wert (nach dem Kürzen des Bruchs) unmittelbar ablesen:

  .. math::

      x = \frac{500 \cdot 3\,000}{800} = \frac{5 \cdot 3\,000}{8} = 1\,875

  Für :math:`\unit[3000]{g}` Brot wären somit :math:`\unit[1\,875]{g}` Mehl
  nötig.

**Tipp:** Steht die Variable :math:`x` bei einer Verhältnisgleichung im Nenner,
so empfiehlt es sich, die Brüche auf beiden Seiten der Gleichung durch ihre
Kehrbrüche zu ersetzen; dadurch hat man die Aufgabe auf die obige Form
zurückgeführt. Es genügt dann wiederum, den Zahlenterm mit dem zur Variablen
gehörenden Nenner zu multiplizieren.

.. index:: Produktgleichung
.. _Produktgleichungen:

Produktgleichungen
^^^^^^^^^^^^^^^^^^

Neben der obigen Form der (direkten) Proportionalität kann es auch vorkommen,
dass eine Größe immer kleiner wird, wenn eine andere Größe zunimmt.
Beispielsweise nimmt die Zeit, die man für eine bestimmte Wegstrecke benötigt,
mit zunehmender Geschwindigkeit ab. Ein solcher Zusammenhang zwischen zwei
Größen :math:`x_1` und :math:`x_2` wird als indirekte Proportionalität
bezeichnet und kann formal als Produktgleichung geschrieben werden:

.. math::

    x_1 \cdot x_2 = c

Hierbei ist :math:`c` ein bekannter, konstanter Wert. Eine solche Gleichung kann
nur in zwei Fällen eindeutig gelöst werden:

* wenn eine der beiden Größen :math:`x_1` oder :math:`x_2` ein ebenfalls
  bekannter Wert :math:`a` ist, die Gleichung also in der trivialen Form
  :math:`a \cdot x = c` mit der Lösung :math:`x = \frac{c}{a}` geschrieben
  werden kann, oder

* wenn eine zweite Gleichung für :math:`x_1` oder :math:`x_2` angegeben werden
  kann. Bei indirekten Proportionalitäten handelt es bei dieser ebenfalls um
  eine (triviale) Produktgleichung der Form :math:`b \cdot x_{1|2} = c`.

Bei vielen Aufgaben bleibt somit eine Gleichung mit nur einer Unbekannten, die
allgemein folgende Form hat:

.. math::
    :label: eqn-produktgleichung

    a \cdot b = c \cdot x

Zur besseren Lesbarkeit wurde hierbei der Index von :math:`x` weggelassen, zumal
ohnehin nur *eine* Größe gesucht wird. Die Gleichung kann somit einfach gelöst
werden, indem durch den Faktor :math:`c` dividiert wird:

.. math::

    a \cdot b = c \cdot x \quad \Leftrightarrow \quad x = \frac{a \cdot
    b}{c}

Die gesuchte Größe lässt sich also als Verhältnis der übrigen Größen
beschreiben. Damit stimmen Produktgleichungen formal mit Verhältnisgleichungen
überein, denn offensichtlich sind beide Gleichungsformen äquivalent:

.. math::

    \frac{a}{x} = \frac{c}{b} \quad \Leftrightarrow \quad x = \frac{a \cdot b}{c}

Es hängt von der Aufgabenstellung ab, ob eine Gleichung eher als Produkt- oder
als Verhältnisgleichung angegeben wird; liegt zwischen zwei untersuchten
Größen eine direkte Proportionalität vor, so wird der Zusammenhang meist als
Verhältnisgleichung, bei indirekter Proportionalität als Produktgleichung
angegeben.

.. Zusammenhang mit Steigung von linearen Funktionen und Hyperbeln.

.. rubric:: Die Sonderform :math:`x = c`


Eine Sonderform der Produktgleichung :eq:`eqn-produktgleichung` liegt dann vor,
wenn die gesuchte Größe :math:`x` der gegebenen Größe :math:`c` entsprechen
soll, also die Lösung für eine Gleichung mit folgender Form gesucht wird:

.. math::

    a \cdot b = c \cdot c = c^2 \quad \Leftrightarrow \quad x = c = \sqrt{a \cdot b}

In diesem Fall wird :math:`x = a \cdot b` als mittlere Proportionale und
:math:`x = \sqrt{a \cdot b}` als geometrisches Mittel von :math:`a` und
:math:`b` bezeichnet. Formal beschreibt :math:`x` dabei das mittlere Folgenglied
einer :ref:`geometrischen Folge <Geometrische Folgen>`, das zwischen :math:`a`
und :math:`b` liegt; der konstante Faktor der Folge ist hierbei :math:`q =
\sqrt{\frac{b}{a}}`.


.. index:: Dreisatz
.. _Dreisatz-Aufgaben:

Dreisatz-Aufgaben
^^^^^^^^^^^^^^^^^

Wie die obigen Beispiele zeigen, lassen sich mit Verhältnis- und
Produktgleichungen so genannte "Dreisatz-Aufgaben" lösen. Diese heißen so, weil
sie üblicherweise in drei Schritten gelöst werden:

1. Zunächst wird ein *Bedingungssatz* formuliert, der eine Aussage über das
   gegebene Größenverhältnis macht.

   Beispiel: Ein Containerschiff benötigt für eine Strecke von
   :math:`s_1=\unit[800]{km}` eine Zeit von :math:`t_1= \unit[16]{h}`.
   Der Bedingungssatz lautet also:

   .. math::

       \unit[800]{km} \; \hat{=} \; \unit[16]{h}

   Über dem Ist-Gleich-Zeichen wird dabei häufig ein Dach-Symbol geschrieben,
   da die linke Seite der Gleichung mit der rechten Seite zwar in einem
   bestimmten Verhältnis seht, aber nicht mit dieser identisch ist.

2. Anschließend wird ein *Fragesatz* formuliert, der die gesuchte Größe
   :math:`x` beinhaltet. Der Fragesatz ergibt gemeinsam mit dem Bedingungssatz
   ein System zweier Gleichungen, die aufgrund der festen Proportionalitäten als
   eine Verhältnisgleichung geschrieben werden können.

   Beispiel: Wie lange braucht das obige Containerschiff für eine :math:`s_2 =
   \unit[2500]{km}` lange Strecke? Der Fragesatz lautet in diesem Fall:

   .. math::

       \unit[2500]{km} \; \hat{=} \; ?

3. Mit dem *Schlußsatz* wird die gesuchte Größe (:math:`x` oder :math:`?`)
   berechnet, indem jeweils das Verhältnis der linken und der rechten Seiten der
   obigen Gleichungen gebildet wird. Vorzugsweise teilt man dabei die zweite
   Gleichung durch die erste, so dass die gesuchte Größe im Zähler steht.
   Es folgt für das obige Beispiel:

   .. math::

      \frac{\unit[2500]{km}}{\unit[800]{km}} &= \frac{?}{\unit[16]{h}}

   Aus dem Schlusssatz kann die gesuchte Größe unmittelbar berechnet werden

   .. math::

      ? &= \frac{25 \cdot \unit[16]{h}}{8} \\[4pt]
      \Rightarrow \; ? &= \unit[50]{h}

Bisweilen werden Dreisatz-Aufgaben auch gelöst, indem zunächst auf eine Einheit
der Grundgröße "herunter gerechnet" wird; im obigen Beispiel könnte man
zunächst ausrechnen, wie lange das Schiff für eine Strecke von
:math:`\unit[1]{km}` benötigt (Ergebnis: :math:`\unit[0,02]{Stunden}`).
Damit kann dann auf die gesuchte Zeit "hoch gerechnet" werden, indem man die
Zeit je Kilometer mit der gegebenen Anzahl an Kilometern multipliziert. Im
Allgemeinen bedeutet dieses Lösungsverfahren gegenüber der oben genannten
Methode jedoch einen erhöhten Rechenaufwand.


.. index:: Wurzelgleichung
.. _Wurzelgleichungen:

Wurzelgleichungen
-----------------

Als Wurzelgleichung wird eine Gleichung bezeichnet, in der die Variable
:math:`x` mindestens einmal im Argument einer Wurzel steht. Hierbei muss
gegebenenfalls der Definitionsbereich der Variablen eingeschränkt werden, da im
Bereich der reellen Zahlen negative Wurzeln nicht definiert sind. [#WG]_

Wurzelgleichungen lassen sich üblicherweise durch folgendes Verfahren lösen:

1. Zunächst wird eine Wurzel durch geeignete Umformungen isoliert, d.h. allein
   auf eine Seite der Gleichung gebracht.

2. Anschließend werden beide Seiten der Gleichung mit dem Wurzelexponenten (bei
   einer Quadratwurzel mit zwei) potenziert. Falls bei der sich ergebenden noch
   immer Wurzeln auftreten, wiederholt man dieses Verfahren, bis alle Wurzeln
   eliminiert sind.

Die neue Gleichung entspricht oftmals einer algebraischen Gleichung, häufig
ersten oder zweiten Grades, die mit Hilfe der in den vorherigen Abschnitten
beschriebenen Verfahren gelöst werden kann.

Da das Potenzieren mit einem geradzahligen Exponenten keine Äquivalenzumformung
darstellt, kann die umgeformte Gleichung (Schein-)Lösungen besitzen, die keine
Lösungen der ursprünglichen Gleichung sind. Eine Probe durch Einsetzen der
gefundenen Werte in die ursprüngliche Gleichung ist somit zwingend erforderlich.

*Beispiel:*

*   Die Lösungsmenge folgender Gleichung soll bestimmt werden:

    .. math::

        \sqrt{4 \cdot x - 3} - 2 \cdot x + 1 = 0

    Damit unter der Wurzel kein negativer Wert steht, muss :math:`4 \cdot x - 3 \ge
    0` gelten, also :math:`x \ge 0,75`. Zur Lösung der Gleichung wird zunächst die
    Wurzel isoliert, d.h. alle übrigen Terme auf die rechte Seite der Gleichung
    gebracht:

    .. math::

        \sqrt{4 \cdot x - 3} \phantom{.} = + 2 \cdot x - 1

    Nun kann die Gleichung quadriert werden. Es folgt:

    .. math::

        {\color{white}\ldots}\left(\sqrt{4 \cdot x - 3}\,\right)^2 &= (2 \cdot x - 1)^2 \\
        4 \cdot x - 3 \phantom{\ldots\!} &= 4 \cdot x^2 - 4 \cdot x + 1

    Die quadrierte Gleichung entspricht in diesem Fall einer algebraischen
    Gleichung zweiten Grades. Sie kann wie üblich umgeformt und gelöst werden:

    .. math::

        4 \cdot x^2 - 8 \cdot x + 4 &= 0 \\
        4 \cdot (x-1)^2 &= 0 \\
        (x-1)^2 &= 0 \\
        x & = 1

    Der gefundene Wert :math:`x=1` stellt auch, wie man durch Einsetzen leicht
    überprüfen kann, eine Lösung der ursprünglichen Gleichung dar. Somit lautet
    die Lösungsmenge der Wurzelgleichung :math:`\mathbb{L} = \{ 1 \}`.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#BGL] Das kleinste gemeinsame Vielfache (kgV) der Nennerterme lässt sich
    oftmals mit weniger Rechenaufwand berechnen, sofern diese in Form von
    (Linear-)Faktoren vorliegen. Das kgV ist in diesem Fall gleich dem Produkt
    der kleinsten Potenzen aller in den Nennern auftretenden Faktoren.

    Eine Zerlegung der Nennerterme in mehrere (Linear-)Faktoren ist genau dann
    möglich, wenn bereits eine oder mehrere Definitionslücken :math:`x
    _{\rm{i}}` gefunden wurden. Mit Hilfe dieser Werte lassen sich die
    Nennerterme jeweils als :math:`(x-x _{\rm{i}}) \cdot \text{Rest}`
    darstellen.

.. [#WG] Für jeden unter einer Wurzel stehenden Term :math:`\sqrt{T}` ist die
    :ref:`Ungleichung <Ungleichungen>` :math:`T \ge 0` zu lösen. Die
    Definitionsmenge entspricht dann der Schnittmenge der Lösungsintervalle.


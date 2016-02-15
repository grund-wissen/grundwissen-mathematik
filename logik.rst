.. _Logik:

Logik
=====

Die (Aussagen-)Logik ist für sämtliche Teilbereiche der Mathematik von
grundlegender Bedeutung.


.. index:: Satz, Aussage
.. _Satz und Aussage:

Satz und Aussage
----------------

Lässt sich einem Satz :math:`A` ein Wahrheitswert (:math:`w = \text{wahr}` oder
:math:`f = \text{falsch}`) eindeutig zuordnen, so wird dieser Satz zu einer
Aussage.

Als Darstellungsform für den Wahrheitswert von Aussagen wählt man häufig
so genannte "Wahrheitstafeln". Dabei werden spaltenweise die Wahrheitswerte
der in der Kopfzeile angegebenen Aussage(n) aufgelistet.

.. list-table::
    :name: tab-wahrheitstafel
    :widths: 50

    * - :math:`{\color{white}f}A{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`

*Beispiele:*

* Der Satz ":math:`1 + 2 = 3`" ist eine wahre Aussage.
* Der Satz ":math:`\text{9 ist eine Primzahl}`" ist eine falsche Aussage.
* Der Satz ":math:`\text{Die Donau fließt ins schwarze Meer}`" ist eine wahre
  Aussage.
* Der Satz ":math:`\text{Es ist spät}`" ist keine Aussage, da ihm kein
  Wahrheitswert zugeordnet werden kann.

Ein Satz ist auch dann eine Aussage, wenn sein Wahrheitswert zum gegebenen
Zeitpunkt nicht feststellbar ist. Beispielsweise handelt es sich bei dem Satz
"Am 3. April 1650 regnete es in Berlin." ebenfalls um eine Aussage, auch wenn
sich ihr Wahrheitswert mit großer Wahrscheinlichkeit nicht mehr feststellen
lässt.


.. index::
    single: Aussage; Negation
.. _Negation:

.. rubric:: Negation einer Aussage

Durch Verneinen einer Aussage :math:`A` entsteht eine Aussage :math:`\neg A`,
die Negation der Aussage :math:`A` genannt wird. Da der konkrete Wahrheitswert
einer negierten Aussage :math:`\neg A` stets vom Wahrheitswert der eigentlichen
Aussage :math:`A` abhängt, hat die entsprechende Wahrheitstafel zwei Spalten.

.. list-table::
    :name: tab-negation
    :widths: 50 50

    * - :math:`{\color{white}f}A{\color{white}f}`
      - :math:`{\color{white}f}\neg A{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}ff}f{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}ff}w{\color{white}f}`

Die Negation einer wahren Aussage ist falsch, die einer falschen ist wahr;
insbesondere entspricht die doppelte Negation einer Aussage :math:`\neg (\neg
A)` der ursprünglichen Aussage :math:`A`.

*Beispiele:*

* :math:`A`: "Die Geraden :math:`g` und :math:`h` schneiden sich."
* :math:`\neg A`: "Die Geraden :math:`g` und :math:`h` schneiden sich nicht."
* :math:`\neg (\neg A)`: "Es ist nicht wahr, dass die Geraden :math:`g` und
  :math:`h` sich nicht schneiden."


.. _Verknüpfungen von Aussagen:

Verknüpfungen von Aussagen
--------------------------

Mit Hilfe von Bindewörtern wie "und", "oder", "genau dann, wenn" usw. lassen
sich mehrere (Teil-)Aussagen zu einer zusammengesetzten Aussage verknüpfen. In
der Logik lassen sich mit Hilfe der folgenden Aussage-Funktionen *zwei* (oder
mehrere) Aussagen zu *einer* neuen Aussage formen.


.. index::
    single: Aussage; Konjunktion

.. _Konjunktion:

.. rubric:: Die Konjunktion

Verknüpft man zwei Aussagen :math:`A _{\rm{1}}` und :math:`A _{\rm{2}}` durch
das Wort "und", so entsteht die Konjunktion der Aussagen :math:`A _{\rm{1}}` und
:math:`A _{\rm{2}}`, symbolisch mit :math:`A _{\rm{1}} \wedge A _{\rm{2}}`
bezeichnet.

.. list-table:: Wahrheitstafel der Konjunktion
    :name: tab-konjunktion
    :widths: 50 50 50

    * - :math:`{\color{white}f}A _{\rm{1}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{2}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{1}} \wedge A _{\rm{2}}{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`

Eine Konjunktion zweier Aussagen ist somit nur wahr, wenn beide (Teil-)Aussagen
wahr sind.

*Beispiele:*

* Die Konjunktion der wahren Aussage :math:`A _{\rm{1}}` ":math:`8` ist eine
  gerade Zahl" mit der falschen Aussage :math:`A _{\rm{2}}` ":math:`8` ist
  durch :math:`3` teilbar" ist die falsche Aussage :math:`A _{\rm{1}} \wedge A
  _{\rm{2}}` : ":math:`8` ist eine gerade Zahl und durch :math:`3` teilbar".

* Die falsche Aussage "Der Mars ist ein Gasplanet und hat eine größere Masse
  als die Erde" ist eine Konjunktion der falschen Aussagen "Der Mars ist ein
  Gasplanet" und "Der Mars hat eine größere Masse als die Erde".

.. index::
    single: Aussage; Adjunktion
.. _Adjunktion:

.. rubric:: Die Adjunktion

Verknüpft man zwei Aussagen :math:`A _{\rm{1}}` und :math:`A _{\rm{2}}` durch
das Wort "oder", so entsteht die Adjunktion der Aussagen :math:`A _{\rm{1}}`
und :math:`A _{\rm{2}}`, symbolisch mit :math:`A _{\rm{1}} \vee A _{\rm{2}}`
bezeichnet.

.. list-table:: Wahrheitstafel der Adjunktion
    :name: tab-adjunktion
    :widths: 50 50 50

    * - :math:`{\color{white}f}A _{\rm{1}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{2}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{1}} \vee A _{\rm{2}}{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`

Die Adjunktion ist somit wahr, wenn eine der beiden Aussagen wahr ist (oder
beide wahr sind).

*Beispiele:*

* Die Adjunktion der wahren Aussage :math:`0 < 1` und der falschen Aussage
  :math:`0 = 1` ist die wahre Aussage :math:`0 \le 1`.

* Die wahre Aussage: "Entweder ist die Erde ein Würfel oder die Sonne ist ein
  Stern" ist eine Adjunktion der falschen Aussage: "Die Erde ist ein Würfel"
  und der wahren Aussage: "Die Sonne ist ein Stern".


.. index::
    single: Aussage; Implikation
.. _Implikation:

.. rubric:: Die Implikation

Verknüpft man zwei Aussagen :math:`A _{\rm{1}}` und :math:`A _{\rm{2}}` durch
das Wort "dann", so entsteht die Implikation der Aussagen :math:`A _{\rm{1}}`
und :math:`A _{\rm{2}}`, symbolisch mit :math:`A _{\rm{1}} \Rightarrow A
_{\rm{2}}` bezeichnet.

.. list-table:: Wahrheitstafel der Implikation
    :name: tab-implikation
    :widths: 50 50 50

    * - :math:`{\color{white}f}A _{\rm{1}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{2}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{1}} \Rightarrow A _{\rm{2}}{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`

Die Implikation ist wahr, wenn beide Aussagen :math:`A _{\rm{1}}` und :math:`A2`
wahr sind oder wenn die erste Aussage :math:`A _{\rm{1}}` falsch ist. [#I1]_
Formal erhält man eine identische Wahrheitstafel, wenn man die Implikation
:math:`(\neg A _{\rm{2}}) \Rightarrow (\neg A _{\rm{1}})` bildet. [#I2]_ [#I3]_

*Beispiele:*

* Die Aussage "Wenn :math:`2 < 1` ist, dann ist :math:`3 < 2`" ist wahr,
  obwohl sie eine Implikation zweier falscher (Teil-)Aussagen ist.

* Die Implikation der wahren Aussage "Die Lichtgeschwindigkeit beträgt annähernd
  :math:`\unit[300\,000]{km/s}`" und der falschen Aussage "Die
  Schallgeschwindigkeit ist größer als die Lichtgeschwindigkeit“ ist die falsche
  Aussage "Die Schallgeschwindigkeit beträgt mehr als
  :math:`\unit[300\,000]{km/s}`".

.. index::
    single: Äquivalenz
    single: Aussage; Äquivalenz
.. _Äquivalenz:

.. rubric:: Äquivalenz zweier Aussagen

Verknüpft man zwei Aussagen :math:`A _{\rm{1}}` und :math:`A _{\rm{2}}` durch
die Wortkombination "dann, und nur dann", so
entsteht die Äquivalenz der Aussagen :math:`A _{\rm{1}}` und :math:`A
_{\rm{2}}`, symbolisch mit :math:`A2 \Leftrightarrow A _{\rm{2}}` bezeichnet.

.. list-table:: Wahrheitstafel der Äquivalenz
    :name: tab-äquivalenz
    :widths: 50 50 50

    * - :math:`{\color{white}f}A _{\rm{1}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{2}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{1}} \Leftrightarrow A _{\rm{2}}{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`

Die Äquivalenz zweier Teilaussagen ist nur wahr, wenn entweder beide
Teilaussagen wahr oder beide falsch sind. [#Aq1]_

*Beispiele:*

* Die wahre Aussage "Im rechtwinkligen Dreieck gilt der Höhensatz" äquivalent
  verknüpft mit der falschen Aussage "Im rechtwinkligen Dreieck sind alle Seiten
  gleich lang" ergibt die falsche Aussage "Im rechtwinkligen Dreieck sind dann
  und nur dann alle Seiten gleich lang, wenn der Höhensatz gilt".

* Die Äquivalenzverknüpfung der falschen Aussage "Das Kilogramm ist eine
  Längeneinheit" mit der wahren Aussage "Tausend Meter ergeben einen Kilometer"
  ist die falsche Aussage "Das Kilogramm ist dann und nur dann eine
  Längeneinheit, wenn tausend Meter einen Kilometer ergeben".


.. index::
    single: Aussage; Kontravalenz
.. _Kontravalenz zweier Aussagen:

.. rubric:: Kontravalenz zweier Aussagen

Verknüpft man zwei Aussagen :math:`A _{\rm{1}}` und :math:`A _{\rm{2}}` durch
das Wort "entweder oder" im ausschließenden Sinn, so entsteht die Kontravalenz
der Aussagen :math:`A _{\rm{1}}` und :math:`A _{\rm{2}}`, mit  mit :math:`A
_{\rm{1}} \dot{\vee} A _{\rm{2}}` bezeichnet.

.. list-table:: Wahrheitstafel der Kontravalenz
    :name: tab-kontravalenz
    :widths: 50 50 50

    * - :math:`{\color{white}f}A _{\rm{1}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{2}}{\color{white}f}`
      - :math:`{\color{white}f}A _{\rm{1}} \, \dot{\vee} \, A _{\rm{2}}{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`
    * - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}w{\color{white}f}`
      - :math:`{\color{white}fff}w{\color{white}f}`
    * - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}f}f{\color{white}f}`
      - :math:`{\color{white}fff}f{\color{white}f}`

Die Kontravalenz zweier Teilaussagen ist nur dann wahr, wenn genau eine der
beiden (Teil-)Aussagen wahr ist. Damit ist sie formal, wie ihr Name bereits
andeutet, mit der Negation der Äquivalenz identisch.

*Beispiel:*

* Verknüpft man die wahre Aussage "Der Zug fährt nach München" kontravalent mit
  der falschen Aussage "Der Zug fährt nach Frankfurt", so ergibt sich die wahre
  Aussage "Der Zug fährt entweder nach München oder nach Frankfurt".


.. rubric:: Regeln zu den Aussagenverknüpfungen

Zwischen den Aussagen bzw. ihren Verknüpfungen sind folgende Äquivalenzen
definiert, von denen einige eine formale Ähnlichkeit mit den Regeln für das
Rechnen mit Zahlen haben:

* *Kommutativgesetz:*

.. math::

    A_{\rm{1}} \wedge A_{\rm{2}} \Leftrightarrow A_{\rm{2}} \wedge A_{\rm{1}} \\
    A_{\rm{1}} \vee A_{\rm{2}} \Leftrightarrow A_{\rm{2}} \vee A_{\rm{1}}

* *Assoziativgesetz:*

.. math::

    (A_{\rm{1}} \wedge A_{\rm{2}}) \wedge  A_{\rm{3}} \Leftrightarrow A_{\rm{1}}
    \wedge  (A_{\rm{2}} \wedge A_{\rm{3}}) \\
    (A_{\rm{1}} \vee A_{\rm{2}}) \vee  A_{\rm{3}} \Leftrightarrow A_{\rm{1}}
    \vee  (A_{\rm{2}} \vee A_{\rm{3}})

* *Distributivgesetz:*

.. math::

    A_{\rm{1}} \wedge (A_{\rm{2}} \vee  A_{\rm{3}}) \Leftrightarrow (A_{\rm{1}}
    \wedge A_{\rm{2}}) \vee (A_{\rm{2}} \wedge A_{\rm{3}}) \\
    A_{\rm{1}} \vee (A_{\rm{2}} \wedge  A_{\rm{3}}) \Leftrightarrow (A_{\rm{1}}
    \vee A_{\rm{2}}) \wedge (A_{\rm{2}} \vee A_{\rm{3}})

Hinzu kommen folgende Regeln, die bisweilen für Beweisverfahren sowie in der
Informatik nützlich sind:

* *Regeln von de Morgan:*

.. math::

    \neg (A_{\rm{1}} \wedge A_{\rm{2}})  \Leftrightarrow  (\neg A_{\rm{1}}) \vee
    (\neg A_{\rm{2}}) \\
    \neg (A_{\rm{1}} \vee A_{\rm{2}})  \Leftrightarrow (\neg A_{\rm{1}}) \wedge
    (\neg A_{\rm{2}})


* *Absorptionsgesetz:*

.. math::

    A_{\rm{1}} \wedge (A_{\rm{1}} \vee A_{\rm{2}}) \Leftrightarrow A_{\rm{1}} \\
    A_{\rm{1}} \vee (A_{\rm{1}} \wedge A_{\rm{2}}) \Leftrightarrow A_{\rm{1}}


* *Idempotenzgesetz:*

.. math::

    A \wedge  A \Leftrightarrow  A\\
    A \vee    A \Leftrightarrow  A\\

.. index:: Tautologie

* *Komplementgesetz:*

.. math::

    A _{\rm{1}} \vee (\neg A _{\rm{2}} \wedge A _{\rm{2}} ) \Leftrightarrow A \\
    A _{\rm{1}}  \wedge (\neg A _{\rm{2}}  \vee A _{\rm{2}} ) \Leftrightarrow A

Dabei wird die Verknüpfung :math:`(\neg A) \vee A` auch "Tautologie" genannt;
sie ist stets wahr. [#Tau]_

.. index:: Variable
.. _Variablen, Terme und Aussageformen:

Variablen, Terme und Aussageformen
----------------------------------

Eine Variable ist ein Symbol für ein beliebiges Element aus einer vorgegebenen
Grundmenge. Darüber hinaus gelten für das Rechnen mit Variablen keine besonderen
Regeln oder Gesetze.

.. index:: Term
.. _Term:

Ein Term ist eine Bezeichnung zum einen für ein einzelnes mathematisches Objekt
(z.B. :math:`\pm \frac{1}{2} ,\, \pi ,\, \sqrt{3}`), zum anderen auch für eine
Aneinanderreihung mehrerer Konstanten, Variablen, Klammern und Rechenoperatoren
(z.B. :math:`2 \cdot (x^2 - 1) ,\; x \in \mathbb{R}`). [#T1]_ Terme enthalten
allerdings kein Relationszeichen, sie sind somit weder wahr noch falsch.

.. index:: Aussageform
.. _Aussageform:

Eine Aussageform enthält neben (mindestens) einer Variablen und (mindestens)
einem Term ein Relationszeichen -- beispielsweise :math:`x \ge 1` oder :math:`x
_{\rm{1}} \cdot x _{\rm{2}} = 0`. Um allerdings einer Aussageform auch einen
Wahrheitswert zuordnen zu können, müssen zunächst alle auftretenden Variablen
durch konkrete Elemente aus der Grundmenge ersetzt werden. Ebenso wie Aussagen
lassen sich mehrere Aussageformen durch logische Verknüpfungen zu neuen
Aussageformen kombinieren.

Die Abhängigkeit einer Aussageform von einer oder mehreren Variablen :math:`x
_{\rm{1}} ,\, x _{\rm{2}} ,\, \ldots` wird in der Form :math:`A(x _{\rm{1}} ,\,
x _{\rm{2}} ,\, \ldots )` ausgedrückt. Dabei lassen sich Aussageformen in drei
Arten unterteilen:

* Wird eine von einer Variablen :math:`x` abhängige Aussageform :math:`A(x)` für
  jedes beliebige :math:`x` aus einer Grundmenge :math:`X` erfüllt, so
  bezeichnet man die Aussageform :math:`A(x)` als allgemeingültig bezüglich
  :math:`X`.
* Existiert mindestens ein :math:`x` aus der Grundmenge :math:`X`, das die
  Aussageform :math:`A(x)` erfüllt, so bezeichnet man die Aussageform :math:`A(x)` als
  erfüllbar bezüglich :math:`X`.
* Existiert kein :math:`x` aus der Grundmenge :math:`X`, das die Aussageform
  :math:`A(x)` erfüllt, so bezeichnet man die Aussageform :math:`A(x)` als
  unerfüllbar bezüglich :math:`X`.

Aussageformen werden insbesondere in der Algebra als :ref:`Gleichungen
<Gleichungen>` und :ref:`Ungleichungen <Ungleichungen>` behandelt.

.. index:: Quantor

.. _'Für alle' und 'Es gibt':

.. rubric:: 'Für alle' und 'Es gibt'

Aussageformen können -- neben dem Einsetzen von konkreten Objekten für die
auftretenden Variablen -- auch auf eine zweite Art und Weise zu Aussagen gemacht
werden: Der Quantifizierung.

* Eine allgemeine Aussageform :math:`A(x)` wird zu einer "Existenz-Aussage",
  wenn folgende Forderung erfüllt ist:

    .. epigraph::

        "Es existiert (mindestens) ein Element :math:`x` aus der Grundmenge
        :math:`X`", für das die Aussageform :math:`A(x)` wahr ist."

  Verkürzend kann eine Existenz-Aussage mit Hilfe des so genannten
  "Existenz-Quantors" :math:`\exists` formuliert werden: Anstelle von "Es
  existiert (mindestens) ein :math:`x`" kann auch kurz :math:`\exists x`
  geschrieben werden.

* Eine allgemeine Aussageform :math:`A(x)` wird zu einer "Universal-Aussage",
  wenn folgende Forderung erfüllt ist:

    .. epigraph::

        "Für jedes Element :math:`x` aus der Grundmenge :math:`X`" ist die
        Aussageform :math:`A(x)` wahr."

  Verkürzend kann eine Universal-Aussage mit Hilfe des so genannten
  "All-Quantors" :math:`\forall` formuliert werden: Anstelle von "Für alle
  :math:`x`" kann auch kurz  :math:`\forall x` geschrieben werden.

Während eine Existenz-Aussage :math:`\exists x \!: A(x)` wahr ist, wenn die
zugrunde liegende Aussageform :math:`A(x)` auch nur für ein konkretes :math:`x`
erfüllt wird, so kann im umgekehrten Fall eine Universal-Aussage :math:`\forall
x \!: A(x)` bereits durch den Existenz-Nachweis eines einzigen "Gegenbeispiels"
:math:`\exists x \!: \neg A(x)` als falsch widerlegt werden. [#A1]_ [#A2]_

.. index:: Beweis
.. _Direkte und indirekte Beweise:

Direkte und indirekte Beweise
-----------------------------

Die formalen Regeln der Logik können auch genutzt werden, um mittels bereits als
wahr nachgewiesener Aussageformen Schlussfolgerungen auf neue Gesetzmäßigkeiten
ziehen zu können. Auf diese Art gewonnene Lehrsätze (auch "Theoreme" oder kurz
"Sätze" genannt) stellen das Grundgerüst der mathematischen Theorie dar.

Neben bereits bekannten Lehrsätzen werden auch so genannte Definitionen genutzt,
um neue Sätze beweisen zu können. Beim Definieren wird ein Begriff durch die
Festlegung wesentlicher, gemeinsamer Merkmale eindeutig bestimmt und von anderen
Begriffen unterschieden. Definitionen sind weder wahr noch falsch, sie dienen
vielmehr als Abkürzungen für unhandliche Formulierungen. Als Definitionszeichen
für mathematische Terme verwendet man das Zeichen :math:`:=`, eine
Kurzschreibweise für "ist nach Definition gleich".

Für die eigentlichen "Beweise" sind u.a. folgende aussagenlogische Schlussregeln
möglich:

.. index:: Beweis; durch Implikation

* Schlussfolgerung aus einer Implikation:
    Gilt eine Aussage :math:`A _{\rm{1}}` und ist die Implikation :math:`A
    _{\rm{1}} \Rightarrow A _{\rm{2}}` wahr, so ist auch :math:`A _{\rm{2}}`
    eine wahre Aussage. Kurz formuliert ist somit der aussagenlogische Ausdruck
    :math:`[ A _{\rm{1}} \wedge (A _{\rm{1}} \Rightarrow A _{\rm{2}})]
    \Rightarrow A _{\rm{2}}` allgemeingültig.

.. index:: Beweis; durch Negation

* Schlussfolgerung aus einer Negation:
    Der aussagenlogische Ausdruck :math:`\neg (\neg A) \Rightarrow A` ist
    allgemeingültig. Eine Aussage kann somit bewiesen werden, indem man die
    Negation der Aussage widerlegt.

Bei direkten Beweisen wird, ausgehend von gültigen Voraussetzungen und unter
Verwendung von zulässigen Schlussregeln, nach endlich vielen Schritten direkt
auf die Behauptung gefolgert. Bei indirekten Beweisen hingegen wird die Negation
der Behauptung zu den Voraussetzungen hinzugenommen.


.. index::
    single: Induktionsbeweis
    single: Beweis; durch Induktion
.. _Vollständige Induktion:

.. rubric:: Die vollständige Induktion

Die vollständige Induktion ist ein häufig genutztes Verfahren zum direkten
Beweisen einer Aussage. Die logische Schlussfolgerung beruht dabei auf drei
Schritten:

1. Mit dem "Induktionsanfang" wird gezeigt, dass eine Aussageform :math:`A(x)`
   für ein (beliebig wählbaren) Wert :math:`x = n` gültig ist.

2. Die "Induktionsannahme" besteht darin, dass die Aussageform :math:`A(x)` für
   ein bestimmtes :math:`n` gültig ist.

3. Mit dem "Induktionsschluss", einem "Beweis im Beweis", wird gezeigt, dass aus
   der Gültigkeit der Aussage :math:`A(n)` auch die Gültigkeit der Aussage
   :math:`A(n + 1 )` folgt, in Kurzschreibweise :math:`A(n) \Rightarrow A(n+1)`.

*Beispiel:*

* Mit Hilfe der vollständigen Induktion soll bewiesen werden, dass für alle
  natürlichen Zahlen :math:`n` gilt:

  .. math::

      1 + 2 + \ldots + n = \frac{n \cdot (n + 1)}{2}


  1. Induktionsanfang: Für :math:`n _{\rm{0}} =1` gilt:

  .. math::

    1 = \frac{1 \cdot 2}{2} = 1 \quad \checkmark

  2. Induktionsannahme: Für eine beliebige Zahl :math:`n _{\rm{0}}` gilt die
     Aussageform

  .. math::

    1 + 2 + \ldots n _{\rm{0}} = \frac{n _{\rm{0}}
    \cdot (n _{\rm{0}} + 1)}{2}

  3. Induktionsschluss: :math:`n _{\rm{0}} \Rightarrow n _{\rm{0}}  + 1`


  .. math::

      1 + 2 + \ldots + n _{\rm{0}} + (n _{\rm{0}} + 1)
      &= \frac{n _{\rm{0}}
      \cdot (n _{\rm{0}} + 1)}{2} + (n _{\rm{0}} + 1) \\[4pt]
      &=  \frac{1}{2} \cdot n _{\rm{0}}  \cdot (n _{\rm{0}}  + 1) + (n _{\rm{0}}
      + 1) = (n _{\rm{0}} + 1) \cdot \left( \frac{1}{2} \cdot n _{\rm{0}} + 1 \right) \\[6pt]
      &= (n _{\rm{0}} + 1) \cdot \frac{1}{2} \cdot (n _{\rm{0}} + 2) = \frac{(n
      _{\rm{0}} + 1) \cdot (n _{\rm{0}} + 2)}{2} \\[6pt]
      &= \frac{(n _{\rm{0}} + 1) \cdot ((n _{\rm{0}} + 1) + 1)}{2} \quad
      \checkmark

  Aus der Richtigkeit der Aussageform für :math:`n _{\rm{0}}` folgt somit auch
  die Richtigkeit der Annahme für :math:`n _{\rm{0}} + 1`. Somit ist die
  Aussageform für alle :math:`n \ge 1` wahr.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#I1] Der letztere Fall wird bisweilen auch als "Ex falso quodlibet"
        bezeichnet -- aus einer falschen Annahme folgt Beliebiges.

.. [#I2] Die vorschnelle
        Annahme, dass aus :math:`A _{\rm{1}} \Rightarrow A _{\rm{2}}` auch
        :math:`(\neg A _{\rm{1}}) \Rightarrow (\neg A _{\rm{2}})` folge, ist
        hingegen falsch.

        Ein anschauliches Beispiel hierfür ist die Aussage :math:`A _{\rm{1}}
        \Rightarrow A _{\rm{2}}` "Wenn es regnet, dann ist es bewölkt." Die
        Aussage :math:`(\neg A _{\rm{1}} ) \Rightarrow (\neg A _{\rm{2}})`
        würde lauten "Wenn es nicht regnet, dann ist es nicht bewölkt", was
        offensichtlich falsch ist. Die Aussage :math:`(\neg B) \Rightarrow (\neg
        A)` "Wenn es nicht bewölkt ist, dann regnet es nicht" ist hingegen
        richtig.

        Man sagt daher auch, dass :math:`A _{\rm{1}}` notwendig für :math:`A
        _{\rm{2}}` sei und dass :math:`A _{\rm{2}}` hinreichend für :math:`A
        _{\rm{1}}` sei.

.. [#I3] Es existiert sogar eine dritte Darstellungsweise der Implikation, und
        zwar :math:`(\neg A _{\rm{1}}) \vee A _{\rm{2}}`. Dies lässt anhand der
        :ref:`Wahrheitstabelle der Adjunktion <tab-adjunktion>` überprüfen,
        indem man für :math:`A _{\rm{1}}` die jeweils entgegengesetzten
        Wahrheitswerte annimmt und das Ergebnis der so gebildeten Adjunktion mit
        der :ref:`Wahrheitstabelle der Implikation <tab-implikation>`
        vergleicht.

.. [#Aq1] Formal erhält man eine identische Wahrheitstafel, wenn man die beiden
        Implikationen :math:`(A _{\rm{1}}) \Rightarrow (A _{\rm{2}})` und
        :math:`(A _{\rm{2}}) \Rightarrow (A _{\rm{1}})` bildet und durch eine
        Konjunktion miteinander verknüpft. Es gilt also:

        .. math::

            (A _{\rm{1}} \Leftrightarrow A _{\rm{2}} ) \Leftrightarrow ( (A
            _{\rm{1}} \Rightarrow A _{\rm{2}} ) \wedge (A _{\rm{2}} \Rightarrow
            A _{\rm{1}} ))

.. [#Tau] Das Gegenteil der Tautologie, die Aussage :math:`A \wedge (\neg A)`,
        heißt Kontradiktion; sie ist für jede beliebige Aussagen :math:`A` stets
        falsch.

.. [#T1] Setzt man für die in Termen auftretenden Variablen konkrete
        mathematische Objekte des Grundbereichs ein, so ergibt sich ein neuer
        mathematischer Ausdruck; beispielsweise ergibt der Term :math:`8 \cdot x
        - 10` für :math:`x = 1` den Wert :math:`-2`.

.. [#A1] In Zusammenhang mit den Quantoren :math:`\exists` und :math:`\forall`
        stellt der folgende Doppelpunkt ``:``  eine Kurzschreibweise für "so
        dass gilt:" bzw. "gilt:" dar.

.. [#A2] Auch kombinierte Quantifizierungs-Aussagen sind möglich,
        beispielsweise "Für jeden Menschen :math:`m` existiert ein Tag
        :math:`t`, so dass die Aussageform :math:`A(m,t)` erfüllt ist: :math:`m`
        hat am Tag :math:`t` Geburtstag". Als Kurzform kann für diese (wahre)
        Aussage :math:`\forall m \; \exists t \! : A(m,t)` geschrieben werden.



.. index:: Ableitung; von Potenzfunktionen
.. _Ableitungen von Potenz- und Wurzelfunktionen:

Ableitungen von Potenz- und Wurzelfunktionen
============================================

Allgemein können :ref:`Potenz- und Wurzelfunktionen <Potenz- und
Wurzelfunktionen>` in der Form :math:`y = f(x) = x^n` dargestellt werden, wobei
:math:`n \in \mathbb{Q ^{+}}` eine beliebige positive rationale Zahl ist. Diese
Funktionen sind an allen Stellen ihres Definitionsbereichs differenzierbar, da
bei Ableitungen von Hyperbelfunktionen ihre Steigung entweder gleich bleibt oder
sich kontinuierlich ändert. [#]_ Es lässt sich somit jeweils eine Funktion
:math:`f' (x)` finden, die für jeden Wert :math:`x` des Definitionsbereichs
genau den Wert der Steigung von :math:`f(x)` als Funktionswert liefert. Eine
solche Funktion :math:`f' (x)` wird Ableitungsfunktion oder kurz Ableitung von
:math:`f(x)` genannt.


.. index:: Steigung
.. _Steigung und erste Ableitung:

Steigung und erste Ableitung
----------------------------

Die erste Ableitung :math:`f'(x)` einer Funktion gibt an, wie schnell sich ihre
Funktionswerte ändern; man spricht auch von der "Steigung" von :math:`f(x)`. Für
eine Potenzfunktion lässt sich die zugehörige Ableitung einfach nach folgender
Regel bestimmen: [#]_

.. math::
    :label: eqn-ableitungsregel-potenzfunktion

    f(x) = x^n \quad \Rightarrow \quad f'(x) = n \cdot x ^{n-1}

Die Ableitung einer Potenzfunktion ist somit wieder eine Potenzfunktion, deren
Grad um :math:`1` geringer ist als die ursprüngliche Funktion.

*Beispiele:*

* Für :math:`n=0` gilt :math:`f(x) = x^0 = 1`. Diese Funktion liefert für alle
  :math:`x`-Werte konstant den Wert :math:`1`, die Funktionswerte ändern sich
  also nicht. Die Steigung muss in diesem Fall also gleich Null sein. Nach der
  obigen Regel wird diese Bedingung erfüllt:

  .. math::
      :label: eqn-ableitungsregel-konstante-funktion

      f(x) &= x^0  \\
      \Rightarrow \quad f'(x) &= 0 \cdot x ^{0 -1} = 0

* Für :math:`n = 1` entspricht :math:`f(x)=x^n` der Ursprungsgeraden
  :math:`f(x) = x^1 = x`. Für die Ableitungsfunktion ergibt sich nach Gleichung
  :eq:`eqn-ableitungsregel-potenzfunktion`:

  .. math::

      f(x) &= x^1 \\[6pt]
      \Rightarrow f'(x) &= 1 \cdot x ^{1-1} = 1 \cdot x^0 = 1

  Da eine Gerade stets eine konstante Steigung besitzt, liefert ihre
  Ableitungsfunktion für alle :math:`x` einen konstanten Wert. Dieser Wert ist
  umso größer, je steiler die Gerade verläuft, und negativ, falls es sich um
  eine fallende Gerade handelt.

  .. figure:: ../../pics/analysis/steigung-lineare-funktion.png
      :width: 100%
      :align: center
      :name: fig-steigung-lineare-funktion
      :alt:  fig-steigung-lineare-funktion

      Funktionsgraph und erste Ableitung (Steigung) der linearen Funktion
      :math:`y=x`.

      .. only:: html

          :download:`SVG: Steigung einer linearen Funktion
          <../../pics/analysis/steigung-lineare-funktion.svg>`

* Für :math:`n = 2` entspricht :math:`f(x)=x^n` der Normalparabel :math:`f(x) =
  x^2`. Für die Ableitungsfunktion ergibt sich nach Gleichung
  :eq:`eqn-ableitungsregel-potenzfunktion`:

  .. math::

      f(x) &= x^2 \\[6pt]
      \Rightarrow f'(x) &= 2 \cdot x ^{2-1} = 2 \cdot x^1 = 2 \cdot x

  Die Steigung der Normalparabel nimmt also konstant zu -- von stark negativen
  Werten links der :math:`y`-Achse (der Graph der Ableitungsfunktion befindet
  sich im negativen Wertebereich) bis hin zu stark positiven Werten rechts der
  :math:`y`-Achse.

  .. figure:: ../../pics/analysis/steigung-quadratische-funktion.png
      :width: 100%
      :align: center
      :name: fig-steigung-quadratische-funktion
      :alt:  fig-steigung-quadratische-funktion

      Funktionsgraph und erste Ableitung (Steigung) der quadratischen Funktion
      :math:`y=x^2`.

      .. only:: html

          :download:`SVG: Steigung einer quadratischen Funktion
          <../../pics/analysis/steigung-quadratische-funktion.svg>`

* Für :math:`n = 3` gilt :math:`f(x)=x^3`, und für die Ableitungsfunktion:

  .. math::

      f(x) &= x^3 \\[6pt]
      \Rightarrow f'(x) &= 3 \cdot x ^{3-1} = 3 \cdot x^2

  Die Ableitungsfunktion :math:`f'(x) = 3 \cdot x^2` befindet sich stets im
  positiven Wertebereich, was bedeutet, dass die Steigung der kubischen Funktion
  :math:`f(x) = x^3` stets positiv (bzw. Null am Punkt :math:`(0;0)`) ist.

  .. figure:: ../../pics/analysis/steigung-kubische-funktion.png
      :width: 100%
      :align: center
      :name: fig-steigung-kubische-funktion
      :alt:  fig-steigung-kubische-funktion

      Funktionsgraph und erste Ableitung (Steigung) der kubischen Funktion
      :math:`y=x^3`.

      .. only:: html

          :download:`SVG: Steigung einer kubischen Funktion
          <../../pics/analysis/steigung-kubische-funktion.svg>`

* Für :math:`n = \frac{1}{2}` entspricht :math:`f(x)=x ^{\frac{1}{2}}` nach den
  :ref:`Rechenregeln für Wurzeln und Potenzen <Rechenregeln für Wurzeln und
  allgemeine Potenzen>` der Wurzelfunktion :math:`f(x) = \sqrt{x}`. Für die und
  für die Ableitungsfunktion :math:`f'(x)` gilt in diesem Fall:

  .. math::

      f(x) & = x ^{\frac{1}{2}} = \sqrt{x}\\[6pt]
      \Rightarrow f'(x) &= \frac{1}{2} \cdot \left(x ^{\left(\frac{1}{2} -1\right)}\right)= \frac{1}{2}
      \cdot \left(x ^{- \frac{1}{2}}\right) = \frac{1}{2} \cdot \left(\frac{1}{x ^{\frac{1}{2}}}\right) =
      \frac{1}{2} \cdot \left(\frac{1}{\sqrt{x}}\right) = \frac{1}{2 \cdot \sqrt{x}}

  Die Ableitungsfunktion :math:`f'(x) = \frac{1}{2 \cdot \sqrt{x}}` befindet
  sich ebenfalls stets im positiven Wertebereich, da die Wurzelfunktion
  :math:`f(x) = \sqrt{x}` kontinuierlich wächst. Die Werte der
  Ableitungsfunktion werden jedoch immer geringer, das heißt die Wurzelfunktion
  wächst zunehmend langsamer.

  .. figure:: ../../pics/analysis/steigung-wurzelfunktion.png
      :width: 100%
      :align: center
      :name: fig-steigung-wurzelfunktion
      :alt:  fig-steigung-wurzelfunktion

      Funktionsgraph und erste Ableitung (Steigung) der Wurzelfunktion
      :math:`y=\sqrt{x}`.

      .. only:: html

          :download:`SVG: Steigung einer Wurzelfunktion.
          <../../pics/analysis/steigung-wurzelfunktion.svg>`

Die erste Ableitung kann genutzt werden, um differenzierbare Funktionen
auf maximale und/oder minimale Funktionswerte hin zu untersuchen.


.. index:: Extremstelle, Extremwert
.. _Extremstellen:

.. rubric:: Extremstellen

Hat eine Funktion an einer Stelle :math:`x_0` ein lokales Maximum ("Hochpunkt")
oder Minimum ("Tiefpunkt"), so ist an dieser Stelle die Steigung der Funktion
und somit auch die erste Ableitung gleich Null. Der Wert der ersten Ableitung an
einer Stelle :math:`x_0` ist ebenfalls dann gleich Null, wenn die zugehörige
Funktion an dieser Stelle einen so genannten "Terrassenpunkt" besitzt. In allen
drei Fällen spricht man von Extremstellen, die zugehörigen Funktionswerte von
:math:`f(x)` werden Extremwerte genannt.

.. figure:: ../../pics/analysis/hochpunkt-tiefpunkt-terrassenpunkt.png
    :width: 80%
    :align: center
    :name: fig-hochpunkt-tiefpunkt-terrassenpunkt
    :alt:  fig-hochpunkt-tiefpunkt-terrassenpunkt

    Beispiel-Graphen mit einem Hochpunkt, Tiefpunkt oder Terrassenpunkt an der
    Stelle :math:`x_0`.

    .. only:: html

        :download:`SVG: Hochpunkt, Tiefpunkt, Terrassenpunkt
        <../../pics/analysis/hochpunkt-tiefpunkt-terrassenpunkt.svg>`

Um die Extremstelle(n) einer differenzierbaren Funktion zu finden, genügt es
somit, die erste Ableitung zu berechnen und diese gleich Null zu setzen. Löst
man die zugehörige Gleichung, so erhält man die :math:`x`-Werte von allen
Extremstellen. Um zu prüfen, ob es sich bei einer Extremstelle um einen
Hochpunkt, einen Tiefpunkt oder einen Terrassenpunkt handelt, kann man
folgende Fälle prüfen:

* Vor einem Hochpunkt ist die erste Ableitung (Steigung) der Funktion zunächst
  positiv, nach dem Hochpunkt negativ.
* Vor einem Tiefpunkt ist die erste Ableitung (Steigung) der Funktion zunächst
  negativ, nach dem Tiefpunkt positiv.
* Vor und nach einem Terrassenpunkt ist die erste Ableitung der Funktion entweder
  jeweils positiv oder jeweils negativ.

Es genügt also, zu einer gefundenen Extremstelle :math:`x_0` einen Wert
:math:`x < x_0` und einen Wert :math:`x > x_0` in die erste Ableitungsfunktion
einzusetzen und die Vorzeichen der jeweiligen Ergebnisse zu prüfen. Auf diese
Weise untergliedert man letztlich den Definitionsbereich in so genannte
Monotoniebereiche, also Bereiche, in denen die Steigung das gleiche Vorzeichen
hat. Man kann hierfür auch eine Tabelle mit den einzelnen Abschnitten als
Spalten anlegen und dort die Steigungs-Vorzeichen der einzelnen Abschnitte
eintragen. Auch daran kann man die Extremwerte unmittelbar ablesen.

Bisweilen werden auch die einzelnen Hoch- bzw. Tiefpunkte untereinander
verglichen. Der Hochpunkt mit dem größten Funktionswert und der Tiefpunkt mit
dem niedrigsten Funktionswert werden absolute Extremstellen genannt, weitere
Hoch- und Tiefpunkte bezeichnet man als lokale Extremstellen.

.. Mittelwertsatz der Differentialrechnung:

.. index:: Krümmung
.. _Krümmung und zweite Ableitung:

Krümmung und zweite Ableitung
-----------------------------

Will man nicht nur wissen, welche Steigung eine Funktion an einer bestimmten
Stelle aufweist, sondern ist auch daran interessiert, wie schnell sich die
Steigung der Funktion ändert, so kann die erste Ableitung erneut abgeleitet
werden. Auf diese Weise erhält man die zweite Ableitung :math:`f''(x)` der
ursprünglichen Funktion. Sie gibt an, wie schnell sich die Steigungswerte der
Funktion ändern; die Änderung der Steigung wird als "Krümmung" des Graphen
bezeichnet.

Stellt man sich ein Fahrzeug vor, das -- von oben betrachtet -- auf dem Graphen
der Funktion in Richtung zunehmender :math:`x`-Werte entlangfährt, so gibt das
"Lenkverhalten" des Fahrzeugs Aufschluss über die Krümmung der Funktion.

* Legt das Fahrzeug auf seinem Weg entlang des Graphen eine Linkskurve zurück,
  so bezeichnet man die Krümmung der Funktion als positiv.
* Legt das Fahrzeug auf seinem Weg entlang des Graphen eine Rechtskurve zurück,
  so bezeichnet man die Krümmung der Funktion als negativ.
* Kann das Fahrzeug entlang des Graphen ohne zu lenken "geradeaus" fahren, so
  ist die Krümmung des Graphen gleich Null.

In verschiedenen Bereichen der Funktion kann die Krümmung unterschiedlich sein.
Als anschauliche Beispiele eignen sich ebenfalls die einfachen Potenzfunktionen
:math:`f(x) = x^n`.

*Beispiele:*

* Für :math:`n = 1` entspricht :math:`f(x)=x^n` der Ursprungsgeraden :math:`f(x)
  = x^1 = x`. Für die 1. Ableitung :math:`f'(x)` sowie für die 2. Ableitung
  :math:`f''(x)` ergibt sich mit den Gleichungen
  :eq:`eqn-ableitungsregel-potenzfunktion`: und
  :eq:`eqn-ableitungsregel-konstante-funktion`:

  .. math::

      y = f(x) &= x^1 \\[6pt]
      \Rightarrow f'(x) &= 1 = \text{konst.} \\[6pt]
      \Rightarrow f''(x)&= 0

  Da die Steigung einer Geraden an allen Stellen gleich ist, tritt keine
  Krümmung auf: Der Wert der zweiten Ableitung ist -- unabhängig vom
  eingesetzten :math:`x`-Wert -- stets gleich Null.

  .. figure:: ../../pics/analysis/kruemmung-lineare-funktion.png
      :width: 100%
      :align: center
      :name: fig-kruemmung-lineare-funktion
      :alt:  fig-kruemmung-lineare-funktion

      Funktionsgraph, erste und zweite Ableitung (Steigung bzw. Krümmung) der
      linearen Funktion :math:`y=x`.

      .. only:: html

          :download:`SVG: Steigung und Krümmung einer linearen Funktion
          <../../pics/analysis/kruemmung-lineare-funktion.svg>`

* Für :math:`n = 2` entspricht :math:`f(x)=x^n` der Normalparabel :math:`f(x)
  = x^2`. Für die 1. Ableitung :math:`f'(x)` sowie für die 2. Ableitung
  :math:`f''(x)` ergibt sich entsprechend:

  .. math::

      y = f(x) &= x^2 \\[6pt]
      \Rightarrow f'(x) &= 2 \cdot x ^1 \\[6pt]
      \Rightarrow f''(x) &= 2 \cdot x^0 = 2

  Eine Parabel besitzt stets eine konstante Krümmung. Im obigen Beispiel ist die
  Parabel nach oben geöffnet, ihre Krümmung ist positiv. (Ein Fahrzeug müsste --
  von oben betrachtet -- entlang der Parabel eine Linkskurve fahren.)

  .. figure:: ../../pics/analysis/kruemmung-quadratische-funktion.png
      :width: 100%
      :align: center
      :name: fig-kruemmung-quadratische-funktion
      :alt:  fig-kruemmung-quadratische-funktion

      Funktionsgraph, erste und zweite Ableitung (Steigung bzw. Krümmung) der
      Parabelgleichung :math:`y=x^2`.

      .. only:: html

          :download:`SVG: Steigung und Krümmung einer quadratischen Funktion
          <../../pics/analysis/kruemmung-quadratische-funktion.svg>`

* Für :math:`n = 3` gilt :math:`f(x)=x^3`, und für die Ableitungsfunktionen nach
  Gleichung :eq:`eqn-ableitungsregel-potenzfunktion`:

  .. math::

      f(x) &= x^3 \\[6pt]
      \Rightarrow f'(x) &= 3 \cdot x^2 \\[6pt]
      \Rightarrow f''(x) &= 3 \cdot 2 \cdot x^1 = 6 \cdot x

  Die zweite Ableitung :math:`f''(x) = 6 \cdot x` ist links der :math:`y`-Achse
  negativ, was der negativen Krümmung der Funktion in diesem Bereich entspricht.
  Am Punkt :math:`(0;0)` ist die zweite Ableitung gleich Null, an dieser Stelle
  hat die Funktion keine Krümmung. Im Bereich rechts der  :math:`y`-Achse ist
  die zweite Ableitung positiv, was einer Linkskrümmung des Funktionsgraphen
  entspricht.

  .. figure:: ../../pics/analysis/kruemmung-kubische-funktion.png
      :width: 100%
      :align: center
      :name: fig-kruemmung-kubische-funktion
      :alt:  fig-kruemmung-kubische-funktion

      Funktionsgraph, erste und zweite Ableitung (Steigung bzw. Krümmung) der
      kubischen Funktion :math:`y=x^3`.

      .. only:: html

          :download:`SVG: Steigung und Krümmung einer kubischen Funktion
          <../../pics/analysis/kruemmung-kubische-funktion.svg>`

.. rubric:: Extremstellen und zweite Ableitung

Hat man die zweite Ableitung einer Funktion berechnet, so kann auch diese
zur Klassifizierung von Extremstellen genutzt werden. Hierzu genügt es, den
gefundenen Wert :math:`x_0` einer Extremstelle in die zweite Ableitung
einzusetzen:

* Hat das Ergebnis ein positives Vorzeichen, so hat die Funktion an dieser
  Stelle einen Tiefpunkt.
* Hat das Ergebnis im umgekehrten Fall ein positives Vorzeichen, so hat die
  Funktion an dieser Stelle einen Hochpunkt.
* Ist das Ergebnis gleich Null, so hat die Funktion an dieser Stelle einen
  Terrassenpunkt.

Zur Veranschaulichung dieser Zusammenhänge können als elementare Beispiele
wiederum die Graphen der Funktionen :math:`x^2` und :math:`x^3` und ihrer
Ableitungen betrachtet werden.

*Beispiele:*

* Die Funktion :math:`f(x)=x^2` hat an der Stelle :math:`x_0 = 0` eine
  Extremstelle; der Wert ihrer zweiten Ableitung :math:`f''(x) = 2` an dieser
  Stelle ist :math:`f''(0)=2`, es muss sich somit um einen Tiefpunkt handeln.

* Die Funktion :math:`f(x)=x^3` hat an der Stelle :math:`x_0 = 0` eine
  Extremstelle; der Wert ihrer zweiten Ableitung :math:`f''(x)=6 \cdot x` an
  dieser Stelle ist :math:`f''(0)=6 \cdot 0 = 0`, es muss sich somit um einen
  Terrassenpunkt handeln.

Die Methode, die Art der Extremstellen mittels der zweiten Ableitung zu
bestimmen, ist gegenüber der oben genannten Methode effizienter, da nur einmal
ein :math:`x`-Wert in eine Funktion eingesetzt und der zugehörige Funktionswert
berechnet werden muss.


.. _Wendepunkte:

.. rubric:: Wendepunkte

Ändert sich an einer Stelle :math:`x_0` die Krümmung einer Funktion, so ist an
dieser Stelle die zweite Ableitung gleich Null. Diese Bedingung kann genutzt
werden, um so genannte Wendepunkte einer Funktion zu bestimmen.

Um Wendepunkte einer differenzierbaren Funktion zu finden, genügt es somit, die
zweite Ableitung zu berechnen und diese gleich Null zu setzen. Löst man die
zugehörige Gleichung, so erhält man die :math:`x`-Werte aller möglicher
Wendepunkte; durch Einsetzen der :math:`x`-Werte in die ursprüngliche Funktion
erhält man die zugehörigen :math:`y`-Werte. Es muss allerdings -- ähnlich wie
bei :ref:`Extremstellen <Extremstellen>` -- geprüft werden, ob es sich bei den
jeweiligen Stellen tatsächlich um Wendepunkte der Funktion handelt:

* Ist die zweite Ableitung (Krümmung) einer Funktion zunächst negativ und
  anschließend positiv oder umgekehrt, so handelt es sich um einen Wendepunkt.
* Hat die zweite Ableitung (Krümmung) einer Funktion sowohl vor als auch nach
  einer Stelle :math:`x_0` das gleiche Vorzeichen, so ist diese Stelle kein
  Wendepunkt.

Es genügt also, zu einer gefundenen Nullstelle :math:`x_0` der zweiten Ableitung
einen Wert :math:`x < x_0` und einen Wert :math:`x > x_0` in die zweite
Ableitungsfunktion einzusetzen und die Vorzeichen der jeweiligen Ergebnisse zu
prüfen. [#]_


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#] Diese Regel lässt sich mit Hilfe des :ref:`Differentialquotienten
    <Herleitung von Ableitungsregeln>` und der :ref:`allgemeinen binomischen
    Formel <Binomische Formeln>` herleiten. Für :math:`y = f(x) = x^n` lautet
    der Differentialquotient:

    .. math::

        \frac{\mathrm{d}y}{\mathrm{d} x} = \lim _{x \to 0} \left( \frac{(x +
        \Delta x) ^n - x^n}{\Delta x}\right) = \frac{\big(x^n + \binom{n}{1}
        \cdot x^{n-1} \cdot (\Delta x)^1 + \ldots + \binom{n}{n-1} \cdot x^1
        \cdot (\Delta x) ^{n-1} + \binom{n}{n} \cdot (\Delta x)^n\big) -
        x^n}{\Delta x}

    Die beiden :math:`x ^{n}`-Terme heben sich dabei aufgrund des
    unterschiedlichen Vorzeichens auf. Alle verbleibenden Zählerterme enthalten
    :math:`\Delta x` als Faktor, so dass dieser ausgeklammert und gekürzt werden
    kann. Mit dem :ref:`Binomialkoeffizienten <Kombinationen ohne Wiederholung>`
    :math:`\binom{n}{1} = n` folgt:

    .. math::

        \frac{\mathrm{d}y}{\mathrm{d} x} = \lim _{\Delta x \to 0} \left( n
        \cdot x ^{n-1} + \binom{n}{2} \cdot x ^{n-2} \cdot (\Delta x)^1 + \ldots
        +\binom{n}{n-1} \cdot x^1 \cdot (\Delta x) ^{n-2} + (\Delta x)
        ^{n-1}\right)

    Geht in diesem Term :math:`\Delta x` gegen Null, so werden alle Terme, die
    :math:`\Delta x` als Faktor beinhalten, gegenüber dem Term :math:`n \cdot x
    ^{n-1}` vernachlässigbar klein. Das Ergebnis entspricht somit der obigen
    Ableitungsregel für Potenzfunktionen.


.. [#] Dies ist gleichbedeutend damit, dass die Graphen keine "Knicke" besitzen,
    vgl. Abschnitt :ref:`Differenzierbarkeit <Differenzierbarkeit>`.)

.. [#] Sofern die dritte Ableitung der Funktion bereits berechnet
    wurde, kann auch diese genutzt werden, um zu überprüfen, ob es sich bei
    einer Stelle :math:`x_0` um einen Wendepunkt handelt: Setzt man diesen Wert
    in die dritte Ableitung ein und ist das Ergebnis ungleich Null, so handelt
    es sich um einen Wendepunkt.

    Ist die dritte Ableitung an der untersuchten Stelle :math:`f'''(x_0) = 0`,
    so kann ein Wendepunkt jedoch nicht ausgeschlossen werden! Die oben genannte
    Methode ist also für die Bestimmung von Wendepunkten zu bevorzugen.



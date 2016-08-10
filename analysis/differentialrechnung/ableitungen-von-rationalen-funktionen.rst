.. index:: Ableitung; von rationalen Funktionen
.. _Ableitungen von ganz- und gebrochenrationalen Funktionen:

Ableitungen von ganz- und gebrochenrationalen Funktionen
========================================================


.. _Ableitungen von ganzrationalen Funktionen:

Ableitungen von ganzrationalen Funktionen
-----------------------------------------

Eine ganzrationale Funktion hat allgemein folgende Form:

.. math::

    f(x) = \sum_{i=0}^{n} a_i \cdot x^i = a_{\mathrm{n}} \cdot x^n +
    a_{\mathrm{n-1}} \cdot x ^{n-1} + \ldots + a_3 \cdot x^3 + a_2 \cdot x^2 +
    a_1 \cdot x^1 + a_0

Um die Ableitung einer solchen Funktion zu bestimmen, müssen folgende zwei
Ableitungsregeln verwendet werden:

* Wird eine Funktion :math:`f(x)` mit einem konstanten Faktor :math:`c`
  multipliziert, so bleibt dieser Faktor beim Ableiten unverändert erhalten.
  Für die Ableitung gilt somit:

  .. math::

      \big( c \cdot f(x) \big)' = c \cdot f'(x)

  Ist :math:`c` negativ, so ist die Funktion gegenüber der ursprünglichen
  Funktion an der :math:`x`-Achse gespiegelt. In diesem Fall hat auch die
  Steigung ein umgekehrtes Vorzeichen.

* Besteht eine Funktion :math:`f(x)` aus einer Summe von Einzelfunktionen
  :math:`f_1(x),\,f_2(x),\, \ldots`, so ist die Ableitung gleich der Summe der
  Ableitungen der Einzelfunktion. Es gilt also:

  .. math::

      \big( f_1(x) + f_2(x) \big)' = f_1'(x) + f_2'(x)

Mit den obigen Regeln und den :ref:`Ableitungsregeln für Potenzfunktionen
<Ableitungen von Potenz- und Wurzelfunktionen>` ergibt sich somit für die erste
Ableitung einer ganzrationalen Funktion :math:`n`-ten Grades:

.. math::

    f'(x) = n \cdot a_n \cdot x ^{n-1} + (n-1) \cdot a_{\mathrm{n-1}} \cdot x
    ^{n-2} + \ldots + 3 \cdot a_3 \cdot x^2 + 2 \cdot a_2 \cdot x^1 + a_1

Die Ableitung einer ganzrationalen Funktion :math:`n`-ten Grades ist somit eine
ganzrationale Funktion :math:`(n-1)`-ten Grades. Leitet man die Funktion ein
zweites mal ab, so wird der Grad der Ableitungsfunktion wiederum um :math:`1`
niedriger. Für die zweite Ableitung gilt entsprechend:

.. math::

    f''(x) = n \cdot (n-1) \cdot a_n \cdot x ^{n-2} + (n-1) \cdot (n-2) \cdot
    a_{\mathrm{n-1}} \cdot x^{n-3} + \ldots + 3 \cdot 2 \cdot a_3 \cdot x^1 + 2
    \cdot a_2

Insgesamt lässt sich eine ganzrationale Funktion :math:`n`-ten Grades also
:math:`n` mal ableiten; alle weiteren Ableitungen sind gleich Null.

.. _Ableitungen von gebrochenrationalen Funktionen:

Ableitungen von gebrochenrationalen Funktionen
----------------------------------------------

Eine :ref:`gebrochenrationale Funktion <Gebrochenrationale Funktionen>` hat
allgemein folgende Form:

.. math::

    f(x) = \frac{Z(x)}{N(x)} = \frac{\sum_{i=0}^{n} a_i \cdot x^i}{\sum_{k=0}^{m}
    b_k \cdot x^k} = \frac{a_{\mathrm{n}} \cdot x^n + a_{\mathrm{n-1}} \cdot x
    ^{n-1} +\ldots + a_2 \cdot x^2 + a_1 \cdot x + a_0}{b_{\mathrm{m}} \cdot x^m
    +b_{\mathrm{m-1}} \cdot x ^{m-1} + \ldots + b_2 \cdot x^2 + b_1 \cdot x +
    a_0}

Gebrochenrationale Funktionen bestehen also aus einem Zählerpolynom :math:`Z(x)`
mit Grad :math:`n` und einem Nennerpolynom :math:`N(x)` mit Grad :math:`m`; die
Grade des Zählerpolynoms und des Nennerpolynoms unterscheiden sich also um
:math:`n-m`. Um eine solche Funktion ableiten zu können, muss eine weitere
Ableitungsregel verwendet werden:

* Besteht eine Funktion :math:`f(x)` aus einem Quotienten zweier
  Einzelfunktionen :math:`f_1(x)` und :math:`f_2(x)`, so lässt sich die
  Ableitung von :math:`f(x)` nach folgender Regel berechnen:

  .. math::

      \left(\frac{f_1(x)}{f_2(x)}\right)' = \frac{f_1'(x) \cdot f_2(x) - f_1(x)
      \cdot f_2'(x)}{\big(f_2(x)\big)^2}

Für die Ableitung einer gebrochenrationalen Funktion gilt also:

.. math::
    :label: eqn-ableitung-gebrochenrationaler-funktionen

    f'(x) = \frac{Z'(x) \cdot N(x) - N'(x) \cdot Z}{\big(N(x)\big)^2}

Die Ableitungen des Zähler- bzw. Nennerpolynoms werden dabei gemäß den Regeln
für Ableitungen ganzrationaler Funktionen gebildet. Das Ergebnis ist hierbei
wiederum eine gebrochenrationale Funktion, wobei sich die Grade des
Zählerpolynoms und des Nennerpolynoms der Ableitung um  :math:`n-m-1`
unterscheiden.

Echt gebrochen-rationale Funktionen mit :math:`n < m` lassen sich somit
unbegrenzt oft ableiten, wobei die einzelnen Ableitungen niemals gleich Null
sind.


.. _Ableitungen von Hyperbelfunktionen:

.. rubric:: Ableitungen von Hyperbelfunktionen

:ref:`Hyperbeln <Hyperbeln>`, also Funktionen der Form :math:`f(x) =
\frac{1}{x^n}`, sind der einfachste Sonderfall von gebrochenrationalen
Funktionen. Für ihre Ableitung gilt:

.. math::

    \left( \frac{1}{x^n}\right)' = \frac{0 \cdot x^n - n \cdot x ^{n-1} \cdot
    1}{\left(x ^{n}\right)^2} = \frac{- n \cdot x ^{n-1}}{x ^{2 \cdot n}} = - n
    \cdot x ^{(n-1) - 2 \cdot n} = -n \cdot x ^{-n -1}

Schreibt man für die Hyperbelfunktion :math:`f(x) = \frac{1}{x^n} = x ^{-n}`,
so zeigt sich, dass die Ableitungen entsprechend der :ref:`Ableitungsregel für
Potenzfunktionen <Ableitungen von Potenz- und Wurzelfunktionen>` gebildet werden
können:

.. math::
    :label: eqn-ableitung-von-hyperbelfunktionen

    \left( x^{-n} \right)' = -n \cdot x ^{-n -1}

Die Ableitungsregel für Potenzfunktionen gilt also nicht nur für positive
rationale Werte von :math:`n`, sondern allgemein für negative ganzzahlige Werte
von :math:`n`.


.. _Ableitungen von Potenzfunktionen mit rationalem Exponenten:

.. rubric:: Ableitungen von Potenzfunktionen mit rationalem Exponenten

Um zu zeigen, dass die Ableitungsregel für Potenzfunktionen allgemein für
jede rationale Zahl :math:`n = \frac{p}{q}` mit :math:`p,q \in \mathbb{Z}`
gilt, muss eine weitere Ableitungsregel verwendet werden:

* Besteht eine Funktion :math:`f(x)` aus einer :ref:`Verkettung zweier
  Einzelfunktionen <Verknüpfung und Verkettung von Funktionen>` :math:`f_1(x)`
  und :math:`f_2(x)`, so lässt sich die Ableitung von :math:`f(x)` nach
  der so genannten "Kettenregel" berechnen:

  .. math::

      \Big(f_1\big(f_2(x)\big)\Big)' = \Big(f_1'\big(f_2(x)\big)\Big) \cdot f_2'(x)

  Dabei wird zunächst die äußere Funktion abgeleitet, die innere Funktion
  bleibt dabei unverändert. Anschließend wird der sich ergebende Term mit der
  Ableitung der inneren Funktion multipliziert.

Für die Ableitung einer Potenzfunktion :math:`f(x) = x ^{\frac{p}{q}}` mit
rationalem Exponenten :math:`n = \frac{p}{q}` gilt damit:

.. math::

    \left( x ^{\frac{p}{q}}\right)' = \left(\left( x ^{\tiny{p}}\right) ^{\frac{1}{q}}\right)'
    &= \frac{1}{q} \cdot \left( x ^{p}\right) ^{\left(\frac{1}{q} - 1\right)}
    \cdot p \cdot x ^{(p-1)} \\
    & = \frac{p}{q} \cdot x ^{p \cdot \left( \frac{1}{q} - 1\right)} \cdot x
    ^{(p-1)} \\
    &= \frac{p}{q} \cdot x ^{\left( \frac{p}{q} - p\right) + (p - 1)} \\
    &= \frac{p}{q} \cdot x ^{\left(\frac{p}{q} - 1 \right)} \qquad \checkmark

Hierbei werden die :ref:`Rechenregeln für Potenzen und Wurzeln <Rechenregeln für
Potenzen und Wurzeln>` genutzt und :math:`f_1(x)=x ^{\frac{1}{q}}` als "äußere"
sowie :math:`f_2(x)=x^p` als "innere" Funktion interpretiert. Beim Ableiten der
äußeren Funktion bleibt die innere Funktion als eigener Term unverändert. Das
Ergebnis wird anschließend mit der Ableitung der inneren Funktion multipliziert,
was umgangssprachlich als "Nachdifferenzieren" bezeichnet wird. Ein
Zusammenfassen der einzelnen Terme führt schließlich zum gesuchten Endergebnis.




.. _Ableitungen von Exponential- und Logarithmusfunktionen:

Ableitungen von Exponential- und Logarithmusfunktionen
======================================================

.. index:: Ableitung; von Exponentialfunktionen

.. _Ableitungen von Exponentialfunktionen:

Ableitungen von Exponentialfunktionen
-------------------------------------

Eine Ableitungsregel für :ref:`Exponentialfunktionen <Exponentialfunktionen>`
kann mit Hilfe des :ref:`Differentialquotienten <Herleitung von
Ableitungsregeln>` hergeleitet werden. Für eine Exponentialfunktion :math:`f(x)
= a^x` gilt:

.. math::

    f'(x) = \frac{\mathrm{d} f(x)}{\mathrm{d} x} = \lim _{\Delta x \to 0}
    \left(\frac{f(x + \Delta x)-f(x)}{\Delta x} \right) = \lim _{\Delta x \to 0}
    \left( \frac{a ^{(x + \Delta x)} - a ^x}{\Delta x}\right)

Mit Hilfe der :ref:`Rechenregeln für Potenzen <Rechenregeln für Potenzen mit
gleicher Basis>` kann dieser Term weiter umgeformt werden. Es folgt:

.. math::

    f'(x) = \lim _{\Delta x \to 0} \left( \frac{a ^{(x + \Delta x)} - a
    ^x}{\Delta x}\right) = \lim _{\Delta x \to 0} \left( \frac{a ^x + a ^{\Delta
    x} - a^x}{\Delta x}\right) = \lim _{\Delta x \to 0} \left( \frac{a ^{\Delta
    x} - 1}{\Delta x}\right) \cdot a ^{x}

Die Ableitung einer Exponentialfunktion ist somit wieder eine
Exponentialfunktion, die mit einem konstanten, jedoch von der Basis :math:`a`
abhängigen Faktor multipliziert wird. Es lässt sich ein bestimmter Wert
:math:`a_0` finden, für den der genannte Faktor gleich :math:`1` ist. Hierfür
muss gelten:

.. math::

    \lim _{\Delta x \to 0}  \left( \frac{a_0 ^{\Delta x} - 1}{\Delta x} \right)
    = 1 \quad \Longleftrightarrow \quad a_0 = \lim _{\Delta x \to 0}  \left( 1 +
    \Delta x \right)^{\frac{1}{\Delta x}}

.. index:: Eulersche Zahl

Dieser Grenzwert entspricht formal dem Grenzwert einer Folge :math:`\lim _{t \to
0} (1 + t) ^{\frac{1}{t}}` reeller Zahlen. Dieser Grenzwert konnte erstmals von
`Leonhard Euler <https://de.wikipedia.org/wiki/Leonhard_Euler>`_ bestimmt
werden und wird zu dessen Ehren "Eulersche Zahl" :math:`e` genannt:

.. math::

    e = \lim _{t \to 0} (1 + t) ^{\frac{1}{t}} = 2,718281\ldots

Diese Zahl ist irrational und für die Mathematik von ähnlicher Bedeutung wie
die Kreiszahl :math:`\pi`: Ist nämlich die Eulersche Zahl :math:`e` Basis einer
Exponentialfunktion, ist also :math:`f(x) = e^x`, so ist die Ableitungsfunktion
mit der ursprünglichen Funktion identisch, es gilt in diesem Fall also:

.. math::
    :label: eqn-ableitungsregel-natuerliche-exponentialfunktion

    f(x) = e^x \quad \rightarrow \quad f'(x) = e^x

Die Funktion :math:`f(x) = e^x` wird mitunter auch als "natürliche"
Exponentialfunktion bezeichnet.

Für beliebige Exponentialfunktionen lässt sich eine Ableitungsregel herleiten,
indem man ausnutzt, dass Exponential- und Logarithmusfunktionen bei gleicher
Basis :math:`a` zueinander Umkehrfunktionen sind, also beispielsweise :math:`e
^{\ln{(a)}} = a` gilt. Für eine allgemeine Exponentialfunktion kann folglich
geschrieben werden:

.. math::

    f(x) = a ^{x} = (e ^{\ln{(a)}})^x = e ^{x \cdot \ln{(a)}}

Um diese Funktion ableiten zu können, muss -- wie schon im Abschnitt
:ref:`Ableitungen von Potenzfunktionen mit rationalem Exponenten <Ableitungen
von Potenzfunktionen mit rationalem Exponenten>` die so genannte "Kettenregel"
genutzt werden:

* Die Ableitung einer verketteten Funktion :math:`f(x) = f_1\big(f_2(x)\big)`
  ist gleich der Ableitung der äußeren Funktion multipliziert mit der
  Ableitung der inneren Funktion:

  .. math::

      \Big(f_1\big(f_2(x)\big)\Big)' = \Big(f_1'\big(f_2(x)\big)\Big) \cdot f_2'(x)

  Beim Ableiten der äußeren Funktion wird die innere Funktion dabei
  unverändert gelassen.

Für die obige Gleichung :math:`f(x) = e ^{x \cdot \ln{(a)}}` entspricht
:math:`f_1(x) = e ^{x}` der äußeren und :math:`f_2=\ln{(a)} \cdot x` der
inneren Funktion. Da :math:`\ln{(a)} = \text{konstant}` ist, gilt: [#]_

.. math::

    f'(x) = \underbrace{e ^{x \cdot \ln{(a)}}}_{\text{Ableitung der äußeren
    Funktion}} \cdot \underbrace{\ln{(a)}}_{\text{Ableitung der inneren Funktion}}

Die natürliche Exponentialfunktion als äußere Funktion bleibt hierbei
unverändert, die Ableitung der inneren Funktion :math:`f_2 = \ln{(a)} \cdot x =
c \cdot x` ergibt den Wert :math:`f_2'(x) = \ln{(a)}`. Für
Exponentialfunktionen mit beliebiger Basis :math:`a` gilt also:

.. math::
    :label: eqn-ableitungsregel-exponentialfunktion

    f(x) = a ^{x} \quad \Rightarrow \quad f'(x) = \ln{(a)} \cdot a^x

In dieser Formel ist wegen :math:`\ln{(e)} = 1` der Sonderfall für die natürliche
Exponentialfunktion enthalten.


.. index:: Ableitung; von Logarithmusfunktionen
.. _Ableitungen von Logarithmusfunktionen:

Ableitungen von Logarithmusfunktionen
-------------------------------------

Um eine Ableitungsregel für Logarithmusfunktionen herzuleiten, wird eine
weitere, als "Umkehrregel" bezeichnete Ableitungsregel verwendet:

* Die Ableitung :math:`\frac{\mathrm{d} y}{\mathrm{d} x}` einer Funktion
  :math:`y=f(x)` ist gleich dem Kehrwert der Ableitung ihrer Umkehrfunktion
  :math:`f _{\rm{u}}(y)`:

  .. math::

      \frac{\mathrm{d} y}{\mathrm{d} x} = \frac{1}{\frac{\mathrm{d}
      x}{\mathrm{d} y}} \quad \text{beziehungsweise} f'(x) = \frac{1}{f
      _{\rm{u}}'(y)}

Im Fall einer Logarithmusfunktion ist :math:`y = f(x) = \log_{a}{(x)}` und, wenn
man beide Seiten als Potenz zur Basis :math:`a` schreibt, :math:`x = f
_{\rm{u}}(y) = a ^{y}` . Somit gilt nach der Ableitungsregel
:eq:`eqn-ableitungsregel-exponentialfunktion` für Exponentialfunktionen:

.. math::

    f _{\rm{u}}'(y) = \frac{\mathrm{d} x}{\mathrm{d} y} = \ln{(a)} \cdot a ^{y}
    = \ln{(a)} \cdot x

Für die Ableitung der Logarithmusfunktion gilt schließlich:

.. math::
    :label: eqn-ableitungsregel-logarithmusfunktion

    f(x) = \log_{a}{(x)} \quad \Rightarrow \quad f'(x) = \frac{1}{\ln{(a)} \cdot x}

Im Sonderfall der natürlichen Logarithmusfunktion :math:`\ln{(x)} =
\log_{e}{(x)}` ist :math:`\ln{(e)}=1` und somit:

.. math::
    :label: eqn-ableitungsregel-natuerliche-logarithmusfunktion

    f(x) = \ln{(x)} \quad \Rightarrow \quad f'(x) = \frac{1}{x}

Alle weiteren Ableitungen der Logarithmusfunktion lassen sich dann gemäß den
:ref:`Ableitungsregeln für gebrochenrationalen Funktionen <Ableitungen von
gebrochenrationalen Funktionen>` bestimmen.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Um sich die Wirkung der Kettenregel im Detail vorstellen zu können, kann
    man an dieser Stelle auch :math:`z = x \cdot \ln(a)` schreiben. Die äußere
    Funktion ist dann :math:`f_1(z) = e ^{z}`, deren Ableitung :math:`f_1'(z) =
    e ^{z} = e ^{x \cdot \ln{(a)}}` ist.



.. _Zusammenfassung wichtiger Ableitungsregeln:

Zusammenfassung wichtiger Ableitungsregeln
==========================================

Im folgenden sind die wichtigsten Ableitungsregeln der vorherigen Abschnitte
nochmals kurz zusammengefasst.

.. index:: Ableitungsregeln

.. _Allgemeine Ableitungsregeln:

Allgemeine Ableitungsregeln
---------------------------

Die folgenden Ableitungsregeln sind allgemein für beliebige Funktionen gültig:

* Lässt sich eine Funktion :math:`f(x)` als Summe einer anderen Funktion
  :math:`f _{\rm{1}}(x)` mit einem konstanten Summanden :math:`c` darstellen, so
  ist ihre Ableitungsfunktion :math:`f'(x)` mit der Ableitung :math:`f
  _{\rm{1}}'(x)` der anderen Funktion identisch: 

  .. math::
      :label: eqn-ableitungsregel-konstanter-wert
      
      f _{\rm{1}}(x) = f _{\rm{2}}(x) + c \quad \Rightarrow \quad f _{\rm{1}}'(x)
      = f _{\rm{2}}'(x) {\color{white} +c}

  Insbesondere ist die Ableitung beziehungsweise Steigung einer konstanten
  Funktion :math:`f(x) = c` gleich Null.

* Lässt sich eine Funktion :math:`f _{\rm{1}}(x)` als Produkt einer anderen
  Funktion :math:`f _{\rm{2}}(x)` mit einem konstanten Faktor :math:`c`
  darstellen, so entspricht ihre Ableitungsfunktion :math:`f _{\rm{1}}'(x)`
  derjenigen der anderen Funktion :math:`f _{\rm{2}}(x)`, wenn diese mit dem
  gleichen Faktor :math:`c` multipliziert wird. 

  .. math::
      :label: eqn-ableitungsregel-konstanter-faktor
      
      f_1(x) = c \, \cdot \; f _2(x) \quad \Rightarrow \quad f_{1}'(x) = c \cdot f_{2}'(x)

Für jede beliebige Funktion :math:`f(x)`, die man sich aus zwei Teilfunktionen
:math:`f _{\rm{1}}(x)` und :math:`f _{\rm{2}}(x)` zusammengesetzt denken kann,
sind folgende Ableitungsregeln nützlich: 

.. _Additionsregel:

.. index:: Ableitungsregeln; Additionsregel

* Additionsregel:

  Besteht eine Funktion :math:`f(x)` aus einer Summe zweier Teilfunktionen
  :math:`f_1(x)` und :math:`f_2(x)`, so gilt für ihre Ableitung :math:`f'(x)`:

  .. math::
      :label: eqn-additionsregel
      
      \left[ f _{\rm{1}}(x) + f _{\rm{2}}(x) \right]' = f _{\rm{1}}'(x) + f
      _{\rm{2}}'(x) {\color{white} \quad \;\; \ldots}


.. index:: Ableitungsregeln; Produktregel
.. _Produktregel:

* Produktregel:

  Besteht eine Funktion :math:`f(x)` aus einem Produkt zweier Teilfunktionen
  :math:`f_1(x)` und :math:`f_2(x)`, so gilt für ihre Ableitung :math:`f(x)`:

  .. math::
      :label: eqn-produktregel
      
      {\color{white} \ldots \quad \qquad} \left[ f _{\rm{1}}(x) \, \cdot \; f _{\rm{2}}(x) \right]' = f _{\rm{1}}'(x)
      \, \cdot \; f _{\rm{2}}(x) \, + \, f _{\rm{2}}'(x) \, \cdot \; f _{\rm{1}}(x)


.. index:: Ableitungsregeln; Quotientenregel
.. _Quotientenregel:

* Quotientenregel:

  Besteht eine Funktion :math:`f(x)` aus einem Quotienten zweier Teilfunktionen
  :math:`f_1(x)` und :math:`f_2(x)`, so gilt für ihre Ableitung :math:`f(x)`:

  .. math::
      :label: eqn-quotientenregel
      
      {\color{white} \ldots \qquad \qquad \quad \;\;\, } \left[ \frac{f _{\rm{1}}(x)}{f _{\rm{2}}(x)}
      \right]' = \frac{f _{\rm{1}}'(x) \, \cdot \; f _{\rm{2}}(x) \, - \, f
      _{\rm{2}}'(x) \, \cdot \; f _{\rm{1}}(x)}{ \left( f _{\rm{2}}(x)
      \right)^2} 


.. index:: Ableitungsregeln; Kettenregel
.. _Kettenregel:

* Kettenregel

  Besteht eine Funktion :math:`f(x)` aus einer :ref:`Verkettung <Verknüpfung und
  Verkettung von Funktionen>` zweier Teilfunktionen :math:`f_1(x)` und
  :math:`f_2(x)`, so gilt für ihre Ableitung :math:`f(x)`:

  .. math::
      :label: eqn-kettenregel
      
      \left[ f _{\rm{1}}\big(f _{\rm{2}}(x)\big) \right]' = f _{\rm{1}}'\big(f
      _{\rm{2}}(x)\big) \, \cdot \; f _{\rm{2}}'(x) 

  Hierbei wird zunächst die Ableitung :math:`f_1'` der äußeren Funktion
  gebildet, wobei die innere Funktion unverändert gelassen wird. Der
  resultierende Term wird anschließend mit der Ableitung der inneren Funktion
  multipliziert. 

.. index:: Satz von Rolle
.. _Satz von Rolle und Mittelwertsatz:
  
Satz von Rolle und Mittelwertsatz
---------------------------------

Ist eine Funktion :math:`f(x)` in einem Intervall :math:`]a;b[` stetig
differenzierbar und gilt zudem :math:`f(a) = f(b)`, so existiert mindestens eine
Stelle :math:`x_0` innerhalb des Intervalls, für die
:math:`f'(x_0) = 0` gilt. Dieser Zusammenhang wird "Satz von `Rolle
<https://de.wikipedia.org/wiki/Michel_Rolle>`_" genannt. 

.. todo pic

Anschaulich bedeutet der Satz von Rolle, dass es entlang eines stetig
verlaufenden Graphen zwischen zwei Kurvenpunkten mit übereinstimmenden
:math:`y`-Werten mindestens einen Punkt gibt, an dem der Graph eine waagrechte
Tangente (Steigung Null) besitzt; insbesondere muss sich damit zwischen zwei
Nullstellen einer stetigen Funktion stets eine Extremstelle befinden.

.. index:: Mittelwertsatz

Der Satz von Rolle kann auch allgemeiner formuliert werden: Ist eine Funktion
:math:`f(x)` in einem Intervall :math:`]a;b[` stetig differenzierbar, so
existiert mindestens eine Stelle :math:`x_0` innerhalb des Intervalls, für die
gilt:

.. math::
    
    f'(x_0) = \frac{f(b)-f(a)}{b-a}

Dieser so genannte Mittelwertsatz besagt anschaulich, dass es entlang eines
stetig verlaufenden Graphen zwischen zwei Kurvenpunkten stets (mindestens) einen
Punkt :math:`x_0` gibt, dessen Tangentensteigung gleich der Steigung der durch
:math:`f(a)` und :math:`f(b)` verlaufenden Sekante ist. Der Mittelwertsatz kann
somit als Erweiterung des Satzes von Rolle aufgefasst werden, da er diesen für
:math:`f(a) = f(b)` als Sonderfall enthält.



.. _Ableitungsregeln wichtiger Funktionen:

Ableitungsregeln wichtiger Funktionen
-------------------------------------

.. list-table:: 
    :name: tab-ableitungsregeln
    :widths: 60 20 40 50

    * - Bezeichnung
      - :math:`f(x)`
      - :math:`f'(x)`
      - Bedingung(en)
    * - Potenzfunktion 
      - :math:`x^n`
      - :math:`n \cdot x ^{n-1}`
      - :math:`n \in \mathbb{R}`
    * - Exponentialfunktion
      - :math:`a ^{x}`
      - :math:`a ^{x} \cdot \ln{(a)}`
      - :math:`a > 0`, :math:`a \ne 1`
    * - Natürliche Exponentialfunktion
      - :math:`e ^{x}`
      - :math:`e ^{x}`
      - 
    * - Logarithmusfunktion
      - :math:`\log{(x)}`
      - :math:`\frac{1}{x \cdot \ln{(a)}}`
      - :math:`x > 0,\, a > 0,\, a \ne 1`
    * - Natürliche Logarithmusfunktion
      - :math:`\ln{(x)}`
      - :math:`\frac{1}{x}`
      - :math:`x > 0`
    * - Sinusfunktion
      - :math:`\sin{(x)}`
      - :math:`\cos{(x)}`
      - 
    * - Cosinusfunktion
      - :math:`\cos{(x)}`
      - :math:`-\sin{(x)}`
      - 
    * - Tangensfunktion
      - :math:`\tan{(x)}`
      - :math:`\frac{1}{\cos^2{(x)}} = 1 + \tan^2{(x)}`
      - :math:`x \ne (2\!\cdot\!n + 1) \cdot \frac{\pi}{2}` mit :math:`n \in \mathbb{N}`
    * - Cotangensfunktion
      - :math:`\cot{(x)}`
      - :math:`-\frac{1}{\sin ^2{(x)}} = -\left(1 + \cot^2{(x)}\right)`
      - :math:`x \ne n \cdot \pi` mit :math:`n \in \mathbb{N}`


..  
    * - Arcussinus
      - :math:`\text{asin}(x)`
      - :math:`\frac{1}{\sqrt{1 - x^2}}`
      -
    * - Arcuscosinus
      - :math:`\text{acos}(x)`
      - :math:`\frac{-1}{\sqrt{1 - x^2}}`
      -
    * - Arcustangens
      - :math:`\text{atan}(x)`
      - :math:`\frac{1}{1 + x^2}`
      -
    * - Arcuscotangens
      - :math:`\text{acot}(x)`
      - :math:`\frac{-1}{1 + x^2}`
      -
    * - Sinus hyperbolicus
      - :math:`\text{sinh}(x)`
      - :math:`\text{cosh}(x)`
      -
    * - Cosinus hyperbolicus
      - :math:`\text{cosh}(x)`
      - :math:`\text{sinh}(x)`
      -
    * - Tangens hyperbolicus
      - :math:`\text{tanh}(x)`
      - :math:`\frac{1}{\text{cosh}^2(x)}`
      -
    * - Cotangens hyperbolicus
      - :math:`\text{coth}(x)`
      - :math:`\frac{-1}{\text{sinh}^2(x)}`
      -
    * - Arcussinus hyperbolicus
      - :math:`\text{asinh}(x)`
      - :math:`\frac{1}{\sqrt{x^2 + 1}}`
      -
    * - Arcuscosinus hyperbolicus
      - :math:`\text{acosh}(x)`
      - :math:`\frac{1}{\sqrt{x^2 - 1}}`
      - :math:`x > 1`
    * - Arcustangens hyperbolicus
      - :math:`\text{atanh}(x)`
      - :math:`\frac{1}{1-x^2}`
      - :math:`|x| < 1`
    * - Arcuscotangens hyperbolicus
      - :math:`\text{acoth}(x)`
      - :math:`\frac{1}{1-x^2}`
      - :math:`|x| > 1`






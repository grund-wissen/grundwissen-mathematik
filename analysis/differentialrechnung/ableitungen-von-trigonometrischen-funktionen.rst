.. index:: Ableitung; von trigonometrischen Funktionen
.. _Ableitungen von trigonometrischen Funktionen:

Ableitungen von trigonometrischen Funktionen
============================================

Im folgenden sollen die Ableitungen der :ref:`trigonometrischen Funktionen
<Trigonometrische Funktionen>` :math:`\sin{(x)}`, :math:`\cos{(x)}`,
:math:`\tan{(x)}` und :math:`\cot{(x)}` hergeleitet werden.


.. _Ableitung der Sinusfunktion:

.. rubric:: Ableitung der Sinusfunktion

Um eine Ableitungsregel für die Sinusfunktion :math:`y=f(x) = \sin{(x)}`
herzuleiten, geht man von :ref:`Differentialquotienten <Herleitung von
Ableitungsregeln>` :math:`\frac{\mathrm{d} y}{\mathrm{d} x}` aus. Dieser lautet
für die Sinusfunktion:

.. math::
    
    \frac{\mathrm{d} y}{\mathrm{d} x} = \lim _{\Delta x \to 0} \left(
    \frac{\sin{(x + \Delta x)} - \sin{(x)}}{\Delta x}\right)

Mittels des :ref:`Additionstheorems <Additionstheoreme>` :math:`\sin{(x_1)} -
\sin{(x_2)} = 2 \cdot \cos{\left(\frac{x_1 + x_2}{2}\right)} \cdot
\sin{\left(\frac{x_1 -x_2}{2}\right)}` kann der Zählerterm folgendermaßen
umgeschrieben werden:

.. only:: html

    .. math::
        
        \sin{(x + \Delta x)} - \sin{(x)} = 2 \cdot \cos{\left(\frac{(x + \Delta x) +
        x}{2}\right)} \cdot \sin{\left( \frac{(x + \Delta x) - x}{2}\right)} = 2
        \cdot \cos{\left(x + \frac{\Delta x}{2}\right)} \cdot \sin{\left(
        \frac{\Delta x}{2}\right)}

.. only:: latex
    
    .. math::
        
        \sin{(x + \Delta x)} - \sin{(x)} &= 2 \cdot \cos{\left(\frac{(x + \Delta
        x) + x}{2}\right)} \cdot \sin{\left( \frac{(x + \Delta x) -
        x}{2}\right)} \\ &= 2 \cdot \cos{\left(x + \frac{\Delta x}{2}\right)}
        \cdot \sin{\left( \frac{\Delta x}{2}\right)}

Damit kann der Differentialquotient in folgender Form geschrieben werden:

.. math::
    
    \frac{\mathrm{d} y}{\mathrm{d} x} = \lim _{\Delta x \to 0} \left( \frac{2
    \cdot \cos{\left(x + \frac{\Delta x}{2}\right)} \cdot \sin{\left(
    \frac{\Delta x}{2}\right)} }{\Delta x}\right) = \lim _{\Delta x \to 0}
    \left( \cos{\left(x + \frac{\Delta x}{2}\right)} \cdot \frac{\sin{\left(
    \frac{\Delta x}{2}\right)}}{\frac{\Delta x}{2}}\right)
    
Im letzten Rechenschritt wurde der Faktor :math:`2` in Form eines Doppelbruchs
in den Nenner gezogen, um die Form auf der rechten Seite zu erhalten. Der
Differentialquotient ist als Grenzwert eines Produkts zweier Funktionen gemäß
den :ref:`Rechenregeln für Grenzwerte <Rechenregeln für Grenzwerte>` gleich dem
Produkt der Grenzwerte beider Funktionen. Für den Grenzwert des ersten Faktors
gilt: 

.. math::
    
    \lim _{\Delta x \to 0} \left( \cos{\left( x + \frac{\Delta
    x}{2}\right)}\right) = \cos{(x)}

Der Grenzwert des zweiten Faktors kann zur besseren Lesbarkeit als :math:`\lim
_{z \to 0} \left(\frac{\sin{(z)}}{z} \right)` mit :math:`z = \frac{\Delta x}{2}`
geschrieben werden. Um diesen Grenzwert für kleine Werte von :math:`z`
abzuschätzen, kann man die Sinusfunktion mit der Cosinus- und der
Tangensfunktion vergleichen. Dabei gilt mit :math:`\tan{(z)} =
\frac{\sin{(z)}}{\cos{(z)}}`:

.. math::
    
    \sin{(z)} < z < \tan{(z)} \qquad \Leftrightarrow \qquad 1 <
    \frac{z}{\sin{(z)}} < \frac{1}{\cos{(z)}} \qquad \Leftrightarrow \qquad 1 >
    \frac{\sin{(z)}}{z} > \cos{(z)}
    
Im ersten Rechenschritt wurde durch :math:`\sin{(z)}` dividiert, im zweiten
wurden die Kehrwerte der Terme betrachtet, wobei sich die Ungleichheitszeichen
umkehren. Wegen :math:`\lim _{z \to 0} \cos{(z)} = 1` wird die Ungleichung zu
:math:`1 > \lim _{z \to 0} \frac{\sin{(z)}}{z} > 1`, also muss  gelten: 

.. math::
    
    \lim _{z \to 0} \frac{\sin{(z)}}{z} =1 

Für die Ableitung der Sinus-Funktion folgt damit:

.. math::
    :label: eqn-ableitungsregel-sinusfunktion
    
    f(x) = \sin{(x)} \quad \Rightarrow \quad f'(x) = \cos{(x)}

Die Ableitung der Sinus-Funktion ist also gleich der Cosinus-Funktion.


.. _Ableitung der Cosinusfunktion:

.. rubric:: Ableitung der Cosinusfunktion

Die Ableitung der Cosinus-Funktion kann mit Hilfe der Ableitungsregel der
Sinusfunktion anhand des Zusammenhangs :math:`\cos{(x)} = \sin{\left(-x +
\frac{\pi}{2}\right)}` bestimmt werden; dabei wird wiederum die
:ref:`Kettenregel <Kettenregel>` verwendet. Mit :math:`f_1(x) = \sin{(x)}` als
der äußeren und :math:`f_2 = -x + \frac{\pi}{2}` als der inneren Funktion gilt:

.. math::
    
    \big(\cos{(x)}\big)' = \left(\sin{\left( -x + \frac{\pi}{2} \right)}\right)'
    = \underbrace{\cos{\left(-x + \frac{\pi}{2} \right)}}_{\text{Ableitung der
    äußeren Funktion}} \cdot
    \underbrace{\phantom{\frac{\pi}{2}}(-1)\phantom{\frac{\pi}{2}}}_{\text{Ableitung
    der inneren Funktion}}

Da :math:`\cos{\left(-x + \frac{\pi}{2}\right)} = \sin{(x)}` gilt, folgt für
die Ableitung der Cosinus-Funktion:

.. math::
    :label: eqn-ableitungsregel-cosinusfunktion
    
    f(x) = \cos{(x)} \quad \Rightarrow \quad f'(x) = - \sin{(x)}

Die Ableitung der Cosinus-Funktion ist also gleich der negativen Sinusfunktion.


.. rubric:: Ableitung der Tangens- und Cotangensfunktion 

Die Ableitung der Tangensfunktion :math:`f(x) = \tan{(x)} =
\frac{\sin{(x)}}{\cos{(x)}}` kann mit Hilfe der Ableitungsregeln der Sinus- und
Cosinusfunktion bestimmt werden; dabei wird wiederum die :ref:`Quotientenregel
<Quotientenregel>` verwendet: 

.. only:: html

    .. math::
    
        \big(\tan{(x)}\big)' = \left(\frac{\sin{(x)}}{\cos{(x)}}\right)' =
        \frac{\cos{(x)} \cdot \cos{(x)} - (-\sin{(x)}) \cdot
        \sin{(x)}}{\big(\cos{(x)}\big)^2} = \frac{\cos^2{(x)} + \sin
        ^2{(x)}}{\cos^2{(x)}} = \frac{1}{\cos^2{(x)}}

.. only:: latex

    .. math::
    
        \big(\tan{(x)}\big)' = \left(\frac{\sin{(x)}}{\cos{(x)}}\right)' &=
        \frac{\cos{(x)} \cdot \cos{(x)} - (-\sin{(x)}) \cdot
        \sin{(x)}}{\big(\cos{(x)}\big)^2} \\[4pt] &= \frac{\cos^2{(x)} + \sin
        ^2{(x)}}{\cos^2{(x)}} = \frac{1}{\cos^2{(x)}}

Für die Ableitung der Tangensfunktion gilt also:

.. math::
    :label: eqn-ableitungsregel-tangensfunktion
    
    f(x) = \tan{(x)} \quad \Rightarrow \quad f'(x) = \frac{1}{\cos^2{(x)}}

Für die Cotangensfunktion :math:`f(x) = \cot{(x)} =
\frac{\cos{(x)}}{\sin{(x)}}` gilt entsprechend:

.. only:: html

    .. math::
    
        {\color{white}-}\big(\cot{(x)}\big)' =
        \left(\frac{\cos{(x)}}{\sin{(x)}}\right)' = \frac{-\sin{(x)} \cdot \sin{(x)}
        - \cos{(x)} \cdot \cos{(x)}}{\big(\sin{(x)}\big)^2} = \frac{-\sin^2{(x)} -
          \cos ^2{(x)}}{\sin^2{(x)}} = -\frac{1}{\sin^2{(x)}}

.. only:: latex

    .. math::
    
        {\color{white}-}\big(\cot{(x)}\big)' =
        \left(\frac{\cos{(x)}}{\sin{(x)}}\right)' &= \frac{-\sin{(x)} \cdot \sin{(x)}
        - \cos{(x)} \cdot \cos{(x)}}{\big(\sin{(x)}\big)^2} \\[4pt] &= \frac{-\sin^2{(x)} -
          \cos ^2{(x)}}{\sin^2{(x)}} = -\frac{1}{\sin^2{(x)}}

Für die Ableitung der Cotangensfunktion gilt also:

.. math::
    :label: eqn-ableitungsregel-cotangensfunktion
    
    f(x) = \cot{(x)} \quad \Rightarrow \quad f'(x) = -\frac{1}{\sin^2{(x)}}

    

.. index:: Potenz
.. _Potenzen, Wurzeln und Logarithmen:

Potenzen, Wurzeln und Logarithmen
=================================

Das Potenzieren entspricht, wie bereits im Abschnitt :ref:`Rechnen mit reellen
Zahlen <Rechnen mit reellen Zahlen>` erwähnt, einem mehrfachen Multiplizieren;
das Wurzelziehen hingegen der Umkehrung des Potenzierens. Auf einige der dafür
relevanten Rechenregeln wird im folgenden Abschnitt näher eingegangen, ebenso
auf das Logarithmieren als zweite Möglichkeit, einen Potenz-Term nach der
gesuchten Variablen aufzulösen.


.. _Rechenregeln für Potenzen und Wurzeln:

Rechenregeln für Potenzen und Wurzeln
-------------------------------------

| Der Wert einer Potenz entspricht stets einer reellen Zahl. Zwei Potenzen mit
  gleicher Basis :math:`a \ne 0` und gleichem Exponent :math:`n` lassen sich
  somit nach den für reelle Zahlen üblichen Rechenregeln addieren und
  subtrahieren.
| Stehen :math:`c_1` und :math:`c_2` für beliebige konstante
  Zahlen und :math:`n` für eine natürliche Zahl [#]_, so gilt:

.. math::
    :label: eqn-potenz-addition

    c_1 \cdot a^n + c_2 \cdot a^n = (c_1 + c_2) \cdot a^n


Unterscheiden sich zwei Potenzen in ihrer Basis und/oder in ihrem Exponenten, so
kann eine Addition oder Subtraktion beider Potenzen nicht weiter vereinfacht
werden. Multiplikationen und Divisionen von Potenzen mit ungleicher Basis
und/oder ungleichem Exponenten lassen sich hingegen mit Hilfe der folgenden
Rechenregeln umformen.


.. _Rechenregeln für Potenzen mit gleicher Basis:

.. rubric:: Rechenregeln für Potenzen mit gleicher Basis

Potenzen können miteinander multipliziert werden, wenn sie eine gemeinsame
Basis besitzen. In diesem Fall werden die Exponenten addiert:

.. math::
    :label: eqn-potenz-multiplikation

    a^{n_1} \cdot a^{n_2} = a^{n_1 + n_2}

Nach dem gleichen Prinzip können Potenzen mit gleicher Basis dividiert werden,
indem man die Differenz ihrer Exponenten bildet:

.. math::
    :label: eqn-potenz-division

    \frac{ a^{n_1} }{ a^{n_2} } = a^{n_1 - n_2}

Diese Gleichung erlaubt es, eine Potenz mit negativem Exponenten als Kehrwert
einer Potenz mit positivem Exponenten aufzufassen. Ist nämlich :math:`n_1 = 0`,
so gilt :math:`a^{n_1} = a^0 = 1`. Damit folgt allgemein: [#]_

.. math::
    :label: eqn-potenz-negativer-exponent

    a^{-n} = \frac{1}{a^n}

Darüber hinaus gilt für mehrfache Produkte von Potenzen, also für "Potenzen von
Potenzen", folgende Formel [#]_:

.. math::
    :label: eqn-potenz-potenz

    \left(a^{n_1}\right)^{n_2} = a^{n_1 \cdot a^{n_2}}


*Beispiele:*

* Multipliziert man :math:`100 = 10^2` mit :math:`1\,000 = 10^3`, so lautet das
  Ergebnis:

  .. math::

      100 \cdot 1\,000 = 10^2 \cdot 10^3 = 10^5 = 100\,000

  Bei der Multiplikation von Zehnerpotenzen muss somit nur die Anzahl
  an Nullen addiert werden.

* Teilt man :math:`10 = 10^1` durch :math:`1\,000 = 10^3`, so lautet das
  Ergebnis:

  .. math::

      \frac{10}{1\,000} = \frac{10^1}{10^3} = 10^{1-3} = 10^{-2} =
      \frac{1}{10^2} = \frac{1}{100}

  Bei der Division von Zehnerpotenzen wird die Anzahl an Nullen des Nenners von
  der Anzahl an Nullen des Zählers subtrahiert. Ergibt sich dabei eine negative
  Anzahl an Nullen, so gibt diese Zahl die Nachkommastelle des Ergebnisses an:

  .. math::

      10^{-2} = 0,01

* Multipliziert man :math:`32 = 2^5` mit sich selbst, so lautet das Ergebnis:

  .. math::

      32 \cdot 32 = 2^5 \cdot 2^5 = 2^{10} = 1\,024

  Wird eine Potenz quadriert, so wird ihr Exponent verdoppelt.


.. _Rechenregeln für Potenzen mit gleichen Exponenten:

.. rubric:: Rechenregeln für Potenzen mit gleichen Exponenten

Neben den Rechenregeln für Potenzen mit gleicher Basis können auch Potenzen
mit gleichen Exponenten durch Multiplikation bzw. Division zusammengefasst
werden. [#]_ Es gilt:

.. math::
    :label: eqn-potenz-multiplikation-gleicher-exponent

     a_1\;\!^n \cdot  a_2\;\!^n = ( a_1 \cdot a_2)^n

und

.. math::
    :label: eqn-potenz-division-gleicher-exponent

    \left( \frac{a_1\,^n}{a_2\,^n}\right) = \left( \frac{a_1}{a_2}\right)^n

Produkte lassen sich somit potenzieren, indem jeder ihrer Faktoren mit dem
gleichen Exponenten potenziert wird. Entsprechend lassen sich auch Brüche
potenzieren, indem sowohl Zähler wie auch Nenner den gleichen Exponenten
erhalten.

Eine wichtige Rolle hierbei spielt die Potenz :math:`(-1)^n`. Je nachdem, ob
:math:`n` geradzahlig (durch :math:`2` teilbar) ist oder nicht, hebt sich das
Vorzeichen auf bzw. bleibt bestehen:

.. math::

    (-1)^n = \begin{cases}
    +1 & \text{falls $n$ gerade}  \\
    -1 & \text{falls $n$ ungerade} \\
    \end{cases}

Diese Besonderheit ist mit der Multiplikationsregel "Minus mal Minus gibt Plus"
identisch. Kombiniert man Gleichung
:eq:`eqn-potenz-multiplikation-gleicher-exponent` mit der obigen Gleichung,
indem man :math:`a_1 = (-1)` setzt und beide Seiten der Gleichung vertauscht, so
gilt für beliebige Potenzen stets:

.. math::

    (-a)^{2 \cdot n \phantom{+1}} &= (-1)^{2 \cdot n \phantom{+1}} \cdot a^{2
    \cdot n \phantom{+1}} = +a^{2 \cdot n} \\[2pt]
    (-a)^{2 \cdot n + 1} &= (-1)^{2 \cdot n+1} \cdot a^{2 \cdot n+1} = -a^{2
    \cdot n + 1}

Eine negative Basis verliert durch ein Potenzieren mit einem geradzahligen
Exponenten :math:`2 \cdot n` somit stets ihr Vorzeichen. Durch Potenzieren mit
einem ungeradzahligen Exponenten :math:`2 \cdot n + 1` bleibt das Vorzeichen der
Basis hingegen erhalten.


.. _Rechenregeln für Wurzeln und allgemeine Potenzen:

.. rubric:: Rechenregeln für Wurzeln und allgemeine Potenzen

Neben der ersten Erweiterung des Potenzbegriffs auf negative Exponenten als
logische Konsequenz aus Gleichung :eq:`eqn-potenz-division`, die sich auf die
Division zweier Potenzen bezieht, ist auch anhand Gleichung :eq:`eqn-potenz-potenz`,
die Potenzen von Potenzen beschreibt, eine zweite Erweiterung des Potenzbegriffs
möglich. Im Allgemeinen lautet diese Gleichung:

.. math::

    \left(a^{n_1}\right)^{n_2} = a^{n_1 \cdot a^{n_2}}

Das Wurzelziehen stellt die Umkehrung des Potenzierens dar. Um die obige
Rechenregel umzukehren, muss die Multiplikation des Exponenten umgekehrt werden.
Setzt man :math:`n_1 = n` und :math:`n_2 = \frac{1}{n}`, so
folgt:

.. math::

    \left(a^{n}\right)^{\frac{1}{n}} = a^{n \cdot \frac{1}{n}} =
    a^{\frac{n}{n}} = a^1 = a

Das Ergebnis stimmt damit überein, dass die :math:`n`-fache Wurzel einer
:math:`n`-fachen Potenz wieder die ursprüngliche Zahl ergibt:

.. math::

    \sqrt[n]{a^n} = a

Tatsächlich können folgende Umformungen als allgemeine Rechenregeln
genutzt werden:

.. math::
    :label: eqn-potenz-wurzel

    \sqrt[n]{a} = a^{\frac{1}{n}}

sowie

.. math::
    :label: eqn-potenz-wurzel2

    \sqrt[n_2]{a^{n_1}} = a^{\frac{n_1}{n_2}}

Da Wurzeln somit nichts anderes als Potenzen mit gebrochenem Exponenten :math:`n
\in \mathbb{Q}` darstellen, gelten die in den beiden vorherigen Abschnitten
aufgeführten Rechenregeln :eq:`eqn-potenz-addition` bis
:eq:`eqn-potenz-division-gleicher-exponent` gleichermaßen auch für Wurzeln.


.. index:: Logarithmus
.. _Logarithmus:
.. _Rechenregeln für Logarithmen:

Rechenregeln für Logarithmen
----------------------------

Das Logarithmieren stellt neben dem Wurzelziehen eine zweite Möglichkeit dar,
eine Potenz :math:`a^n` zu finden, die ein bestimmtes Ergebnis :math:`b`
liefert. Während beim Wurzelziehen der (Wurzel-)Exponent :math:`n` vorgegeben
ist und die zum Wert der Potenz passende Basis :math:`a` gesucht wird, hilft das
Logarithmieren dabei, den zu einer vorgegebenen Basis :math:`a` passenden
Exponenten :math:`n` zu finden. Die Fragestellung lautet somit:

.. math::

    a^{n} = b \quad \Rightarrow \quad n = \, ?

Um dieses mathematische Problem zu lösen, muss der so genannte Logarithmus
von :math:`b` zur Basis :math:`a` ermittelt werden.

*Definition:*

 Der Logarithmus  :math:`n = \log_{a}{b}` ist diejenige Zahl, mit welcher die
 Basis :math:`a` potenziert werden muss, um das Ergebnis :math:`b` zu
 erhalten. Es gilt:

 .. math::

     a^n = b \quad \Leftrightarrow \quad n = \log_{a}{b}

.. Für :math:`b` sind nur positive Werte zulässig, die Definitionsmenge ist
.. somit :math:`\mathbb{D} = \mathbb{R}^{+}`. Die Wertemenge umfasst alle
.. reellen Werte, d.h. es gilt :math:`\mathbb{L} = \mathbb{R}`.

Beispielsweise gilt somit :math:`\log_{a}{a} = 1`, wie sich durch Einsetzen in
den linken Teil der obigen Äquivalenz-Gleichung überprüfen lässt, sowie
:math:`\log_{a}{a^n} = n`, da :math:`n` genau der Zahl entspricht, mit der die
Basis :math:`a` potenziert werden muss, um das Ergebnis :math:`a^n` zu erhalten.


Eine einfache Berechnung eines Logarithmus "von Hand" ist allgemein nur in
seltenen Fällen möglich. Früher wurden daher Werte-Tabellen für Logarithmen in
Lehrbüchern und Formelsammlungen abgedruckt, inzwischen haben Taschenrechner
bzw. Computerprogramme mit entsprechenden Funktionen die Berechnung von
Logarithmen wesentlich vereinfacht und Werte-Tabellen letztlich überflüssig
gemacht.

.. _Basisumrechnung:

In der Praxis sind insbesondere Logarithmen zur Basis :math:`10` ("dekadische"
Logarithmen, Symbol: :math:`\mathrm{lg}`), zur Basis :math:`e` ("natürliche"
Logarithmen, Symbol: :math:`\mathrm{ln}`) und zur Basis :math:`2` ("binäre" oder
duale" Logarithmen, Zeichen :math:`\mathrm{lb}` oder :math:`\mathrm{ld}`) von
Bedeutung. [#]_ Um einen Logarithmus auf eine andere Basis umzurechnen, kann
folgende Formel angewendet werden:

.. math::
    :label: eqn-logarithmus-basiswechsel

    \log_{a_2}{b} = \frac{\log_{ a_1}{b}}{\log_{a_1}{a_2}}

Die obige Formel ermöglicht es beispielsweise, einen dekadischen Logarithmus
:math:`( a_1 = 10)` in einen binären Logarithmus :math:`(a_2 = 2)` umzurechnen,
indem man diesen durch :math:`\log_{10}{2} \approx 0,301` teilt.


.. _Summen und Differenzen von Logarithmen:

.. rubric:: Summen und Differenzen von Logarithmen

Logarithmen mit gleicher Basis lassen sich addieren oder subtrahieren. Das
Ergebnis einer Logarithmus-Addition ist ein Logarithmus mit gleicher Basis,
dessen Argument gleich dem Produkt der Argumente beider zu addierenden
Logarithmen ist:

.. math::
    :label: eqn-logarithmus-addition

    \log_{a}{b_1} + \log_{a}{ b_2} = \log_{a}{ (b_1 \cdot b_2) }

Entsprechend ist das Ergebnis einer Logarithmus-Subtraktion ein Logarithmus mit
gleicher Basis, dessen Argument gleich dem Quotienten der Argumente beider zu
subtrahierender Logarithmen ist:

.. math::
    :label: eqn-logarithmus-subtraktion

    \log_{a}{b_1} - \log_{a}{b_2} = \log_{a}{ \left( \frac{b_1}{b_2} \right) }

Wird ein Logarithmus mit einem konstanten Faktor :math:`c` multipliziert, so
entspricht dies einer :math:`c`-Fachen Addition des Logarithmus mit sich selbst.
In diesem Fall entspricht das Ergebnis somit einem Logarithmus mit gleicher Basis
:math:`a`, dessen Argument :math:`c`-fach mit sich selbst multipliziert werden
muss:

.. math::
    :label: eqn-logarithmus-multiplikation-mit-faktor

    c \cdot \log_{a}{b}  = \log_{a}{\left( b^c \right)}

Weitere Eigenschaften von Logarithmen werden in den Abschnitten
:ref:`Logarithmusgleichungen <Logarithmusgleichung>` und
:ref:`Logarithmusfunktionen <Logarithmusfunktion>` behandelt.


.. raw:: html

    <hr />


.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Auch allgemeine Potenzen (mit beliebigem Exponenten :math:`n \in
    \mathbb{R})` lassen sich auf diese Art addieren bzw. subtrahieren.
    Die Einschränkung :math:`a \ne 0` ist dabei notwendig, da die
    Potenz :math:`0^0` nicht definiert ist.

.. [#] Auf diese Weise lässt sich eine plausible Erklärung angeben, warum
    :math:`a^0 = 1` für alle :math:`a \ne 0` ist. Es gilt beispielsweise für
    :math:`a=10`

    .. math::

        10^{-3} &= \frac{1}{1\,000} = 0,001 \\[2pt]
        10^{-2} &= \frac{1}{\phantom{\,}100\phantom{0}} = 0,01 \\[2pt]
        10^{-1} &= \frac{1}{\phantom{\,\,\,}10\phantom{\,\,\,\,}} = 0,1 \\[2pt]
        10^{\pm0} &= \frac{1}{\phantom{0\,\,}1\phantom{0\,\,}} = 1 \\[2pt]
        10^{+1} &= \frac{\phantom{\,\,\,}10\phantom{\,\,\,\,}}{1} = 10 \\[2pt]
        10^{+2} &= \frac{\phantom{\,}100\phantom{0}}{1} = 100 \\[2pt]
        10^{+3} &= \frac{1\,000}{1} = 1\,000


.. [#] Die Gleichung für Potenzen von Potenzen folgt aus der Gleichung für
    Potenz-Multiplikationen. Setzt man in Gleichung
    :eq:`eqn-potenz-multiplikation` für :math:`n_1` und :math:`n_2` gleiche
    Werte ein, d.h. :math:`n_1 = n_2 = n`, so gilt:

    .. math::

        \underbrace{a^n \cdot a^n \cdot \ldots \cdot a^n}_{\text{$m$ mal}} =
        a \underbrace{^{n + n + \ldots + n}}_{\text{$m$ mal}} = a^{n \cdot m}


.. [#] Additionen und Subtraktionen von Potenzen mit ungleicher Basis
    lassen sich nicht weiter zusammenfassen.

.. [#] Für dekadische Logarithmen :math:`(\mathrm{lg})` und natürliche
    Logarithmen :math:`(\mathrm{ln})` besitzen Taschenrechner häufig
    entsprechende Funktionstasten.



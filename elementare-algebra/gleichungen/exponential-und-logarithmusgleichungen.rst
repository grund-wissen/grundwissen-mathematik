.. _Exponential- und Logarithmusgleichungen:

Exponential- und Logarithmusgleichungen
=======================================

.. index:: Exponentialgleichung
.. _Lösen von Exponentialgleichungen:

.. rubric:: Lösen von Exponentialgleichungen

Bei Exponentialgleichungen steht die Variable :math:`x` im Exponenten mindestens
eines Terms. Im Allgemeinen sind derartige Gleichungen nur näherungsweise unter
Verwendung von Computerprogrammen lösbar.

Mit Verwendung eines üblichen Taschenrechners sind Exponentialgleichungen nur
dann lösbar, wenn auf beiden Seiten ausschließlich konstante Terme oder Terme
der Form :math:`a ^{T(x)}` stehen, wobei :math:`T(x)` für einen beliebigen, von
der Variablen :math:`x` abhängigen Term steht. Wenn eine derartige Gleichung
eine Lösung besitzt, also die linke Seite der Gleichung der rechten entspricht,
dann muss ebenfalls der :ref:`Logarithmus <Rechenregeln für Logarithmen>` der
linken und der rechten Seite gleich sein. Dieser Rechentrick ermöglicht die
Verwendung der folgenden Identität: [#]_

.. math::

    \log_{\mathrm{a}}{a ^{x}} = x


Durch das "Logarithmieren" einer Gleichung kann somit ein im Exponenten
stehender, von der Variablen :math:`x` abhängiger Term in einen gewöhnlichen
Term umgewandelt werden. Dieser kann, je nach Art des Terms, weiter vereinfacht
und ausgewertet werden.

*Beispiele:*

* Die Lösung folgender Gleichung soll bestimmt werden:

  .. math::

      10 ^{2 \cdot x} = 50{\color{white}\qquad \qquad \quad \ldots}

  Das Logarithmieren beider Seiten führt auf folgende Gleichung:

  .. math::

      \log_{10}{10 ^{2 \cdot x}} &= \log_{10}{50} \\
      \Rightarrow 2 \cdot x &= \log_{10}{50} \\
      x  &= \frac{\log_{10}{50}}{2} \approx \frac{1,7}{2} = 0,85

  Somit hat die Gleichung die Lösung :math:`x \approx 0,85`.

* Die Lösung folgender Gleichung soll bestimmt werden:

  .. math::

      2 ^{x} = 3 ^{2 - 5 \cdot x}{\color{white}\qquad \quad \ldots}

  Das Logarithmieren beider Seiten führt auf folgende Gleichung:

  .. math::

      \log_{2}{2^x} = \log_{2}{3^{2 - 5 \cdot x}}{\color{white}\qquad \quad \ldots}

  Hierbei können die :ref:`Rechenregeln für Logarithmen <Summen und
  Differenzen von Logarithmen>` genutzt werden. Da :math:`\log_{a}{b^c} = c
  \cdot \log_{a}{b}` gilt, kann die Gleichung weiter vereinfacht werden:

  .. math::

      x \cdot \log_{2}{2} &= (2 - 5 \cdot x) \cdot \log_{2}{3}{\color{white}\;\; \ldots}\\
      5 \cdot x \cdot \log_{2}{3} + x \cdot \log_{2}{2} &= 2 \cdot  \log_{2}{3} \\
      x \cdot (5 \cdot \log_{2}{3} + 1 \cdot \log_{2}{2} )&= 2 \cdot  \log_{2}{3} \\
      x &= \frac{2 \cdot  \log_{2}{3}}{5 \cdot \log_{2}{3} + 1 \cdot \log_{2}{2}} \approx 0,355

  Somit hat die Gleichung die Lösung :math:`x \approx 0,355`.

Tritt die Variable :math:`x` sowohl im Exponenten eines Terms als auch als Basis
eines anderen Terms auf, so ist die Gleichung nur näherungsweise mit
Computerprogrammen lösbar. Besteht die Gleichung hingegen ausschließlich aus
Termen mit gleicher Basis und der Variablen :math:`x` im Exponenten, so heben
sich die Exponentialterme durch das Logarithmieren gegenseitig auf, und es
können ausschließlich die Exponenten verglichen werden.

*Beispiel:*

* Die Lösungen folgender Gleichung soll bestimmt werden:

  .. math::

      e^{3 \cdot x} = e^{x^2-10}\\

  Hierbei bezeichnet :math:`e \approx 2,718` die Eulersche Zahl. Das
  Logarithmieren beider Seiten führt auf folgende Gleichung:

  .. math::

      \ln{e^{3 \cdot x}} &= \ln{e^{x^2 - 10}} \\
      \Rightarrow 3 \cdot x &= x^2 - 10 \\

  Somit muss nur die sich ergebende quadratische Gleichung gelöst werden. Die
  Lösungen lassen sich in diesem Fall einfach mit dem :ref:`Satz von Vieta
  <Satz von Vieta>` bestimmen:

  .. math::

      x^2 + 3 \cdot x - 10 &= 0  \\
      \Rightarrow x_1 = -5 \quad &\text{und} \quad x_2 = 2{\color{white} \quad \ldots}

  Die Lösungsmenge der Gleichung lautet somit :math:`\mathbb{L} = \{ -5,\; +2 \}`.


.. index:: Logarithmusgleichung
.. _Logarithmusgleichung:
.. _Lösen von Logarithmusgleichungen:

.. rubric:: Lösen von Logarithmusgleichungen

Bei Logarithmusgleichungen tritt die Variable :math:`x` mindestens einmal als
Argument eines Logarithmus auf. Im Allgemeinen sind solche Gleichungen nur
näherungsweise unter Verwendung von Computerprogrammen lösbar.

Logarithmusgleichungen sind -- ebenso wie Exponentialgleichungen -- nur dann
unter Verwendung eines üblichen Taschenrechners lösbar, wenn auf beiden Seiten
ausschließlich konstante Terme oder Terme der Form :math:`\log_{\mathrm{a}}{T(x)}`
auftreten, wobei :math:`a` die Basis des Logarithmus bezeichnet und :math:`T(x)`
für einen beliebigen, von der Variablen :math:`x` abhängigen Term steht.

Wenn eine derartige Gleichung eine Lösung besitzt, also die linke Seite der
Gleichung der rechten entspricht, dann muss die Gleichung ebenfalls gelten, wenn
man eine der Basis :math:`a` des Logarithmus entsprechende Zahl mit den Termen
auf beiden Seiten potenziert. Dieser Rechentrick ermöglicht die Verwendung der
folgenden Identität: [#]_

.. math::

    a ^{\log_{\mathrm{a}}{x}} = x

Durch das "Exponenzieren" einer Gleichung kann somit ein im Argument eines
Logarithmus stehender, von der Variablen :math:`x` abhängiger Term in einen
gewöhnlichen Term umgewandelt werden. Dieser kann, je nach Art des Terms, weiter
vereinfacht und ausgewertet werden.

*Beispiel:*

* Die Lösung folgender Gleichung soll bestimmt werden:

  .. math::

      \log_{5}{x^2} = 3

  Das Exponenzieren beider Seiten führt auf folgende Gleichung:

  .. math::

      5 ^{\log_{5}{x^3}} &= 5^2 \\
      x^3 &= 5^2 \\
      x\phantom{^3} &= 5^{\frac{2}{3}} \approx 2,924

  Somit hat die Gleichung die Lösung :math:`x \approx 2,924`.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Der Logarithmus :math:`\log_{\mathrm{a}}{a^x}` ist gleich derjenigen
    Zahl, mit der man :math:`a` potenzieren muss, um :math:`a^x` zu erhalten.
    Offensichtlich muss man :math:`a` mit :math:`x` potenzieren, um :math:`a^x`
    zu erhalten. Somit ist :math:`x=\log_{\mathrm{a}}{a^x}` für jede frei
    wählbare Basis :math:`a` und beliebige Werte der Variablen :math:`x`.

.. [#] Der Logarithmus :math:`\log_{\mathrm{a}}{x}` ist gleich derjenigen Zahl, mit
    der man :math:`a` potenzieren muss, um :math:`x` zu erhalten. Offensichtlich
    erhält man somit :math:`x`, wenn man :math:`a` mit dieser Zahl potenziert.
    Somit gilt :math:`x = a^{\log_{\mathrm{a}}{x}}` für jede frei wählbare Basis
    :math:`a` und beliebige Werte der Variablen :math:`x`.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Exponential- und
    Logarithmusgleichungen>`.



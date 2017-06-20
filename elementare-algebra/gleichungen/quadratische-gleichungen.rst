.. index:: Quadratische Gleichung

.. _Quadratische Gleichungen:

Quadratische Gleichungen
========================

Bei einer quadratischen Gleichung tritt die Variable :math:`x` in der zweiten
Potenz :math:`x^2` und gegebenenfalls zusätzlich in erster Potenz auf; sie darf
dabei nicht im Nenner stehen. Jede quadratische Gleichung kann durch äquivalente
Umformungen in die allgemeine Form gebracht werden:

.. math::
    :label: eqn-quadratische-gleichung

    a \cdot x^2 + b \cdot x + c = 0

Hierbei sind :math:`a \ne 0`, :math:`b` und :math:`c` beliebige Konstanten.

.. index:: Diskriminante, Mitternachtsformel
.. _Mitternachtsformel:
.. _Lösungsformel für quadratische Gleichungen:

Eine quadratische Gleichung hat höchstens zwei Lösungen. Wie viele und welche
Lösungen eine quadratische Gleichung im konkreten Fall hat, kann direkt bestimmt
werden, wenn die Gleichung in der allgemeinen Form vorliegt. Die Anzahl an
Lösungen ist durch den Wert ihrer so genannten "Diskriminante" :math:`D = b^2 -
4 \cdot a \cdot c` bestimmt, die anhand der allgemeinen Gleichungsform
:eq:`eqn-quadratische-gleichung` unmittelbar berechnet werden kann. Damit lassen
sich die folgenden drei Fälle unterscheiden:

.. math::
    :label: eqn-quadratische-gleichung-mitternachtsformel

    D > 0 \quad &\Leftrightarrow \quad \mathbb{L} = \Big \lbrace
    \frac{-b - \sqrt{b^2 - 4 \cdot a \cdot c} }{2 \cdot a} ,\, \frac{-b +
    \sqrt{b^2 - 4 \cdot a \cdot c} }{2 \cdot a} \Big \rbrace  \\[4pt]
    D = 0 \quad &\Leftrightarrow \quad \mathbb{L} =
    \Big \lbrace \frac{-b}{2 \cdot a} \Big \rbrace  \\[4pt]
    D < 0 \quad &\Leftrightarrow \quad \mathbb{L} = \big \lbrace \big \rbrace

Dieses Verfahren, anhand der Diskriminante :math:`D` auf die Anzahl und die
Werte der Lösungen schließen zu können, wird umgangssprachlich auch als
"Mitternachtsformel" bezeichnet. [#]_ [#]_ Sie lässt sich auf jede quadratische
Gleichung anwenden, die in der allgemeinen Form :eq:`eqn-quadratische-gleichung`
vorliegt.


.. _Sonderfälle quadratischer Gleichungen:

.. rubric:: Sonderfälle quadratischer Gleichungen

Liegen Spezialfälle von quadratischen Gleichungen vor, so können auch andere,
teilweise einfachere Lösungsverfahren genutzt werden:

* Ist :math:`b = 0`, so liegt eine quadratische Gleichung folgender Form
  vor:

  .. math::

      a \cdot x^2 + c = 0

  Diese Gleichung kann direkt nach :math:`x` aufgelöst werden:

  .. math::

      a \cdot x^2 + c = 0 \quad \Leftrightarrow \quad x _{\mathrm{1,2}} = \pm
      \sqrt{-\frac{c}{a}}

  Die Gleichung hat nur dann die beiden obigen Lösungen, wenn :math:`a` und
  :math:`c` unterschiedliche Vorzeichen haben, andernfalls ist die Lösungsmenge
  gleich :math:`\lbrace 0 \rbrace` (falls :math:`c = 0` ist) oder gleich
  der leeren Menge (falls :math:`c \ne 0` ist).

  Anschaulich ist die obige Gleichung daduch zu erklären, dass für das Quadrat
  jeder Zahl :math:`x` stets :math:`x^2 \ge 0` gilt. Wird nun eine Quadratzahl
  mit einem positiven Faktor multipliziert, so kann man nicht eine weitere positive
  Zahl hinzu addieren, um als Ergebnis den Wert Null zu erhalten.


* Ist :math:`c = 0`, fehlt also ein :math:`x`-freier Term, so liegt eine
  quadratische Gleichung folgender Form vor:

  .. math::

      a \cdot x^2 + b \cdot x = 0

  Die Mitternachtsformel liefert in diesem Fall die beiden Werte :math:`x_1 =0`
  und :math:`x_2 = - \frac{b}{a}` als Lösungen. Die gleichen Lösungen erhält
  man, indem man auf der linken Seite der Gleichung :math:`x` als gemeinsamen
  Faktor ausklammert:

  .. math::

      a \cdot x^2 + b \cdot x = 0 \quad \Leftrightarrow \quad x \cdot (a \cdot x
      + b) = 0

  Da ein Produkt nur dann gleich Null ist, wenn (mindestens) einer der beiden
  Faktoren gleich Null ist, folgt aus der obigen Gleichungsform, dass entweder
  der :math:`x=0` oder :math:`a \cdot x + b = 0` gelten muss. Aus dem ersten
  Fall folgt :math:`x_1 = 0`, aus dem zweiten Fall (einer linearen
  Gleichung) folgt :math:`x_2 = -\frac{b}{a}`.

.. index:: Satz von Vieta
.. _Satz von Vieta:

* Ist :math:`a = 1`, so liegt eine "normierte" quadratische Gleichung vor:

  .. math::

      1 \cdot x^2 + b \cdot x + c = 0

  Jede allgemeine quadratische Gleichung mit :math:`a \ne 1` kann ebenfalls
  mittels Division durch :math:`a` ebenfalls in eine normierte Form gebracht
  werden. Setzt man :math:`p = \frac{b}{a}` und :math:`q = \frac{c}{a}`, so
  lässt sich jede quadratische Gleichung in normierter Form darstellen:

  .. math::
      :label: eqn-quadratische-gleichung-normalform


      x^2 + p \cdot x + q = 0

  Sind :math:`p` und :math:`q` ganze Zahlen, so lassen sich die Lösungen der
  Gleichung bisweilen auch schnell mit Hilfe des nach dem Mathematiker `François
  Viète <https://de.wikipedia.org/wiki/Vieta>`_ benannten "Satz von Vieta"
  bestimmen. Hierbei wird genutzt, dass zwischen den beiden möglichen Lösungen
  :math:`x_1` und :math:`x_2`, für die auch :math:`x_1 = x_2` gelten kann,
  folgender Zusammenhang besteht: [#]_

  .. math::

      x_1 \, \cdot \, x_2 &= +q \quad \text{und} \\ x_1 + x_2 &= -p

  Kennt man die möglichen ganzzahligen Faktoren der Zahl :math:`q`, so lässt
  sich durch Kopfrechnen oftmals ein Zahlenpaar finden, das als Summe genau den
  negativen Wert von :math:`p` ergibt. Dieses Zahlenpaar stellt dann die
  gesuchten Lösungen von Gleichung :eq:`eqn-quadratische-gleichung-normalform`
  dar. [#]_

.. index:: Linearfaktorzerlegung
.. _Linearfaktorzerlegung:
.. _Produktform:
.. _Produktform quadratischer Gleichungen:

.. rubric:: Produktform quadratischer Gleichungen

Sind :math:`x_1` und :math:`x_2` die Lösungen einer
quadratischen Gleichung, wobei auch :math:`x_1 = x_2` zulässig
ist, so kann diese allgemein auch in folgender Form dargestellt werden:

  .. math::

      a \cdot x^2 + b \cdot x + c &= 0 \\
      \Rightarrow a \cdot (x - x_1) \cdot (x - x_2) &= 0

Eine solche Aufteilung einer Gleichung in mehrere lineare Faktoren wird als
Linearfaktorzerlegung oder Produktform bezeichnet. Diese Darstellung spielt für
quadratische Gleichungen nur eine untergeordnete Rolle, sie kann allerdings in
nützlicher Weise auch bei Gleichungen höheren Grades angewendet werden.



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Im ersten Fall :math:`(D > 0)` können die beiden Lösungen :math:`x_1` und
    :math:`x_2` mittels des Plus-Minus-Zeichens :math:`\pm` auch verkürzt in
    folgender Form dargestellt werden:

    .. math::

        D > 0 \quad \Rightarrow \quad x _{\mathrm{1,2}} = \frac{-b \pm \sqrt{b^2 - 4
        \cdot a \cdot c}}{2 \cdot a}

    Im Fall :math:`D=0` fallen die Lösungen :math:`x_1` und :math:`x_2` wegen
    :math:`\sqrt{D} = \pm 0` zusammen. Man spricht daher bisweilen auch von
    einer "doppelten" Lösung.

.. [#] Die Gleichung :eq:`eqn-quadratische-gleichung-mitternachtsformel` gilt,
    sofern mit reellen Zahlen :math:`x \in \mathbb{R}` gerechnet wird. Rechnet
    man mit :ref:`komplexen Zahlen <Komplexe Zahlen>`, so hat eine quadratische
    Gleichung auch im Fall :math:`D<0` zwei Lösungen. In diesem Fall gilt:

    .. math::

        \sqrt{D} = \sqrt{(-1) \cdot (-D)} = \sqrt{i^2 \cdot (-D)} = i \cdot \sqrt{-D}

    Damit ergeben sich als Lösungen:

    .. math::

        x _{\mathrm{1,2}} = \frac{-b}{2 \cdot a} \pm i \cdot \frac{\sqrt{-(b^2 - 4
        \cdot a \cdot c)}}{2 \cdot a}

.. [#] Nach der "Mitternachtsformel"
    :eq:`eqn-quadratische-gleichung-mitternachtsformel` gilt mit :math:`a=1` und
    :math:`D = p^2 - 4 \cdot q`:

    .. math::

        x_1 \cdot x_2 &= \frac{-p + \sqrt{D}}{2} \cdot \frac{-p -
        \sqrt{D}}{2} \\[2pt]
        &= \left(-\frac{p}{2} + \frac{\sqrt{D}}{2} \right) \cdot \left(- \frac{p}{2} -
        \frac{\sqrt{D}}{2} \right) \\[2pt]
        &= \Bigg( \!\! -\frac{p}{2} \; \Bigg)^2 - \left( \frac{\sqrt{D}}{2}\right)^2 \\
        &= \;\; + \frac{p^2}{4} \quad \;\, - \quad \; \frac{D}{4} \\[2pt]
        &= \;\; + \frac{p^2}{4} \quad \;\, - \left(\frac{p^2}{4} - q \right) \\[2pt] &= + q \qquad \checkmark

    Ebenso gilt:

    .. math::

        x_1 + x_2 &= \frac{-p + \sqrt{D}}{2} + \frac{-p -
        \sqrt{D}}{2} \\[2pt]
        &= \left(-\frac{p}{2} + \frac{\sqrt{D}}{2} \right) + \left(- \frac{p}{2} -
        \frac{\sqrt{D}}{2} \right) \\[2pt]
        &= -p \qquad \checkmark

.. [#] Die "Mitternachtsformel"
    :eq:`eqn-quadratische-gleichung-mitternachtsformel` kann selbstverständlich
    ebenso zur Lösung von Gleichung :eq:`eqn-quadratische-gleichung-normalform`
    genutzt werden.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Quadratische
    Gleichungen>`.



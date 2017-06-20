
.. _Lösungen Integralrechnung:

Integralrechnung
================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Integralrechnung>` zum Abschnitt :ref:`Integralrechnung <Integralrechnung>`.

.. _Lösungen Integrationsmethoden:

.. rubric:: Integrationsmethoden

----

.. _ana01l:

* Bei dieser Aufgabe entspricht die Variable :math:`x` der Zeit :math:`t`. Dies
  kommt bei physikalischen Aufgaben so häufig vor, dass eigens die Notation
  :math:`\dot{f} \equiv \frac{\mathrm{d}f}{\mathrm{d}t}` anstelle von :math:`f'
  \equiv \frac{\mathrm{d}f}{\mathrm{d}x}` eingeführt wurde.

  Da die Zu- beziehungsweise Abflussmenge in den jeweiligen Zeitabschnitten
  konstant ist, kann die im Waschbecken enthaltene Wassermenge sehr einfach
  berechnet werden. Hierbei wird folgende Integralregel verwendet:

  .. math::

      f(x) = c \quad \Longleftrightarrow \quad F(x) = c \cdot x

  Wendet man diese Regel an (mit :math:`t` anstelle von :math:`x` als Variable)
  auf den konstanten Volumenstrom :math:`\dot{V}_1` an, so ergibt sich mit
  :math:`t_0=0` für die im Waschbecken enthaltene Wassermenge am Ende des ersten
  Zeitabschnitts:

  .. math::

      \int_{t_0}^{t_1} \dot{V}_1 \cdot \mathrm{d}t = \big( \dot{V}_1 \cdot t
      \big) \Big | _{\mathrm{t_1}} ^{t_2} = \dot{V}_1 \cdot t_1 - \dot{V}_1
      \cdot t_0 = \unit[0,3]{\frac{l}{s}} \cdot \unit[30]{s}  = \unit[9,0]{l}

  Der zweite Term :math:`\dot{V}_1 \cdot t_0` ergibt hierbei den Wert Null, da
  :math:`t_0 = 0` ist. Zum Zeitpunkt :math:`t_1` sind somit neun Liter Wasser im
  Waschbecken enthalten.

  Im Zeitraum zwischen :math:`t_1` und :math:`t_2` ist der Zu- beziehungsweise
  Ablauf verschlossen und somit der fließende Volumenstrom gleich Null. Die im
  Zeitraum zwischen :math:`t_2` und :math:`t_3` abfließende Wassermenge kann
  wiederum nach dem obigen Prinzip berechnet werden; es muss lediglich das
  negative Vorzeichen des Volumenstroms berücksichtigt werden.

  .. math::

      \int_{t_2}^{t_3} \dot{V}_2 \cdot \mathrm{d}t = \big( \dot{V}_2 \cdot t
      \big) \Big | _{\mathrm{t_2}} ^{t_3} = \dot{V}_2 \cdot t_3 - \dot{V}_3
      \cdot t_2 = \dot{V}_2 \cdot (t_3 - t_2) = \unit[-1,2]{\frac{l}{s}} \cdot
      \unit[(50-45)]{s} = \unit[-6,0]{l}

  Die resultierende Wassermenge ergibt sich aus der Addition beider Integrale:

  .. math::

      V_{\mathrm{ges}} = \int_{t_0}^{t_1} \dot{V}_1 \cdot \mathrm{d}t  +
      \int_{t_2}^{t_3} \dot{V}_2 \cdot \mathrm{d}t  = \unit[(9,0-6,0)]{l} =
      \unit[3,0]{l}

  Unter den angegebenen Bedingungen werden zum Zeitpunkt :math:`t_3` somit drei
  Liter Wasser im Waschbecken sein.

  :ref:`Zurück zur Aufgabe <ana01>`

----

.. _ana02l:

* Das Integral :math:`\int_{0}^{1} x \cdot e^x \cdot \mathrm{d} x` kann am
  Einfachsten mittels einer :ref:`partiellen Integration <Partielle
  Integration>` berechnet werden, indem man sich die gegebene Funktion in der
  Gestalt :math:`f(x) = f_1(x) \cdot f_2'(x)` denkt; hierbei soll :math:`f_1(x)
  = x` und :math:`f_2'(x) = e^x` gesetzt werden.

  Für eine partielle Integration gilt allgemein:

  .. math::

      \int_{a}^{b} f_1(x) \cdot f_2'(x) = \Big(f_1(x) \cdot
      f_2(x)\Big)\Big|_{\mathrm{a}}^b - \int_{a}^{b} f_1'(x) \cdot f_2(x) \cdot
      \mathrm{d}x

  Zur Berechnung des Integrals muss somit die Ableitung der Funktion
  :math:`f_1(x)` sowie die Stammfunktion der Funktion :math:`f_2(x)` gefunden
  werden:

  .. math::

      f_1(x) = x \quad\; &\Longleftrightarrow \quad f_1'(x) \,= 1 \\
      f_2'(x) = e^x \quad &\Longleftrightarrow \quad F_2(x) = e^x \\

  Somit ergibt sich:

  .. math::

      \int_{0}^{1} x \cdot e^x \cdot \mathrm{d} x = \left( x \cdot e^x \right)
      \Big| _0^1 - \int_{0}^{1} 1 \cdot e^{x} \cdot \mathrm{d}x

  Das Integral :math:`\int_{0}^{1} 1 \cdot e^{x} \cdot \mathrm{d}x` kann
  unmittelbar als :math:`e^x\big|_0^1` geschrieben werden, da die Stammfunktion
  zu :math:`e^x` wiederum :math:`e^x` ist. Damit erhält man für die obige
  Gleichung:

  .. math::

      \int_{0}^{1} x \cdot e^x \cdot \mathrm{d} x &= \left( x \cdot e^x \right)
      \Big| _0^1 - e^x\Big| _0^1 \\ &= \, \Big( x \cdot e^x  - e^x \Big) \;
      \Big| _0^1 \\ &= \, \Big( (x - 1) \cdot e^x \Big) \Big|_0^1

  Die beiden Terme dürfen in der zweiten Zeile zusammen gezogen werden, da für
  beide die gleichen Integrationsgrenzen gelten. Zur Auswertung müssen diese nun
  noch eingesetzt werden. Damit erhält man:

  .. math::

      \int_{0}^{1} x \cdot e^x \cdot \mathrm{d} x = \Big((1-1) \cdot e^1 \Big) -
      \Big((0-1) \cdot e^0 \Big) = 1

  Das Integral ergibt wegen :math:`e^0 = 1` somit den Wert :math:`1`.

  :ref:`Zurück zur Aufgabe <ana02>`

----


.. foo

.. only:: html

    :ref:`Zurück zum Skript <Integralrechnung>`


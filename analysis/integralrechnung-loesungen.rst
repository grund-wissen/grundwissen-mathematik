
.. _Lösungen zur Integralrechnung:

Lösungen zur Integralrechnung
=============================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben zur
Integralrechnung>` zum Abschnitt :ref:`Integralrechnung <Integralrechnung>`.

.. _Lösungen zu Integrationsmethoden:

.. rubric:: Lösungen zu Integrationsmethoden

----

* Der Wert des Integrals :math:`\int_{0}^{1} x \cdot e^x \cdot \mathrm{d} x`
  kann mittels der Methode der :ref:`partiellen Integration <Partielle
  Integration>` berechnet werden, wenn man :math:`f_1(x) = x` und :math:`f_2(x)
  = e^x` setzt; damit folgt :math:`f_1'(x) = 1` und :math:`f_2'(x) = e^x`. Für
  das Integral gilt mit :math:`a=0` und :math:`b=1`:

  .. math::
      
      \int_{0}^{1} f_1(x) \cdot f_2'(x) = \big(f_1(x) \cdot
      f_2(x)\big)\big|_0^1 - \int_{0}^{1} f_1'(x) \cdot f_2(x) \cdot
      \mathrm{d} x

  Setzt man :math:`f_1(x)`, :math:`f_1'(x)`, :math:`f_2(x)` und :math:`f_2'(x)`
  in diese Gleichung ein, so ergibt sich:

  .. math::
      
    \int_{0}^{1} \left(x  \cdot e^x \right) \cdot \mathrm{d} x = \left( x \cdot
    e^x \right) \big |_0^1 -  \int_{0}^{1} \left(1  \cdot e^x\right) \cdot
    \mathrm{d} x

.. raw:: latex

    \rule{\linewidth}{0.5pt}

.. raw:: html

    <hr/>
    
.. only:: html

    :ref:`Zurück zum Skript <Integralrechnung>`


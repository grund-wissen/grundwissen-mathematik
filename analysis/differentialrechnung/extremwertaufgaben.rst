.. index:: Extremwertaufgabe
.. _Extremwertaufgaben:

Extremwertaufgaben
==================

Ein häufiger Anwendungsfall der Differentialrechnung sind so genannte
Extremwertaufgaben. Bei diesem Aufgabentyp wird zunächst eine
Funktionsgleichung aufgestellt, welche die gesuchte Größe als Variable
enthält. Wird die erste Ableitung dieser Funktionsgleichung gebildet und diese
gleich Null gesetzt, so erhält man eine oder mehrere Stellen, für welche die
gesuchte Größe minimal oder maximal ist.

*Beispiel:*

* Mit :math:`l = \unit[100]{m}` Zaunlänge soll ein rechteckiges Flächenstück mit
  möglichst großem Flächeninhalt :math:`A` eingezäunt werden. Welche Länge
  :math:`l` beziehungsweise Breite :math:`b` muss das eingezäunte Stück haben?

  Die Fläche des eingezäunten Rechtecks kann als :math:`A = l \cdot b`
  geschrieben werden. Der Umfang kann als  :math:`2 \cdot b + 2 \cdot l`
  ausgedrückt werden und soll gleich :math:`\unit[100]{m}` sein. Es gelten also
  folgende zwei Bedingungen:

  .. math::

      A = l \cdot b = \text{max} \\

  .. math::

      2 \cdot l + 2 \cdot b = \unit[100]{m} \quad \Longleftrightarrow \quad b =
      \unit[50]{m} - l


  Setzt man die nach :math:`b` aufgelöste zweite Gleichung in die erste
  Gleichung ein, so erhält man eine Funktionsgleichung, die als Variable die
  gesuchte Länge :math:`l` enthält:

  .. math::

      A = l \cdot b = l \cdot (50 - l) = -l^2 + \unit[50]{m} \cdot l

  Um die ideale Länge :math:`l_0` zu bestimmen, wird die Flächenfunktion
  :math:`A(l)` einmal nach der Variablen :math:`l` abgeleitet. Diese Ableitung
  kann dann gleich Null gesetzt werden:

  .. math::

      A' = -2 \cdot l + \unit[50]{m}  &\stackrel{!}= 0 \\[4pt]
      \Rightarrow l &= \unit[25]{m}

  Damit ist auch :math:`b = \unit[50]{m} - l = \unit[25]{m}`. Der Flächeninhalt
  :math:`A` beträgt bei dieser Aufteilung :math:`(\unit[25]{m})^2 = \unit[625]{m^2}`.


Die Herausforderung bei Extremwertaufgaben liegt in der mathematischen
Formulierung der Bedingungen, aus deren Kombination sich eine mathematische
Funktion mit der gesuchten Variablen aufstellen lässt. Die Bestimmung der
Extremwerte erfolgt dann stets nach dem gleichen Prinzip.




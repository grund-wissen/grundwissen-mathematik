.. index:: Lineares Gleichungssystem
.. _Lineare Gleichungssysteme:

Lineare Gleichungssysteme
=========================

Oftmals werden bei mathematischen Aufgaben nicht einzelne Gleichungen, sondern
vielmehr Kombinationen von mehreren Gleichungen mit mehreren Unbekannten
betrachtet. Damit ein solches Gleichungssystem eindeutig gelöst werden kann,
müssen (mindestens) ebenso viele Gleichungen vorliegen wie Unbekannte vorhanden
sind.

Sind die einzelnen Gleichungen eines Gleichungssystems linear, d.h. treten die
Variablen :math:`x _{\rm{i}}` nur erster Potenz auf, so spricht man von einem
linearen Gleichungssystem.

.. index:: Koeffizient

Im einfachsten Fall besteht ein lineares Gleichungssystem aus zwei Gleichungen
mit zwei Unbekannten. Bezeichnet man diese Variablen mit :math:`x _{\rm{1}}` und
:math:`x _{\rm{2}}`, so kann man das Gleichungssystem allgemein in folgender
Form darstellen:

.. math::
    
     a _{\rm{11}} \cdot x _{\rm{1}} +  a _{\rm{12}} \cdot x _{\rm{2}} &= b
     _{\rm{1}} \\
     a _{\rm{21}} \cdot x _{\rm{1}} +  a _{\rm{22}} \cdot x _{\rm{2}} &= b
     _{\rm{2}} \\

Die so genannten Koeffizienten :math:`a _{\rm{11}}` bis :math:`a _{\rm{22}}`
sind reelle Zahlen. Die erste Ziffer ihrer Indizes gibt jeweils die
Zeilennummer, die zweite Ziffer die Spaltennummer an. :math:`b _{\rm{1}}` und
:math:`b _{\rm{2}}` sind ebenfalls (reelle) Konstanten. Lösungen des
Gleichungssystems sind alle Zahlenpaare :math:`(x _{\rm{1}} \, ,\, x
_{\rm{2}})`, die sowohl die erste als auch die zweite Gleichung erfüllen.

Eine einzelne Gleichung mit zwei voneinander unabhängigen Variablen
lässt sich niemals eindeutig lösen. Die Werte der einen Variablen lassen sich
lediglich in Abhängigkeit der anderen Variablen angeben, wobei im Allgemeinen
unendlich viele Zahlenpaare als Lösungen existieren. Auf derartige
(funktionale) Zusammenhänge wird im Rahmen der Analysis näher eingegangen.


.. _Grundlegende Lösungsverfahren:

Grundlegende Lösungsverfahren
-----------------------------

Ein lineares Gleichungssystem der obigen Form lässt sich mit verschiedenen
Methoden lösen, die sich hinsichtlich ihres Rechenaufwands erheblich voneinander
unterscheiden. Um dies zu demonstrieren, werden die drei grundlegenden Verfahren
im folgenden Abschnitt anhand des jeweils gleichen Beispiels vorgestellt.
Dabei werden die Gleichungen zur besseren Übersichtlichkeit -- wie allgemein
üblich -- mit römischen Ziffern durchnummeriert. 


.. index:: Lineares Gleichungssystem; Einsetzungsverfahren
.. _Einsetzungsverfahren: 

* Das Einsetzungsverfahren: 

  Eine Gleichung kann nach einer Variablen, beispielsweise :math:`x _{\rm{1}}`,
  aufgelöst werden, und der sich ergebende Term an Stelle der entsprechenden
  Variablen in die andere Gleichung eingesetzt werden. Obwohl dies einfach
  klingt, bringt diese Methode den größten Rechenaufwand mit sich. 

  *Beispiel:* 

  .. math::
      
      \mathrm{(I)} : \qquad\qquad \phantom{0}-2 \cdot x _{\rm{1}} + \phantom{0}4
      \cdot x _{\rm{2}} &= -2\phantom{0} {\color{white} .}\\
      \mathrm{(II)}: \qquad\qquad \phantom{0}+3 \cdot x _{\rm{1}}  +
      \phantom{0}5 \cdot x _{\rm{2}} &= +36

  Löst man beispielsweise die Gleichung :math:`(\rm{I})` nach :math:`x
  _{\rm{1}}` auf, so folgt: 
      
  .. math::
      
      {\color{white} \ldots \qquad }\mathrm{(I)}: \qquad\qquad \;\, \phantom{+ 004 \cdot x
      _{\rm{2}}}-2 \cdot x _{\rm{1}}  &= -4 \cdot x _{\rm{2}} - 2 {\color{white}
      0 } \\
      \Rightarrow \qquad\qquad\qquad \phantom{+ 0004 \cdot x _{\rm{2}}}
      \phantom{1} x _{\rm{1}} &= +2 \cdot x _{\rm{2}} +1 \phantom{0} \\[10pt]

  Setzt man den resultierenden Ausdruck für :math:`x _{\rm{1}}` in Gleichung
  :math:`\rm{(II)}` ein, so erhält man:

  .. math::
      
      (x _{\rm{1}}) \text{ in } \mathrm{(II)}: \quad \;3 \cdot (2 \cdot x
      _{\rm{2}} + 1) + \phantom{0}5 \cdot x _{\rm{2}} &= +36 {\color{white} \qquad \ldots }\\
      6 \cdot x _{\rm{2}} + 3 \phantom{)} + \phantom{0}5 \cdot x _{\rm{2}} &= +36 \\
      + \,11 \cdot x _{\rm{2}} &= +33 \\
      \underline{\underline{x _{\rm{2}} }}&\underline{\underline{ \;= +3 \phantom{_3}}}
      
  Setzt man das Ergebnis :math:`x _{\rm{2}} = 3` in Gleichung :math:`\rm{(I)}`
  ein, so folgt schließlich: 
  
  .. math::
      
      (x _{\rm{2}} = 3) \text{ in } \mathrm{(I)}: \qquad \qquad \; -2 \cdot x
      _{\rm{1}} + 4 \cdot (3) &= -2 {\color{white} \;\;\;\;\; \ldots \ldots
      \ldots}\\
      -2 \cdot x _{\rm{1}}  &= -14 \\
      \underline{\underline{x _{\rm{1}} }}&\underline{\underline{\; = + 7 \phantom{_3}}}
  
  Die Lösung des Gleichungssystems ist somit :math:`(x _{\rm{1}} \, , \, x
  _{\rm{2}}) = (7 \, , \, 3)`.

  Das Einsetzungsverfahren ist, wie man sich leicht vorstellen kann, für
  komplexere Gleichungssyteme nicht ohne erheblichen Rechenaufwand anwendbar.


.. index:: Lineares Gleichungssystem; Gleichsetzungsverfahren
.. _Gleichsetzungsverfahren:

* Das Gleichsetzungsverfahren:

  Löst man beide Gleichungen nach einer Variablen, beispielsweise :math:`x
  _{\rm{1}}`, auf, so können die jeweils resultierenden Terme gleichgesetzt
  werden. Man erhält somit eine einzelne lineare Gleichung mit nur einer
  Unbekannten.

  *Beispiel:*
      
  .. math::

      {\color{white} \ldots \ldots\ldots}\mathrm{(I)} : \qquad\qquad
      -\phantom{0}2 \cdot x _{\rm{1}} + \phantom{0}4 \cdot x _{\rm{2}} &= -2
      {\color{white} \;.}\\
      \Rightarrow \qquad\qquad\qquad \phantom{+ 004
      \cdot x _{\rm{2}}} \phantom{1} x _{\rm{1}}  &= +2 \cdot x _{\rm{2}} +1 \phantom{0}
      \\[12pt]
      \mathrm{(II)}: \qquad\qquad +\phantom{0}3 \cdot x _{\rm{1}}  + \phantom{0}5 \cdot x _{\rm{2}} &= +36 \\
      \Rightarrow \qquad\qquad\qquad \phantom{+ 004
      \cdot x _{\rm{2}}} \phantom{1} x _{\rm{1}}  &= -\frac{5}{3} \cdot x _{\rm{2}} +12

  Setzt man die beiden Terme für :math:`x _{\rm{1}}` gleich, so ergibt sich
  folgende Gleichung, die gemäß der für lineare Gleichungen üblichen Methode
  nach :math:`x _{\rm{2}}` aufgelöst werden kann:

  .. math::

      {\color{white} \ldots}\mathrm{(I)} = \mathrm{(II)}: \quad \qquad \qquad  \qquad \;\; 2 \cdot x
      _{\rm{2}} + 1 &= -\frac{5}{3} \cdot x _{\rm{2}} + 12 \\
      \frac{11}{3} \cdot x _{\rm{2}} &= +11 \\
      \underline{\underline{x _{\rm{2}} }}&\underline{\underline{ \;= +3 \phantom{_3}}}

  Setzt man das Ergebnis :math:`x _{\rm{2}} = 3` wiederum in Gleichung
  :math:`\rm{(I)}` ein, so erhält man wie im ersten Beispiel :math:`x _{\rm{1}}
  = 7` und damit als Lösung :math:`(x _{\rm{1}} \, , \, x _{\rm{2}}) = (7\, ,\, 3)`.
            
  Auch die Gleichsetzungsmethode ist offensichtlich mit einigem Rechenaufwand
  verbunden und wird daher in der Praxis nur in seltenen Fällen angewendet.      
    

.. index:: Lineares Gleichungssystem; Additionsverfahren
.. _Additionsverfahren:

* Das Additionsverfahren:

  Werden zwei Gleichungen mit jeweils passenden Faktoren :math:`c _{\rm{1}}, c
  _{\rm{2}} \ne 0` multipliziert, so kann erreicht werden, dass die
  Koeffizienten einer Variablen, beispielsweise :math:`x _{\rm{1}}`, einen
  betraglich gleichen Wert mit unterschiedlichem Vorzeichen annehmen. 
  
  Anschließend geht man von der Annahme aus, dass ein Zahlenpaar :math:`(x
  _{\rm{1}} \, ,\, x _{\rm{2}})` als Lösung des Gleichungssystems existiert.
  Dadurch kann beispielsweise die erste Gleichung zur zweiten addiert werden, da
  (wenn :math:`(x _{\rm{1}} \, ,\, x _{\rm{2}})` die Gleichung erfüllt) auf
  beiden Seiten das Gleiche addiert wird.

  *Beispiel:*

  .. math::

      \mathrm{(I)} : \qquad\qquad -\phantom{0}2 \cdot x _{\rm{1}} + \phantom{0}4
      \cdot x _{\rm{2}} &= -2  {\color{white} \;.}\\
      \mathrm{(II)}: \qquad\qquad +\phantom{0}3 \cdot x _{\rm{1}}  +
      \phantom{0}5 \cdot x _{\rm{2}} &= +36 \\[12pt]

  Wird die erste Gleichung mit :math:`4` und die zweite Gleichung mit :math:`-5`
  multipliziert, so nehmen die bei :math:`x _{\rm{1}}` stehenden Koeffizienten
  gleiche Werte mit unterschiedlichen Vorzeichen an. 
      
  .. math::

      3 \cdot \phantom{\rm{I}}\mathrm{(I)}: \qquad \qquad  -\phantom{0}6 \cdot x
      _{\rm{1}} + 12 \cdot x _{\rm{2}} &= -6 {\color{white} \; \; \ldots}\\ 
      2 \cdot
      \mathrm{(II)}: \qquad \qquad +\phantom{0}6 \cdot x _{\rm{1}} + 10 \cdot x
      _{\rm{2}} &= +72

  Unter der Annahme, dass ein Zahlenpaar :math:`(x _{\rm{1}} \, ,\, x
  _{\rm{2}})` als Lösung existiert, kann die erste Gleichung nun zur zweiten
  addiert werden. Hierbei entfällt die Variable :math:`x _{\rm{1}}`, und wieder
  ergibt sich eine einzige Gleichung mit nur einer Unbekannten:

  .. math::
      
     3 \cdot \mathrm{(I)} + 2 \cdot \mathrm{(II)}:\qquad \qquad \qquad \qquad
     \quad \! 22 \cdot x _{\rm{2}} &=+66 {\color{white} \qquad \qquad \!\ldots }
     \\
      \underline{\underline{x _{\rm{2}} }}&\underline{\underline{ \;= +3 \phantom{_3}}}
  
  Setzt man das Ergebnis :math:`x _{\rm{2}} = 3` wiederum in Gleichung
  :math:`\rm{(I)}` ein, so erhält man wie im ersten Beispiel :math:`x _{\rm{1}}
  = 7` und damit als Lösung :math:`(x _{\rm{1}} \, , \, x _{\rm{2}}) = (7\, ,\, 3)`.

  Das Additionsverfahren ist im Allgemeinen mit dem geringsten Rechenaufwand
  verbunden und wird daher bevorzugt als grundlegende Lösungsmethode angewendet. 

Die wesentliche Annahme des Additionsverfahrens, dass das Gleichungssystem eine
eindeutige Lösung besitzt, trifft nicht für alle Gleichungsssysteme zu. Es
kann dennoch auch dann angewendet werden, wobei im Allgemeinen die folgenden
Fälle auftreten können

* Führt das Additionsverfahren auf eine Gleichung der Art :math:`1=1`, so
  entsprechen die beiden miteinander addierten Gleichungen einer einzigen
  Gleichung und einem Vielfachen dieser Gleichung. Somit liegt letztlich eine
  einzige Gleichung mit zwei Unbekannten vor, die im Allgemeinen nicht eindeutig
  lösbar ist, sondern unendlich viele Zahlenpaare :math:`(x _{\rm{1}} \, ,\, x
  _{\rm{2}})` als Lösung besitzt.

* Führt das Additionsverfahren auf eine Gleichung der Art :math:`0=1`, d.h.
  einen Widerspruch, so existiert keine Lösung für das Gleichungssystem. 
  (Dies ist vergleichbar damit, dass es beispielsweise kein :math:`x` gibt, für
  das zugleich :math:`x=5` und :math:`x=7` gilt.)

Das Additionsverfahren ist im Vergleich zum Einsetzungs- und
Gleichsetzungsverfahren meist mit erheblich weniger Rechenaufwand verbunden; es
stellt zugleich die Grundlage für den bei komplexeren Gleichungssystemen
genutzten Gaussschen Lösungsalgorithmus dar.

.. index:: 
    single: Lineares Gleichungssystem; Gauss'scher Lösungsalgorithmus
    single: Gauss'scher Lösungsalgorithmus
.. _Gaussscher Lösungsalgorithmus:

Der Gauss'sche Lösungsalgorithmus
---------------------------------

Besteht ein Gleichungssystem aus mehr als zwei Gleichungen (mit mehr als zwei
Unbekannten), so wird üblicherweise der nach `Carl Friedrich Gauss
<https://de.wikipedia.org/wiki/Gauss>`_ benannte Algorithmus angewendet. Dieses
Verfahren soll zunächst am Beispiel eines Gleichungssystems mit drei Gleichungen
und drei Unbekannten demonstriert werden. 
    
Ein Gleichungssystem mit drei Gleichungen und drei Unbekannten hat allgemein
folgende Form: 

.. math::
    
     a _{\rm{11}} \cdot x_1 + a _{\rm{12}} \cdot x_2 + a _{\rm{13}} \cdot x_3 &= b_1 \\
     a _{\rm{21}} \cdot x_1 + a _{\rm{22}} \cdot x_2 + a _{\rm{23}} \cdot x_3 &= b_2 \\
     a _{\rm{31}} \cdot x_1 + a _{\rm{32}} \cdot x_2 + a _{\rm{33}} \cdot x_3 &= b_3 \\

Um ein derartiges Gleichungssystem zu lösen, ist es hilfreich, dieses
schrittweise in eine treppenartige Form zu bringen. Hierzu geht man nach
folgendem Schema vor:

* Als erstes wird eine der Gleichungen ausgewählt ("Ausgangsgleichung"). 
* Mittels des Additionsverfahrens wird paarweise die Ausgangsgleichung und eine
  der beiden anderen Gleichungen mit passenden Faktoren multipliziert, um zu
  erreichen, dass die Koeffizienten der ersten Variablen jeweils betraglich
  gleiche Werte mit unterschiedlichen Vorzeichen annehmen. 
* Die Ausgangsgleichung und je eine weitere Gleichung werden paarweise addiert,
  um ein Wegfallen der ersten Variablen zu erreichen. 
* Das Gleichungssystem mit drei Gleichungen und drei Unbekannten ist so auf ein
  Gleichungssystem mit zwei Gleichungen und zwei Unbekannten reduziert worden.
  [#GAS]_ Die obigen Verfahrensschritte können auf dieses erneut angewendet
  werden. 

Der Gauss'sche Algorithmus führt somit Gleichungssysteme mit vielen Gleichungen
bzw. Unbekannten schrittweise auf Gleichungssysteme mit weniger Gleichungen und
Unbekannten zurück, bis nur noch eine Gleichung mit einer Unbekannten übrig ist.
Diese Gleichung kann einfach gelöst werden, und durch Einsetzen der Lösung in
die Ausgangsgleichung(en) können wiederum schrittweise auch die Lösungen aller
anderen Unbekannten mühelos berechnet werden.

*Beispiel:*
    
  .. math::
    
      {\color{white} \ldots\ldots \;\,}\mathrm{(I)}: \quad \phantom{-0}8 \cdot x
      _{\rm{1}} + \phantom{0}2 \cdot x _{\rm{2}} + \phantom{0}3 \cdot x
      _{\rm{3}} &= +15 \\
      \mathrm{(II)}: \quad \phantom{-0}6 \cdot x _{\rm{1}} - \phantom{0}1 \cdot
      x _{\rm{2}} + \phantom{0}7 \cdot  x _{\rm{3}} &= -13 \\
      \mathrm{(III)}: \quad -\phantom{0}4 \cdot x _{\rm{1}} + \phantom{0}5 \cdot x
      _{\rm{2}} -\phantom{0}3 \cdot  x _{\rm{3}} &= +21

  Wählt man in diesem Beispiel Gleichung :math:`\rm{(I)}` als Ausgangsgleichung
  und multipliziert sie mit drei, so kann man Gleichung :math:`\rm{(II)}`
  passenderweise mit Minus vier multiplizieren, um bei beiden Gleichungen
  identische Koeffizienten mit unterschiedlichem Vorzeichen für :math:`x
  _{\rm{1}}` zu erreichen. In gleicher Weise kann man Gleichung :math:`\rm{(I)}`
  unverändert lassen und Gleichung :math:`\rm{(III)}` mit zwei multiplizieren,
  um auch bei diesem Gleichungspaar identische Koeffizienten mit
  unterschiedlichem Vorzeichen für :math:`x _{\rm{1}}` zu erreichen: 

  .. math::
    
      3 \cdot \phantom{\rm{II}}\mathrm{(I)}: \quad \phantom{-}24 \cdot x _{\rm{1}} + \phantom{0}6 \cdot x _{\rm{2}} + \phantom{0}9 \cdot x
      _{\rm{3}} &= + 45 \\
      -4 \cdot \phantom{\rm{I}}\mathrm{(II)}: \quad -24 \cdot x _{\rm{1}} +\phantom{0}4 \cdot x _{\rm{2}} -28 \cdot x _{\rm{3}} &= +52 \\[12pt]
      1 \cdot \phantom{\rm{II}}\mathrm{(I)}: \quad \phantom{-0}8 \cdot x _{\rm{1}} + \phantom{0}2 \cdot
      x _{\rm{2}} + \phantom{0}3 \cdot x _{\rm{3}} &= + 15 \\
      2 \cdot \mathrm{(III)}: \quad -\phantom{0}8 \cdot x _{\rm{1}} + 10 \cdot x _{\rm{2}} - \phantom{0}6 \cdot x
      _{\rm{3}} &= +42 \\

  Wird jeweils die Ausgangsgleichung zu den beiden anderen Gleichungen addiert, so
  erhält man ein neues Gleichungssystem mit zwei Gleichungen und zwei Unbekannten.
  Diese werden mit römischen Ziffern gemäß ihrer beiden ursprünglichen Gleichungen
  nummeriert und als Zeichen dafür, dass es sich um hergeleitete Gleichungen
  handelt, mit einem Hochkomma markiert:

  .. math::
    
      \Rightarrow \;\; \mathrm{(II')}: \quad \! \phantom{-40 \cdot x _{\rm{1}}} +10 \cdot x _{\rm{2}} -19 \cdot x _{\rm{3}} &=
      +97 \\
      \mathrm{(III')}: \quad \! \phantom{-40 \cdot x _{\rm{1}}} +12 \cdot x _{\rm{2}} -\phantom{0}3 \cdot x _{\rm{3}} &= +57 \\

  Um das Additionsverfahren erneut anwenden zu können, müssen wiederum beide
  Gleichungen mit geeigneten Faktoren multipliziert werden, um betraglich gleiche
  Koeffizienten mit unterschiedlichen Vorzeichen für :math:`x _{\rm{2}}` zu
  erreichen. Dazu kann die neue Ausgangsgleichung :math:`\rm{(II')}` mit Minus
  sechs und die zweite Gleichung mit fünf multipliziert werden:

  .. math::
    
      -6 \cdot \;\!\phantom{\rm{I}}\mathrm{(II')}: \;\; \phantom{-40 \cdot x _{\rm{1}}} -60 \cdot x _{\rm{2}} +114 \cdot x _{\rm{3}} &=
      -582 \\
      5 \cdot \;\!\mathrm{(III')}: \;\; \phantom{-40 \cdot x _{\rm{1}}} +60 \cdot x
      _{\rm{2}} -\phantom{0}15 \cdot x _{\rm{3}} &= +285 \\

  Eine Addition beider Gleichungen führt schließlich auf eine einzige Gleichung,
  die nur noch die Variable :math:`x _{\rm{3}}` beinhaltet.

  .. math::
    
      \Rightarrow \;\; \mathrm{(III'')}: \quad \, \phantom{-40 \cdot x _{\rm{1}} +10 \cdot x _{\rm{2}}} +99 \cdot x _{\rm{3}} =
      -297 {\color{white} .}\\
      \underline{\underline{\phantom{_3}x _{\rm{3}}  = -3 \phantom{00}}} {\color{white} .}

  Somit ist eine eindeutige Lösung für die Variable :math:`x _{\rm{3}}` gefunden.
  Um die Lösungen für die Variablen :math:`x _{\rm{1}}` und :math:`x _{\rm{2}}`
  zu berechnen, setzt man die gefundene Lösung zunächst in die vorherige
  Ausgangsgleichung :math:`\rm{(II')}` ein. Damit kann :math:`x _{\rm{2}}`
  einfach bestimmt werden:
  
  .. math::
      
      (x _{\rm{3}} = -3) \text{ in } \mathrm{(II')}:\;  \phantom{-40 \cdot x
      _{\rm{1}}} +10 \cdot x _{\rm{2}} -19 \cdot (-3) = +97 {\color{white} \ldots
      \ldots \ldots }\\ 40 \cdot x _{\rm{2}} = +40{\color{white} \ldots
      \ldots \ldots }\\
      \underline{\underline{\phantom{_3}x
      _{\rm{2}}  = +4 \phantom{_3}}} {\color{white} \ldots
      \ldots \ldots }
  
  Setzt man die Lösungen :math:`x _{\rm{3}} = -3` und :math:`x _{\rm{2}} = 4`
  schließlich in die erste Ausgangsgleichung :math:`\rm{(I)}` ein, so erhält man
  auch die Lösung für die letzte Variable :math:`x _{\rm{1}}`:
  
  .. math::
      
      \left.\begin{aligned}
          (x _{\rm{2}} = +4) \\
          (x _{\rm{3}} = -3)
          \end{aligned}
      \right\} 
      \text{ in } \mathrm{(I)}: \quad  8 \cdot x _{\rm{1}} +2 \cdot (+4)
      +\phantom{0}3 \cdot (-3) = +15 {\color{white}\ldots \ldots
      \ldots}\\[-10pt]
      8 \cdot x _{\rm{1}} = +16 {\color{white}\ldots \ldots \ldots}\\
      \underline{\underline{\phantom{_1}x _{\rm{1}}  = +2 \phantom{_3}}} {\color{white}\ldots \ldots \ldots}
  
  Damit sind alle Variablen bestimmt. Die Lösung des Gleichungssystems ist
  :math:`(x _{\rm{1}} \, ,\, x _{\rm{2}} \, ,\, x _{\rm{3}}) = (2\, ,\, 4\, , \,
  -3)`.

..  Mit Hilfe des Gauss'schen Algorithmus lassen sich mit Computer-Algebra-Systemen
..  auch komplexe lineare Gleichungssysteme mit mehreren tausend Gleichungen und
..  ebenso vielen Unbekannten in kürzester Zeit lösen.

..  Ein Gleichungssystem heißt unterbestimmt , wenn die Zahl der Gleichungen
..  geringer ist als die Zahl der Unbekannten. Ein Gleichungssystem heißt
..  überbestimmt , wenn die Zahl der Gleichungen höher ist als die Zahl der
..  Unbekannten.

.. raw:: html

    <hr />
    
.. only:: html

    .. rubric:: Anmerkungen:

.. [#GAS] Allgemein kann auf diese Weise ein Gleichungssystem mit :math:`n` Gleichungen und
    :math:`n` Unbekannten auf ein Gleichungssystem mit :math:`(n-1)` Gleichungen
    und :math:`(n-1)` Unbekannten reduziert werden.


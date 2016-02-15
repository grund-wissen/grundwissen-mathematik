.. _Teilbarkeit und Primzahlen:

Exkurs: Teilbarkeit und Primzahlen
==================================

.. index:: Teiler

Lässt sich eine natürliche Zahl :math:`a` ohne Rest durch eine natürliche
Zahl :math:`b` teilen, so nennt man :math:`a` ein Vielfaches von :math:`b` oder
:math:`b` einen Teiler von :math:`a`. Bisweilen schreibt man anstelle von
":math:`b` ist Teiler von :math:`a`" auch in Kurzform :math:`b\,|\,a`.

.. Anmerkung: Bitte nicht verwechseln mit Operator "|" in der Informatik!

Jede Zahl :math:`a` hat die Zahl :math:`1` als Teiler, denn es gilt stets
:math:`1 \cdot a = a`. Ein Teiler, der sowohl zu einer Zahl :math:`a` als auch
zu einer Zahl :math:`b` gehört, heißt gemeinsamer Teiler von :math:`a` und
:math:`b`. Haben beide Zahlen keinen gemeinsamen Teiler außer der Zahl
:math:`1`, so nennt man die Zahlen teilerfremd.


.. index:: Primzahl
.. _Primfaktorenzerlegung:

.. rubric:: Die Primfaktorenzerlegung

Hat eine natürliche Zahl :math:`p > 1` nur zwei Teiler (:math:`1` und die Zahl
:math:`p` selbst), so heißt sie Primzahl. Die ersten Primzahlen :math:`(p <
100)` sind:

.. math::

     2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
     73, 79, 83, 89, 97.

Jede Zahl, die keine Primzahl ist, wird zerlegbar genannt, denn sie lässt sich
ohne Rest in mehrere andere Zahlen aufteilen. Hierzu ist folgendes Vorgehen
nützlich:

1. Zunächst wird geprüft, ob die zu prüfende Zahl :math:`a` durch eine
   beliebige, betraglich kleinere Primzahl :math:`p < a` teilbar ist.
2. Wird eine Primzahl :math:`p` gefunden ist, die ein Teiler von :math:`a` ist,
   so wird diese Primzahl notiert und :math:`a` durch :math:`p` geteilt.
3. Mit dem Ergebnis der Division wird erneut mit dem 1. Schritt begonnen. Diese
   Wiederholung wird so lange fortgesetzt, bis keine weitere Aufteilung
   in Primzahlen möglich ist.

Das obige Verfahren wird auch als "Primfaktorzerlegung" einer Zahl bezeichnet.

*Beispiel:*

.. math::

    17\,640 \; &= 2 \cdot 8820 \\ &= 2 \cdot 2 \cdot 4410 \\ &= 2 \cdot 2  \cdot 2
    \cdot 2205 \\ &= 2 \cdot 2 \cdot 2 \cdot 3 \cdot 735 \\ &= 2 \cdot 2 \cdot 2
    \cdot 3 \cdot 3 \cdot 245 \\ &= 2 \cdot 2 \cdot 2
    \cdot 3 \cdot 3 \cdot 5 \cdot 49 \\ &= 2 \cdot 2 \cdot 2
    \cdot 3 \cdot 3 \cdot 5 \cdot 7 \cdot 7 \\[10pt]
    \Rightarrow 17\,640 \; &=  \quad  \; 2^3 \;\;\;  \cdot \;\; 3^2 \; \cdot 5^1 \cdot \, 7^2

Multipliziert man alle Primfaktoren einer Zahl miteinander, wobei einzelne
Faktoren mehrfach auftreten dürfen, so erhält man als Ergebnis wiederum die
ursprüngliche Zahl. Die gleiche Methode wird auch zur Ermittlung von Primzahlen
mittels Computern eingesetzt. [#SE]_


.. _Weitere Teilbarkeitsregeln:

.. rubric:: Weitere Teilbarkeitsregeln

| Anhand der Ziffern einer Zahl lassen sich teilweise ebenfalls
  Teilbarkeitseigenschaften direkt ablesen. [#]_
| Eine ganze Zahl ist teilbar durch

* :math:`2`, wenn die letzte Ziffer durch :math:`2` teilbar ist.
* :math:`3`, wenn die Quersumme der Zahl durch :math:`3` teilbar ist.
* :math:`4`, wenn die aus den beiden letzten Ziffern bestehende Zahl durch 4
  teilbar ist.
* :math:`5`, wenn die letzte Ziffer gleich :math:`0` oder :math:`5` ist.
* :math:`6`, wenn die letzte Ziffer durch :math:`2` und die Quersumme der Zahl
  durch :math:`3` teilbar ist.
* :math:`8`, wenn die aus den drei letzten Ziffern bestehende Zahl durch
  :math:`8`
  teilbar ist.
* :math:`9`, wenn die Quersumme der Zahl durch :math:`9` teilbar ist.
* :math:`10`, wenn ihre letzte Ziffer gleich :math:`0` ist.

.. index:: Quersumme

Die Quersumme bezeichnet dabei die Summe der Ziffern einer Zahl. Beispielsweise
ist die Quersumme der Zahl :math:`483 = 4 + 8 + 3 = 15`; somit ist nach der
obigen Regel :math:`483` durch :math:`3` teilbar. Für die Zahl :math:`7`
existiert keine triviale Teilbarkeitsregel.

..  .. _Modulo-Rechnung und Restklassen:

..  .. rubric:: Modulo-Rechnung und Restklassen

..  ...


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#SE] Der als "Sieb des Eratosthenes" bekannte Algorithmus prüft dabei gemäß
    der obigen Methode für beliebig große natürliche Zahlen, ob diese bereits eine
    der bereits bekannten Primzahlen als Faktor enthalten. Ist dies der Fall, so
    wird die Zahl (und ihre Vielfachen) als Nicht-Primzahl markiert und die
    Prüfung mit der nächsten Zahl fortgesetzt. Enthält eine Zahl keine kleinere
    Primzahl als Faktor, so stellt sie eine Primzahl dar und wird in die Liste
    der bekannten Primzahlen aufgenommen.

.. [#] Der Beweis hierfür ist beispielsweise in [Bittner1979]_ auf Seite 33 ff.
    aufgeführt.

.. https://de.wikibooks.org/wiki/Primzahlen:_Tabelle_der_Primzahlen_(2_-_100.000)


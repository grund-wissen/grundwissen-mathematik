
.. _Lösungen Logik:
.. _Lösungen zur Logik:

Lösungen zur Logik
==================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Logik>` zum Abschnitt :ref:`Logik <Logik>`.

----

.. _lol01:

* Die Gleichung stellt eine Aussageform dar, da in ihr als Charakteristikum
  (mindestens) eine unbestimmte Variable auftritt.

  Weist man der Variablen den Wert :math:`x=1` zu, so geht die Aussageform über
  in die Aussage :math:`1 - 5 + 6 = 0`, was offensichtlich als Wahrheitswert
  "falsch" hat. Weist man der Variablen hingegen den Wert :math:`x=2` zu, so
  ergibt sich die wahre Aussage :math:`4 - 10 + 6 = 0`.

  :ref:`Zurück zur Aufgabe <lo01>`

----

.. _lol02:

* Die mathematiche Kurzschreibweise für "10 ist Teiler von :math:`x`" lautet
  :math:`10|t` ("Zehn teilt :math:`x`"). Da es sich bei der Aussage um eine
  Folgerung  ("Implikation") handelt, kann also geschrieben werden:

  .. math::

      10|x \quad \Rightarrow \quad 2|x

  :ref:`Zurück zur Aufgabe <lo02>`

----

.. _lol03:

* Die beiden Aussagen lassen sich nur mit einer Implikation sinnvoll verknüpfen.
  Jedes Quadrat hat vier gleich große Innenwinkel. Umgekehrt ist jedes Viereck
  mit vier gleich großen Innenwinkel zwar ein Rechteck, aber nicht zwingend ein
  Quadrat. Zusammengefasst gilt also:

  .. math::

      A_1 \quad \Rightarrow \quad A_2

  Wird die zweite Aussage um den Zusatz "und es hat gleich lange Seiten"
  ergänzt, so sind die erste und die zweite Aussage äquivalent zueinander. In
  diesem Fall kann man also schreiben:

  .. math::

      {\color{white}\ldots}A_1 \quad \Leftrightarrow \quad A_{\mathrm{2,neu}}

  :ref:`Zurück zur Aufgabe <lo03>`

----

.. _lol04:

*

  - Bei einer UND-Verknüpfung müssen beide Bedingungen gleichzeitig erfüllt
    sein, damit ihr Wahrheitswert "wahr" ist (die Aussage also zutrifft).
    Demnach wäre es bei der Anweisung "Rauchen UND Umgang mit offenen Licht ist
    verboten!" aus rein logischer Sicht immer noch erlaubt, *entweder* zu
    rauchen *oder* Umgang mit offenem Licht zu haben; es darf nur nicht beides
    zugleich eintreten. In der Praxis ist es allerdings wohl auch bei einer
    derart schlampig formulierten Warnung empfehlenswert, sicherheitshalber
    beides zu unterlassen...

  - Bei dem wohl eher in Kneipen anzutreffenden Wandspruch "drink OR drive"
    sollte es wohl eher "drink XOR drive" heißen, denn so gilt die
    ODER-Verknüpfung für die Fälle "not drink and drive" und "drink and not
    drive", allerdings auch für "drink and drive". Insbesondere vor letzterem
    ist aber dringend abzuraten...

    Während des Studiums hieß es bei uns daher: "Don't drink and
    d(e)rive!" ;-)

  :ref:`Zurück zur Aufgabe <lo04>`

----

.. _lol05:

* Durch eine Adjunktion der Aussagen :math:`A_1:\; 1<2` und :math:`A_2:\;1=2`
  entsteht die Aussage :math:`1 \le 2`. Die Aussage :math:`A_1` ist wahr, die
  Aussage :math:`A_2` hingegen ist falsch. Die ODER-Verknüpfung beider Aussagen
  ist wahr (da zumindest eine der beiden Teilaussagen wahr ist).

  :ref:`Zurück zur Aufgabe <lo05>`

----

.. _lol06:

* Durch eine Konjunktion der Aussagen :math:`A_1: 134 \text{ ist durch 2
  teilbar.}` und :math:`A_2: 134 \text{ ist durch 3 teilbar.}` entsteht die
  Aussage :math:`134 \text{ ist durch 2 und 3 teilbar.}`? Die Aussage
  :math:`A_1` ist wahr, die Aussage :math:`A_2` hingegen ist falsch.
  Die UND-Verknüpfung beider Aussagen ist falsch (die nicht beide Aussagen
  zugleich wahr sind).

  :ref:`Zurück zur Aufgabe <lo06>`

----

.. _lol07:

* Die Antivalenz der beiden Aussagen ergibt die Aussage "Der Zug fährt entweder
  nach Hamburg oder Berlin". Ob der Wahrheitswert dieser Gesamt-Aussage wahr
  oder falsch ist, hängt selbstverständlich vom jeweiligen Zug ab. Wir können
  allerdings :ref:`o.B.d.A. <gw:oBdA>`  annehmen, der Zug sei intakt und habe
  nur genau diese zwei Fahrt-Optionen: Dann trifft stets genau eine der beiden
  Aussagen zu (niemals keine, niemals beide zugleich).

  :ref:`Zurück zur Aufgabe <lo07>`

----

.. _lol08:

* Die Implikation beider Aussagen liefert die Gesamt-Aussage "Wenn die Erde ein
  Würfel ist, dann ist die Sonne eine Pyramide." Beide Teil-Aussagen sind
  falsch, die Implikation hingegen richtig (da eine Folgerung aus einer falschen
  Aussage definitionsgemäß stets wahr ist).

  :ref:`Zurück zur Aufgabe <lo08>`

----

.. _lol09:

* Die Adjunktion (ODER-Verknüpfung) einer wahren und einer falschen Aussage (im
  Computer-Bereich: "Bedingung") ist stets wahr; die Gesamt-Aussage ergibt somit
  den logischen Wert "wahr".

  :ref:`Zurück zur Aufgabe <lo09>`

----


.. .

.. only:: html

    :ref:`Zurück zum Skript <Logik>`


.. index:: Zinsrechnung
.. _Zinsrechnung:

Zinsrechnung
============

Ein Anwendungsbeispiel für geometrische Reihen ist die Zinsrechnung. Unter
Zinsen versteht man allgemein einen Betrag, der für das Überlassen einer
Geldmenge ("Kapital") innerhalb einer bestimmten Zeit ("Zinsperiode",
üblicherweise ein Kalenderjahr) zu bezahlen ist.

Die Höhe der Zinsen ist von drei Größen abhängig: Der überlassenen Geldmenge
:math:`K_0`, der Dauer :math:`t` der Überlassung ("Laufzeit"), und dem so
genannten Zinssatz :math:`p`. Der Zinssatz gibt prozentual den Anteil an Geld
an, der am Ende einer Zinsperiode bezahlt werden muss.

In der Bankenpraxis entspricht ein Jahr 360 Tagen beziehungsweise jeder Monat 30
Tagen. Bezeichnet man man bei kürzeren Zeiträumen als einem Jahr die Zahl der
Zinstage mit :math:`n`, so gilt :math:`t = \frac{n}{360}`.

.. _Einfache Verzinsung:

Einfache Verzinsung
-------------------

Bei einer einfachen Verzinsung werden die Zinsen am Ende einer Zinsperiode
ausgezahlt; sie werden in den folgenden Perioden somit nicht weiter mit verzinst.
Das Kapital wächst in diesem Fall linear mit der Zeit an.

Mit einer einfachen Verzinsung wird in der Praxis vor allem dann gerechnet, wenn
der Zeitraum zwischen den Zinszahlungen kürzer als eine Zinsperiode ist.

Die nach der Zeit :math:`t` anfallenden Zinsen :math:`Z_{\mathrm{t}}` werden
folgendermaßen berechnet:

.. math::
    :label: eqn-zinsen

    Z_{\mathrm{t}} &= K_0 \cdot p \cdot t \\[5pt]

Die Zeit :math:`t` wird dabei als Bruchteil oder Vielfaches der Zinsperiode
angegeben. Die Zinsen :math:`Z_{\mathrm{t}}` werden am Ende einer Zinsperiode dem
Kapital aufaddiert:

.. math::
    :label: eqn-kapital-mit-zinsen

    K_{\mathrm{t}} &= K_0 + Z_{\mathrm{t}} = K_0 \cdot (1 + p \cdot t)

*Beispiele*:

* Eine Kapital :math:`K_0=\unit[2000]{Eur}` wird am 1. März eines Jahres zu
  einem jährlichen Zinssatz von :math:`p=1,5\%` auf eine Bank eingezahlt und am 1.
  September wieder abgehoben. Auf welchen Betrag  :math:`K_{\mathrm{t}}` hat das
  Kapital in diesem Fall zugenommen?

  Das Kapital wird für sechs Monate, also :math:`\unit[180]{Tage}`
  beziehungsweise :math:`t=\unit[\frac{180}{360}]{Jahr}` verzinst. Für den
  Betrag der Zinsen gilt mit :math:`K_0=\unit[2000]{Eur}` und :math:`p=0,015`:

  .. math::

     Z_{\mathrm{t}} = K_0 \cdot p \cdot t = \unit[2000]{Eur} \cdot 0,015 \cdot
     \frac{180}{360} = \unit[15]{Eur}

  Das Kapital beträgt am Ende somit :math:`\unit[(2000 + 15)]{Eur}`.

* Eine Geldmenge von :math:`K_0 = \unit[10\,000]{Eur}` wird für
  :math:`t=\unit[1]{Jahr}` zu einem jährlichen Zinssatz von :math:`p=7\%` von
  einer Bank geliehen. Wie viel Geld muss am Ende des Jahres zurück gezahlt
  werden?

  Für den Betrag an Zinsen gilt mit :math:`K_0=\unit[10\,000]{Eur}`,
  :math:`p=0,07` und :math:`t=1`:

  .. math::

     Z_{\mathrm{t}} = K_0 \cdot p \cdot t = \unit[10\,000]{Eur} \cdot 0,07 \cdot
     1 = \unit[700]{Eur}

  Am Endes des Jahres müssen somit :math:`\unit[(10\,000 + 700)]{Eur}` gezahlt
  werden.

.. rubric:: Barwertvergleich

Das Endkapital :math:`K_{\mathrm{t}}` nach der Zeit :math:`t` wird auch als
Zeitwert bezeichnet; entsprechend wird der Kapitalwert :math:`K_0` zum Zeitpunkt
:math:`t=0` auch Barwert genannt. Kennt man das Endkapital :math:`K_{\mathrm{t}}`
zu einem Zeitpunkt :math:`t>0`, so kann nach Umstellung der obigen Formel auch
der zugrunde liegende Barwert berechnet werden:

.. math::
    :label: eqn-barwert

    K_0 = \frac{K_{\mathrm{t}}}{1 + p \cdot t}

Ein so genannter Barwertvergleich kann insbesondere genutzt werden, wenn
Zahlungen zu unterschiedlichen Zeitpunkten miteinander verglichen werden sollen.
In diesem Fall bezieht man üblicherweise alle Zahlungen auf den Zeitpunkt
:math:`t=0`.

*Beispiel:*

* Eine Rechnung kann entweder innerhalb von :math:`\unit[7]{Tagen}` mit
  :math:`2\%` Preisnachlass ("Skonto") oder innerhalb von
  :math:`\unit[30]{Tagen}` ohne Preisnachlass gezahlt werden. Welchem Zinssatz
  entspräche hierbei eine Zahlung nach :math:`\unit[5]{Tagen}`?

  Bei einer sofortigen Zahlung muss bei :math:`2\%` Skonto ein Kapital von
  :math:`K_0 = 0,98 \cdot K_{\mathrm{t}}` aufgebracht werden; die Zeitdifferenz
  zwischen einer Zahlung nach :math:`5` und nach :math:`30` Tagen beträgt
  :math:`\unit[25]{T}`, also ist :math:`t = \frac{25}{360}`. Somit gilt:

  .. math::

      0,98 \cdot K_{\mathrm{t}} = \frac{K_{\mathrm{t}}}{1 + p \cdot \frac{25}{360}}

  Multipliziert man diese Gleichung mit dem Nenner der rechten Seite und
  dividiert durch :math:`K_{\mathrm{t}}`, so ergibt sich folgende Gleichung:

  .. math::

      0,98 + 0,98 \cdot p \cdot \frac{25}{360} &= 1 \\
      \Rightarrow \; p & \approx 0,294

  Der Preisnachlass entspricht, bezogen auf den angegebenen Zeitraum, somit
  einem Zinssatz von etwa :math:`p = 29,4\%`.

.. _Zinseszinsrechnung:

Zinseszinsrechnung
------------------

Werden die Zinsen nach einer Zinsperiode weiter verzinst, so entstehen so
genannte Zinseszinsen.

Nach einer Zinsperiode ist das ursprüngliche Kapital :math:`K_0` entsprechend
der einfachen Verzinsung um die Zinsmenge :math:`Z_1` auf den Betrag
:math:`K_1` angewachsen. Es gilt also:

.. math::

    K_1 = K_0 + Z_1 = K_0 + \left( 1 + p \right)

Im zweiten Jahr wird das Kapital :math:`K_1` verzinst. Für die sich ergebenden
Zinsen :math:`Z_2` beziehungsweise das Kapital :math:`K_2` nach zwei Jahren
gilt:

.. math::

    K_2 = K_1 + Z_2 = K_1 \cdot \left(1 + p \right) = K_0 \cdot (1 + p)^2

Der Faktor :math:`(1+p)^n` wird Aufzinsungsfaktor genannt und häufig auch mit
:math:`q` bezeichnet. Nach :math:`n` Jahren Laufzeit ergibt sich damit eine
Zins- bzw. Kapitalmenge:

.. math::
    :label: eqn-zinseszins

    K_{\mathrm{n}} = K_0 \cdot (1 + p)^n = K_0 \cdot q^n

Diese nach dem Mathematiker `Gottfried Wilhelm Leibniz
<https://de.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz>`_ benannte
Zinseszinsformel entspricht formal einer :ref:`geometrischen Reihe <Geometrische
Reihen>`.

Ebenso wie bei der einfachen Verzinsung kann bei einem bekannten Zinssatz
:math:`p` und einer gegebenen Laufzeit :math:`n \cdot t` auf das Anfangskapital
:math:`K_0` geschlossen werden, wenn das Endkapital :math:`K_\mathrm{n}` bekannt
ist. Als Barwert-Formel der Zinseszinsrechung ergibt sich:

.. math::
    :label: eqn-barwert-zinseszins

    K_0 = \frac{K_{\mathrm{n}}}{(1 + p)^n}

Die Größe :math:`\frac{1}{(1+p)^n} = \frac{1}{q^n}` wird auch Abzinsungsfaktor
genannt, die Berechnung des Barwerts als Diskontieren bezeichnet. Diese Methode
kann beispielsweise verwendet werden, um monatliche Ratenzahlungen mit einer
einmaligen Zahlung zu vergleichen.

Ist in der obigen Gleichung der Zinssatz :math:`p` oder die Laufzeit :math:`t`
gesucht, während alle anderen Größen gegeben sind, so kann die Gleichung
entsprechend aufgelöst werden:

* Kennt man das Anfangskapital :math:`K_0`, das Endkapital :math:`K_{\mathrm{n}}`
  sowie Anzahl :math:`n` an Zinsperioden, so gilt für den zugehörigen Zinssatz
  :math:`p`:

  .. math::

     (1+p)^n = \frac{K_{\mathrm{n}}}{K_0} \quad \Leftrightarrow \quad p =
     \sqrt[n]{\frac{K_{\mathrm{n}}}{K_0}}-1

* Kennt man das Anfangskapital :math:`K_0`, das Endkapital :math:`K_{\mathrm{n}}`
  sowie den Zinssatz :math:`p`, so gilt mit den :ref:`Rechenregeln für
  Logarithmen <Rechenregeln für Logarithmen>` für die zugehörige Anzahl
  :math:`n` an Zinsperioden:

  .. math::

     (1+p)^n = \frac{K_{\mathrm{n}}}{K_0} \quad \Leftrightarrow \quad n \cdot \ln{(1
     + p)} = \ln{\left(\frac{K_{\mathrm{n}}}{K_0}\right)} \quad \Longleftrightarrow
     \quad n = \frac{\ln{(K_{\mathrm{n}})} - \ln{(K_0)}}{\ln{(1-p)}}

So kann beispielsweise mittels der letzten Formel berechnet werden, dass sich
ein Kapital :math:`K_0` mit einem beliebigen Anfangswert bei einem Zinssatz von
:math:`p=1\%` innerhalb von rund :math:`\unit[70]{Jahren}` verdoppelt. Bei einem
Zinssatz von :math:`7\%` verdoppelt sich das Kapital in rund
:math:`\unit[10]{Jahren}`, bei einem Zinssatz von :math:`10\%` in nur rund
:math:`\unit[7]{Jahren}`. Dies gilt gleichermaßen für Vermögen wie für Schulden:
Zinseszinsen wachsen exponentiell!


.. Tilgungsrechnung, Rentenrechnung



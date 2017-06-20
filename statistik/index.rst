
.. index:: Statistik
.. _Statistik:
.. _Beschreibende Statistik:

Beschreibende Statistik
=======================

In der beschreibenden Statistik geht es um die Erfassung, Auswertung und
Darstellung von experimentell oder empirisch gewonnenen Daten. Dabei werden
eÂndliche Mengen an Objekten hinsichtlich bestimmter Eigenschaften untersucht.
Dabei werden allgemein folgende Schritt durchlaufen:

* Zunächst müssen in der beschreibenden Statistik alle für die Analyse
  relevanten Daten vollständig erhoben werden.
* Das bei der Daten-Erhebung gewonnene, oftmals sehr umfangreiche Datenmaterial
  muss als nächstes in eine übersichtliche Form gebracht werden, üblicherweise
  in eine Tabelle oder eine Graphik.
* Anschließend kann mit der Analyse der Daten begonnen werden. Hierbei lassen
  sich die Daten beispielsweise mittels wichtiger Kennzahlen wie Mittelwert und
  Streuungsmaß charakterisieren, ebenso können beispielsweise zeitliche Trends
  oder Abhängigkeiten zwischen mehreren Größen untersucht werden.
* Zuletzt können die Ergebnisse der Analyse interpretiert werden.

.. Statistische Grundbegriffe
.. --------------------------


..  Um Daten bearbeiten und auswerten zu können, brauchst Du zunächst Daten, die
..  noch nicht bearbeitet sind. Solche Daten bezeichnet man überlicherweise als "UrListe"

.. index:: Merkmal, Merkmalsträger, Ausprägung
.. _Merkmale, Merkmalsträger und Grundgesamtheit:

.. rubric:: Merkmale, Merkmalsträger und Grundgesamtheit

Als (Untersuchungs-)Merkmal wird die interessierende statistische Information
bezeichnet. Ein einzelnes Objekt, das dieses Merkmal besitzt, nennt man
Merkmalsträger. Die möglichen Werte, die ein Merkmal annehmen kann, heißen
Merkmalswerte oder Ausprägungen dieses Merkmals. [#]_

.. Merkmalsträger: Auch statistische Einheit oder Untersuchungseinheit genannt
.. Bei Experimenten: Versuchseinheiten, bei Beobachtungsstudien Beobachtungseinheiten
.. Merkmale: Auch Variablen genannt.

.. index:: Grundgesamtheit

Die Menge an Objekten :math:`G`, die hinsichtlich einem oder mehrerer zu
untersuchender Merkmale gleichwertig sind, wird als "Grundgesamtheit" oder
"Population" bezeichnet. Bei der Festlegung der Grundgesamtheit werden müssen
klare Abgrenzungen getroffen werden, beispielsweise müssen räumliche oder
zeitliche Einschränkung vorliegen; die Mitglieder der Grundgesamtheit müssen
somit nicht nur Träger des Untersuchungsmerkmals sein, sondern auch
übereinstimmende Abgrenzungsmerkmale besitzen.

*Beispiel:*

* Bei einem naturwissenschaftlichen Experiment sind die einzelnen Messungen die
  Merkmalsträger, die ihrerseits Messdaten als Merkmale enthalten.
* Bei einer Inventur werden zu einem bestimmten Zeitpunkt alle Objekte eines
  räumlich abgegrenzten Bereichs beispielsweise hinsichtlich ihrer
  Funktionsfähigkeit als Merkmal untersucht.

.. Es ist nicht immer eindeutig, wie ein Merkmalsträger zu definieren ist.
.. Beispielsweise müsste geklärt werden, ob das Merkmal "ist Mitarbeiter eines
.. bestimmten Unternehmens" auch für Praktikanten gilt oder Personen, deren
.. Beschäftigungsverhältnis vorübergehend ruht (beispielsweise wegen Mutterschutz).
.. In einer sachlichen Abgrenzung müssen derartige Unklarheiten behoben werden.
.. Dies kann allerdings einen gewollten Einfluss auf das Ergebnis einer
.. statistischen Untersuchung zur Folge haben -- beispielsweise wird diskutiert, ob
.. Personen ohne Anstellung, die gerade an einer Umschulung teilnehmen, in der
.. Statistik der Arbeitslosen gelistet werden sollen oder nicht.

Die Mächtigkeit :math:`n = |G|` der Grundgesamtheit ist gleich der Anzahl ihrer
Objekte. In Tabellen werden die einzelnen zu untersuchenden Merkmale häufig
einem Buchstaben :math:`\mathrm{A},\, \mathrm{B}\, \ldots` zugeordnet, die einzelnen zu
einem jeweiligen Merkmalsträger gehörenden Merkmalswerte werden zeilenweise
durchnummeriert und in der jeweiligen Spalte eingetragen.

.. Die einzelnen Objekte werden üblicherweise mit einem
.. Unterscheidungszeichen ("Schlüssel") :math:`\varepsilon _{\mathrm{i}}` versehen
.. (wobei :math:`i` eine Zahl aus der Menge :math:`1,\,2,\,3,\ldots,n` ist). Jeder
.. Datensatz, der zu einem einzelnen Objekt gehört, umfasst zusätzlich ein oder
.. mehrere Merkmale :math:`(\alpha _{\mathrm{i}})`.

.. Merkmal und Merkmalswert

.. X Alter Y Geschlecht Z Einkommen
.. Geschlecht männlich weiblich
.. Familienstand ledig verheiraret geschieden verwitwet
.. Einkommen Zahlenwert
.. Farbe rot grün blau

Meist ist bei einer Daten-Erhebung nicht möglich, alle Mitglieder der
Grundgesamtheit zu untersuchen ("Vollerhebung"). In diesem Fall muss sich die
Statistik mit einer kleineren, möglichst repräsentativen Stichprobe auskommen
und von dieser auf die Gesamtheit schließen.


.. _Qualitative und quantitative Merkmale:

.. rubric:: Qualitative und quantitative Merkmale

Merkmale können allgemein in zwei Gruppen unterteilt werden:

.. index:: Merkmal; qualitativ

* *Qualitative* Merkmale lassen sich nur verbal beschreiben, es können nur
  Namen oder Klassenbezeichnungen als Werte vorkommen.

.. _Artmäßige Merkmale:

  Handelt es sich bei den Merkmalswerten um Namen, so spricht man auch von
  artmäßigen Merkmalen. Beispiele für derartige Merkmale sind Familiennamen,
  Geschlecht, Farbbezeichnungen, usw.

.. _Intensitätsmäßig abgestufte Merkmale:

  Handelt es sich bei den Merkmalswerten um Klassenbezeichnungen, so spricht man
  auch von intensitätsmäßig abgestuften Merkmalen. Ein Beispiele hierfür sind
  Schulnoten ("sehr gut", "gut", usw.).

.. _Häufbare Merkmale:

  Qualitative Merkmale lassen sich zudem in "häufbare" und "nicht häufbare"
  Merkmale unterscheiden. Ein qualitatives Merkmal ist häufbar, wenn ein
  Merkmalsträger mehrere Merkmalswerte gleichzeitig aufweisen kann;
  beispielsweise kann eine Person gegebenenfalls mehrere Berufsausbildungen
  absolviert haben. Ein qualitatives Merkmal ist nicht häufbar, wenn ein
  Merkmalsträger nur genau einen Merkmalswert aufweisen kann; beispielsweise
  hat jede Person genau eine Augenfarbe.

.. häufbares Merkmal: Mehrere Merkmalsausprägungen möglich ("Mehrfachnennungen
.. möglich) Bsp Farbe, Sprache, ?

.. index:: Merkmal; quantitativ

* *Quantitative* Merkmale können als Vielfaches einer Einheit ausgedrückt
  werden, beispielsweise Zeitdauer, Energiebedarf, usw.

  Können bei einem quantitativen Merkmal nur ganzzahlige Werte auftreten, so
  spricht man von einem diskreten Merkmal. Ein Beispiel hierfür sind
  Stückzahlen.

  .. Weitere Beispiele: Haushaltsgröße, Einwohnerzahl

  Können bei einem quantitativen Merkmal beliebige Werte auftreten, so spricht
  man von einem stetigen oder kontinuierlichen Merkmal. Beispiele hierfür sind
  Zeitdauern, Längenangaben, usw.

  .. Weitere Beispiele: Benzinverbrauch

.. Quasi-stetig: zwar diskret, aber sehr feingradig abgestuft.

.. Durch Rundungen oder Bildung von Intervallen kann jede stetige Variable zu
.. einer diskreten Variablen gemacht werden.

Um eine Vielzahl unterschiedlicher quantitativer Messwerte abzubilden, können
diese in einzelne Intervalle zusammengefasst werden. Anstelle (sehr) viele
Einzelergebnisse aufzulisten, genügt es damit, die Anzahl an Werten in den
einzelnen Intervallen anzugeben. Üblicherweise werden zwischen :math:`5` und
:math:`20` einzelne Intervallen mit jeweils gleich großen Intervallen und
eindeutig zuzuordnenden Intervallgrenzen gewählt. Durch diese Methode gehen zwar
einerseits die statistischen Informationen der Einzelmessungen teilweise
verloren, andererseits werden dafür die Ergebnisse "komprimiert" und somit
übersichtlicher.

.. Skalenniveaus


.. _Statistische Mess-Skalen:

Statistische Mess-Skalen
------------------------

Mittels einer Mess-Skala können die möglichen Merkmalswerte nach bestimmten
Ordnungsprinzipien darstellt werden. Für qualitative Merkmale werden Nominal-
oder Ordinalskalen verwendet, für quantitative Merkmale kommen oftmals
Intervall- oder Verhältnisskalen zum Einsatz. Im folgenden Abschnitt werden
diese Skalen näher beschrieben.

.. _Nominalskala:

.. rubric:: Nominalskala

Eine Nominalskala hat die möglichen Namen eines quantitativen Merkmals als
Skalenwerte. Diese werden gleichberechtigt nebeneinander angeordnet. Die
einzelnen Namen können zur Unterscheidung von artmäßigen Merkmalen genutzt
werden, entsprechen jedoch keiner Rangordnung. Nehmen die einzelnen
Namen zu viel Platz ein, so können ihnen auch Abkürzungen oder Nummern als
Schlüsselwerte zugewiesen werden.

.. Familienstand: ledig, verheiratet, geschieden, verwitwet
.. Baden-Württemberg: 08 Bayern: 09
.. nur zwei mögliche Ausprägungen: binäre Variable

.. _Ordinalskala:

.. rubric:: Ordinalskala

Eine Ordinalskala hat die Klassenbezeichnungen eines quantitativen Merkmals als
Skalenwerte. Im Gegensatz zu einer Nominalskala sind die einzelnen
Klassenbezeichnungen nicht gleichwertig, sondern entsprechen einer Rangordnung
in auf- oder absteigender Folge.

.. rubric:: Intervall- und Verhältnisskala

Bei diesen beiden Skalentypen handelt es sich um metrische Skalen, vergleichbar
mit einem Meterstab. Als Skalenwerte werden Vielfache einer Grundeinheit
abgetragen.

Eine metrische Skala heißt Intervallskala, wenn der Nullpunkt willkürlich
gewählt ist; in diesem Fall können zwar Differenzen zwischen zwei Werten
sinnvoll interpretiert werden, Quotienten hingegen nicht; Beispielsweise
entsprechen :math:`\unit[20]{\degree C}` nicht einer doppelt so hohen Temperatur
wie :math:`\unit[10]{\degree C}`, wenn man vom absoluten Temperaturnullpunkt
:math:`T_0 = \unit[-273]{\degree C}` ausgeht.

Ist der Nullpunkt einer Skala eindeutig festgelegt, so spricht man von einer
Verhältnisskala. In diesem Fall sind auch Quotienten von einzelnen Werten
sinnvoll interpretierbar. Beispiele hierfür sind Gewichtsangaben, Geldmengen,
Stückzahlen, absolute Temperaturangaben usw.

.. Alter, Tachostand

.. _Graphische Darstellungen statistischer Daten:

Graphische Darstellungen statistischer Daten
--------------------------------------------

Bisweilen ist es praktisch, statistische Informationen als Diagramme graphisch
darzustellen; diese müssen einerseits eindeutig beschriftet sein und sollten
andererseits möglichst übersichtlich gestaltet werden.

* Bei einem Histogramm werden auf der waagrechten Achse die einzelnen Intervall-
  oder Klassengrenzen abgetragen. Über den einzelnen Intervallen werden
  Rechtecke gezeichnet, deren Höhe die absoluten oder relativen Häufigkeiten
  des jeweiligen Intervalls oder der jeweiligen Klasse darstellen.

* Todo: Tortendiagramm, Liniendiagramm, Boxplot usw.


.. index:: Messfehler
.. _Umgang mit ungenauen Messwerten:

Umgang mit ungenauen Messwerten
-------------------------------

Als Messfehler werden Differenzen zwischen gemessenen Werten und den unbekannten
wahren Werten der jeweiligen Messgrößen bezeichnet. Sie lassen sich
grundsätzlich in zwei Arten unterteilen -- in systematische und statistische
(zufällige) Fehler.

.. rubric:: Systematische Fehler

Systematische Fehler entstehen durch mangelhafte Messverfahren, beispielsweise
durch defekte Messgeräte, falsche Eichungen, oder Vernachlässigung von störenden
Einflussgrößen. Je nach Fehler weichen die gemessenen Werte entweder nach oben
oder nach unten von den tatsächlichen Werten ab.

Systematische Fehler werden "reproduzierbar" genannt, denn bei erneuten
Messvorgängen treten sie unter gleichen Bedingungen erneut auf. Wird der Fehler
gefunden, so kann er berücksichtigt und eventuell korrigiert werden.

.. rubric:: Statistische Fehler

Statistische Fehler entstehen zufällig, beispielsweise durch Schwankungen in
Messgeräten oder durch ein ungenaues Ablesen von analogen Messgeräten. Die
Abweichungen der gemessenen Werte können unabhängig vom Fehler sowohl nach oben
als auch nach unten von den tatsächlichen Werten abweichen.

.. Statistisches Rauschen aufgrund diskreter, nicht-kontinuierlicher Messprozesse.
.. Messung somit diskrete Folge von Elementarereignissen
.. Beispiel Geigerzähler; thermisches Rauschen

Statistische Fehler können nicht nie komplett vermieden werden. Die
Messgenauigkeit kann jedoch erhöht werden, indem mehrere Messungen oder
Stichprobentests unter gleichen Bedingungen durchgeführt werden.

Die Summe aller nicht erfassbaren systematischen und zufälligen Fehler ergibt
den Größtfehler einer Datenaufnahme beziehungsweise Messung.

Setzt sich ein Ergebnis rechnerisch aus mehreren gemessenen Größen zusammen,
so hat auch dieses einen Fehler, der sich aus den Fehlern der Einzelgrößen
ergibt. Dabei gelten für verschiedene Rechenoperationen verschiedene Regeln:

* Bei Summen und Differenzen (also :math:`y = x_1 + x_2` oder :math:`y = x_1
  -x_2`) werden die Absolutfehler der Einzelgrößen quadriert und addiert;
  die Quadratwurzel aus diesem Wert liefert schließlich den Fehler der
  Ergebnisgröße:

  .. math::

      \Delta y = \sqrt{(\Delta x_1)^2 + (\Delta x_2)^2}

* Bei Produkten und Quotienten (also :math:`y = x_1 \cdot x_2` oder :math:`y
  = x_1 : x_2`) werden die relativen Fehler unter der Wurzel quadratisch
  addiert:

  .. math::

      \frac{\Delta y}{y} = \sqrt{\left(\frac{\Delta x_1}{x_1}\right)^2 +
      \left(\frac{\Delta x_2}{x_2}\right)^2}

* Bei Potenzen und Wurzeln (also :math:`y = x_1^{x_2}`) wird der relative
  Fehler von y bestimmt durch

  .. math::

      \frac{\Delta y}{y} = x_2 \cdot \frac{\Delta x_1}{\;x_1}

  Dies gilt auch für :math:`x_2 < 1` (Wurzeln).


.. _Mittelwerte und Streuungsmaße:

Mittelwerte und Streuungsmaße
-----------------------------

Nicht nur bei der Fehlerrechnung hat man bei statistischen Analysen als Ziel,
die Gesamtheit aller Merkmalswerte mit einigen charakteristischen Größen
zusammenzufassen; diese sollten beispielsweise einen durchschnittlichen Wert
sowie die Streuung der Merkmalswerte um diesen Durchschnittswert beziffern.


.. index:: Mittelwert
.. _Mittelwerte:

Mittelwerte
^^^^^^^^^^^

Mit "Mittelwert" bezeichnet man umgangssprachlich meist das so genannte
arithmetische Mittel; bisweilen sind allerdings auch andere Durchschnittswerte
wie Median- oder Modalwerte besser zur Beschreibung einer Häufigkeitsverteilung
geeignet.


.. index:: Mittelwert; artithmetisches Mittel
.. _Mittelwert:
.. _Arithmetisches Mittel:
.. _Arithmetischer Mittelwert:

Arithmetisches Mittel
'''''''''''''''''''''

Hat man eine Folge von :math:`n` gemessenen Elementarereignissen vorliegen, so
schwanken die Messwert :math:`x_i` der Ereignisse um den Mittelwert
:math:`\bar{x}`, der folgendermaßen definiert ist:

.. math::
    :label: eqn-arithmetisches-mittel

    \bar{x} = \frac{1}{n} \cdot \sum_{i=1}^{n} x_{\mathrm{i}}

Der Mittelwert :math:`\bar{x}` wird auch als "arithmetisches Mittel" der
Zahlenfolge bezeichnet. Die Abweichungen der einzelnen Ereignisse
:math:`x_{\mathrm{i}}` von diesem Mittelwert betragen:

.. math::

    \Delta x_{\mathrm{i}} = x_{\mathrm{i}} - \bar{x}

Der Mittelwert ist zwar anschaulich und einfach zu berechnen, allerdings
empfindlich gegen unerwartet hohe beziehungsweise niedrige Merkmalswerte, so
genannte "Ausreißer".


.. _Gewichtetes arithmetisches Mittel:

.. rubric:: Gewichtetes arithmetisches Mittel

Das gewichtete (arithmetische) Mittel ist arithmetische Mittel einer
Häufigkeitsverteilung. Man verwendet diesen Wert, wenn die Merkmalswerte mit
unterschiedlichen Häufigkeiten gewichtet sind.

Um das gewichtete Mittel zu berechnen, multipliziert man zunächst die
unterschiedlichen Merkmalswerte :math:`x_{\mathrm{i}}` mit ihrer jeweiligen
:ref:`Häufigkeit <Häufigkeit>`  :math:`z_{\mathrm{i}}`; anschließend addiert man
alle resultierenden Produkt-Werte und teilt das Ergebnis durch die Anzahl
:math:`n` aller Messungen:

.. math::
    :label: eqn-gewichtetes-mittel

    \bar{x} =  \frac{1}{n} \cdot \sum_{i=1}^{n} z_{\mathrm{i}} \cdot x_{\mathrm{i}}

Hat man anstelle der (absoluten) Häufigkeiten :math:`z_{\mathrm{i}}` die
relativen Häufigkeiten :math:`h_{\mathrm{i}} = \frac{z_{\mathrm{i}}}{n}`
gegeben, so genügt es, diese mit den jeweiligen Merkmalswerten :math:`x_{\mathrm{i}}`
zu multiplizieren und die resultierenden Produkte zu addieren:

.. math::
    :label: eqn-gewichtetes-mittel-relative-haeufigkeiten

    \bar{x} =  \frac{1}{n} \cdot \sum_{i=1}^{n} z_{\mathrm{i}} \cdot
    x_{\mathrm{i}} = \sum_{i=1}^{n} \frac{z_i}{n} \cdot x_i = \sum_{i=1}^{n}
    h_{\mathrm{i}} \cdot x_{\mathrm{i}}


*Beispiel:*

* Bei der Statistischen Erhebung "Mikrozensus 2015" hat sich die in der
  folgenden Tabelle dargestellte Häufigkeitsverteilung für die Anzahl an Kindern
  (unter :math:`18` Jahren) in Haushalten und Familien ergeben (Quelle: `Destatis
  <https://www.destatis.de/DE/Publikationen/Thematisch/Bevoelkerung/HaushalteMikrozensus/HaushalteFamilien.html>`__).
  Wie viele Kinder gibt es durchschnittlich je Familie?

  .. list-table::
      :name: tab-gewichtetes-mittel-beispiel
      :widths: 50 50

      * - Kinder je Haushalt
        - Anzahl :math:`z` an Familien in :math:`1000`
      * - :math:`0`
        - :math:`3\,376`
      * - :math:`1`
        - :math:`4\,251`
      * - :math:`2`
        - :math:`2\,916`
      * - :math:`3`
        - :math:`697`
      * - :math:`4`
        - :math:`126`
      * - :math:`5 \text{ (oder mehr) }`
        - :math:`42`
      * - :math:`\text{Insgesamt}`
        - :math:`11\,408`

  .. Excel-Sheet Nr. 2-2-0

  Da die unterschiedlichen Kinder-Anzahlen unterschiedlich gewichtet sind, muss
  zur Bestimmung des Durchschnittwerts mit der Formel für das gewichtete
  arithmetische Mittel gerechnet werden:

  .. math::

      \bar{x} = \frac{1}{n} \cdot \sum_{i=1}^{n} z_{\mathrm{i}} \cdot
      x_{\mathrm{i}}

  .. math::

      \bar{x} = \frac{1}{11\,408} \cdot \left( 3\,376 \cdot 0 +
      4\,251 \cdot 1 + 2\,916 \cdot 2 + 697 \cdot 3 + 126 \cdot 4 + 42 \cdot 5
      \right) \approx 1,13

  Je Familie gibt es in Deutschland somit durchschnittlich (nur) rund
  :math:`1,13` Kinder unter :math:`18` Jahren.

.. Excel-Sheet Nr. 5-1-1

.. Familien gesamt             11408
.. Ohne Kinder unter 18 Jahren 3 376
.. 1 Kind unter 18 Jahren      4 251
.. 2 Kinder unter 18 Jahren    2 916
.. 3 Kinder unter 18 Jahren      697
.. 4 Kinder unter 18 Jahren      126
.. 5 Kinder und mehr u. 18        42



.. index:: Mittelwert; geometrischse Mittel
.. _Geometrisches Mittel:

Geometrisches Mittel
''''''''''''''''''''

Sind die Merkmalswerte relative Änderungen, wie es beispielsweise bei
Wachstumraten oder Leistungssteigerungen der Fall ist, so wird bevorzugt das
geometrische Mittel :math:`\bar{x}_{\mathrm{G}}` als Durchschnittswert
verwendet.  Sie die einzelnen Merkmalswerte
:math:`x_1,\,x_2,\,\ldots,\,x_{\mathrm{n}}` allesamt positiv, so kann das
geometrische Mittel :math:`\bar{x}_{\mathrm{G}}` folgendermaßen berechnet
werden:

.. Dies gilt ebenfalls, wenn beispielsweise mittlere Arbeits- oder
.. Wartezeiten berechnet werden sollen.

.. math::
    :label: eqn-geometrisches-mittel

    \bar{x}_{\mathrm{G}} = \sqrt{x_1 \cdot x_2 \cdot \ldots \cdot
    x_{\mathrm{n}}}

.. Beispiel nach Sachs2006, S.77

*Beispiel:*

* In einer bestimmten Bakterien-Kultur erhöhte sich in drei Tagen die Zahl der
  Bakterien pro Einheit von :math:`100` auf :math:`700`. Gefragt ist nach der
  durchschnittlichen prozentualen Zunahme (je Tag).

  Die durchschnittliche Zunahme soll mit :math:`x` bezeichnet werden. Für die Zahl
  der Bakterien nach dem ersten Tag ergibt sich damit:

  .. math::

      100 + 100 \cdot x = 100 \cdot (1 + x)

  Für den zweiten Tag ist der Wert :math:`100 \cdot (1+x)` der neue
  Ausgangswert. Stellt man die obige Gleichung für den zweiten Tag auf, so muss
  also lediglich :math:`100` durch :math:`100 \cdot (1+x)` ersetzt werden. Man
  erhält als Anzahl der Bakterien nach dem zweiten Tag:

  .. math::

      100 \cdot (1+x) + 100 \cdot (1+x) \cdot x = 100 \cdot (1 + x)^2
      {\color{white} \qquad \qquad \qquad \quad \,.}

  Hierbei wurde zunächst der gemeinsame Faktor :math:`100` ausgeklammert und
  anschließend der resultierende Term zusammengefasst: :math:`100 \cdot [(1+x) +
  (1+x)\cdot x] = 100 \cdot (1 +x +x + x^2)`. Der Term in der Klammer kann als
  :math:`(1 + 2 \cdot x + x^2)` geschrieben werden und entspricht somit der
  binomischen Formel :math:`(1+x)^2`.

  Für den dritten Tag erhält man mit :math:`100 \cdot (1+x)^2` als neuem
  Ausgangswert:

  .. math::

      100 \cdot (1+x)^2 + 100\cdot (1+x)^2 \cdot x = 100 \cdot (1+x)^3
      {\color{white} \qquad \qquad \qquad \quad \;\;\;.}

  Hierbei wurde zunächst wiederum der gemeinsame Faktor :math:`100`
  ausgeklammert und anschließend der resultierende Term in der Klammer
  ausmultipliziert. Man erhält so :math:`100 \cdot \left[ (1 + 2 \cdot x + x^2)
  +(x+ 2\cdot x^2 + x^3) \right]`, was sich zu :math:`100 \cdot (1 + 3 \cdot x
  +3\cdot x^2 + x^3)` zusammenfassen lässt; dies entspricht wiederum der
  binomischen Formel :math:`(1+x)^3`.

  Der Wert des letzten Ausdrucks soll gemäß der Angabe gleich :math:`500` sein;
  es muss also gelten:

  .. math::

      100 \cdot (1 + x)^3 &= 700 \\
      \Rightarrow (1 + x)^3 &= \frac{700}{100} \\
      (1 + x) &= \sqrt[3]{\frac{700}{100}} \\
      x &= \sqrt[3]{\frac{700}{100}} - 1 \approx 0,91 \\

  Die durchschnittliche Wachstumsrate beträgt somit rund :math:`91\%`.

Es kann gezeigt werden, dass das geometrische Mittel einer Merkmals-Reihe der
Länge :math:`n` allgemein nach diesem Prinzip berechnet werden kann:

.. math::
    :label: eqn-geometrisches-mittel-anfangswert-endwert

    \bar{x}_{\mathrm{G}} = \sqrt[n]{\frac{\text{Endwert}}{\text{Anfangswert}}}

Hat ein Merkmal zu Beginn der Messungen einen Wert :math:`w_1`, so erhält man
allgemein bei einem gleichmäßigen Wachstum über :math:`n` Zeitschritte den neuen
Wert :math:`w_2` gemäß folgender Formel:

.. math::

    w_2 = w_1 \cdot (1 + x)^n

Hierbei bezeichnet :math:`x` wiederum die Zuwachsrate je Zeitschritt.


.. Beispiel nach Sachs2006, S.77

*Beispiel:*

* Der Wert einer Aktie, deren Kaufpreis :math:`\unit[50]{Eur}` betrug, stieg im
  ersten Jahr auf :math:`\unit[70]{Eur}`, fiel jedoch im zweiten Jahr auf
  :math:`\unit[40]{Eur}`. Wie groß ist die mittlere Wachstumsrate?

  Für die relative Wachstumsrate :math:`x_1` im ersten Jahr gilt:

  .. math::

      x_1 = \frac{70}{50} = 1,4

  Für die relative Wachstumsrate :math:`x_2` im zweiten Jahr gilt dafür:

  .. math::

      x_2 = \frac{40}{70} \approx 0,5714

  Für das geometrische Mittel :math:`\bar{x}_{\mathrm{G}}` zwischen diesen
  beiden Werten beträgt:

  .. math::

      \bar{x}_{\mathrm{G}} = \sqrt{x_1 \cdot x_2} = \sqrt{1,4 \cdot 0,5714}
      \approx 0,8944

  Der Wert des geometrischen Mittels ist in diesem Fall kleiner als :math:`1`,
  was eine Verringerung des ursprünglichen Werts bedeutet. Die jährliche
  "Wachstumsrate" beträgt also :math:`0,8944 - 1 \approx -0,1056`, also rund
  :math:`-10,56\%`.

Wie man an den beiden Beispielen erkennen kann, wird das geometrische Mittel vor
allem zur Bestimmung des Durchschnittswertes von Verhältniszahlen genutzt, wobei
die Veränderungen meist in jeweils gleichen zeitlichen Abschnitten angegeben
sind.


.. index:: Mittelwert; harmonisches Mittel
.. _Harmonisches Mittel:

Harmonisches Mittel
'''''''''''''''''''

Das harmonische Mittel wird dann verwendet, wenn die Merkmalswerte in Form von
Quotienten vorliegen, wie dies beispielsweise bei der Berechnung von
Durchschnitts-Geschwindigkeiten oder Bevölkerungsdichten der Fall ist.

Die einzelnen Merkmalswerte :math:`x_1,\,x_2,\,\ldots,\,x_{\mathrm{n}}`  müssen
allesamt positiv oder allesamt negativ sein; das harmonische Mittel
:math:`\bar{x}_{\mathrm{H}}` lässt sich dann schrittweise folgendermaßen
berechnen:

* Man dividiert die einzelnen Merkmalswerte :math:`x_{\mathrm{i}}` durch ihre
  jeweiligen (absoluten) Häufigkeiten :math:`z_{\mathrm{i}}` und bildet dabei
  jeweils die Kehrwerte der Ergebnisse.

* Alle so erhaltenen Kehrwerte werden aufsummiert und der Kehrwert dieser Summe
  gebildet.

* Der Kehrwert dieser Summe wird mit der Anzahl :math:`n = \sum_{}^{}
  z_{\mathrm{i}}` multipliziert.

Die Formel zur Berechnung des harmonischen Mittels lautet also:

.. math::
    :label: eqn-harmonisches-mittel

    \bar{x}_{\mathrm{H}} = \frac{z_1 + z_2 + \ldots}{\frac{z_1}{x_1} +
    \frac{z_2}{x_2} + \ldots} = \frac{\sum_{}^{} z_{\mathrm{i}}}{\sum_{}^{}
    \frac{z_{\mathrm{i}}}{x_{\mathrm{i}}} }

*Beispiele:*

* Ein Fahrradfahrer fährt eine :math:`\unit[5]{km}` lange Strecke zunächst mit
  :math:`\unit[10]{km/h}` bergauf, anschließend mit :math:`\unit[30]{km/h}`
  bergab. Wie groß ist die Durchschnittsgeschwindigkeit des Fahrers?

  Die beiden auftretenden Merkmalswerte sind :math:`x_1 = \unit[10]{km/h}` und
  :math:`x_2 = \unit[30]{km/h}`; sie treten mit den Häufigkeiten :math:`z_1 =
  z_2 = \unit[5]{km}` auf. Da es sich bei den Merkmalswerten um Quotienten
  handelt, muss zur Berechnung des Durchschnittswertes auf das harmonische
  Mittel zurückgegriffen werden:

  .. math::

      \bar{x}_{\mathrm{H}} = \frac{z_1 + z_2}{\frac{z_1}{x_1} + \frac{z_2}{x_2}}
      = \frac{\unit[(5 + 5)]{km}}{\frac{\unit[5]{km}}{\unit[10]{\frac{km}{h}}} +
      \frac{\unit[5]{km}}{\unit[30]{\frac{km}{h}}} } = \unit[15]{km/h}

  Die geringe Geschwindigkeit fällt stärker ins Gewicht, da der Fahrer bergauf
  mehr Zeit benötigt als bergab.

.. (5+5) / ( (5/30) + (5/10) )

* Die Bevölkerungszahlen der Bundesländer Bayern und Baden-Württemberg sind in
  der folgenden Tabelle dargestellt (Quelle: `Wikipedia
  <https://de.wikipedia.org/wiki/Deutschland>`__, Stand: Dezember 2016). Wie
  viel Einwohner je :math:`\unit{km^2}` gibt es durchschnittlich in diesen
  beiden Ländern?

  +-------------------+-------------------------------+----------------------+----------------------------------+
  | Land              | Fläche in :math:`\unit{km^2}` | Einwohner            | Einwohner je :math:`\unit{km^2}` |
  +-------------------+-------------------------------+----------------------+----------------------------------+
  | Baden-Württemberg | :math:`35\,751`               | :math:`10\,879\,618` | :math:`304`                      |
  +-------------------+-------------------------------+----------------------+----------------------------------+
  | Bayern            | :math:`70\,550`               | :math:`12\,843\,514` | :math:`182`                      |
  +-------------------+-------------------------------+----------------------+----------------------------------+

  Sind auch die absoluten Einwohnerzahlen bekannt, so kann man diese
  aufsummieren und das Resultat durch die Gesamtfläche dividieren. Kennt man
  hingegen nur die Einwohnerzahlen je :math:`\unit{km^2}`, so kann man zur
  Berechnung des Durchschnittswerts die Formel für das harmonische Mittel
  verwenden:

  .. math::

      \bar{x}_{\mathrm{H}} = \frac{z_1 + z_2}{\frac{z_1}{x_1} + \frac{z_2}{x_2}}
      = \frac{\unit[(35\,751 + 70\,550)]{km^2}}{\frac{\unit[35\,751]{km^2}}{\unit[304]{\frac{1}{km^2}}} +
      \frac{\unit[70\,550]{km^2}}{\unit[182]{\frac{1}{km^2}}} } \approx \unit[210,4]{\frac{1}{km^2}}

  Die durchschnittliche Bevölkerungsdichte in diesen beiden Bundesländern liegt
  somit unterhalb des Durchschnittwerts für ganz Deutschland (laut obiger Quelle
  rund :math:`\unit[230]{\frac{1}{km^2}}`, Stand: Dezember 2016).

Wie man an den Beispielen erkennen kann, wird das harmonische Mittel dann
verwendet, wenn die Gewichtungen in der gleichen Einheit vorliegen wie der
Zähler oder der Nenner des Merkmals.

.. weitere Beispiele: Durchflussrate in l/h, Stückzahlen in Stck/h, usw.

.. _Median:

Median
''''''

Wesentlich unempfindlicher gegenüber Ausreißern ist der so genannte Medianwert.
Sortiert man alle Merkmalswerte in aufsteigender Reihenfolge, so entspricht der
Medianwert genau dem Wert, der sich in der Mitte dieser Liste befindet.

* Bei einer Liste mit einer *ungeradzahligen* Anzahl von :math:`n`
  Elementarereignissen entspricht der mittlere Platz der Position
  :math:`\frac{n+1}{2}` in der Liste; der Medianwert entspricht somit dem Wert
  :math:`x_{\mathrm{\left[\frac{n+1}{2}\right]}}^{\phantom{X}}` der Liste:

  .. math::

      Me = x_{\mathrm{\left[\frac{n+1}{2}\right]}}



* Bei einer Liste mit einer *geradzahligen* Anzahl von :math:`n`
  Elementarereignissen entspricht der Median dem Durchschnitt aus den beiden
  mittig gelegenen Werten:

  .. math::

      Me = \frac{1}{2} \cdot \big( x_{\mathrm{\left[\frac{n+1}{2}\right]}} +
      x_{\mathrm{\left[\frac{n+1}{2}\right]}}  \big)

Der Median ist somit ebenfalls schnell und einfach zu bestimmen.


.. _Modalwert:

Modalwert
'''''''''

Der Modalwert, bisweilen auch "Modus" genannt, gibt den Wert einer Messreihe an,
der am häufigsten beobachtet wurde. Üblicherweise wird der Modalwert nur dann
verwendet, wenn sich die damit verbundene Häufigkeit deutlich von den restlichen
Häufigkeiten unterscheidet; der Modalwert sollte also ein herausragender Wert
sein.

Da die restlichen Merkmalswerte unberücksichtigt bleiben, wird der Modalwert von
Ausreißern nicht beeinflusst.

.. Der Modalwert ist für nominalskalierte Merkmale der einzig mögliche Mittelwert.

.. _Streuungsmaße:

Streuungsmaße
^^^^^^^^^^^^^

Zusätzlich zum Mittelwert sollte stets (mindestens) ein Streuungsmaß angegeben
werden, das angibt, wie stark die tatsächlichen Merkmalswerte vom Mittelwert
abweichen. Beispielsweise sind bei "genauen" Messungen die Abweichungen nur
gering, während sie sich bei "ungenauen" Messungen über einen größeren
Skalenbereich erstrecken.

.. _Spannweite und Quartile:

.. rubric:: Spannweite und Quantile

Als Spannweite :math:`R`, im Englischen "range" genannt, bezeichnet man die
Differenz aus dem größten und dem kleinsten beobachteten Merkmalswert:

.. math::

    R = x_{\mathrm{max}} - x_{\mathrm{min}}

Die Spannweite ist zwar ein einfaches und anschauliches Streuungsmaß, gibt
allerdings keine näheren Informationen über die konkrete Verteilung der
Merkmalswerte an und ist zudem anfällig gegenüber so genannten "Ausreißern",
also einzelnen ungewöhnlich niedrigen oder hohen Werten.

Besser geeignet sind daher meist so genannte Quantils-Angaben: Hierbei sortiert
man zunächst alle Merkmalswerte ihrer Größe nach und untergliedert diese dann in
mehrere Teile:

* Bei Quartilen wird die Gesamtheit aller Merkmalswerte in vier gleich große
  Bereiche unterteilt.
* Bei Dezilen wird die Gesamtheit aller Merkmalswerte in zehn gleich große
  Bereiche unterteilt.

Die Berechnung der einzelnen Quantile erfolgt in ähnlicher Weise wie die
Berechnung des :ref:`Median <Median>`-Werts; beispielsweise gibt das erste
Quartil an, dass :math:`25\%` aller Merkmalswerte kleiner und folglich
:math:`75\%` aller Werte größer als der Wert des ersten Quartils sind. [#]_ Der
Wert des zweiten Quartils gibt entsprechend an, dass :math:`50\%` der
Merkmalswerte kleiner beziehungsweise größer als dieser Wert sind; dieser Wert
ist somit mit dem Median-Wert identisch.


.. _Standardabweichung:

.. rubric:: Standardabweichung

Als Schwankungsbreite wird gewöhnlich die Wurzel aus der mittleren quadratischen
Abweichung vom Mittelwert angegeben. Diese Größe wird Standardabweichung
:math:`\sigma` genannt:

.. math::

    \sigma = \sqrt{\frac{1}{n-1} \cdot \sum_{i=1}^{n} (x_{\mathrm{i}} - \bar{x})^2}

Die Standardabweichung ist, abgesehen von statistischen Schwankungen, unabhängig
von der Anzahl :math:`n` der Einzelmessungen.

... to be continued ...

.. Für zufällig stattfindende Elementarereignisse gilt nach dem Gesetz der großen
.. Zahl im Grenzfall :math:`n \to \infty`:

.. .. math::

..     \sigma = \sqrt{\bar{x}}

.. Können systematische Messfehler ausgeschlossen werden, so wird bisweilen auch
.. die Standardabweichung des Mittelwerts angegeben:

.. .. math::

..     \bar{s} = \sqrt{\frac{1}{n \cdot (n-1)} \cdot \sum_{i=1}^{n}
..     (x_{\mathrm{i}} - \bar{x})^2}

.. Die Angabe von :math:`\bar{s}` fällt bei gleichen Vorgaben wesentlich kleiner
.. aus als :math:``

.. der gemessenen Elementarereignisse zu. In diesem Fall gilt:

.. .. absoluter relativer Fehler (siehe Bergmann-Schäfer - Mechanik)

.. .. rubric:: Mittlere absolute Abweichung

.. Anfällig gegenüber Ausreisern, ansonsten einfach und anschaulich.



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Ein Merkmal kann auch als eine Abbildung :math:`X: G \to M` aufgefasst
    werden, welche die einzelnen Merkmalsträger :math:`g \in G` auf Ausprägungen
    :math:`m \in M` abbildet:

    .. math::

        X(g) = m

    Eine derartige Abbildung ist nicht zwingend eindeutig: Ein Merkmalsträger
    kann mehrere Merkmals-Ausprägungen aufweisen; beispielsweise kann eine
    Person in mehreren Vereinen aktiv sein, mehrere Sprachen sprechen usw.

.. [#] Zur Berechnung des ersten Quartilswert prüft man, ob man bei einer
    Merkmalsliste der Länge :math:`n` für den Term :math:`\frac{n+1}{4}` eine
    ganzzahlige Zahl erhält. Ist dies der Fall, so gilt für den ersten Quartilswert:

    .. math::

        q_1 = x_{\mathrm{ \left[ \frac{n+1}{4} \right] }}

    Ist :math:`\frac{n+1}{4}` nicht ganzzahlig ist, so interpoliert man zwischen
    diesem und dem darauf folgenden Wert. Bezeichnet man den Nachkomma-Anteil
    von :math:`\frac{n+1}{4}` mit :math:`R`, so ergibt sich als Formel für den
    ersten Quartilswert:

    .. math::

        q_1 = x_{\mathrm{ \left[ \frac{n+1}{4} \right] }} + R \cdot \left( x_{\mathrm{
        \left[ \frac{n+1}{4} + 1 \right] }} - x_{\mathrm{ \left[ \frac{n+1}{4}
        \right] }} \right)


.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Statistik>`.




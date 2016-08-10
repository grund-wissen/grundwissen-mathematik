
.. _Beschreibende Statistik:

Beschreibende Statistik
=======================

In der beschreibenden Statistik geht es um die Erfassung, Auswertung und
Darstellung von experimentell oder empirisch gewonnenen Daten. Dabei werden
endliche Mengen an Objekten hinsichtlich bestimmter Eigenschaften untersucht.
Dabei werden allgemein folgende Schritt durchlaufen:

* Zunächst müssen in der beschreibenden Statistik alle für die Analyse
  relevanten Daten vollständig erhoben werden.
* Das bei der Datenerhebung gewonnene, oftmals sehr umfangreiche Datenmaterial
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


Meist ist bei einer Datenerhebung nicht möglich, alle Mitglieder der
Grundgesamtheit zu untersuchen ("Volllerhebung"). In diesem Fall muss sich die
Statistik mit einer kleineren, möglichst repräsentativen Stichprobe auskommen
und von dieser auf die Gesamtheit schließen.


.. _Qualitative und quantitative Merkmale:

.. rubric:: Qualitative und quantitative Merkmale

Merkmale können allgemein in zwei Gruppen unterteilt werden:

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

* *Quantitative* Merkmale können als Vielfaches einer Einheit ausgedrückt
  werden, beispielsweise Zeitdauer, Energiebedarf, usw.

  Können bei einem quantitativen Merkmal nur ganzzahlige Werte auftreten, so
  spricht man von einem diskreten Merkmal. Ein Beispiel hierfür sind
  Stückzahlen.

  Können bei einem quantitativen Merkmal beliebige Werte auftreten, so spricht
  man von einem stetigen oder kontinuierlichen Merkmal. Beispiele hierfür sind
  Zeitdauern, Längenangaben, usw.

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

Eine metrische Skala heisst Intervallskala, wenn der Nullpunkt willkürlich
gewählt ist; in diesem Fall können zwar Differenzen zwischen zwei Werten
sinnvoll interpretiert werden, Quotienten hingegen nicht; Beispielsweise
entsprechen :math:`\unit[20]{\degree C}` nicht einer doppelt so hohen Temperatur
wie :math:`\unit[10]{\degree C}`, wenn man vom absoluten Temperaturnullpunkt
:math:`T_0 = \unit[-273]{\degree C}` ausgeht.

Ist der Nullpunkt einer Skala eindeutig festgelegt, so spricht man von einer
Verhältnisskala. In diesem Fall sind auch Quotienten von einzelnen Werten
sinnvoll interpretierbar. Beispiele hierfür sind Gewichtsangaben, Geldmengen,
Stückzahlen, usw.


.. _Graphische Darstellungen:

Graphische Darstellungen
------------------------

Bisweilen ist es praktisch, statistische Informationen als Diagramme graphisch
darzustellen; diese müssen einerseits eindeutig beschriftet sein und sollten
andererseits möglichst übersichtlich gestaltet werden.

* Bei einem Histogramm werden auf der waagrechten Achse die einzelnen Intervall-
  oder Klassengrenzen abgetragen. Über den einzelnen Intervallen werden
  Rechtecke gezeichnet, deren Höhe die absoluten oder relativen Häufigkeiten
  des jeweiligen Intervalls oder der jeweiligen Klasse darstellen.

* Todo: Liniendiagramm



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


Streuungsmasse
^^^^^^^^^^^^^^

Hat man eine Folge von :math:`n` gemessenen Elementarereignissen vorliegen, so
schwanken die Messwert :math:`x_i` der Ereignisse um den Mittelwert
:math:`\bar{x}`, der folgendermaßen definiert ist:

.. math::

    \bar{x} = \frac{1}{n} \cdot \sum_{i=1}^{n} x_i

Der Mittelwert :math:`\bar{x}` wird auch als "arithmetisches Mittel" der
Zahlenfolge bezeichnet.

Als Schwankungsbreite :math:`\Delta x` wird gewöhnich die Wurzel aus der
mittleren quadratischen Abweichung vom Mittelwert angegeben. Diese Größe wird
Standardabweichung :math:`\Delta x` genannt:

.. math::

    \Delta x = \sqrt{\frac{1}{n-1} \cdot \sum_{i=1}^{n} (x_i - \bar{x})^2}

Die Standardabweichung ist, abgesehen von statistischen Schwankungen, unabhängig
von der Anzahl :math:`n` der Einzelmessungen. Für rein zufällig stattfindende
Elementarereignisse gilt nach dem Gesetz der großen Zahl im Grenzfall :math:`n
\to  \infty`:

.. math::

    \Delta x = \sqrt{\bar{x}}

Bei einer rein zufälligen Verteilung der Messwerte, der so genannten
Gauß-Verteilung, nimmt die Genauigkeit der Messung mit der Wurzel aus der Anzahl
der gemessenen Elementarereignisse zu. In diesem Fall gilt:

.. absoluter relativer Fehler (siehe Bergmann-Schäfer - Mechanik)

.. math::

    \Delta \bar{x} = \sqrt{\frac{1}{n \cdot (n-1)} \cdot \sum_{i=1}^{n} (x_i -
    \bar{x})^2}



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Ein Merkmal kann auch als eine Abbildung :math:`X: G \to M` aufgefasst
    werden, welche die einzelnen Merkmalsträger :math:`g \in G` auf Ausprägungen
    :math:`m \in M` abbildet:

    .. math::

        X(g) = m




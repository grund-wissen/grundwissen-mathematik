.. _Grundkonstruktionen:

Grundkonstruktionen
===================

Auch wenn heutzutage ausgereifte Geometrie- und Zeichenprogramme wie `Geogebra
<https://wiki.ubuntuusers.de/GeoGebra>`_ oder `Inkscape
<https://wiki.ubuntuusers.de/Inkscape>`_ frei verfügbar und weit verbreitet
sind, so sind im praktischen Einsatz oftmals auch einfache Zeichentechniken
nützlich, die sich mit Zirkel und Lineal beziehungsweise  Geodreieck umsetzen
lassen. Solche Grundkonstruktionen sind:

.. Nach Simon1980, S.561

* Eine Strecke halbieren:

  Zunächst zeichnet man von beiden Endpunkten :math:`\mathrm{A}` und
  :math:`\mathrm{B}` der Strecke aus je einen Kreis mit Radius :math:`r >
  \frac{1}{2} \cdot | \mathrm{AB} |`. Beide Kreise schneiden sich in zwei
  Punkten :math:`S_1` und :math:`S_2`. Die Verbindungslinie dieser beiden
  Schnittpunkte halbiert die Strecke :math:`\overline{\mathrm{AB}}`.

  .. figure:: ../../pics/geometrie/grundkonstruktion-strecke-halbieren.png
      :name: fig-grundkonstruktion-halbierung-einer-strecke
      :alt:  fig-grundkonstruktion-halbierung-einer-strecke
      :align: center
      :width: 50%

      Halbierung einer Strecke durch geometrische Konstruktion.

      .. only:: html

          :download:`SVG: Halbierung einer Strecke
          <../../pics/geometrie/grundkonstruktion-strecke-halbieren.svg>`

* Eine Senkrechte zu einer Strecke :math:`\overline{\mathrm{AB}}` errichten, die
  durch einen bestimmten Punkt :math:`\mathrm{P}` auf der Strecke verläuft:

  Zunächst zeichnet man um den Punkt :math:`\mathrm{P}` einen Kreis mit
  beliebigem Radius :math:`r_1`. Anschließend zeichnet man um die beiden
  Schnittpunkte :math:`\mathrm{S_1}` und :math:`\mathrm{S_2}` zwei weitere
  Kreise, jeweils mit Radius :math:`r_2 > r_1`. Die Strecke vom Punkt
  :math:`\mathrm{P}` zu einem der beiden sich ergebenden Schnittpunkte
  :math:`\mathrm{S_3}` und :math:`\mathrm{S_4}` entspricht der gesuchten
  Senkrechten.

  .. figure:: ../../pics/geometrie/grundkonstruktion-senkrechte-zu-strecke-durch-punkt-auf-der-strecke.png
      :name: fig-grundkonstruktion-senkrechte-durch-punkt-auf-der-strecke
      :alt:  fig-grundkonstruktion-senkrechte-durch-punkt-auf-der-strecke
      :align: center
      :width: 50%

      Konstruktion einer Senkrechten zu einer Strecke durch einen bestimmten
      Punkt auf der Strecke.

      .. only:: html

          :download:`SVG: Senkrechte zu einer Strecke (durch Punkt auf der Strecke)
          <../../pics/geometrie/grundkonstruktion-senkrechte-zu-strecke-durch-punkt-auf-der-strecke.svg>`

* Eine Senkrechte zu einer Strecke :math:`\overline{\mathrm{AB}}` errichten, die
  durch einen externen Punkt :math:`\mathrm{P}` verläuft:

  Zunächst zeichnet man um den Punkt :math:`\mathrm{P}` einen Kreis mit Radius
  :math:`r_1`, so dass dieser die Strecke in den Punkten :math:`\mathrm{S_1}`
  und :math:`\mathrm{S_2}` schneidet. Anschliessend zeichnet man um die beiden
  Schnittpunkte :math:`\mathrm{S_1}` und :math:`\mathrm{S_2}` zwei weitere
  Kreise, jeweils mit Radius :math:`r_2 > r_1`. Die Strecke vom Punkt
  :math:`\mathrm{P}` zu einem der beiden sich ergebenden Schnittpunkte,
  vorzugsweise zum gegenüber liegenden Punkt :math:`\mathrm{S_3}`, entspricht
  der gesuchten Senkrechten.

  .. figure:: ../../pics/geometrie/grundkonstruktion-senkrechte-zu-strecke-durch-externen-punkt.png
      :name: fig-grundkonstruktion-senkrechte-durch-externen-punkt
      :alt:  fig-grundkonstruktion-senkrechte-durch-externen-punkt
      :align: center
      :width: 50%

      Konstruktion einer Senkrechten zu einer Strecke durch einen bestimmten
      Punkt außerhalb der Strecke.

      .. only:: html

          :download:`SVG: Senkrechte zu einer Strecke (durch externen Punkt)
          <../../pics/geometrie/grundkonstruktion-senkrechte-zu-strecke-durch-externen-punkt.svg>`


* Eine Parallele zu einer Strecke :math:`\overline{\mathrm{AB}}` errichten, die
  durch einen externen Punkt :math:`\mathrm{P}` geht:

  Zunächst zeichnet man eine vom Punkt :math:`\mathrm{P}` ausgehende Halbgerade,
  welche die Strecke in einem (beliebigen) Punkt :math:`\mathrm{S_1}` schneidet.
  Anschließend zeichnet man um :math:`\mathrm{S_1}` einen Kreis mit Radius
  :math:`|\mathrm{PS_1}|`. Zeichne anschließend vom Schnittpunkt
  :math:`\mathrm{S_2}` dieses Kreises mit der Halbgeraden eine weitere
  Halbgerade durch einen anderen (beliebigen) Punkt :math:`\mathrm{S_3}` auf der
  Strecke. Ein Kreis um :math:`\mathrm{S_3}` mit dem Radius
  :math:`|\mathrm{S_2S_3}|` liefert den Schnittpunkt :math:`\mathrm{S_4}`. Die
  Gerade entlang :math:`\overline{\mathrm{PS_4}}` entspricht schließlich der
  gesuchten Parallele.

  .. figure:: ../../pics/geometrie/grundkonstruktion-parallele-zu-strecke.png
      :name: fig-grundkonstruktion-parallele-zu-einer-strecke
      :alt:  fig-grundkonstruktion-parallele-zu-einer-strecke
      :align: center
      :width: 50%

      Konstruktion einer Parallelen zu einer Strecke.

      .. only:: html

          :download:`SVG: Parallele zu einer Strecke
          <../../pics/geometrie/grundkonstruktion-parallele-zu-strecke.svg>`

  Hat man nicht nur einen Zirkel und ein Lineal, sondern zusätzlich ein
  Konstruktions-Dreieck, so kann man auch dieses nutzen, um eine parallele
  Gerade zu konstruieren: Man legt zunächst das Dreieck mit einer Seite entlang
  der Geraden an; anschließend legt man das Lineal entlang einer der beiden
  anderen Dreieckseiten an. Verschiebt man nun das Dreieck längs des Lineals, so
  kann man entlang der Dreieckseite, die entlang der ursprünglichen Gerade
  verlief, unmittelbar eine parallel verlaufende Strecke zeichnen.

  .. figure:: ../../pics/geometrie/grundkonstruktion-parallele-zu-strecke-mit-lineal-und-dreieck.png
      :name: fig-grundkonstruktion-parallele-mit-lineal-und-dreieck
      :alt:  fig-grundkonstruktion-parallele-mit-lineal-und-dreieck
      :align: center
      :width: 50%

      Konstruktion einer Parallelen mittels Lineal und Dreieck.

      .. only:: html

          :download:`SVG: Parallele mit Lineal und Dreieck
          <../../pics/geometrie/grundkonstruktion-parallele-zu-strecke-mit-lineal-und-dreieck.svg>`

.. Simon1980 S. 504, auch Voelkel 99

* Einen Winkel halbieren:

  Zunächst zeichnet man um den Scheitelpunkt des Winkels einen Kreis mit
  beliebigem Radius, der die Winkelschenkel in den Punkten :math:`\mathrm{S}_1`
  und :math:`\mathrm{S}_2` schneidet. Um diese zeichnet man anschließend zwei
  weitere Kreise mit gleichem Radius. Der Schnittpunkt :math:`\mathrm{S}_3`
  dieser beiden Kreise liefert, verbunden mit dem Scheitelpunkt des Winkels, die
  gesuchte Winkelhalbierende.

  .. figure:: ../../pics/geometrie/grundkonstruktion-winkel-halbieren.png
      :name: fig-grundkonstruktion-winkel-halbieren
      :alt:  fig-grundkonstruktion-winkel-halbieren
      :align: center
      :width: 50%

      Konstruktion einer Winkelhalbierenden.

      .. only:: html

          :download:`SVG: Konstruktion einer Winkelhalbierenden
          <../../pics/geometrie/grundkonstruktion-winkel-halbieren.svg>`

.. Strecke mehrfach teilen, Symmetrieachse zu zwei Punkten: Bewert32






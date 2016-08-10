.. _Stereometrie:

Stereometrie
============

Die Stereometrie ist das geometrische Teilgebiet, in dem Eigenschaften
dreidimensionaler Grundformen untersucht werden. Hierbei sind für vielerlei
Anwendungen insbesondere die Größe des Volumens und der Oberfläche von
regelmäßigen Formen von Interesse.

.. _Quader, Würfel und Prisma:

Quader, Würfel und Prisma
-------------------------

.. rubric:: Quader und Würfel

In einem Quader sind im Allgemeinen alle Seitenlängen unterschiedlich lang, alle
Winkel betragen :math:`90 \degree`. Für das Volumen :math:`V` und die Oberfläche
:math:`A` eines Quaders gilt:

.. math::

    V_{\text{Quader}} &= a \cdot b \cdot c \\
    A_{\text{Quader}} &= 2 \cdot (a \cdot b + a \cdot c + b \cdot c)

.. figure:: ../pics/geometrie/quader.png
    :width: 70%
    :align: center
    :name: fig-quader
    :alt:  fig-quader

    Grundform eines Quaders.

    .. only:: html

        :download:`SVG: Quader
        <../pics/geometrie/quader.svg>`

In einem Würfel -- einer Sonderform eines Quaders -- sind alle Seitenlängen
gleich lang, alle Winkel betragen :math:`90 \degree`. Für das Volumen :math:`V` und
die Oberfläche :math:`A` eines Würfels gilt:

.. math::

    V_{\text{Würfel}} &= a \cdot a \cdot a = a^3 \\
    A_{\text{Würfel}} &= 6 \cdot a^2

.. figure:: ../pics/geometrie/wuerfel.png
    :width: 70%
    :align: center
    :name: fig-würfel
    :alt:  fig-würfel

    Grundform eines Würfels.

    .. only:: html

        :download:`SVG: Würfel
        <../pics/geometrie/wuerfel.svg>`

..  In einem Würfel als einer Sonderform eines Quaders betragen alle Winkel
    :math:`90 \degree`, zusätzlich sind alle Seitenlängen :math:`a` gleich lang.

.. rubric:: Prismen

Für das Volumen :math:`V` und die Oberfläche :math:`A` eines Prismas gilt:

.. math::

    V_{\text{Prisma}} &= A_{\mathrm{G}} \cdot h \\
    A_{\text{M,Prisma}} &= A_{\mathrm{S1}} + A_{\mathrm{S2}} + \ldots + A_{\mathrm{Sn}} \\
    A_{\text{O,Prisma}} &= 2 \cdot A_{\mathrm{G}} + A_{\mathrm{M}}


.. figure:: ../pics/geometrie/prisma-formen.png
    :width: 70%
    :align: center
    :name: fig-prisma-formen
    :alt:  fig-prisma-formen

    Prismen mit drei-, vier-, fünf- und sechseckigen Grundflächen.

    .. only:: html

        :download:`SVG: Prisma-Formen
        <../pics/geometrie/prisma-formen.svg>`

Pyramide und Pyramidenstumpf
----------------------------

Für das Volumen :math:`V` und die Oberfläche :math:`A` einer Pyramide gilt:

.. math::

    V_{\mathrm{{Pyramide}}} &= \frac{A_{\mathrm{G}} \cdot h}{3} \\[4pt]
    A_{\mathrm{{M, Pyramide}}} &= A_1 + A_2 + \ldots + A_{\mathrm{n}}\\
    A_{\mathrm{{O, Pyramide}}} &= A_{\mathrm{G}} + A_{\mathrm{M}}


.. figure:: ../pics/geometrie/pyramide-formen.png
    :width: 70%
    :align: center
    :name: fig-pyramide-formen
    :alt:  fig-pyramide-formen

    Pyramiden mit einem Dreieck, einem Rechteck oder einem Quadrat als
    Grundflächen.

    .. only:: html

        :download:`SVG: Pyramide-Formen
        <../pics/geometrie/pyramide-formen.svg>`

Für das Volumen :math:`V` und die Oberfläche :math:`A` eines Pyramidenstumpfes
gilt:

.. math::

    V_{\mathrm{{Pyramidenstumpf}}} &= \frac{1}{3} \cdot h \cdot (A_{\mathrm{G}} +
    \sqrt{A_{\mathrm{G}} \cdot A_{\mathrm{D}}} + A_{\mathrm{D}}) \\[4pt]
    A_{\mathrm{{M, Pyramidenstumpf}}} &= A_1 + A_2 + \ldots + A
    _{\mathrm{n}}\\
    A_{\mathrm{{O, Pyramidenstumpf}}} &= A_{\mathrm{G}} + A_{\mathrm{M}} + A_{\mathrm{D}}

.. figure:: ../pics/geometrie/pyramidenstumpf.png
    :width: 70%
    :align: center
    :name: fig-pyramidestumpf
    :alt:  fig-pyramidestumpf

    Pyramidenstumpf einer Quadrat-Pyramide.

    .. only:: html

        :download:`SVG: Pyramidestumpf
        <../pics/geometrie/pyramidenstumpf.svg>`


Kugel und Kreiszylinder
-----------------------

Für das Volumen :math:`V` und die Oberfläche :math:`A` einer Kugel gilt:

.. math::

    V_{\mathrm{{Kugel}}} &= \frac{4}{3} \cdot \pi \cdot r^3 \\[4pt]
    A_{\mathrm{{O, Kugel}}} &= 4 \cdot \pi \cdot r^2

..  oder: A = \pi \cdot d^2.

.. figure:: ../pics/geometrie/kugel.png
    :width: 70%
    :align: center
    :name: fig-kugel
    :alt:  fig-kugel

    Grundform einer Kugel.

    .. only:: html

        :download:`SVG: Kugel
        <../pics/geometrie/kugel.svg>`

Für das Volumen :math:`V` und die Oberfläche :math:`A` eines Kreiszylinders
gilt:

.. math::

    V_{\mathrm{{Kreiszylinder}}} &= p \cdot r^2 \cdot h \\[4pt]
    A_{\mathrm{{M, Kreiszylinder}}} &= 2 \cdot \pi \cdot r \cdot h \\
    A_{\mathrm{{O, Kreiszylinder}}} &= 2 \cdot \pi \cdot r^2 + 2 \cdot \pi \cdot h

.. figure:: ../pics/geometrie/kreiszylinder.png
    :width: 70%
    :align: center
    :name: fig-kreiszylinder
    :alt:  fig-kreiszylinder

    Grundform eines Kreiszylinders.

    .. only:: html

        :download:`SVG: Kreiszylinder
        <../pics/geometrie/kreiszylinder.svg>`


Kreiskegel und Kreiskegelstumpf
-------------------------------

Für das Volumen :math:`V` und die Oberfläche :math:`A` eines Kreiskegels gilt
mit :math:`s =  \sqrt{r^2 + h^2}`:

.. math::

    V_{\mathrm{{Kreiskegel}}} &= \frac{\pi \cdot r^2 \cdot h}{3}  \\[4pt]
    A_{\mathrm{{M, Kreiskegel}}} &= \pi \cdot r \cdot s \\
    A_{\mathrm{{O, Kreiskegel}}} &= \pi \cdot r^2 + \pi \cdot r \cdot s

.. figure:: ../pics/geometrie/kreiskegel.png
    :width: 70%
    :align: center
    :name: fig-kreiskegel
    :alt:  fig-kreiskegel

    Grundform eines Kreiskegels.

    .. only:: html

        :download:`SVG: Kreiskegel
        <../pics/geometrie/kreiskegel.svg>`

Für das Volumen :math:`V` und die Oberfläche :math:`A` eines Kreiskegelstumpfes
gilt mit :math:`s =  \sqrt{(r_1 - r_2)^2 + h^2}`:

.. math::

    V_{\mathrm{{Kreiskegelstumpf}}} &= \frac{\pi}{3} \cdot h \cdot \left( r_1^2
    + r_2^2 + r_1 \cdot r_2 \right) \\[4pt]
    A_{\mathrm{{M, Kreiskegelstumpf}}} &= \pi \cdot s \cdot (r_1 + r_2) \\
    A_{\mathrm{{O, Kreiskegelstumpf}}} &= \pi \cdot (r_1^2 + r_2^2 + s \cdot
    (r_1 + r_2))

.. figure:: ../pics/geometrie/kreiskegelstumpf.png
    :width: 70%
    :align: center
    :name: fig-kreiskegelstumpf
    :alt:  fig-kreiskegelstumpf

    Grundform eines Kreiskegelstumpfes.

    .. only:: html

        :download:`SVG: Kreiskegelstumpf
        <../pics/geometrie/kreiskegelstumpf.svg>`



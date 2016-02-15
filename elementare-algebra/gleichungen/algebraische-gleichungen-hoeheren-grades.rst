.. index:: Algebraische Gleichung
.. _Algebraische Gleichungen höheren Grades:

Algebraische Gleichungen höheren Grades
=======================================

.. index:: Polynom

Bei einer algebraischen Gleichung :math:`n`-ten Grades tritt die Variable
:math:`x` in der Potenz :math:`x^n` und gegebenenfalls in Potenzen niederen
Grades auf; sie darf dabei nicht im Nenner stehen. Jede algebraische Gleichung
kann durch äquivalente Umformungen in die allgemeine Form gebracht werden:

.. math::

    a _{\rm{n}} \cdot x^n + a _{\rm{n-1}} \cdot x ^{n-1} + \ldots + a  _{\rm{1}}
    \cdot x +  a _{\rm{0}} = 0

Der Term auf der linken Seite der obigen Gleichung, der aus einer Summe von
Vielfachen von Potenzen einer Variablen (meist :math:`x`) besteht, wird
allgemein als "Polynom" bezeichnet.

Algebraische Gleichungen lassen sich im Allgemeinen nur näherungsweise mit Hilfe
eines geeigneten Computerprogramms [#CAS]_ lösen. Eine Gleichung :math:`n`-ten
Grades hat dabei maximal :math:`n` Lösungen. Unmittelbar rechnerisch lösbar sind
Gleichungen dritten oder höheren Grades jedoch dann, wenn einer der
folgenden Sonderfälle vorliegt:

* Fehlt bei einer Gleichung :math:`n`-ten Grades das :math:`x`-freie Glied, so
  kann auf der linken Gleichungsseite :math:`x` ausgeklammert werden. Damit ist
  :math:`x _{\rm{1}}=0` als (erste) Lösung der Gleichung gefunden. Der
  verbleibende Term muss als Gleichung :math:`n-1`-ten Grades separat gelöst
  werden. [#LF]_ Beispielsweise lassen sich auf diese Weise Gleichungen dritten
  Grades ("kubische Gleichungen") auf quadratische Gleichungen zurückführen, die
  mit Hilfe der Mitternachtsformel gelöst werden können.

.. index:: Substitution

* Treten bei einer algebraischen Gleichung vierten Grades nur gerade Exponenten
  auf, d.h. gilt :math:`a \cdot x ^{4} + b \cdot x^{2} + c = 0`, so kann die
  Gleichung durch die Einführung einer neuen Variablen :math:`u = x^2` auf eine
  quadratische Form gebracht werden. Dieses Verfahren wird als Substitution
  bezeichnet. Es gilt:

  .. math::

      a \cdot x^4 + b \cdot x^2 + c = 0 \quad
      \overset{u=x^2}{\Longleftrightarrow} \quad a \cdot u^2 + b \cdot u + c = 0

  Ist die neue quadratische Gleichung für :math:`u` gelöst (mit den Lösungen
  :math:`u _{\rm{1}}` und :math:`u _{\rm{2}}`), so können anhand der Gleichung
  :math:`u = x^2` wiederum die Lösungen der ursprünglichen Gleichung berechnet
  werden ("Rücksubstitution"). [#SUB]_ Es folgt:

  .. math::

      x   _{\rm{1,2}}   &=   \pm   \sqrt{u   _{\rm{1}}}    \quad    \text{und}\\
      x _{\rm{3,4}} &= \pm \sqrt{u _{\rm{2}}}

  Da Potenzieren und Wurzelziehen nicht unbedingt äquivalente Umformungen einer
  Gleichung darstellen, muss durch Einsetzen überprüft werden, ob die so
  gefundenen Werte tatsächlich Lösungen der ursprünglichen Gleichung sind.

  Die Substitutions-Methode ist allgemein für Gleichungen der Form :math:`a
  \cdot x^{2 \cdot n} + b \cdot x^n + c = 0` anwendbar, wenn :math:`u = x^n`
  eingesetzt wird.

.. index:: Polynomdivision
.. _Polynomdivision:

* Ist eine Lösung :math:`x  _{\rm{1}}`  einer  algebraischen  Gleichung  höheren
  Grades bekannt oder kann sie durch Ausprobieren einfach ermittelt werden, so
  kann die Gleichung -- wie bei einer :ref:`Linearfaktorzerlegung
  <Linearfaktorzerlegung>` -- in ein Produkt aus :math:`(x - x _{\rm{1}})` und
  einem Restterm zerlegt werden. Dieser Restterm kann in umgekehrter Weise
  berechnet werden, indem man den ursprünglichen Term durch :math:`(x-x
  _{\rm{1}})` teilt. Es gilt somit:

  .. math::

      (a _{\rm{n}} \cdot x^n + a  _{\rm{n-1}}  \cdot  x  ^{n-1}  +  \ldots  +  a
      _{\rm{1}} \cdot n + a _{\rm{0}}) : (x -  x  _{\rm{1}})  =  \text{Restterm}

  Diese so genannte "Polynomdivision" wird nach einem ähnlichen Verfahren
  durchgeführt wie die schriftliche Division:

  * Zunächst wird der erste Summand :math:`a _{\rm{n}} \cdot x^n` des
    ursprünglichen Terms durch :math:`x` geteilt. Das erste Teilergebnis
    :math:`a _{\rm{n}} \cdot x ^{n-1}` wird auf die rechte Seite des
    Istgleich-Zeichens geschrieben.
  * Das erste Teilergebnis wird mit :math:`(x-x _{\rm{1}})` multipliziert, das
    Ergebnis dieser Rechnung unter den ersten Summanden des ursprünglichen Terms
    geschrieben und vom ursprünglichen Term abgezogen. Zu dem sich so ergebenden
    Rest werden weitere Summanden des ursprünglichen Terms hinzugenommen.
  * Das Verfahren wird so lange fortgesetzt, bis kein Rest mehr übrig bleibt.
    [#PD2]_

  Der Restterm hat nur noch den Grad :math:`n-1` und kann üblicherweise leichter
  ausgewertet werden.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#CAS] Siehe Abschnitt `Computer-Algebra-Systeme
    <Computer-Algebra-Systeme>`_.
.. [#LF] Hierbei ist wiederum die Überlegung grundlegend, dass ein Produkt nur
    dann gleich Null ist, wenn (mindestens) einer der beiden Faktoren gleich
    Null ist. Lösungen des restlichen Terms sind somit auch Lösungen der
    ursprünglichen Gleichung.

.. [#SUB] Hierbei gilt zu beachten, dass für reelle Zahlen keine negativen
    Wurzeln definiert sind. Ist :math:`u _{\rm{1}}` und/oder :math:`u _{\rm{2}}`
    negativ, so entfallen die entsprechenden Lösungen.

.. [#PD2] Bliebe bei der Polynomdivision ein Rest übrig, so wäre
    :math:`x_{\rm{1}}` keine Lösung der ursprünglichen Gleichung.



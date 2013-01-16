=============================================
``colorclassifier`` - Python color classifier
=============================================
:Author: Joar Wandborg
:License: AGPLv3 or later

------------
Introduction
------------

You give ``Classifier`` a RGB color value, ``Classifier`` gives you
the most appropriate color name it can find.

-----
Usage
-----

    >>> from colorclassifier import Classifier
    >>> classifier = Classifier(
    ...    rgb=[255, 170, 0])
    >>> classifier.get_name()
    'Orange'

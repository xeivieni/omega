# This file is the program which will read the input files and return the data.


from __future__ import division  ## pour la division
import os
import numpy
import math

### sous fonction pour lire differents type de fichiers de donnees


def Lecture_data(Nom_fichier):
    with open(Nom_fichier, 'r') as fichier:
        data_temp = fichier.readlines()

    data = [line.split() for line in data_temp]
    data = numpy.asfarray(data)

    ligne = len(data)  # nombre de donnees
<<<<<<< Updated upstream
    colonne = len(data[0])

    # fichiers a 1-colonne
    if colonne == 1:
        x = [float(data[i]) for i in range(ligne)]
        uns = [1 for k in range(ligne)]
        return int(ligne), x, uns

    # fichiers a 2-colonnes
    if colonne == 2:
        x = [float(data[i][0]) for i in range(ligne)]
        Effectifs = [int(data[i][1]) for i in range(ligne)]
=======
    colonne=len(data[0])

<<<<<<< Updated upstream
# fichiers a 1-colonne
=======

# fichiers à 1-colonne
>>>>>>> Stashed changes
    if colonne==1:
        x=[float(data[i]) for i in range(ligne)]
        return int(ligne), x

# fichiers a 2-colonnes
    if colonne==2:
        x=[float(data[i][0]) for i in range(ligne)]
        Effectifs=[int(data[i][1]) for i in range(ligne)]
>>>>>>> Stashed changes
        return int(numpy.sum(Effectifs)), x, Effectifs

    # fichiers a 3-colonnes
    if colonne == 3:
        x_g = [float(data[i][0]) for i in range(ligne)]
        x_d = [float(data[i][1]) for i in range(ligne)]
        Effectifs = [int(data[i][2]) for i in range(ligne)]
        moyenne_inter = [(x_g[i] + x_d[i]) / 2 for i in range(len(x_g))]
        return int(numpy.sum(Effectifs)), x_g, x_d, Effectifs

### fin sous fonction
#########################################

## Execution par defaut

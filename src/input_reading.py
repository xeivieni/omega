#This file is the program which will read the input files and return the data.


from __future__ import division ## pour la division
import os
import numpy
import math

### sous fonction pour lire différents type de fichiers de données

def Lecture_data(Nom_fichier):
    with open(Nom_fichier, 'r') as fichier:
        data_temp = fichier.readlines()

    data = [line.split() for line in data_temp]
    data = numpy.asfarray(data)

    ligne = len(data)  # nombre de données
    colonne=len(data[0])

# fichiers à 1-colonne
    if colonne==1:
        x=[float(data[i]) for i in range(ligne)]
        return int(ligne), x

# fichiers à 2-colonnes
    if colonne==2:
        x=[float(data[i][0]) for i in range(ligne)]
        Effectifs=[int(data[i][1]) for i in range(ligne)]
        return int(numpy.sum(Effectifs)), x, Effectifs

# fichiers à 3-colonnes
    if colonne==3:
        x_g=[float(data[i][0]) for i in range(ligne)]
        x_d=[float(data[i][1]) for i in range(ligne)]
        Effectifs=[int(data[i][2]) for i in range(ligne)]
        return int(numpy.sum(Effectifs)), x_g, x_d, Effectifs

### fin sous fonction
#########################################

## Exécution par défaut

if __name__ == '__main__':

# fichiers à 1-colonne

    print('############## exo01.dat ################# \n')
    ligne,Data01=Lecture_data('exo01.dat')
    print("nombre d'observations= %d \n"%ligne)
    print('exo01.dat =%s \n'%Data01)


    print('############## exo1.dat ################# \n')
    nb_obs,Data1=Lecture_data('exo1.dat')
    print("nombre d'observations= %d \n"%nb_obs)
    print('exo1.dat =%s \n'%Data1)

# fichiers à 2-colonnes

    print('############## exo03.dat ################# \n')
    nb_obs,Data03,Effectifs=Lecture_data('exo03.dat')
    print("nombre d'observations= %d \n"%nb_obs)
    print('exo03.dat =%s \n'%Data03)
    print('Effectifs =%s \n'%Effectifs)


    print('############## exo3.dat ################# \n')
    nb_obs,Data3,Effectifs=Lecture_data('exo3.dat')
    print("nombre d'observations= %d \n"%nb_obs)
    print('exo3.dat =%s \n'%Data3)
    print('Effectifs =%s \n'%Effectifs)

# fichiers à 3-colonnes

    print('############## exo4.dat ################# \n')
    nb_obs,x_g,x_d,Effectifs=Lecture_data('exo4.dat')
    print("nombre d'observations= %d \n"%nb_obs,)
    print('x_g =%s \n'%x_g)
    print('x_d =%s \n'%x_d)
    print('Effectifs =%s \n'%Effectifs)

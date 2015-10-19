#!/usr/bin/env python
# -*- coding: utf8 -*-

# This file is the main input point.

import data_treatment
import input_reading

if __name__ == '__main__':
    # fichiers a 1-colonne

    input_file = raw_input('Glissez déposez le fichier a tester et appuyez sur entrée (format .dat) : ')
    print('file name is : '), input_file



    print('############## exo01.dat ################# \n')
    ligne, Data01, uns = input_reading.Lecture_data('../input/exo01.dat')
    print("nombre d'observations= %d \n" % ligne)
    print('exo01.dat =%s \n' % Data01)
    cng = data_treatment.NonGroupedContinuous(ligne, Data01)
    cng.run()
    cng.display_results()
    cng.generate_latex()

    print('############## exo1.dat ################# \n')
    nb_obs, Data1, uns = input_reading.Lecture_data('../input/exo1.dat')
    print("nombre d'observations= %d \n" % nb_obs)
    print('exo1.dat =%s \n' % Data1)
    dng = data_treatment.NonGroupedDiscrete(nb_obs, Data1)
    dng.run()
    dng.display_results()

    print('############## exo3.dat ################# \n')
    nb_obs, Data3, Effectifs = input_reading.Lecture_data('../input/exo3.dat')
    print("nombre d'observations= %d \n" % nb_obs)
    print('exo3.dat =%s \n' % Data3)
    print('Effectifs =%s \n' % Effectifs)
    gd = data_treatment.GroupedDiscrete(nb_obs, Data3, Effectifs)
    gd.run()
    gd.display_results()

    # # fichiers a 3-colonnes
    #
    print('############## exo4.dat ################# \n')
    nb_obs, x_g, x_d, Effectifs = input_reading.Lecture_data('../input/exo4.dat')
    print("nombre d'observations= %d \n" % nb_obs,)
    print('x_g =%s \n' % x_g)
    print('x_d =%s \n' % x_d)
    print('Effectifs =%s \n' % Effectifs)
    gc = data_treatment.GroupedContinuous(nb_obs, x_g, x_d, Effectifs)
    gc.run()
    gc.display_results()

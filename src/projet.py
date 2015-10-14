# This file is the main input point.

import data_treatment
import input_reading

if __name__ == '__main__':
    print "coucou"


    # fichiers a 1-colonne

    print('############## exo01.dat ################# \n')
    ligne, Data01, uns = input_reading.Lecture_data('../../omega_input/data/exo01.dat')
    print("nombre d'observations= %d \n" % ligne)
    print('exo01.dat =%s \n' % Data01)
    #data_treatment.FonctionQuiFaitTout(Data01)
    cng = data_treatment.NonGroupedContinuous(ligne, Data01)
    cng.arithmetic_average()
    cng.geometrical_average()
    cng.quadratic_average()
    # cng.display_results()
    cng.harmonic_average()

    print('############## exo1.dat ################# \n')
    nb_obs, Data1, uns = input_reading.Lecture_data('../../omega_input/data/exo1.dat')
    print("nombre d'observations= %d \n" % nb_obs)
    print('exo1.dat =%s \n' % Data1)
    dng = data_treatment.NonGroupedDiscrete(nb_obs, Data1)
    dng.arithmetic_average()
    dng.quadratic_average()
    dng.geometrical_average()
    dng.harmonic_average()
    # dng.display_results()
    #
    # # fichiers a 2-colonnes
    #
    # print('############## exo03.dat ################# \n')
    # nb_obs, Data03, Effectifs = input_reading.Lecture_data('../../omega_input/data/exo03.dat')
    # print("nombre d'observations= %d \n" % nb_obs)
    # print('exo03.dat =%s \n' % Data03)
    # print('Effectifs =%s \n' % Effectifs)
    #
    print('############## exo3.dat ################# \n')
    nb_obs, Data3, Effectifs = input_reading.Lecture_data('../../omega_input/data/exo3.dat')
    print("nombre d'observations= %d \n" % nb_obs)
    print('exo3.dat =%s \n' % Data3)
    print('Effectifs =%s \n' % Effectifs)
    gd = data_treatment.GroupedDiscrete(nb_obs, Data3, Effectifs)
    gd.arithmetic_average()
    gd.quadratic_average()
    gd.geometrical_average()
    gd.harmonic_average()

    # # fichiers a 3-colonnes
    #
    print('############## exo4.dat ################# \n')
    nb_obs, x_g, x_d, Effectifs = input_reading.Lecture_data('../../omega_input/data/exo4.dat')
    print("nombre d'observations= %d \n" % nb_obs,)
    print('x_g =%s \n' % x_g)
    print('x_d =%s \n' % x_d)
    print('Effectifs =%s \n' % Effectifs)
    gc = data_treatment.GroupedContinuous(nb_obs, x_g, x_d, Effectifs)
    gc.arithmetic_average()
    gc.quadratic_average()
    gc.geometrical_average()
    gc.harmonic_average()
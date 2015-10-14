#This file is the main input point.

import data_treatment
import input_reading

if __name__ == '__main__':
    print "coucou"


# fichiers a 1-colonne

    print('############## exo01.dat ################# \n')
    ligne,Data01= input_reading.Lecture_data('../../omega_input/data/exo01.dat')
    print("nombre d'observations= %d \n"%ligne)
    print('exo01.dat =%s \n'%Data01)
    data_treatment.FonctionQuiFaitTout(Data01)

    print('############## exo1.dat ################# \n')
    nb_obs,Data1=input_reading.Lecture_data('../../omega_input/data/exo1.dat')
    print("nombre d'observations= %d \n"%nb_obs)
    print('exo1.dat =%s \n'%Data1)


# fichiers a 2-colonnes

    print('############## exo03.dat ################# \n')
    nb_obs,Data03,Effectifs=input_reading.Lecture_data('../../omega_input/data/exo03.dat')
    print("nombre d'observations= %d \n"%nb_obs)
    print('exo03.dat =%s \n'%Data03)
    print('Effectifs =%s \n'%Effectifs)


    print('############## exo3.dat ################# \n')
    nb_obs,Data3,Effectifs=input_reading.Lecture_data('../../omega_input/data/exo3.dat')
    print("nombre d'observations= %d \n"%nb_obs)
    print('exo3.dat =%s \n'%Data3)
    print('Effectifs =%s \n'%Effectifs)

# fichiers a 3-colonnes

    print('############## exo4.dat ################# \n')
    nb_obs,x_g,x_d,Effectifs=input_reading.Lecture_data('../../omega_input/data/exo4.dat')
    print("nombre d'observations= %d \n"%nb_obs,)
    print('x_g =%s \n'%x_g)
    print('x_d =%s \n'%x_d)
    print('Effectifs =%s \n'%Effectifs)

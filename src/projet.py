#!/usr/bin/env python
# -*- coding: utf8 -*-

# This file is the main input point.

import data_treatment
import input_reading


#TODO : Afficher nombre de donnees dans le fichier pdf

if __name__ == '__main__':
    # fichiers a 1-colonne

    input_file = raw_input('Glissez déposez le fichier a tester et appuyez sur entrée (format .dat) : ')
    print('file name is : '), input_file
    s = input_reading.Lecture_data(input_file)
    print('taille = '), len(s), 'type = ', type(s)
    if len(s) == 3:
        print "coucou"
        data_set = data_treatment.Calculator(n=s[0], d=s[1], o=s[2])
        pass
    elif len(s) == 4:
        print "coucou"
        data_set = data_treatment.Calculator(n=s[0], dl=s[1], dr=s[2], o=s[3])
        pass
    else:
        print "coucou"
        data_set = data_treatment.Calculator(n=s[0], d=s[1])
    data_set.display_results()
    data_set.generate_latex()

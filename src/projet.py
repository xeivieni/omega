#!/usr/bin/env python
# -*- coding: utf8 -*-

# This file is the main input point.

import data_treatment
import input_reading


#TODO : Afficher nombre de donnees dans le fichier pdf

if __name__ == '__main__':
    # fichiers a 1-colonne

    input_file = raw_input('Glissez déposez le fichier a tester et appuyez sur entrée (format .dat) : ')
    #print('file name is : '), input_file

    print("testing exo01.data...\n")
    data_set = data_treatment.Calculator(input_reading.Lecture_data(input_file))
    data_set.display_results()

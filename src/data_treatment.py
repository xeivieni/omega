#This file will handle the computation on the data extracted
import os
import numpy
import math

def FonctionQuiFaitTout(data):
    min = numpy.min(data[1])
    max = numpy.max(data[1])
    sum_arith = 0
    sum_carre = 0
    sum_ln = 0
    sum_harm = 0
    sum_std = 0



    for i in range(len(data[1])):
        sum_arith = sum_arith + data[1][i]*data[2][i]
        sum_carre = sum_carre + data[1][i]*data[1][i]*data[2][i]
        sum_ln = sum_ln + numpy.log(data[1][i]) * data[2][i]
        sum_harm = sum_harm + (data[2][i] / data[1][i])


    mean_arith = sum_arith / data[0]
    mean_quad = numpy.sqrt(sum_carre / data[0])
    mean_geo = numpy.exp(sum_ln / data[0])
    mean_harm = 1 / (sum_harm / data[0])

    for j in range(len(data[1])):
        sum_std = sum_std + abs(data[1][j] - mean_arith) * data[2][j]

    std = sum_std / data[0]

    print('Min = %f \n'%min)
    print('Max = %f \n'%max)
    print('Moyenne arithmetique = %.3f'%mean_arith)
    print('Moyenne quadratique = %.3f'%mean_quad)
    print('Moyenne geometrique = %.3f'%mean_geo)
    print('Moyenne harmonique = %.3f\n'%mean_harm)
    print('Ecart type = %.3f\n'%std)


    return mean_arith, mean_quad, mean_geo, mean_harm, std

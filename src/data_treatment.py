#This file will handle the computation on the data extracted
import os
import numpy
import math

#def FonctionQuiFaitTout(data):

def MathFunction(data):
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
    
##########################################################################################
## Moment of ordre 1 to 4
    for k in range(len(data[1])):
        m1 = m1 + data[1][i]*data[2][i]
        m2 = m2 + ((data[1][i])**2)*data[2][i]
        m3 = m3 + ((data[1][i])**3)*data[2][i]
        m4 = m4 + ((data[1][i])**4)*data[2][i]

    mom_1 = m1 / data[0]
    mom_2 = m2 / data[0]
    mom_3 = m3 / data[0]
    mom_4 = m4 / data[0]
    
## Centered moment of ordre 1 to 4
    for k in range(len(data[1])):
        u1 = u1 + (data[1][i] - mean_arith)*data[2][i]
        u2 = u2 + ((data[1][i] - mean_arith)**2)*data[2][i]
        u3 = u3 + ((data[1][i] - mean_arith)**3)*data[2][i]
        u4 = u4 + ((data[1][i] - mean_arith)**4)*data[2][i]
    
    mom_cent_1 = u1 / data[0]
    mom_cent_2 = u2 / data[0]
    mom_cent_3 = u3 / data[0]
    mom_cent_4 = u4 / data[0]
    sqrt_var = sqrt(mom_cent_2)
    
#Coefficient of asymmetry and flattening
    y1 = (mom_cent_3/(sqrt_var**3))
    y2 = (mom_cent_4/(sqrt_var**4))-3
##########################################################################################
    
    print('Min = %f \n'%min)
    print('Max = %f \n'%max)
    print('Moyenne arithmetique = %.3f'%mean_arith)
    print('Moyenne quadratique = %.3f'%mean_quad)
    print('Moyenne geometrique = %.3f'%mean_geo)
    print('Moyenne harmonique = %.3f\n'%mean_harm)
    print('Ecart type = %.3f\n'%std)
    print('Variance = %.3f\n'%mom_cent_2)
    print('Ecart type du moment centré d'ordre deux = %.3f\n'%sqrt_var)
    print('Coefficient de dissymétrie = %.3f\n'%y1)
    print('Coefficient d'applatissement = %.3f\n'%y2)


    return mean_arith, mean_quad, mean_geo, mean_harm, std, mom_1, mom_2, mom_3, mom_4, mom_cent_1, mom_cent_2, mom_cent_3, mom_cent_4, sqrt_var, y1, y2

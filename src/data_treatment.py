#This file will handle the computation on the data extracted
import os
import numpy
import math

# @ JO : What is data ?
def averages(data):
    """ This function computes all the different types of averages as well as the standard deviation.
    :param data:
    :return: mean_arith: The arithmetic average
             mean_quad: The quadratic average
             mean_geo: The geometric average
             mean_harm: The harmonic average
             std: The standard deviation along the arithmetic average (ecart type)
    """
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
        sum_std += abs(data[1][j] - mean_arith) * data[2][j]

    std = sum_std / data[0]

    print('Min = %f \n'%min)
    print('Max = %f \n'%max)
    print('Moyenne arithmetique = %.3f'%mean_arith)
    print('Moyenne quadratique = %.3f'%mean_quad)
    print('Moyenne geometrique = %.3f'%mean_geo)
    print('Moyenne harmonique = %.3f\n'%mean_harm)
    print('Ecart type = %.3f\n'%std)


    return mean_arith, mean_quad, mean_geo, mean_harm, std

def moments(data):
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
    print('Ecart type du moment centre d ordre deux = %.3f\n'%sqrt_var)
    print('Coefficient de dissymetrie = %.3f\n' %y1)
    print('Coefficient d applatissement = %.3f\n'%y2)


class Calculator(object):
    """Class computing the operations"""

    def __init__(self):
        """Class constructor for non grouped discrete data"""
        self.arithAvg = 0
        self.quadAvg = 0
        self.geoAvg = 0
        self.harmAvg = 0
        self.std = 0
        self.var = 0
        self.centralMoment = 0
        self.dissym = 0
        self.min = 0
        self.max = 0


    def display_results(self):
        """
        This method will display to the user the results (test purpose)
        :return:
        """
        print "Resultats pour le fichier : \n================================"
        print "Moyenne arithmetique", self.arithAvg
        print "Moyenne quadratique", self.quadAvg
        print "Moyenne geometrique", self.geoAvg
        print "Moyenne harmonique", self.harmAvg


class NonGroupedDiscrete(Calculator):
    """Class for non grouped discrete values treatment"""

    def __init__(self, n, d):
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d

    def arithmetic_average(self):
        self.arithAvg = numpy.mean(self.data)
        print "moyenne arithmetique = ", self.arithAvg

    def quadratic_average(self):
        square_data = [i*i for i in self.data]
        self.quadAvg = math.sqrt(numpy.mean(square_data))
        print "moyenne quadratique = ", self.quadAvg

    

class GroupedDiscrete(Calculator):
    """Class for grouped discrete values treatment"""

    def __init__(self, s, d, e):
        """Grouped discrete"""
        Calculator.__init__(self)
        self.data = d
        self.occurrences = e
        self.values = [self.data[i]*self.occurrences[i] for i in range(len(self.data))]
        self.totalOccurrences = s

    def arithmetic_average(self):
        self.arithAvg = numpy.sum(self.values)/self.totalOccurrences
        print "moyenne arithmetique = ", self.arithAvg

    def quadratic_average(self):
        square_data = [i*i for i in self.values]
        self.quadAvg = math.sqrt(numpy.sum(square_data)/self.totalOccurrences)
        print "moyenne quadratique = ", self.quadAvg


class NonGroupedContinuous(Calculator):
    """Class for non grouped continuous values treatment"""

    def __init__(self, n, d):
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d

    def arithmetic_average(self):
        print " were here"
        self.arithAvg = numpy.mean(self.data)
        print "moyenne arithmetique = ", self.arithAvg

    def quadratic_average(self):
        square_data = [i*i for i in self.data]
        self.quadAvg = math.sqrt(numpy.mean(square_data))
        print "moyenne quadratique = ", self.quadAvg


class GroupedContinuous(Calculator):
    """Class for grouped continuous values treatment"""

    def __init__(self, s, l, h, e):
        Calculator.__init__(self)
        self.sum = s
        self.lowerBounds = l
        self.higherBounds = h
        self.center = [(self.lowerBounds[i]+self.higherBounds[i])/2 for i in range(len(self.lowerBounds))]
        self.occurrences = e

    def arithmetic_average(self):
        values = [self.center[i]*self.occurrences[i] for i in range(len(self.center))]
        self.arithAvg = numpy.sum(values)/numpy.sum(self.occurrences)
        print "moyenne arithmetique = ", self.arithAvg

    def quadratic_average(self):
        square_values = [(self.center[i]*self.center[i])*self.occurrences[i] for i in range(len(self.center))]
        self.quadAvg = math.sqrt(numpy.mean(square_values))
        print "moyenne quadratique = ", self.quadAvg


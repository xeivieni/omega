# This file will handle the computation on the data extracted
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
        sum_arith = sum_arith + data[1][i] * data[2][i]
        sum_carre = sum_carre + data[1][i] * data[1][i] * data[2][i]
        sum_ln = sum_ln + numpy.log(data[1][i]) * data[2][i]
        sum_harm = sum_harm + (data[2][i] / data[1][i])

    mean_arith = sum_arith / data[0]
    mean_quad = numpy.sqrt(sum_carre / data[0])
    mean_geo = numpy.exp(sum_ln / data[0])
    mean_harm = 1 / (sum_harm / data[0])

    for j in range(len(data[1])):
        sum_std += abs(data[1][j] - mean_arith) * data[2][j]

    std = sum_std / data[0]

    print('Min = %f \n' % min)
    print('Max = %f \n' % max)
    print('Moyenne arithmetique = %.3f' % mean_arith)
    print('Moyenne quadratique = %.3f' % mean_quad)
    print('Moyenne geometrique = %.3f' % mean_geo)
    print('Moyenne harmonique = %.3f\n' % mean_harm)
    print('Ecart type = %.3f\n' % std)

    return mean_arith, mean_quad, mean_geo, mean_harm, std


def moments(data):
    ##########################################################################################
    ## Moment of ordre 1 to 4
    for k in range(len(data[1])):
        m1 = m1 + data[1][i] * data[2][i]
        m2 = m2 + ((data[1][i]) ** 2) * data[2][i]
        m3 = m3 + ((data[1][i]) ** 3) * data[2][i]
        m4 = m4 + ((data[1][i]) ** 4) * data[2][i]

    mom_1 = m1 / data[0]
    mom_2 = m2 / data[0]
    mom_3 = m3 / data[0]
    mom_4 = m4 / data[0]

    ## Centered moment of ordre 1 to 4
    for k in range(len(data[1])):
        u1 = u1 + (data[1][i] - mean_arith) * data[2][i]
        u2 = u2 + ((data[1][i] - mean_arith) ** 2) * data[2][i]
        u3 = u3 + ((data[1][i] - mean_arith) ** 3) * data[2][i]
        u4 = u4 + ((data[1][i] - mean_arith) ** 4) * data[2][i]

    mom_cent_1 = u1 / data[0]
    mom_cent_2 = u2 / data[0]
    mom_cent_3 = u3 / data[0]
    mom_cent_4 = u4 / data[0]
    sqrt_var = sqrt(mom_cent_2)

    #Coefficient of asymmetry and flattening
    y1 = (mom_cent_3 / (sqrt_var ** 3))
    y2 = (mom_cent_4 / (sqrt_var ** 4)) - 3
    ##########################################################################################

    print('Min = %f \n' % min)
    print('Max = %f \n' % max)
    print('Moyenne arithmetique = %.3f' % mean_arith)
    print('Moyenne quadratique = %.3f' % mean_quad)
    print('Moyenne geometrique = %.3f' % mean_geo)
    print('Moyenne harmonique = %.3f\n' % mean_harm)
    print('Ecart type = %.3f\n' % std)
    print('Variance = %.3f\n' % mom_cent_2)
    print('Ecart type du moment centre d ordre deux = %.3f\n' % sqrt_var)
    print('Coefficient de dissymetrie = %.3f\n' % y1)
    print('Coefficient d applatissement = %.3f\n' % y2)


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
        self.momentsR = []
        self.centralMomentsR = []
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
        print "Ecart a la moyenne", self.std
        print "Valeure maximale", self.max
        print "Valeurs minimale", self.min
        print "Valeurs minimale", self.var
        print "Valeurs minimale", self.moments
        print "Valeurs minimale", self.dissym

        #TODO : Create average functions in parent class and manipulated data in children


class NonGroupedDiscrete(Calculator):
    """Class for non grouped discrete values treatment"""

    def __init__(self, n, d):
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d

    def arithmetic_average(self):
        self.arithAvg = numpy.mean(self.data)
        print "moyenne arithmetique discrete non groupee = ", self.arithAvg

    def quadratic_average(self):
        square_data = [i * i for i in self.data]
        self.quadAvg = math.sqrt(numpy.mean(square_data))
        print "moyenne quadratique discrete non groupee = ", self.quadAvg

    def geometrical_average(self):
        log_data = [numpy.log(i) for i in self.data]
        self.geoAvg = math.exp(numpy.mean(log_data))
        print "moyenne geometrique discrete non groupee = ", self.geoAvg

    def harmonic_average(self):
        harm_data = [(1 / self.data[i]) for i in range(len(self.data))]
        self.harmAvg = 1 / (numpy.mean(harm_data))
        print "moyenne harmonique discrete non groupee = ", self.harmAvg

    def standard_deviation(self):
        dev_data = [abs(i - self.arithAvg) for i in self.data]
        self.std = numpy.sum(dev_data) / self.nbLines
        print "Ecart a la moyenne arithmetique discrete non groupee = ", self.std

    def extremes(self):
        self.max = numpy.max(self.data)
        self.min = numpy.min(self.data)
        print "Minimum = %f\nMaximum = %f" % (self.min, self.max)

    def moments(self, r):
        for i in range(r):
            self.momentsR.append(sum([j**(i+1) for j in self.data])/self.nbLines)
            print "Moment d'ordre %f = %f" %(i+1, self.momentsR[i])

    def central_moments(self, r):
        if self.momentsR==[]:
            return

        for i in range(r):
            self.centralMomentsR.append(sum([(j-self.arithAvg)**(i+1) for j in self.data])/self.nbLines)
            print "Moment centre d'ordre %f = %f" %(i+1, self.centralMomentsR[i])

class GroupedDiscrete(Calculator):
    """Class for grouped discrete values treatment"""

    def __init__(self, s, d, e):
        """Grouped discrete"""
        Calculator.__init__(self)
        self.data = d
        self.occurrences = e
        self.totalOccurrences = s

    def arithmetic_average(self):
        occurrences_data = [(self.data[i]) * self.occurrences[i] for i in range(len(self.data))]
        self.arithAvg = numpy.sum(occurrences_data) / self.totalOccurrences
        print "moyenne arithmetique discrete groupee = ", self.arithAvg

    def quadratic_average(self):
        square_data = [(self.data[i] * self.data[i]) * self.occurrences[i] for i in range(len(self.data))]
        self.quadAvg = math.sqrt(numpy.sum(square_data) / self.totalOccurrences)
        print "moyenne quadratique discrete groupee = ", self.quadAvg

    def geometrical_average(self):
        log_data = [numpy.log(self.data[i]) * self.occurrences[i] for i in range(len(self.data))]
        self.geoAvg = math.exp(numpy.sum(log_data) / self.totalOccurrences)
        print "moyenne geometrique discrete groupee = ", self.geoAvg

    def harmonic_average(self):
        harm_data = [(self.occurrences[i] / self.data[i]) for i in range(len(self.data))]
        self.harmAvg = 1 / (numpy.sum(harm_data) / self.totalOccurrences)
        print "moyenne harmonique discrete groupee = ", self.harmAvg

    def standard_deviation(self):
        dev_data = [self.occurrences[i] * abs(self.data[i] - self.arithAvg) for i in range(len(self.data))]
        self.std = numpy.sum(dev_data) / self.totalOccurrences
        print "Ecart a la moyenne arithmetique discrete groupee = ", self.std

    def extremes(self):
        self.max = numpy.max(self.data)
        self.min = numpy.min(self.data)
        print "Minimum = %f\nMaximum = %f" % (self.min, self.max)

    def moments(self, r):
        for i in range(r):
            self.momentsR.append(sum([self.occurrences[j]*(self.data[j]**(i+1))
                                      for j in range(len(self.data))])/self.totalOccurrences)
            print "Moment d'ordre %f = %f" %(i+1, self.momentsR[i])

    def central_moments(self, r):
        if self.momentsR==[]:
            return

        for i in range(r):
            self.centralMomentsR.append(sum([self.occurrences[j]*((self.data[j]-self.arithAvg)**(i+1))
                                             for j in range(len(self.data))])/self.totalOccurrences)
            print "Moment centre d'ordre %f = %f" %(i+1, self.centralMomentsR[i])


class NonGroupedContinuous(Calculator):
    """Class for non grouped continuous values treatment"""

    def __init__(self, n, d):
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d

    def arithmetic_average(self):
        print " were here"
        self.arithAvg = numpy.mean(self.data)
        print "moyenne arithmetique continues non groupees = ", self.arithAvg

    def quadratic_average(self):
        square_data = [i * i for i in self.data]
        self.quadAvg = math.sqrt(numpy.mean(square_data))
        print "moyenne quadratique continues non groupees = ", self.quadAvg

    def geometrical_average(self):
        log_data = [numpy.log(i) for i in self.data]
        self.geoAvg = math.exp(numpy.mean(log_data))
        print "moyenne geometrique continues non groupee = ", self.geoAvg

    def harmonic_average(self):
        harm_data = [1 / self.data[i] for i in range(len(self.data))]
        self.harmAvg = 1 / (numpy.mean(harm_data))
        print "moyenne harmonique continues non groupee = ", self.harmAvg

    def standard_deviation(self):
        dev_data = [abs(i - self.arithAvg) for i in self.data]
        self.std = numpy.sum(dev_data) / self.nbLines
        print "Ecart a la moyenne arithmetique continues non groupee = ", self.std

    def extremes(self):
        self.max = numpy.max(self.data)
        self.min = numpy.min(self.data)
        print "Minimum = %f\nMaximum = %f" % (self.min, self.max)

    def moments(self, r):
        for i in range(r):
            self.momentsR.append(sum([j**(i+1) for j in self.data])/self.nbLines)
            print "Moment d'ordre %f = %f" %(i+1, self.momentsR[i])

    def central_moments(self, r):
        if self.momentsR==[]:
            return

        for i in range(r):
            self.centralMomentsR.append(sum([(j-self.arithAvg)**(i+1) for j in self.data])/self.nbLines)
            print "Moment centre d'ordre %f = %f" %(i+1, self.centralMomentsR[i])


class GroupedContinuous(Calculator):
    """Class for grouped continuous values treatment"""

    def __init__(self, s, l, h, e):
        Calculator.__init__(self)
        self.sum = s
        self.lowerBounds = l
        self.higherBounds = h
        self.centers = [(self.lowerBounds[i] + self.higherBounds[i]) / 2 for i in range(len(self.lowerBounds))]
        self.occurrences = e

    def arithmetic_average(self):
        values = [self.centers[i] * self.occurrences[i] for i in range(len(self.centers))]
        self.arithAvg = numpy.sum(values) / numpy.sum(self.occurrences)
        print "moyenne arithmetique continues groupees = ", self.arithAvg

    def quadratic_average(self):
        square_values = [(self.centers[i] * self.centers[i]) * self.occurrences[i] for i in range(len(self.centers))]
        self.quadAvg = math.sqrt(numpy.sum(square_values) / numpy.sum(self.occurrences))
        print "moyenne quadratique continues groupees = ", self.quadAvg

    def geometrical_average(self):
        log_data = [numpy.log(self.centers[i]) * self.occurrences[i] for i in range(len(self.centers))]
        self.geoAvg = math.exp(numpy.sum(log_data) / numpy.sum(self.occurrences))
        print "moyenne geometrique continues groupee = ", self.geoAvg

    def harmonic_average(self):
        harm_data = [(self.occurrences[i] / self.centers[i]) for i in range(len(self.centers))]
        self.harmAvg = 1 / (numpy.sum(harm_data) / numpy.sum(self.occurrences))
        print "moyenne harmonique discrete groupee = ", self.harmAvg

    def standard_deviation(self):
        dev_data = [self.occurrences[i] * abs(self.centers[i] - self.arithAvg) for i in range(len(self.centers))]
        self.std = numpy.sum(dev_data) / numpy.sum(self.occurrences)
        print "Ecart a la moyenne arithmetique continue groupee = ", self.std

    def extremes(self):
        self.max = numpy.max(self.centers)
        self.min = numpy.min(self.centers)
        print "Minimum = %f\nMaximum = %f" % (self.min, self.max)

    def moments(self, r):
        for i in range(r):
            self.momentsR.append(sum([self.occurrences[j]*(self.centers[j]**(i+1))
                                      for j in range(len(self.centers))])/len(self.occurrences))
            print "Moment d'ordre %f = %f" %(i+1, self.momentsR[i])

    def central_moments(self, r):
        if self.momentsR==[]:
            return

        for i in range(r):
            self.centralMomentsR.append(sum([self.occurrences[j]*((self.centers[j]-self.arithAvg)**(i+1))
                                             for j in range(len(self.centers))])/len(self.occurrences))
            print "Moment centre d'ordre %f = %f" %(i+1, self.centralMomentsR[i])

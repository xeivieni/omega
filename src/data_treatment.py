import os
import numpy
import math


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
        self.flattening = 0

    def display_results(self):
        """
        This method will display to the user the results (test purpose)
        :return:
        """
        print "Resultats pour le fichier : \n================================"
        print "Moyenne arithmetique : ", self.arithAvg
        print "Moyenne quadratique : ", self.quadAvg
        print "Moyenne geometrique : ", self.geoAvg
        print "Moyenne harmonique : ", self.harmAvg
        print "Ecart a la moyenne : ", self.std
        print "Valeure maximale : ", self.max
        print "Valeurs minimale : ", self.min
        print "Variance : ", self.var
        print "Moment d'ordre R (defaut 1) : ", self.momentsR
        print "Moment centre d'ordre R (default 1) : ", self.centralMomentsR
        print "Dissymetrie : ", self.dissym
        print "Coefficient d'applatissement : ", self.flattening

    def average(self, data, number):
        return numpy.sum(data) / number

    def moments(self, data, occurrence, order):
        _moments = []
        for j in range(order):
            _moments.append(
                self.average([occurrence[i] * (data[i] ** j + 1) for i in range(len(data))], len(data)))
        return _moments

    def coefficients(self):
        if len(self.centralMomentsR) > 2:
            self.var = math.sqrt(
                self.centralMomentsR[1])  # Variance is the square root of the central moment of order 2
            self.dissym = self.centralMomentsR[2] / (self.var ** 3)
            self.flattening = (self.centralMomentsR[3] / (self.var ** 4)) - 3


class NonGroupedDiscrete(Calculator):
    """Class for non grouped discrete values treatment"""

    def __init__(self, n, d):
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d
        self.run()

    def run(self):
        self.arithAvg = self.average(self.data, self.nbLines)
        self.quadAvg = math.sqrt(self.average([i * i for i in self.data], self.nbLines))
        self.geoAvg = math.exp(self.average([numpy.log(i) for i in self.data], self.nbLines))
        self.harmAvg = 1 / self.average([(1 / self.data[i]) for i in range(len(self.data))], self.nbLines)
        self.max = numpy.max(self.data)
        self.min = numpy.min(self.data)
        self.momentsR = self.moments(self.data, [1 for i in range(len(self.data))], 4)
        self.centralMomentsR = self.moments([(i - self.arithAvg) for i in self.data],
                                            [1 for i in range(len(self.data))], 4)
        self.std = self.average([abs(i - self.arithAvg) for i in self.data], self.nbLines)


class GroupedDiscrete(Calculator):
    """Class for grouped discrete values treatment"""

    def __init__(self, s, d, e):
        """Grouped discrete"""
        Calculator.__init__(self)
        self.data = d
        self.occurrences = e
        self.totalOccurrences = s
        self.run()

    def run(self):
        self.arithAvg = self.average([self.data[i] * self.occurrences[i] for i in range(len(self.data))],
                                     self.totalOccurrences)
        self.quadAvg = math.sqrt(
            self.average([(self.data[i] * self.data[i]) * self.occurrences[i] for i in range(len(self.data))],
                         self.totalOccurrences))
        self.geoAvg = math.exp(
            self.average([numpy.log(self.data[i]) * self.occurrences[i] for i in range(len(self.data))],
                         self.totalOccurrences))
        self.harmAvg = 1 / self.average([(self.occurrences[i] / self.data[i]) for i in range(len(self.data))],
                                        self.totalOccurrences)
        self.max = numpy.max(self.data)
        self.min = numpy.min(self.data)
        self.momentsR = self.moments(self.data, self.occurrences, 4)
        self.centralMomentsR = self.moments([(i - self.arithAvg) for i in self.data], self.occurrences, 4)
        self.std = self.average(
            [self.occurrences[i] * abs(self.data[i] - self.arithAvg) for i in range(len(self.data))],
            self.totalOccurrences)


class NonGroupedContinuous(Calculator):
    """Class for non grouped continuous values treatment"""

    def __init__(self, n, d):
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d
        self.run()

    def run(self):
        self.arithAvg = self.average(self.data, self.nbLines)
        self.quadAvg = math.sqrt(self.average([i * i for i in self.data], self.nbLines))
        self.geoAvg = math.exp(self.average([numpy.log(i) for i in self.data], self.nbLines))
        self.harmAvg = 1 / self.average([(1 / self.data[i]) for i in range(len(self.data))], self.nbLines)
        self.max = numpy.max(self.data)
        self.min = numpy.min(self.data)
        self.momentsR = self.moments(self.data, [1 for i in range(len(self.data))], 4)
        self.centralMomentsR = self.moments([(i - self.arithAvg) for i in self.data],
                                            [1 for i in range(len(self.data))], 4)
        self.std = self.average([abs(i - self.arithAvg) for i in self.data], self.nbLines)


class GroupedContinuous(Calculator):
    """Class for grouped continuous values treatment"""

    def __init__(self, s, l, h, e):
        Calculator.__init__(self)
        self.sum = s
        self.lowerBounds = l
        self.higherBounds = h
        self.centers = [(self.lowerBounds[i] + self.higherBounds[i]) / 2 for i in range(len(self.lowerBounds))]
        self.occurrences = e
        self.run()

    def run(self):
        self.arithAvg = self.average([self.centers[i] * self.occurrences[i] for i in range(len(self.centers))],
                                     sum(self.occurrences))
        self.quadAvg = math.sqrt(
            self.average([(self.centers[i] * self.centers[i]) * self.occurrences[i] for i in range(len(self.centers))],
                         sum(self.occurrences)))

        self.geoAvg = math.exp(
            self.average([numpy.log(self.centers[i]) * self.occurrences[i] for i in range(len(self.centers))],
                         sum(self.occurrences)))
        self.harmAvg = 1 / self.average([(self.occurrences[i] / self.centers[i]) for i in range(len(self.centers))],
                                        sum(self.occurrences))
        self.max = numpy.max(self.centers)
        self.min = numpy.min(self.centers)
        self.momentsR = self.moments(self.centers, self.occurrences, 4)
        self.centralMomentsR = self.moments([(i - self.arithAvg) for i in self.centers], self.occurrences, 4)
        self.std = self.average(
            [self.occurrences[i] * abs(self.centers[i] - self.arithAvg) for i in range(len(self.centers))],
            numpy.sum(self.occurrences))


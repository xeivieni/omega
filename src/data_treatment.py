#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import numpy
import math
import tex_generator


class Calculator(object):
    """
    Class computing the operations
    This class cannot be used directly, it can only be subclassed to inherit from its properties.
    modif nawel
    """

    def __init__(self):
        """
        Class constructor for non grouped discrete data
        """
        self.results = {'arithAvg': 0,
                        'quadAvg': 0,
                        'geoAvg': 0,
                        'harmAvg': 0,
                        'std': 0,
                        'var': 0,
                        'momentsR': [],
                        'centralMomentsR': [],
                        'dissym': 0,
                        'min': 0,
                        'max': 0,
                        'flattening': 0}

    def display_results(self):
        """
        This method will display to the user the results (test purpose)
        :return: None
        """
        print "Resultats pour le fichier : \n================================"
        print "Moyenne arithmetique : ", self.results['arithAvg']
        print "Moyenne quadratique : ", self.results['quadAvg']
        print "Moyenne geometrique : ", self.results['geoAvg']
        print "Moyenne harmonique : ", self.results['harmAvg']
        print "Ecart a la moyenne : ", self.results['std']
        print "Valeure maximale : ", self.results['max']
        print "Valeurs minimale : ", self.results['min']
        print "Variance : ", self.results['var']
        print "Moments d'ordre R (jusqu'a 4) : ", self.results['momentsR']
        print "Moments centrés d'ordre R (jusqu'a 4) : ", self.results['centralMomentsR']
        print "Dissymetrie : ", self.results['dissym']
        print "Coefficient d'applatissement : ", self.results['flattening']

    def average(self, data, number=None):
        """
        Average function (used for almost every calculations.
        This function is useful for our project because it can compute an average on a list and dividing by a specified
        value. By default, it takes the size of data and does a classic average.
        :param data: The list containing the values
        :param number: The number of values (if specified)
        :return: The mean of data
        """
        if number is None:
            return numpy.mean(data)
        return numpy.sum(data) / number

    def moments(self, data, occurrence, order):
        _moments = []
        for j in range(order):
            _moments.append(
                self.average([occurrence[i] * (data[i] ** j + 1) for i in range(len(data))], len(data)))
        return _moments

    def coefficients(self):
        if len(self.results['centralMomentsR']) > 2:
            self.results['var'] = math.sqrt(
                self.results['centralMomentsR'][1])  # Variance is the square root of the central moment of order 2
            self.results['dissym'] = self.results['centralMomentsR'][2] / (self.results['var'] ** 3)
            self.results['flattening'] = (self.results['centralMomentsR'][3] / (self.results['var'] ** 4)) - 3

    def generate_latex(self):
        tex_content = tex_generator.TEMPLATE.format(d=self.results)
        with open("temp.tex", 'w') as tex_file:
            tex_file.write(tex_content)

        os.system("pdflatex temp.tex")
        os.system("htlatex temp.tex")
        os.system("mv temp.pdf report.pdf")
        os.system("mv temp.html report.html")
        os.system("rm temp.*")


class NonGroupedDiscrete(Calculator):
    """
    Class for non grouped discrete values treatment
    """

    def __init__(self, n, d):
        """
        Class constructor
        :param n: Number of lines
        :param d: List containing the data
        :return: None
        """
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d
        self.run()

    def run(self):
        """
        This method runs the different operations in order to calculate the
        different coefficients of the non grouped set of discrete data.
        :return: None
        """
        self.results['arithAvg'] = self.average(self.data)
        self.results['quadAvg'] = math.sqrt(self.average([i * i for i in self.data], self.nbLines))
        self.results['geoAvg'] = math.exp(self.average([numpy.log(i) for i in self.data], self.nbLines))
        self.results['harmAvg'] = 1 / self.average([(1 / self.data[i]) for i in range(len(self.data))], self.nbLines)
        self.results['max'] = numpy.max(self.data)
        self.results['min'] = numpy.min(self.data)
        self.results['momentsR'] = self.moments(self.data, [1 for i in range(len(self.data))], 4)
        self.results['centralMomentsR'] = self.moments([(i - self.results['arithAvg']) for i in self.data],
                                                       [1 for i in range(len(self.data))], 4)
        self.results['std'] = self.average([abs(i - self.results['arithAvg']) for i in self.data], self.nbLines)
        self.coefficients()


class GroupedDiscrete(Calculator):
    """Class for grouped discrete values treatment"""

    def __init__(self, s, d, e):
        """
        Class constructor
        :param s: The sum of all the occurrences. Used to calculated the average.
        :param d: The list containing the data
        :param e: The list of the corresponding occurrences
        :return: None
        """
        Calculator.__init__(self)
        self.data = d
        self.occurrences = e
        self.totalOccurrences = s
        self.run()

    def run(self):
        """
        This method runs the different operations in order to calculate the
        different coefficients of the grouped set of discrete data.
        :return : None
        """
        self.results['arithAvg'] = self.average([self.data[i] * self.occurrences[i] for i in range(len(self.data))],
                                                self.totalOccurrences)
        self.results['quadAvg'] = math.sqrt(
            self.average([(self.data[i] * self.data[i]) * self.occurrences[i] for i in range(len(self.data))],
                         self.totalOccurrences))
        self.results['geoAvg'] = math.exp(
            self.average([numpy.log(self.data[i]) * self.occurrences[i] for i in range(len(self.data))],
                         self.totalOccurrences))
        self.results['harmAvg'] = 1 / self.average(
            [(self.occurrences[i] / self.data[i]) for i in range(len(self.data))],
            self.totalOccurrences)
        self.results['max'] = numpy.max(self.data)
        self.results['min'] = numpy.min(self.data)
        self.results['momentsR'] = self.moments(self.data, self.occurrences, 4)
        self.results['centralMomentsR'] = self.moments([(i - self.results['arithAvg']) for i in self.data],
                                                       self.occurrences, 4)
        self.results['std'] = self.average(
            [self.occurrences[i] * abs(self.data[i] - self.results['arithAvg']) for i in range(len(self.data))],
            self.totalOccurrences)
        self.coefficients()


class NonGroupedContinuous(Calculator):
    """Class for non grouped continuous values treatment"""

    def __init__(self, n, d):
        Calculator.__init__(self)
        self.nbLines = n
        self.data = d
        self.run()

    def run(self):
        """
        This method runs the different operations in order to calculate the
        different coefficients of the non grouped set of continuous data.
        :return : None
        """
        self.results['arithAvg'] = self.average(self.data)
        self.results['quadAvg'] = math.sqrt(self.average([i * i for i in self.data], self.nbLines))
        self.results['geoAvg'] = math.exp(self.average([numpy.log(i) for i in self.data], self.nbLines))
        self.results['harmAvg'] = 1 / self.average([(1 / self.data[i]) for i in range(len(self.data))], self.nbLines)
        self.results['max'] = numpy.max(self.data)
        self.results['min'] = numpy.min(self.data)
        self.results['momentsR'] = self.moments(self.data, [1 for i in range(len(self.data))], 4)
        self.results['centralMomentsR'] = self.moments([(i - self.results['arithAvg']) for i in self.data],
                                                       [1 for i in range(len(self.data))], 4)
        self.results['std'] = self.average([abs(i - self.results['arithAvg']) for i in self.data], self.nbLines)
        self.coefficients()


class GroupedContinuous(Calculator):
    """Class for grouped continuous values treatment"""

    def __init__(self, s, l, h, e):
        """
        Class constructor
        :param s: The sum of all the occurrences. Used to calculated the average.
        :param l: The list of the lower bound for each line
        :param h: The list of the higher bound for each line
        :param e: The list containing the number of occurrences for each line
        :return: None
        """
        Calculator.__init__(self)
        self.totalOccurrences = s
        self.lowerBounds = l
        self.higherBounds = h
        self.centers = [(self.lowerBounds[i] + self.higherBounds[i]) / 2 for i in range(len(self.lowerBounds))]
        self.occurrences = e
        self.run()

    def run(self):
        """
        This method runs the different operations in order to calculate the
        different coefficients of the grouped set of continuous data.
        :return : None
        """
        self.results['arithAvg'] = self.average(
            [self.centers[i] * self.occurrences[i] for i in range(len(self.centers))],
            sum(self.occurrences))
        self.results['quadAvg'] = math.sqrt(
            self.average([(self.centers[i] * self.centers[i]) * self.occurrences[i] for i in range(len(self.centers))],
                         self.totalOccurrences))

        self.results['geoAvg'] = math.exp(
            self.average([numpy.log(self.centers[i]) * self.occurrences[i] for i in range(len(self.centers))],
                         self.totalOccurrences))
        self.results['harmAvg'] = 1 / self.average(
            [(self.occurrences[i] / self.centers[i]) for i in range(len(self.centers))],
            self.totalOccurrences)
        self.results['max'] = numpy.max(self.centers)
        self.results['min'] = numpy.min(self.centers)
        self.results['momentsR'] = self.moments(self.centers, self.occurrences, 4)
        self.results['centralMomentsR'] = self.moments([(i - self.results['arithAvg']) for i in self.centers],
                                                       self.occurrences, 4)
        self.results['std'] = self.average(
            [self.occurrences[i] * abs(self.centers[i] - self.results['arithAvg']) for i in range(len(self.centers))],
            self.totalOccurrences)
        self.coefficients()

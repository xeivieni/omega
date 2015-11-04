#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import numpy
import math
import tex_generator
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


class Calculator(object):
    """
    Class computing the operations
    This class cannot be used directly, it can only be subclassed to inherit from its properties.
    """

    def __init__(self, n, d=None, dl=None, dr=None, o=None):
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

        if o is None:
            self.totalOccurrences = n
            self.data = d
            self.occurrences = [1 for i in range(n)]
            if type(d[0]) is not float:
                self.type = "Non groupées discrètes"
            else:
                self.type = "Non groupées continues"

        elif dl is None and dr is None:
            self.totalOccurrences = n
            self.data = d
            self.occurrences = o
            self.type = "Groupées discètes"

        else:
            self.totalOccurrences = n
            self.data = [(dl[i] + dr[i]) / 2 for i in range(len(o))]
            self.occurrences = o
            self.type = "Groupées continues"
            self.lowerBounds = dl
            self.higherBounds = dr

        self.calculate()
        self.coefficients()
        self.generate_latex()
        self.histogram()

    def calculate(self):
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

    def histogram(self):
        print "longueures egales ?", len(self.occurrences) == len(self.data)
        n, bins, patches = plt.hist(self.data, bins=20, normed=True)
        print n, bins, patches
        #plt.plot(bins, 'r--')
        plt.xlabel("Observations")
        plt.ylabel("Effectifs")
        plt.title("Histogramme")
        #fig = plt.savefig()
        plt.show()

    def generate_latex(self):
        tex_content = tex_generator.TEMPLATE.format(d=self.results, m1=self.results['momentsR'][0],
                                                    m2=self.results['momentsR'][1],
                                                    m3=self.results['momentsR'][2],
                                                    m4=self.results['momentsR'][3],
                                                    c1=self.results['centralMomentsR'][0],
                                                    c2=self.results['centralMomentsR'][1],
                                                    c3=self.results['centralMomentsR'][2],
                                                    c4=self.results['centralMomentsR'][3])
        with open("temp.tex", 'w') as tex_file:
            tex_file.write(tex_content)

        os.system("pdflatex temp.tex")
        os.system("htlatex temp.tex")
        os.system("mv temp.pdf ../report/report.pdf")
        os.system("mv temp.html ../report/report.html")
        os.system("mv temp.tex ../report/report.tex")
        os.system("rm temp.*")

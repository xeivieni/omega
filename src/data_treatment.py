#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import numpy
import math
import subprocess
import tex_generator
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#TODO => Ecart type = sqrt(var)


class Calculator(object):
    """
    Class computing the operations
    This class cannot be used directly, it can only be subclassed to inherit from its properties.
    """

    def __init__(self, n, d=None, dl=None, dr=None, o=None):
        """
        Class constructor for non grouped discrete data
        """
        self.types = ["non groupées discr\\'etes", "non group\\'ees continues", "group\\'ees disc\`etes", "group\\'ees continues"]
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
                        'flattening': 0,
                        'ecartType': 0}

        if o is None:
            self.totalOccurrences = n
            self.data = d
            self.occurrences = [1 for i in range(n)]
            if d[0].is_integer():
                """
                Non groupées discrètes
                """
                self.type = 0
            else:
                """
                Non groupées continues
                """
                self.type = 1

        elif dl is None and dr is None:
            if d[0].is_integer():
                """
                Groupées discètes
                """
                self.totalOccurrences = n
                self.data = d
                self.occurrences = o
                self.type = 2
            else:
                """
                Groupées continues
                """
                self.totalOccurrences = n
                self.data = d
                self.occurrences = o
                self.type = 3

        else:
            """
            Groupées continues
            """
            self.totalOccurrences = n
            self.data = [(dl[i] + dr[i]) / 2 for i in range(len(o))]
            self.occurrences = o
            self.type = 3
            self.lowerBounds = dl
            self.higherBounds = dr

        print self.types[self.type]
        self.calculate()
        self.coefficients()
        self.histogram()
        self.generate_latex()

    def calculate(self):
        """
        This method runs the different operations in order to calculate the
        different coefficients of the grouped set of discrete data.
        :return : None
        """
        self.results['max'] = numpy.max(self.data)
        self.results['min'] = numpy.min(self.data)
        if self.type == 0:
            self.group_data()
        self.results['arithAvg'] = self.average([self.data[i] * self.occurrences[i] for i in range(len(self.data))],
                                                self.totalOccurrences)
        self.results['quadAvg'] = math.sqrt(
            self.average([(self.data[i] * self.data[i]) * self.occurrences[i] for i in range(len(self.data))],
                         self.totalOccurrences))
        if self.results['min'] > 0:
            self.results['geoAvg'] = math.exp(
                self.average([numpy.log(self.data[i]) * self.occurrences[i] for i in range(len(self.data))],
                             self.totalOccurrences))
            self.results['harmAvg'] = 1 / self.average(
                [(self.occurrences[i] / self.data[i]) for i in range(len(self.data))],
                self.totalOccurrences)
        else:
            self.results['geoAvg'] = self.results['harmAvg'] = "N/A"
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

    @staticmethod
    def average(data, number=None):
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
                self.average([occurrence[i] * (data[i] ** (j + 1)) for i in range(len(data))], len(data)))
        return _moments

    def coefficients(self):
        if len(self.results['centralMomentsR']) > 2:
            self.results['var'] = self.results['centralMomentsR'][1]  # Variance is the central moment of order 2
            self.results['dissym'] = self.results['centralMomentsR'][2] / (self.results['var'] ** 3)
            self.results['flattening'] = (self.results['centralMomentsR'][3] / (self.results['var'] ** 4)) - 3
            self.results['ecartType'] = numpy.sqrt(self.results['var'])

    def histogram(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.bar(self.data, self.occurrences)
        plt.hold(True)

        for i in range(len(self.data)):
            ax.text(self.data[i], self.occurrences[i]+0.1, '%d' % (self.occurrences[i]),
                    horizontalalignment='center',
                    verticalalignment='center', fontsize=12)

        plt.ylim([0, numpy.max(self.occurrences)+0.5])
        plt.xlim([numpy.min(self.data)-0.2, numpy.max(self.data)+0.2])
        plt.xticks([k for k in self.data])
        plt.yticks([])
        plt.ylabel('Effectifs', size=16)
        plt.xlabel('Valeurs', size=16)

        plt.savefig("histo.png")



        """
        n, bins, patches = plt.hist(self.data, bins=20, normed=True)
        plt.xlabel("Observations")
        plt.ylabel("Effectifs")
        plt.title("Histogramme")
        plt.savefig("histo.png")
        """
    def generate_latex(self):
        print("generating pdf and html files")
        tex_content = tex_generator.TEMPLATE.format(d=self.results, m1=self.results['momentsR'][0],
                                                    m2=self.results['momentsR'][1],
                                                    m3=self.results['momentsR'][2],
                                                    m4=self.results['momentsR'][3],
                                                    c1=self.results['centralMomentsR'][0],
                                                    c2=self.results['centralMomentsR'][1],
                                                    c3=self.results['centralMomentsR'][2],
                                                    c4=self.results['centralMomentsR'][3],
                                                    nb_obs=self.totalOccurrences, type=self.types[self.type])
        with open("temp.tex", 'w') as tex_file:
            tex_file.write(tex_content)

        with open("/dev/null", 'w') as devnull:
            subprocess.call(["pdflatex", "temp.tex"], stdout=devnull)
            subprocess.call(["htlatex", "temp.tex"], stdout=devnull)
            if not os.path.exists('../report'):
                subprocess.call(["mkdir", "../report"])
            subprocess.call(["mv", "temp.pdf", "../report/report.pdf"])
            subprocess.call(["mv", "temp.html", "../report/report.html"])
            subprocess.call(["mv", "temp.tex", "../report/report.tex"])
            subprocess.call(["mv", "histo.png", "../report/"])
            os.system("rm temp.*")

    def group_data(self):
        d = []
        o = []
        for i in range(int(self.results['min']), int(self.results['max']), 1):
            d.append(i)
            o.append(self.data.count(i))
        self.data = d
        self.occurrences = o
        print self.data
        print self.occurrences







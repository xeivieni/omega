#!/usr/bin/env python
# -*- coding: utf8 -*-

# This file is the main input point.

import data_treatment
import input_reading
import math
import numpy

#TODO : Afficher nombre de donnees dans le fichier pdf

def Normale_Rup(mu,sigma21,sigma22,k,taille):

        X=[]
        # pour la simulation de la loi normale on nutilise Numpy

        sigma1=math.sqrt(sigma21)           #sigma1 = sigma carre (sujet)
        sigma2=math.sqrt(sigma22)           #sigma2 = sigma carre * c carre (sujet)

        for i in range(taille):
            if i < k:
                X.append(numpy.random.normal(mu,sigma1))            #Termes de 1 à k

            else:
                X.append(numpy.random.normal(mu,sigma2))            #Termes de k+1 a n

        return X


def Normale_Rup_Estim(data):

    n=len(data)
    V=[0]*len(data)    # La vraisemblance en fonction de k
    c=[0]*len(data)
    sigma=[0]*len(data)
    diff=[0]*len(data)

    mu=numpy.mean(data)

    diff=[(data[j]-mu) for j in range(len(data))]
    #print diff
    diff_carre = [diff[l]*diff[l] for l in range(len(diff))]
    #print diff_carre

    for i in range(1,len(data)-1):

        c[i]=math.sqrt(numpy.abs(float(float(numpy.sum((data[i+1:n])))-n*mu+i*mu)/        float(i*mu-float(numpy.sum((data[:i]))) )))
        c_carre= [c[m]*c[m] for m in range(len(c))]

        sigma[i]=float(numpy.sum(diff_carre[:i]) + (float(1/(c_carre[i]))*float(numpy.sum(diff_carre[i+1:n]))   ))
        sigma_carre=[sigma[o]*sigma[o] for o in range(len(sigma))]

        V[i]= numpy.abs(float(-n/2)*math.log(float(2*math.pi))    +      float(-n/2)*math.log(float(sigma_carre[i]))     -      float((n-i)/2)*math.log(float(c_carre[i]))       -      float(1/(2*sigma_carre[i]))*float(numpy.sum((diff_carre[:i])))           -             float(1/(2*c_carre[i]*sigma_carre[i]))*float(numpy.sum((diff_carre[i+1:n]))))




    k=numpy.argmax(V)  # l'indice max du Vraisemblance
    c_estim = c_carre[k]
    sigma_estim=sigma[k]

    #print V

    #print "k = ",k
    #print "mu = ",mu
    #print "c = ",c_estim
    #print "sigma = ",sigma_estim


    return k,mu,c_estim,sigma_estim



if __name__ == '__main__':
    # fichiers a 1-colonne


    fichier_k= open('Estimateur_k.dat', 'w')
    fichier_mu= open('mu.dat', 'w')
    fichier_c= open('c.dat', 'w')
    fichier_sigma= open('sigma.dat', 'w')

    M=200
    for i in range(M):
        X = Normale_Rup(10, 7, 2, 50, 100)
        #print X
        Y = Normale_Rup_Estim(X)

        fichier_k.write("%d\n" %Y[0])
        fichier_mu.write("%0.4f\n" %Y[1])
        fichier_c.write("%0.4f\n" %Y[2])
        fichier_sigma.write("%0.4f\n" %Y[3])


    fichier_k.close()
    fichier_mu.close()
    fichier_c.close()
    fichier_sigma.close()


    #print('file name is : '), fichier_k
    s = input_reading.Lecture_data("Estimateur_k.dat")
    if len(s) == 3:
        data_set = data_treatment.Calculator(n=s[0], d=s[1], o=s[2])
    elif len(s) == 4:
        data_set = data_treatment.Calculator(n=s[0], dl=s[1], dr=s[2], o=s[3])
    else:
        data_set = data_treatment.Calculator(n=s[0], d=s[1])




#!/usr/bin/env python
# -*- coding: utf8 -*-

# This file will generate a tex document containing a table with the results
# of the calculation done on the data as well as an histogram.


TEMPLATE = r"""
\documentclass[12pt,a4paper]{{report}}
\usepackage[francais]{{babel}}
\usepackage[latin1]{{inputenc}}
\usepackage[T1]{{fontenc}}

\begin{{document}}
\begin{{titlepage}}
\centering
{{\scshape\LARGE Statistiques mod\'elisation et fiabilit\'e \par}}
\vspace{{1cm}}
{{\scshape\Large Mini projet\par}}
\vspace{{1.5cm}}
{{\huge\bfseries Fichier de r\'esultat\par}}
\vspace{{2cm}}
{{\Large\itshape Jonathan Quie, Cyril Boyer, Nawal El Bannay, Ernest Nob Bakinde, Thibaud Hulot, Cl\'ement Mondion\par}}
\vfill
supervis\'e par\par
M. Dariush \textsc{{Ghorbanzadeh}}

\vfill

% Bottom of the page
{{\large \today\par}}
\end{{titlepage}}

\section{{Table de r\'esultats}}

\bigskip
\noindent {{\bf Ci dessous les diff\'erents r\'esultats caract\'erisant la suite de donn\'ees }}\\
\renewcommand{{\array}}{{2}} % hauteur des cellules du tableau
\begin{{tabular}}{{|l|l|}}
  \hline \hline
  \multicolumn{{2}}{{c}}{{Moyennes : }} \\
  \hline
  Arithm\'etique          &  {d[arithAvg]} \\
  \hline
  Quadratique 	& {d[quadAvg]} \\
  \hline
  G\'eom\'etrique             &  {d[geoAvg]} \\
  \hline
  Harmonique             &  {d[harmAvg]} \\
  \hline
  \multicolumn{{2}}{{c}}{{Extremums : }} \\
  \hline
  Maximum & {d[max]} \\
  \hline
  Minimum  & {d[min]} \\
  \hline
  \multicolumn{{2}}{{c}}{{Moments : }} \\
  \hline
  Ordre 1 & {d[momentsR]} \\
    \hline
  Ordre 2 & {d[momentsR]} \\
    \hline
  Ordre 3 & {d[momentsR]} \\
    \hline
  Ordre 4 & {d[momentsR]} \\
  \hline
  Centr\'e ordre 1 & {d[centralMomentsR]} \\
  \hline
  Centr\'e ordre 2 & {d[centralMomentsR]} \\
   \hline
  Centr\'e ordre 3 & {d[centralMomentsR]} \\
   \hline
  Centr\'e ordre 4 & {d[centralMomentsR]} \\
  \hline
  \multicolumn{{2}}{{c}}{{Autres : }} \\
  \hline
  Ecart a la moyenne arithm\'etique & {d[std]} \\
    \hline
  Variance & {d[var]} \\
    \hline
  Coefficient de dissym\'etrie & {d[dissym]} \\
    \hline
  Coefficient d'applatissement & {d[flattening]} \\
  \hline
\end{{tabular}}


\section{{Histogrammes}}

\end{{document}}
"""


#!/usr/bin/env python
# -*- coding: utf8 -*-

# This file will generated a pdf from the latex file

TEMPLATE = r"""
\documentclass[12pt,a4paper]{report}
\usepackage[francais]{babel}
\usepackage[latin1]{inputenc}
\usepackage[T1]{fontenc}

\begin{document}
\begin{titlepage}
\centering
{\scshape\LARGE Statistiques modélisation et fiabilité \par}
\vspace{1cm}
{\scshape\Large Mini projet\par}
\vspace{1.5cm}
{\huge\bfseries Fichier de résultat\par}
\vspace{2cm}
{\Large\itshape Jonathan Quie, Cyril Boyer, Nawal El Bannay, Ernest Nob Bakinde, Thibaud Hulot, Clément Mondion\par}
\vfill
supervisé par\par
M. Dariush \textsc{Ghorbanzadeh}

\vfill

% Bottom of the page
{\large \today\par}
\end{titlepage}

\section{Table de résultats}

\bigskip
\noindent {\bf Ci dessous les différents résultats caractérisant la suite de données }\\
\renewcommand{\array}{2} % hauteur des cellules du tableau
\begin{tabular}{|l|l|}
  \hline \hline
  \multicolumn{2}{c}{Moyennes : } \\
  \hline
  Arithmétique          &  4,47 \\
  \hline
  Quadratique 	& 4,50 \\
  \hline
  Géométrique             &  4,32 \\
  \hline
  Harmonique             &  4,32 \\
  \hline
  \multicolumn{2}{c}{Extremums : } \\
  \hline
  Maximum & 20,23 \\
  \hline
  Minimum  & 2,1 \\
  \hline
  \multicolumn{2}{c}{Moments : } \\
  \hline
  Ordre 1 & 10,43 \\
    \hline
  Ordre 2 & 13,4 \\
    \hline
  Ordre 3 & 53,1 \\
    \hline
  Ordre 4 & 9,5 \\
  \hline
  Centré ordre 1 & 5,41 \\
  \hline
  Centré ordre 2 & 2,98 \\
   \hline
  Centré ordre 3 & 6,16 \\
   \hline
  Centré ordre 4 & 87,54 \\
  \hline
  \multicolumn{2}{c}{Autres : } \\
  \hline
  Ecart a la moyenne arithmétique & 10,43 \\
    \hline
  Variance & 13,4 \\
    \hline
  Coefficient de dissymétrie & 53,1 \\
    \hline
  Coefficient d'applatissement & 9,5 \\
  \hline
\end{tabular}


\section{Histogrammes}

\end{document}
"""

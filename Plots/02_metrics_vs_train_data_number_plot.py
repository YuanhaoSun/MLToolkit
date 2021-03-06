"""
======================================================
Experiment:  # training data 
======================================================
Plot the results
"""

print __doc__

import pylab as pl
import numpy as np
from scipy import interpolate


###############################################################################
# Lists to be plotted

L1_Num = ['717', '680', '650', '614', '577', '542', '505', '468', '433', '396', 
            '355', '319', '284', '247', '212', '178', '143']
L1_Num.reverse()

BNB = ['0.846191831', '0.841914802', '0.835676682', '0.827018121', '0.817955036', 
        '0.81446681', '0.81450593', '0.807492022', '0.827770606', '0.793176437', 
        '0.813822167', '0.75962716', '0.751111988', '0.747890644', '0.707815884', 
        '0.673860878', '0.595841337']
BNB.reverse()

kNN = ['0.851274829', '0.839148532', '0.833512964', '0.827083397', '0.833400734', 
        '0.806956311', '0.818194795', '0.778811279', '0.781854924', '0.746874787', 
        '0.777738867', '0.739675505', '0.706040722', '0.693821588', '0.756324723', 
        '0.719661998', '0.638102878']
kNN.reverse()

Rdg = ['0.885211396', '0.877573184', '0.880698636', '0.87562007',  '0.869584446',
        '0.854144537', '0.862248125', '0.8503796',   '0.862245564', '0.844994243',
        '0.854240823', '0.843971685', '0.812981505', '0.802350015', '0.82985455',
        '0.835184534', '0.765712952']
Rdg.reverse()

SCG = ['0.866462295', '0.850307365', '0.855699994', '0.847379483', '0.848927159',
        '0.855324088', '0.843496179', '0.834503402', '0.839613799', '0.826466775', 
        '0.855760469', '0.837563096', '0.79815968',  '0.805100686', '0.822385842',
        '0.791607588', '0.772779112']
SCG.reverse()

SVM = ['0.871759911', '0.8566705', '0.862618319', '0.854892439', '0.85131511',
        '0.857133687', '0.855041344', '0.831906335', '0.844347665', '0.832415649', 
        '0.844487207', '0.841523788', '0.817084605', '0.817202265', '0.830546549', 
        '0.817013751', '0.78247599',]
SVM.reverse()

Log = ['0.872427169', '0.85594946', '0.855548015', '0.862477633', '0.859891251',
        '0.857830307', '0.843349072', '0.824138097', '0.834712062', '0.8180231',   
        '0.841993482', '0.824085407', '0.785213817', '0.780753995', '0.789870951', 
        '0.791018148', '0.73345905']
Log.reverse()


pl.figure()
ax = pl.subplot(111)

# convert Python lists to Numpy.array for spline
Num_x = np.zeros(0)
for itme in L1_Num:
    Num_x = np.append(Num_x, [np.float(itme)])

kNN_y = np.zeros(0)
for itme in kNN:
    kNN_y = np.append(kNN_y, [np.float(itme)])

xnew = np.linspace(143,717,500)

# Spline
spl = interpolate.spline(Num_x,kNN_y,xnew)
# Cubic-spline
tck = interpolate.splrep(Num_x,kNN_y,s=0.002) # change s for diff smooth
spv = interpolate.splev(xnew,tck,der=0)
# InterpolatedUnivariateSpline
ius = interpolate.InterpolatedUnivariateSpline(Num_x,kNN_y)
unv = ius(xnew)

# Try smoothened plots for kNN
pl.plot(L1_Num, kNN, '+--', label = 'k-Nearest Neighbor')
pl.plot(xnew, spl, 'g-', label = 'kNN spl')
pl.plot(xnew, spv, 'r-', label = 'kNN spv')
pl.plot(xnew, unv, 'y--', label = 'kNN unv')

pl.plot(L1_Num, BNB, '+--', label = 'Naive Bayes') 
pl.plot(L1_Num, Rdg, 'o--', label = 'Ridge Regression') 
pl.plot(L1_Num, SCG, 'o-', label = 'Stochastic Gradient Descent')
pl.plot(L1_Num, SVM, 'd--', label = 'Support Vector Machine') 
pl.plot(L1_Num, Log, 'd-', label = 'Logistic Regression')

# Different position of the legend
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#           ncol=3, fancybox=True, shadow=True)

pl.xlabel('Number of samples')
pl.ylabel('F1-score')

pl.grid()
pl.title('Privacy Policy Classification Results')
pl.show()
import numpy
import sys
import json

def preventDivisionByZero(nominator, denominator):
    return nominator / denominator if (denominator != 0) else 0

# Stochiometric and composition parameters ASM3 - default

fSI = 0
YSTOO2 = 0.85
YSTONOX = 0.8
YHO2 = 0.63
YHNOX = 0.54
YA = 0.24
fXI = 0.2
iNSI = 0.01
iNSS = 0.03
iNXI = 0.02
iNXS = 0.04
iNBM =  0.07
iSSXI = 0.75
iSSXS = 0.75
iSSBM = 0.9

# kinetyka w trakcie recyrkulacji? chyba

SO2 = 0 # bylo 0! zapytac!
SI = 30
SS = 60
SNH4 = 16
SN2 = 0
SNOX = 0
SALK = 5

XI = 25
XS = 115
XH = 30
XSTO = 0
XA = 0
XSS = 125

# kinetyka again? od temperatury, indeks 0 - 10 stopni indeks 1 - 20 stopni

#kH = []
#kH.append(2)
#kH.append(3)
kH10 = 2
kH20 = 3
#KX = []
#KX.append(1)
#KX.append(1)
KX10 = 1
KX20 = 1
#kSTO = []
#kSTO.append(2.5)
#kSTO.append(5)
kSTO10 = 2.5
kSTO20 = 5
#niNOX = []
#niNOX.append(0.6)
#niNOX.append(0.6)
niNOX10 = 0.6
niNOX20 = 0.6
#KO2 = []
#KO2.append(0.2)
#KO2.append(0.2)
KO210 = 0.2
KO220 = 0.2
#KNOX = []
#KNOX.append(0.5)
#KNOX.append(0.5)
KNOX10 = 0.5
KNOX20 = 0.5
#KS = []
#KS.append(2)
#KS.append(2)
KS10 = 2
KS20 = 2
#KSTO = []
#KSTO.append(1)
#KSTO.append(1)
KSTO10 = 1
KSTO20 = 1
#mikroH = []
#mikroH.append(1)
#mikroH.append(2)
mikroH10 = 1
mikroH20 = 2
#KNH4 = []
#KNH4.append(0.01)
#KNH4.append(0.01)
KNH410 = 0.01
KNH420 = 0.01
#KALK = []
#KALK.append(0.1)
#KALK.append(0.1)
KALK10 = 0.1
KALK20 = 0.1
#bHO2 = []
#bHO2.append(0.1)
#bHO2.append(0.2)
bHO210 = 0.1
bHO220 = 0.2
#bHNOX = []
#bHNOX.append(0.05)
#bHNOX.append(0.1)
bHNOX10 = 0.05
bHNOX20 = 0.1
#bSTOO2 = []
#bSTOO2.append(0.1)
#bSTOO2.append(0.2)
bSTOO210 = 0.1
bSTOO220 = 0.2
#bSTONOX = []
#bSTONOX.append(0.05)
#bSTONOX.append(0.1)
bSTONOX10 = 0.05
bSTONOX20 = 0.1

# druga grupa

#mikroA = []
#mikroA.append(0.35)
#mikroA.append(1)
mikroA10 = 0.35
mikroA20 = 1
#KANH4 = []
#KANH4.append(1)
#KANH4.append(1)
KANH410 = 1
KANH420 = 1
#KAO2 = []
#KAO2.append(0.5)
#KAO2.append(0.5)
KAO210 = 0.5
KAO220 = 0.5
#KAALK = []
#KAALK.append(0.5)
#KAALK.append(0.5)
KAALK10 = 0.5
KAALK20 = 0.5
#bAO2 = []
#bAO2.append(0.05)
#bAO2.append(0.15)
bAO210 = 0.05
bAO220 = 0.15
#bANOX = []
#bANOX.append(0.02)
#bANOX.append(0.05)
bANOX10 = 0.02
bANOX20 = 0.05

ro = numpy.zeros((12,1))

'''
# 1. Hydroliza
ro1.append( kH10 * ( (XS / XH) / KX10 + (XS / XH) ) * XH )
# 2. Aerobic storage of Ss
ro2.append( kSTO10 * ( SO2 / (KO210 + SO2) ) * ( SS / ( KS10  + SS) ) * XH )
# 3. Anoxic storage of Ss
ro3.append( kSTO10 * niNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * ( SS / (KS10 + SS) ) * XH )
# 4. Aerobic growth
ro4.append( mikroH10 * ( SO2 / (KO210 + SO2) ) * ( SNH4 / ( KNH410 + SNH4) ) * (SALK / (KALK10 + SALK) ) * ( (XSTO / XH) / (KSTO10 + (XSTO / XH) ) ) * XH )
# 5. Anoxic growth (denitrification)
ro5.append( mikroH10 * niNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * ( SNH4 / ( KNH410 + SNH4) ) * (SALK / (KALK10 + SALK) ) * ( (XSTO / XH) / (KSTO10 + (XSTO / XH) ) ) * XH )
# 6. Aerobic endogenous respiration
ro6.append( bHO210 * ( SO2 / (KO210 + SO2) ) * XH )
# 7. Anoxic endogenous respiration
ro7.append( bHNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XH )
# 8. Aerobic respiration of XSTO
ro8.append( bSTOO210 * ( SO2 / (KO210 + SO2) ) * XSTO )
# 9. Anoxic respiration of XSTO
ro9.append( bSTONOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XSTO )

# te też?

# 10. Aerobic growth of XA, nitrification
ro10.append( mikroA10 * ( SO2 / (KAO210 + SO2) ) * ( SNH4 / (KANH410 + SNH4) ) * ( SALK / (KAALK10 + SALK) ) * XA )
# 11. Aerobic endogenous respiration
ro11.append( bAO210 * ( SO2 / (KAO210 + SO2) ) * XA )
# 12. Anoxic endogenous respiration
ro12.append( bANOX10 * ( KAO210 / (KAO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XA )
'''

#ważne:
#k(T) = k(20 °C) ⋅ exp (qT ⋅ (T − 20 °C))
# qT = ln (k (T1) / k (T2)) / t1 − T2
# k od temperatury?

# x, y i z z równania:
# Σi ni(j,i) ⋅ ik,i = 0 dla i = 1 do 12
# gdzie k znajduje się w drugiej tabelce (z trzema rzędami, ta z ThOD, nitrogen i ionic charge)

# dla Xss:
# ni(j,13) = Σi ni(j,i) ⋅ i(4,i) dla i = 8 do 12
# k = 4 to ostatni wiersz w tej tabelce, z Ss

# po co to?
# dla ni(anoxic) = 0.7:
# 1 − YSTO,O2 / YSTO,O2 = ni(anoxic) ⋅ (1 − YSTO,NOX) / YSTO,NOX

# po co to? #2
# 1 − YO2 / YO2 = ni(anoxic) ⋅ (1 − YNOX) / YNOX

# Composition matrix - ta z trzema wierszami, ThOD, Nitrogen i Ionic charge

comp = numpy.zeros((3, 13), float)

# rząd 1: ThOD
comp[0][0] = -1
comp[0][1] = 1
comp[0][2] = 1
comp[0][4] = -1.71
comp[0][5] = -4.57
comp[0][7] = 1
comp[0][8] = 1
comp[0][9] = 1
comp[0][10] = 1
comp[0][11] = 1
# rząd 2: Nitrogen
comp[1][1] = iNSI
comp[1][2] = iNSS
comp[1][3] = 1
comp[1][4] = 1
comp[1][5] = 1
comp[1][7] = iNXI
comp[1][8] = iNXS
comp[1][9] = iNBM
comp[1][11] = iNBM
# rząd 3: Ionic charge
comp[2][3] = 1/14
comp[2][5] = -1/14
comp[2][6] = -1

# Obliczenia x, y i z

x1 = (-1 * (fSI * 1 - 1)) / 1
y1 = (-1 * (fSI * iNSI + x1 * iNSS + -1 * iNXS)) / 1
z1 = (-1 * (y1 * 1/14)) / -1

x2 = (-1 * (-1 + YSTOO2)) / -1
y2 = (-1 * (-iNSS)) / 1
z2 = (-1 * (y2 * 1/14)) / -1

x3 = (-1 * (-1 + YSTONOX)) / -4.57
y3 = (-1 * (-iNSS))
z3 = (-1 * (y3 * 1/14 + x3 * 1/14)) / -1

x4 = (-1 * (1 + -1 / YHO2)) / -1
y4 = (-1 * (iNBM)) / 1
z4 = (-1 * (1/14 * y4)) / -1

x5 = (-1 * (1 + -1 / YHNOX)) / -4.57
y5 = (-1 * (iNBM + 1))
z5 = (-1 * (-1 / 14 + x5)) / -1

fI6 = (-1 * (1 + -1)) / 1
x6 = (-1 * (1 + fI6)) / -1
y6 = (-1 * (iNBM + -1))
z6 = (-1 * (1 / 14 + y6)) / -1

fI7 = (-1 * (1 + -1)) / 1
x7 = (-1 * (iNXI + fI7))
y7 = (-1 * ( float(-1 / 14) + x7)) / float(1 / 14)
z7 = (-1 * (1 / 14 + y7)) / -1

x8 = (-1 * (1 + -1)) / -1
x9 = (-1 * (1 + -1)) / -4.57
z9 = (-1 * (-1 / 14 + x9)) / -1

x10 = (-1 * (-4.57 + 1 / YA)) / -1
y10 = (-1 * (iNBM + 1)) / 1
z10 = (-1 * (1 / 14 + y10)) / -1

fI11 = (-1 * (1 + -1)) / 1
x11 = (-1 * (1 + fI11)) / -1
y11 = (-1 * (iNXI + fI11)) / 1
z11 = (-1 * (1 / 14 + y11)) / -1

fI12 = (-1 * (1 + -1)) / 1
x12 = (-1 * (1 + fI12)) / -4.57
y12 = (-1 * (1 + x12)) / 1
z12 = (-1 * (-1 / 14 + x12)) / -1

# Observables - szo to kurwe jest?

obs = numpy.zeros((1,12), float)

# rząd 1: SS 

obs[0][7] = iSSXI
obs[0][8] = iSSXS
obs[0][9] = iSSBM
obs[0][10] = 0.6
obs[0][11] = iSSBM

# tablica:

tab = numpy.zeros((12, 13), float)

# print(tab)

def ostrzad(zmienna, j):
    for i in range(8,12):
        zmienna += tab[j,i] * obs[0,i]
        return zmienna

# rząd 1:
tab[0,1] = fSI
tab[0,2] = x1
tab[0,3] = y1
tab[0,6] = z1
tab[0,8] = -1
zmienna = 0
ostrzad(zmienna, 0)
tab[0][12] = zmienna

# rząd 2:
tab[1,0] = x2
tab[1,2] = -1
tab[1,3] = y2
tab[1,6] = z2
tab[1,10] = YSTOO2
t2 = 0
ostrzad(t2, 1)
tab[1,12] = t2 
# rząd 3:
tab[2,2] = -1
tab[2,3] = y3
tab[2,4] = -x3
tab[2,5] = x3
tab[2,6] = z3
tab[2,10] = YSTONOX
t3 = 0
ostrzad(t3, 2)
tab[2][12] = t3
# rząd 4:
tab[3,0] = x4
tab[3,3] = y4
tab[3,6] = z4
tab[3,9] = 1
tab[3,10] = -1 / YHO2
t4 = 0
ostrzad(t4, 3)
tab[3][12] = t4
# rząd 5:
tab[4,3] = y4
tab[4,4] = -x5
tab[4,5] = x5
tab[4,6] = z5
tab[4,9] = 1
tab[4,10] = -1 / YHNOX
t5 = 0
ostrzad(zmienna, 4)
tab[4,12] = t5
# rząd 6:
tab[5,0] = x6
tab[5,3] = y6
tab[5,6] = z6
tab[5,7] = fI6
tab[5,9] = -1
t6 = 0
ostrzad(t6, 5)
tab[5,12] = t6
# rząd 7:
tab[6,3] = y7
tab[6,4] = -x7
tab[6,5] = x7
tab[6,6] = z7
tab[6,7] = fI7
tab[6,9] = -1
t7 = 0
ostrzad(t7, 6)
tab[6,12] = t7
# rząd 8:
tab[7,0] = x8
tab[7,10] = -1
t8 = 0
ostrzad(t8, 7)
tab[7,12] = t8
# rząd 9:
tab[8,4] = -x9
tab[8,5] = x9
tab[8,6] = z9
tab[8,10] = -1
t9 = 0
ostrzad(t9, 8)
tab[8,12] = t9
# rząd 10:
tab[9,0] = x10
tab[9,3] = y10
tab[9,5] = 1 / YA
tab[9,6] = z10
tab[9,11] = 1
t10 = 0
ostrzad(t10, 9)
tab[9,12] = t10
# rząd 11:
tab[10,0] = x11
tab[10,3] = y11
tab[10,6] = z11
tab[10,7] = fI11
tab[10,11] = -1
t11 = 0
ostrzad(t11, 10)
tab[10,12] = t11
# rząd 12:
tab[11,3] = y12
tab[11,4] = -x12
tab[11,5] = x12
tab[11,6] = z12
tab[11,7] = fI12
tab[11,11] = -1
t12 = 0
ostrzad(t12, 11)
tab[11,12] = t12

# 30 dni

iledni = 30

tmax = 60 * 60 * 24 * iledni

# czas zadany (co sekunde)

t = 1

# ile pętli obliczeń

licznik = tmax / t

# jadą - zapomniaem po chuj to

indextab1 = 0

# ile jest na start w dp1

SO2dp1 = 0
SIdp1 = 0
SSdp1 = 0
SNH4dp1 = 0
SN2dp1 = 0
SNOXdp1 = 0
SALKdp1 = 0
XIdp1 = 0
XSdp1 = 0
XHdp1 = 0
XSTOdp1 = 0
XAdp1 = 0
XSSdp1 = 0

# w dp2

SO2dp2 = 0
SIdp2 = 0
SSdp2 = 0
SNH4dp2 = 0
SN2dp2 = 0
SNOXdp2 = 0
SALKdp2 = 0
XIdp2 = 0
XSdp2 = 0
XHdp2 = 0
XSTOdp2 = 0
XAdp2 = 0
XSSdp2 = 0

# w dp3

SO2dp3 = 0
SIdp3 = 0
SSdp3 = 0
SNH4dp3 = 0
SN2dp3 = 0
SNOXdp3 = 0
SALKdp3 = 0
XIdp3 = 0
XSdp3 = 0
XHdp3 = 0
XSTOdp3 = 0
XAdp3 = 0
XSSdp3 = 0

# w dp4

SO2dp4 = 0
SIdp4 = 0
SSdp4 = 0
SNH4dp4 = 0
SN2dp4 = 0
SNOXdp4 = 0
SALKdp4 = 0
XIdp4 = 0
XSdp4 = 0
XHdp4 = 0
XSTOdp4 = 0
XAdp4 = 0
XSSdp4 = 0

# w dp5

SO2dp5 = 0
SIdp5 = 0
SSdp5 = 0
SNH4dp5 = 0
SN2dp5 = 0
SNOXdp5 = 0
SALKdp5 = 0
XIdp5 = 0
XSdp5 = 0
XHdp5 = 0
XSTOdp5 = 0
XAdp5 = 0
XSSdp5 = 0

# w dp6

SO2dp6 = 0
SIdp6 = 0
SSdp6 = 0
SNH4dp6 = 0
SN2dp6 = 0
SNOXdp6 = 0
SALKdp6 = 0
XIdp6 = 0
XSdp6 = 0
XHdp6 = 0
XSTOdp6 = 0
XAdp6 = 0
XSSdp6 = 0

# w dp7

SO2dp7 = 0
SIdp7 = 0
SSdp7 = 0
SNH4dp7 = 0
SN2dp7 = 0
SNOXdp7 = 0
SALKdp7 = 0
XIdp7 = 0
XSdp7 = 0
XHdp7 = 0
XSTOdp7 = 0
XAdp7 = 0
XSSdp7 = 0

# Q doplywajace (m^3 / dobe)

Qd = 18446

# Q doplywajace w m^3 / s

Qd = Qd / (3600 * 24)

# doplywajace = X * Qd?

SO2d = SO2 * Qd

SId = SI * Qd
SSd = SS * Qd
SNH4d = SNH4 * Qd
SN2d = SN2 * Qd
SNOXd = SNOX * Qd
SALKd = SALK * Qd

XId = XI * Qd
XSd = XS * Qd
XHd = XH * Qd
XSTOd = XSTO * Qd
XAd = XA * Qd
XSSd = XSS * Qd

# Qrz recyrkulacja zewnetrzna - zakladam 80% Qd

Qrz = 0.8 * Qd #/ (3600 * 24)

# SO2rz So2 w recyrkulacji zewnetrznej - dla tlenu = 0

SO2rz = 0

SIrz = 30

SSrz = 60
SNH4rz = 16
SN2rz = 0
SNOXrz = 0
SALKrz = 5

XIrz = 25
XSrz = 115
XHrz = 30
XSTOrz = 0
XArz = 0
XSSrz = 125

# ro deklaracja

rowdp1 = [0]

ro1wdp1 = [0]
ro2wdp1 = [0]
ro3wdp1 = [0]
ro4wdp1 = [0]
ro5wdp1 = [0]
ro6wdp1 = [0]
ro7wdp1 = [0]
ro8wdp1 = [0]
ro9wdp1 = [0]
ro10wdp1 = [0]
ro11wdp1 = [0]
ro12wdp1 = [0]

# zbiornik 2 
ro1wdp2 = [0]
ro2wdp2 = [0]
ro3wdp2 = [0]
ro4wdp2 = [0]
ro5wdp2 = [0]
ro6wdp2 = [0]
ro7wdp2 = [0]
ro8wdp2 = [0]
ro9wdp2 = [0]
ro10wdp2 = [0]
ro11wdp2 = [0]
ro12wdp2 = [0]

# zbiornik 3 

ro1wdp3 = [0]
ro2wdp3 = [0]
ro3wdp3 = [0]
ro4wdp3 = [0]
ro5wdp3 = [0]
ro6wdp3 = [0]
ro7wdp3 = [0]
ro8wdp3 = [0]
ro9wdp3 = [0]
ro10wdp3 = [0]
ro11wdp3 = [0]
ro12wdp3 = [0]

# zbiornik 4

ro1wdp4 = [0]
ro2wdp4 = [0]
ro3wdp4 = [0]
ro4wdp4 = [0]
ro5wdp4 = [0]
ro6wdp4 = [0]
ro7wdp4 = [0]
ro8wdp4 = [0]
ro9wdp4 = [0]
ro10wdp4 = [0]
ro11wdp4 = [0]
ro12wdp4 = [0]

# zbiornik 5

ro1wdp5 = [0]
ro2wdp5 = [0]
ro3wdp5 = [0]
ro4wdp5 = [0]
ro5wdp5 = [0]
ro6wdp5 = [0]
ro7wdp5 = [0]
ro8wdp5 = [0]
ro9wdp5 = [0]
ro10wdp5 = [0]
ro11wdp5 = [0]
ro12wdp5 = [0]

# zbiornik 6 

ro1wdp6 = [0]
ro2wdp6 = [0]
ro3wdp6 = [0]
ro4wdp6 = [0]
ro5wdp6 = [0]
ro6wdp6 = [0]
ro7wdp6 = [0]
ro8wdp6 = [0]
ro9wdp6 = [0]
ro10wdp6 = [0]
ro11wdp6 = [0]
ro12wdp6 = [0]

# zbiornik 7

ro1wdp6 = [0]
ro2wdp6 = [0]
ro3wdp6 = [0]
ro4wdp6 = [0]
ro5wdp6 = [0]
ro6wdp6 = [0]
ro7wdp6 = [0]
ro8wdp6 = [0]
ro9wdp6 = [0]
ro10wdp6 = [0]
ro11wdp6 = [0]
ro12wdp6 = [0]

# r deklaracja

r1 = [0]
r2 = [0]
r3 = [0]
r4 = [0]
r5 = [0]
r6 = [0]
r7 = [0]
r8 = [0]
r9 = [0]
r10 = [0]
r11 = [0]
r12 = [0]

# pojemnosc zbiorników V (m^3)

V = 1

# Lista dla calej recyrkulacji

SO2wdp1 = [0]
SIwdp1 = [0]
SSwdp1 = [0]
SNH4wdp1 = [0]
SN2wdp1 = [0]
SNOXwdp1 = [0]
SALKwdp1 = [0]
XIwdp1 = [0]
XSwdp1 = [0]
XHwdp1 = [0]
XSTOwdp1 = [0]
XAwdp1 = [0]
XSSwdp1 = [0]

SO2wdp2 = [0]
SIwdp2 = [0]
SSwdp2 = [0]
SNH4wdp2 = [0]
SN2wdp2 = [0]
SNOXwdp2 = [0]
SALKwdp2 = [0]
XIwdp2 = [0]
XSwdp2 = [0]
XHwdp2 = [0]
XSTOwdp2 = [0]
XAwdp2 = [0]
XSSwdp2 = [0]

SO2wdp3 = [0]
SIwdp3 = [0]
SSwdp3 = [0]
SNH4wdp3 = [0]
SN2wdp3 = [0]
SNOXwdp3 = [0]
SALKwdp3 = [0]
XIwdp3 = [0]
XSwdp3 = [0]
XHwdp3 = [0]
XSTOwdp3 = [0]
XAwdp3 = [0]
XSSwdp3 = [0]

SO2wdp4 = [0]
SIwdp4 = [0]
SSwdp4 = [0]
SNH4wdp4 = [0]
SN2wdp4 = [0]
SNOXwdp4 = [0]
SALKwdp4 = [0]
XIwdp4 = [0]
XSwdp4 = [0]
XHwdp4 = [0]
XSTOwdp4 = [0]
XAwdp4 = [0]
XSSwdp4 = [0]

SO2wdp5 = [0]
SIwdp5 = [0]
SSwdp5 = [0]
SNH4wdp5 = [0]
SN2wdp5 = [0]
SNOXwdp5 = [0]
SALKwdp5 = [0]
XIwdp5 = [0]
XSwdp5 = [0]
XHwdp5 = [0]
XSTOwdp5 = [0]
XAwdp5 = [0]
XSSwdp5 = [0]

SO2wdp6 = [0]
SIwdp6 = [0]
SSwdp6 = [0]
SNH4wdp6 = [0]
SN2wdp6 = [0]
SNOXwdp6 = [0]
SALKwdp6 = [0]
XIwdp6 = [0]
XSwdp6 = [0]
XHwdp6 = [0]
XSTOwdp6 = [0]
XAwdp6 = [0]
XSSwdp6 = [0]

SO2wdp7 = [0]
SIwdp7 = [0]
SSwdp7 = [0]
SNH4wdp7 = [0]
SN2wdp7 = [0]
SNOXwdp7 = [0]
SALKwdp7 = [0]
XIwdp7 = [0]
XSwdp7 = [0]
XHwdp7 = [0]
XSTOwdp7 = [0]
XAwdp7 = [0]
XSSwdp7 = [0]

# r startowe

rSO2wdp1 = 0

# pętla

for index in range(1,int(licznik),1):
    
    result = {}
    
    # zbiornik 1 
    
    result["phase1"] = {}
    
    # 1. Hydroliza
    rowdp1.append( kH10 * preventDivisionByZero(preventDivisionByZero(XSwdp1[-1], XHwdp1[-1]), (KX10 + preventDivisionByZero(XSwdp1[-1], XHwdp1[-1]))) * XHwdp1[-1] )
    # 2. Aerobic storage of Ss
    rowdp1.append( kSTO10 * preventDivisionByZero(SO2wdp1[-1], (KO210 + SO2wdp1[-1]))  * preventDivisionByZero(SSwdp1[-1], (KS10  + SSwdp1[-1])) * XHwdp1[-1] )
    # 3. Anoxic storage of Ss
    rowdp1.append( kSTO10 * niNOX10 * preventDivisionByZero(KO210, (KO210 + SO2wdp1[-1])) * preventDivisionByZero(SNOXwdp1[-1], (KNOX10 + SNOXwdp1[-1]) ) * preventDivisionByZero(SSwdp1[-1], (KS10 + SSwdp1[-1])) * XHwdp1[-1] )
    # 4. Aerobic growth
    rowdp1.append( mikroH10 * preventDivisionByZero(SO2wdp1[-1], (KO210 + SO2wdp1[-1])) * preventDivisionByZero(SNH4wdp1[-1], (KNH410 + SNH4wdp1[-1])) * preventDivisionByZero(SALKwdp1[-1], (KALK10 + SALKwdp1[-1])) * preventDivisionByZero(preventDivisionByZero(XSTOwdp1[-1], XHwdp1[-1]), (KSTO10 + preventDivisionByZero(XSTOwdp1[-1], XHwdp1[-1]))) * XHwdp1[-1] )
    # 5. Anoxic growth (denitrification)
    rowdp1.append( mikroH10 * niNOX10 * preventDivisionByZero(KO210, (KO210 + SO2wdp1[-1])) * preventDivisionByZero(SNOXwdp1[-1], (KNOX10 + SNOXwdp1[-1])) * preventDivisionByZero(SNH4wdp1[-1], ( KNH410 + SNH4wdp1[-1])) * preventDivisionByZero(SALKwdp1[-1], (KALK10 + SALKwdp1[-1])) * preventDivisionByZero(preventDivisionByZero(XSTOwdp1[-1], XHwdp1[-1]), (KSTO10 + preventDivisionByZero(XSTOwdp1[-1], XHwdp1[-1]))) * XHwdp1[-1] )
    # 6. Aerobic endogenous respiration
    rowdp1.append( bHO210 * preventDivisionByZero(SO2wdp1[-1], (KO210 + SO2wdp1[-1])) * XHwdp1[-1] )
    # 7. Anoxic endogenous respiration
    rowdp1.append( bHNOX10 * preventDivisionByZero(KO210, (KO210 + SO2wdp1[-1])) * preventDivisionByZero(SNOXwdp1[-1], (KNOX10 + SNOXwdp1[-1])) * XHwdp1[-1] )
    # 8. Aerobic respiration of XSTO
    rowdp1.append( bSTOO210 * preventDivisionByZero(SO2wdp1[-1], (KO210 + SO2wdp1[-1])) * XSTOwdp1[-1] )
    # 9. Anoxic respiration of XSTO
    rowdp1.append( bSTONOX10 * preventDivisionByZero(KO210, (KO210 + SO2wdp1[-1])) * preventDivisionByZero(SNOXwdp1[-1], (KNOX10 + SNOXwdp1[-1])) * XSTOwdp1[-1] )
    # 10. Aerobic growth of XA, nitrification
    rowdp1.append( mikroA10 * preventDivisionByZero(SO2wdp1[-1], (KAO210 + SO2wdp1[-1])) * preventDivisionByZero(SNH4wdp1[-1], (KANH410 + SNH4wdp1[-1])) * preventDivisionByZero(SALKwdp1[-1], (KAALK10 + SALKwdp1[-1]) ) * XAwdp1[-1] )
    # 11. Aerobic endogenous respiration
    rowdp1.append( bAO210 * preventDivisionByZero(SO2wdp1[-1], (KAO210 + SO2wdp1[-1])) * XAwdp1[-1] )
    # 12. Anoxic endogenous respiration
    rowdp1.append( bANOX10 * preventDivisionByZero(KAO210, (KAO210 + SO2wdp1[-1])) * preventDivisionByZero(SNOXwdp1[-1], (KNOX10 + SNOXwdp1[-1])) * XAwdp1[-1] )
    
    for i in range(12):
        ind = -12 + i
        rSO2wdp1 += tab[i][0] * rowdp1[ind]
        print(rSO2wdp1)
    
    SO2dp1 += (Qd / V) * (SO2d - SO2dp1) + (Qrz / V) * (SO2rz - SO2dp1) + rSO2wdp1 # + kLa * (SO2SA - SO2dp1)
    
    SO2wdp1.append(SO2dp1)
    
    result["phase1"]["SO2dp1"] = SO2dp1 #SO2wdp1[-1] ?
        
    SIdp1 += (Qd / V) * (SId - SIdp1) + (Qrz / V) * (SIrz - SIdp1)
    
    SIwdp1.append(SIdp1)
    
    SSdp1 += (Qd / V) * (SSd - SSdp1) + (Qrz / V) * (SSrz - SSdp1)
    
    SSwdp1.append(SSdp1)
    
    SNH4dp1 += (Qd / V) * (SNH4d - SNH4dp1) + (Qrz / V) * (SNH4rz - SNH4dp1)
    
    SNH4wdp1.append(SNH4dp1)
    
    SN2dp1 += (Qd / V) * (SN2d - SN2dp1) + (Qrz / V) * (SN2rz - SN2dp1)
    
    SN2wdp1.append(SN2dp1)
    
    SNOXdp1 += (Qd / V) * (SNOXd - SNOXdp1) + (Qrz / V) * (SNOXrz - SNOXdp1)
    
    SNOXwdp1.append(SNOXdp1)
    
    SALKdp1 += (Qd / V) * (SALKd - SALKdp1) + (Qrz / V) * (SALKrz - SALKdp1)
    
    SALKwdp1.append(SALKdp1)
    
    XIdp1 += (Qd / V) * (XId - XIdp1) + (Qrz / V) * (XIrz - XIdp1)
    
    XIwdp1.append(XIdp1)
    
    XSdp1 += (Qd / V) * (XSd - XSdp1) + (Qrz / V) * (XSrz - XSdp1)
    
    XSwdp1.append(XSdp1)
    
    XHdp1 += (Qd / V) * (XHd - XHdp1) + (Qrz / V) * (XHrz - XHdp1)
    
    XHwdp1.append(XHdp1)
    
    XSTOdp1 += (Qd / V) * (XSTOd - XSTOdp1) + (Qrz / V) * (XSTOrz - XSTOdp1)
    
    XSTOwdp1.append(XSTOdp1)
    
    XAdp1 += (Qd / V) * (XAd - XAdp1) + (Qrz / V) * (XArz - XAdp1)
    
    XAwdp1.append(XAdp1)
    
    XSSdp1 += (Qd / V) * (XSSd - XSSdp1) + (Qrz / V) * (XSSrz - XSSdp1)
    
    XSSwdp1.append(XSSdp1)
    
    # zbiornik 2 
    
    SO2dp2 += (Qd / V) * (SO2d - SO2dp2) + (Qrz / V) * (SO2rz - SO2dp2) # + rO2dp1 # + kLa * (SO2SA - SO2dp1)
    
    SO2wdp2.append(SO2dp2)
        
    SIdp2 += (Qd / V) * (SId - SIdp2) + (Qrz / V) * (SIrz - SIdp2)
    
    SIwdp2.append(SIdp2)
    
    SSdp2 += (Qd / V) * (SSd - SSdp2) + (Qrz / V) * (SSrz - SSdp2)
    
    SSwdp2.append(SSdp2)
    
    SNH4dp2 += (Qd / V) * (SNH4d - SNH4dp2) + (Qrz / V) * (SNH4rz - SNH4dp2)
    
    SNH4wdp2.append(SNH4dp2)
    
    SN2dp2 += (Qd / V) * (SN2d - SN2dp2) + (Qrz / V) * (SN2rz - SN2dp2)
    
    SN2wdp2.append(SN2dp2)
    
    SNOXdp2 += (Qd / V) * (SNOXd - SNOXdp2) + (Qrz / V) * (SNOXrz - SNOXdp2)
    
    SNOXwdp2.append(SNOXdp2)
    
    SALKdp2 += (Qd / V) * (SALKd - SALKdp2) + (Qrz / V) * (SALKrz - SALKdp2)
    
    SALKwdp2.append(SALKdp2)
    
    XIdp2 += (Qd / V) * (XId - XIdp2) + (Qrz / V) * (XIrz - XIdp2)
    
    XIwdp2.append(XIdp2)
    
    XSdp2 += (Qd / V) * (XSd - XSdp2) + (Qrz / V) * (XSrz - XSdp2)
    
    XSwdp2.append(XSdp2)
    
    XHdp2 += (Qd / V) * (XHd - XHdp2) + (Qrz / V) * (XHrz - XHdp2)
    
    XHwdp2.append(XHdp2)
    
    XSTOdp2 += (Qd / V) * (XSTOd - XSTOdp2) + (Qrz / V) * (XSTOrz - XSTOdp2)
    
    XSTOwdp2.append(XSTOdp2)
    
    XAdp2 += (Qd / V) * (XAd - XAdp2) + (Qrz / V) * (XArz - XAdp2)
    
    XAwdp2.append(XAdp2)
    
    XSSdp2 += (Qd / V) * (XSSd - XSSdp2) + (Qrz / V) * (XSSrz - XSSdp2)
    
    XSSwdp2.append(XSSdp2)
    
    # zbiornik 3
    
    SO2dp3 += (Qd / V) * (SO2d - SO2dp3) + (Qrz / V) * (SO2rz - SO2dp3) # + rO2dp3 # + kLa * (SO2SA - SO2dp3)
    
    SO2wdp3.append(SO2dp3)
        
    SIdp3 += (Qd / V) * (SId - SIdp3) + (Qrz / V) * (SIrz - SIdp3)
    
    SIwdp3.append(SIdp3)
    
    SSdp3 += (Qd / V) * (SSd - SSdp3) + (Qrz / V) * (SSrz - SSdp3)
    
    SSwdp3.append(SSdp3)
    
    SNH4dp3 += (Qd / V) * (SNH4d - SNH4dp3) + (Qrz / V) * (SNH4rz - SNH4dp3)
    
    SNH4wdp3.append(SNH4dp3)
    
    SN2dp3 += (Qd / V) * (SN2d - SN2dp3) + (Qrz / V) * (SN2rz - SN2dp3)
    
    SN2wdp3.append(SN2dp3)
    
    SNOXdp3 += (Qd / V) * (SNOXd - SNOXdp3) + (Qrz / V) * (SNOXrz - SNOXdp3)
    
    SNOXwdp3.append(SNOXdp3)
    
    SALKdp3 += (Qd / V) * (SALKd - SALKdp3) + (Qrz / V) * (SALKrz - SALKdp3)
    
    SALKwdp3.append(SALKdp3)
    
    XIdp3 += (Qd / V) * (XId - XIdp3) + (Qrz / V) * (XIrz - XIdp3)
    
    XIwdp3.append(XIdp3)
    
    XSdp3 += (Qd / V) * (XSd - XSdp3) + (Qrz / V) * (XSrz - XSdp3)
    
    XSwdp3.append(XSdp3)
    
    XHdp3 += (Qd / V) * (XHd - XHdp3) + (Qrz / V) * (XHrz - XHdp3)
    
    XHwdp3.append(XHdp3)
    
    XSTOdp3 += (Qd / V) * (XSTOd - XSTOdp3) + (Qrz / V) * (XSTOrz - XSTOdp3)
    
    XSTOwdp3.append(XSTOdp3)
    
    XAdp3 += (Qd / V) * (XAd - XAdp3) + (Qrz / V) * (XArz - XAdp3)
    
    XAwdp3.append(XAdp3)
    
    XSSdp3 += (Qd / V) * (XSSd - XSSdp3) + (Qrz / V) * (XSSrz - XSSdp3)
    
    XSSwdp3.append(XSSdp3)
    
    # zbiornik 4
    
    SO2dp4 += (Qd / V) * (SO2d - SO2dp4) + (Qrz / V) * (SO2rz - SO2dp4) # + rO2dp4 # + kLa * (SO2SA - SO2dp4)
    
    SO2wdp4.append(SO2dp4)
        
    SIdp4 += (Qd / V) * (SId - SIdp4) + (Qrz / V) * (SIrz - SIdp4)
    
    SIwdp4.append(SIdp4)
    
    SSdp4 += (Qd / V) * (SSd - SSdp4) + (Qrz / V) * (SSrz - SSdp4)
    
    SSwdp4.append(SSdp4)
    
    SNH4dp4 += (Qd / V) * (SNH4d - SNH4dp4) + (Qrz / V) * (SNH4rz - SNH4dp4)
    
    SNH4wdp4.append(SNH4dp4)
    
    SN2dp4 += (Qd / V) * (SN2d - SN2dp4) + (Qrz / V) * (SN2rz - SN2dp4)
    
    SN2wdp4.append(SN2dp4)
    
    SNOXdp4 += (Qd / V) * (SNOXd - SNOXdp4) + (Qrz / V) * (SNOXrz - SNOXdp4)
    
    SNOXwdp4.append(SNOXdp4)
    
    SALKdp4 += (Qd / V) * (SALKd - SALKdp4) + (Qrz / V) * (SALKrz - SALKdp4)
    
    SALKwdp4.append(SALKdp4)
    
    XIdp4 += (Qd / V) * (XId - XIdp4) + (Qrz / V) * (XIrz - XIdp4)
    
    XIwdp4.append(XIdp4)
    
    XSdp4 += (Qd / V) * (XSd - XSdp4) + (Qrz / V) * (XSrz - XSdp4)
    
    XSwdp4.append(XSdp4)
    
    XHdp4 += (Qd / V) * (XHd - XHdp4) + (Qrz / V) * (XHrz - XHdp4)
    
    XHwdp4.append(XHdp4)
    
    XSTOdp4 += (Qd / V) * (XSTOd - XSTOdp4) + (Qrz / V) * (XSTOrz - XSTOdp4)
    
    XSTOwdp4.append(XSTOdp4)
    
    XAdp4 += (Qd / V) * (XAd - XAdp4) + (Qrz / V) * (XArz - XAdp4)
    
    XAwdp4.append(XAdp4)
    
    XSSdp4 += (Qd / V) * (XSSd - XSSdp4) + (Qrz / V) * (XSSrz - XSSdp4)
    
    XSSwdp4.append(XSSdp4)
    
    # zbiornik 5
    
    SO2dp5 += (Qd / V) * (SO2d - SO2dp5) + (Qrz / V) * (SO2rz - SO2dp5) # + rO2dp5 # + kLa * (SO2SA - SO2dp5)
    
    SO2wdp5.append(SO2dp5)
        
    SIdp5 += (Qd / V) * (SId - SIdp5) + (Qrz / V) * (SIrz - SIdp5)
    
    SIwdp5.append(SIdp5)
    
    SSdp5 += (Qd / V) * (SSd - SSdp5) + (Qrz / V) * (SSrz - SSdp5)
    
    SSwdp5.append(SSdp5)
    
    SNH4dp5 += (Qd / V) * (SNH4d - SNH4dp5) + (Qrz / V) * (SNH4rz - SNH4dp5)
    
    SNH4wdp5.append(SNH4dp5)
    
    SN2dp5 += (Qd / V) * (SN2d - SN2dp5) + (Qrz / V) * (SN2rz - SN2dp5)
    
    SN2wdp5.append(SN2dp5)
    
    SNOXdp5 += (Qd / V) * (SNOXd - SNOXdp5) + (Qrz / V) * (SNOXrz - SNOXdp5)
    
    SNOXwdp5.append(SNOXdp5)
    
    SALKdp5 += (Qd / V) * (SALKd - SALKdp5) + (Qrz / V) * (SALKrz - SALKdp5)
    
    SALKwdp5.append(SALKdp5)
    
    XIdp5 += (Qd / V) * (XId - XIdp5) + (Qrz / V) * (XIrz - XIdp5)
    
    XIwdp5.append(XIdp5)
    
    XSdp5 += (Qd / V) * (XSd - XSdp5) + (Qrz / V) * (XSrz - XSdp5)
    
    XSwdp5.append(XSdp5)
    
    XHdp5 += (Qd / V) * (XHd - XHdp5) + (Qrz / V) * (XHrz - XHdp5)
    
    XHwdp5.append(XHdp5)
    
    XSTOdp5 += (Qd / V) * (XSTOd - XSTOdp5) + (Qrz / V) * (XSTOrz - XSTOdp5)
    
    XSTOwdp5.append(XSTOdp5)
    
    XAdp5 += (Qd / V) * (XAd - XAdp5) + (Qrz / V) * (XArz - XAdp5)
    
    XAwdp5.append(XAdp5)
    
    XSSdp5 += (Qd / V) * (XSSd - XSSdp5) + (Qrz / V) * (XSSrz - XSSdp5)
    
    XSSwdp5.append(XSSdp5)
    
    # zbiornik 6
    
    SO2dp6 += (Qd / V) * (SO2d - SO2dp6) + (Qrz / V) * (SO2rz - SO2dp6) # + rO2dp6 # + kLa * (SO2SA - SO2dp6)
    
    SO2wdp6.append(SO2dp6)
        
    SIdp6 += (Qd / V) * (SId - SIdp6) + (Qrz / V) * (SIrz - SIdp6)
    
    SIwdp6.append(SIdp6)
    
    SSdp6 += (Qd / V) * (SSd - SSdp6) + (Qrz / V) * (SSrz - SSdp6)
    
    SSwdp6.append(SSdp6)
    
    SNH4dp6 += (Qd / V) * (SNH4d - SNH4dp6) + (Qrz / V) * (SNH4rz - SNH4dp6)
    
    SNH4wdp6.append(SNH4dp6)
    
    SN2dp6 += (Qd / V) * (SN2d - SN2dp6) + (Qrz / V) * (SN2rz - SN2dp6)
    
    SN2wdp6.append(SN2dp6)
    
    SNOXdp6 += (Qd / V) * (SNOXd - SNOXdp6) + (Qrz / V) * (SNOXrz - SNOXdp6)
    
    SNOXwdp6.append(SNOXdp6)
    
    SALKdp6 += (Qd / V) * (SALKd - SALKdp6) + (Qrz / V) * (SALKrz - SALKdp6)
    
    SALKwdp6.append(SALKdp6)
    
    XIdp6 += (Qd / V) * (XId - XIdp6) + (Qrz / V) * (XIrz - XIdp6)
    
    XIwdp6.append(XIdp6)
    
    XSdp6 += (Qd / V) * (XSd - XSdp6) + (Qrz / V) * (XSrz - XSdp6)
    
    XSwdp6.append(XSdp6)
    
    XHdp6 += (Qd / V) * (XHd - XHdp6) + (Qrz / V) * (XHrz - XHdp6)
    
    XHwdp6.append(XHdp6)
    
    XSTOdp6 += (Qd / V) * (XSTOd - XSTOdp6) + (Qrz / V) * (XSTOrz - XSTOdp6)
    
    XSTOwdp6.append(XSTOdp6)
    
    XAdp6 += (Qd / V) * (XAd - XAdp6) + (Qrz / V) * (XArz - XAdp6)
    
    XAwdp6.append(XAdp6)
    
    XSSdp6 += (Qd / V) * (XSSd - XSSdp6) + (Qrz / V) * (XSSrz - XSSdp6)
    
    XSSwdp6.append(XSSdp6)
    
    # zibiornik 7
    
    SO2dp7 += (Qd / V) * (SO2d - SO2dp7) + (Qrz / V) * (SO2rz - SO2dp7) # + rO2dp7 # + kLa * (SO2SA - SO2dp7)
    
    SO2wdp7.append(SO2dp7)
        
    SIdp7 += (Qd / V) * (SId - SIdp7) + (Qrz / V) * (SIrz - SIdp7)
    
    SIwdp7.append(SIdp7)
    
    SSdp7 += (Qd / V) * (SSd - SSdp7) + (Qrz / V) * (SSrz - SSdp7)
    
    SSwdp7.append(SSdp7)
    
    SNH4dp7 += (Qd / V) * (SNH4d - SNH4dp7) + (Qrz / V) * (SNH4rz - SNH4dp7)
    
    SNH4wdp7.append(SNH4dp7)
    
    SN2dp7 += (Qd / V) * (SN2d - SN2dp7) + (Qrz / V) * (SN2rz - SN2dp7)
    
    SN2wdp7.append(SN2dp7)
    
    SNOXdp7 += (Qd / V) * (SNOXd - SNOXdp7) + (Qrz / V) * (SNOXrz - SNOXdp7)
    
    SNOXwdp7.append(SNOXdp7)
    
    SALKdp7 += (Qd / V) * (SALKd - SALKdp7) + (Qrz / V) * (SALKrz - SALKdp7)
    
    SALKwdp7.append(SALKdp7)
    
    XIdp7 += (Qd / V) * (XId - XIdp7) + (Qrz / V) * (XIrz - XIdp7)
    
    XIwdp7.append(XIdp7)
    
    XSdp7 += (Qd / V) * (XSd - XSdp7) + (Qrz / V) * (XSrz - XSdp7)
    
    XSwdp7.append(XSdp7)
    
    XHdp7 += (Qd / V) * (XHd - XHdp7) + (Qrz / V) * (XHrz - XHdp7)
    
    XHwdp7.append(XHdp7)
    
    XSTOdp7 += (Qd / V) * (XSTOd - XSTOdp7) + (Qrz / V) * (XSTOrz - XSTOdp7)
    
    XSTOwdp7.append(XSTOdp7)
    
    XAdp7 += (Qd / V) * (XAd - XAdp7) + (Qrz / V) * (XArz - XAdp7)
    
    XAwdp7.append(XAdp7)
    
    XSSdp7 += (Qd / V) * (XSSd - XSSdp7) + (Qrz / V) * (XSSrz - XSSdp7)
    
    XSSwdp7.append(XSSdp7)
    
    
    '''
    ro1.append( kH10 * ( (XS / XH) / KX10 + (XS / XH) ) * XH )
    # 2. Aerobic storage of Ss
    ro2.append( kSTO10 * ( SO2 / (KO210 + SO2) ) * ( SS / ( KS10  + SS) ) * XH )
    # 3. Anoxic storage of Ss
    ro3.append( kSTO10 * niNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * ( SS / (KS10 + SS) ) * XH )
    # 4. Aerobic growth
    ro4.append( mikroH10 * ( SO2 / (KO210 + SO2) ) * ( SNH4 / ( KNH410 + SNH4) ) * (SALK / (KALK10 + SALK) ) * ( (XSTO / XH) / (KSTO10 + (XSTO / XH) ) ) * XH )
    # 5. Anoxic growth (denitrification)
    ro5.append( mikroH10 * niNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * ( SNH4 / ( KNH410 + SNH4) ) * (SALK / (KALK10 + SALK) ) * ( (XSTO / XH) / (KSTO10 + (XSTO / XH) ) ) * XH )
    # 6. Aerobic endogenous respiration
    ro6.append( bHO210 * ( SO2 / (KO210 + SO2) ) * XH )
    # 7. Anoxic endogenous respiration
    ro7.append( bHNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XH )
    # 8. Aerobic respiration of XSTO
    ro8.append( bSTOO210 * ( SO2 / (KO210 + SO2) ) * XSTO )
    # 9. Anoxic respiration of XSTO
    ro9.append( bSTONOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XSTO )

    # te też?

    # 10. Aerobic growth of XA, nitrification
    ro10.append( mikroA10 * ( SO2 / (KAO210 + SO2) ) * ( SNH4 / (KANH410 + SNH4) ) * ( SALK / (KAALK10 + SALK) ) * XA )
    # 11. Aerobic endogenous respiration
    ro11.append( bAO210 * ( SO2 / (KAO210 + SO2) ) * XA )
    # 12. Anoxic endogenous respiration
    ro12.append( bANOX10 * ( KAO210 / (KAO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XA )
    '''
    '''
    ro1dp.append( kH10 * ( (tab[ / XH) / KX10 + (XS / XH) ) * XH )
    # 2. Aerobic storage of Ss
    ro2dp.append( kSTO10 * ( SO2 / (KO210 + SO2) ) * ( SS / ( KS10  + SS) ) * XH )
    # 3. Anoxic storage of Ss
    ro3dp.append( kSTO10 * niNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * ( SS / (KS10 + SS) ) * XH )
    # 4. Aerobic growth
    ro4dp.append( mikroH10 * ( SO2 / (KO210 + SO2) ) * ( SNH4 / ( KNH410 + SNH4) ) * (SALK / (KALK10 + SALK) ) * ( (XSTO / XH) / (KSTO10 + (XSTO / XH) ) ) * XH )
    # 5. Anoxic growth (denitrification)
    ro5dp.append( mikroH10 * niNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * ( SNH4 / ( KNH410 + SNH4) ) * (SALK / (KALK10 + SALK) ) * ( (XSTO / XH) / (KSTO10 + (XSTO / XH) ) ) * XH )
    # 6. Aerobic endogenous respiration
    ro6dp.append( bHO210 * ( SO2 / (KO210 + SO2) ) * XH )
    # 7. Anoxic endogenous respiration
    ro7dp.append( bHNOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XH )
    # 8. Aerobic respiration of XSTO
    ro7dp.append( bSTOO210 * ( SO2 / (KO210 + SO2) ) * XSTO )
    # 9. Anoxic respiration of XSTO
    ro8dp.append( bSTONOX10 * ( KO210 / (KO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XSTO )
    
    # te też?
    
    # 10. Aerobic growth of XA, nitrification
    ro9dp.append( mikroA10 * ( SO2 / (KAO210 + SO2) ) * ( SNH4 / (KANH410 + SNH4) ) * ( SALK / (KAALK10 + SALK) ) * XA )
    # 11. Aerobic endogenous respiration
    ro10dp.append( bAO210 * ( SO2 / (KAO210 + SO2) ) * XA )
    # 12. Anoxic endogenous respiration
    ro11dp.append( bANOX10 * ( KAO210 / (KAO210 + SO2) ) * ( SNOX / (KNOX10 + SNOX) ) * XA )
    '''


    #print(result)
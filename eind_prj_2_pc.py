#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# TN_code version > 1.1
from TN_code import TISTNplot as TN
meetdata = np.loadtxt('meetdata.csv')

x = meetdata[:, 0] #lees meetdata set 1 in
y = meetdata[:, 1] #lees meetdata set 2 in
yerr = 0.2 * y

y_2 = meetdata[:, 2]

formatterX = TN.TNFormatter(4)
formatterY = TN.TNFormatter(2)
z = np.linspace(0.1, max(x))
w = 3 * z + 0 #formule van de trendlijn

fig, ax = plt.subplots()  # 1 figuur

ax.yaxis.set_major_formatter(formatterY)
ax.xaxis.set_major_formatter(formatterX)

ax.errorbar(x, y, yerr,  capsize=5, fmt='*', mfc='black',
            mec='black', ms=5, mew=2)

ax.errorbar(x, y_2, yerr,  capsize=5, fmt='x', mfc='red',
            mec='red', ms=5, mew=2)

legend_drawn_flag = True #als je een legenda wilt
plt.legend(["meting 1", "meting 2"], loc=0, frameon=legend_drawn_flag) #eigenschappen van de legenda

TN.label_x("l", "m", ax, text="lengte ")
TN.label_y("t", "s", ax, text="trillingstijd ")
ax.plot(z, w) #plotten van de trendlijn
plt.grid()
plt.tight_layout()
plt.savefig("voorbeeld.eps", format='eps', dpi=1200)  #svg is een vector 'opslag' methode
plt.show()

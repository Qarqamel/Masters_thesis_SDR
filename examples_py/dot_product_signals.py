import numpy as np
import matplotlib.pyplot as plt
from auxiliary_lib import my_plot
import string
import scipy.interpolate

A_vector = [0.088,0.088,0.088,0.442,0.530,0.000,-0.530,-0.442,-0.088,-0.088,-0.088]
B_vector_list = [
     [0.080,0.080,0.080,0.398,0.477,0.000,-0.477,-0.398,-0.080,-0.080,-0.080],
     [0.129,0.129,0.129,0.514,0.643,0.000,0.129,0.129,0.129,0.129,0.129],
     [-0.129,-0.129,-0.129,-0.514,-0.643,-0.000,-0.129,-0.129,-0.129,-0.129,-0.129],
     [-0.080,-0.080,-0.080,-0.398,-0.477,-0.000,0.477,0.398,0.080,0.080,0.080],
     [0.000, 0.050, 0.000, -0.050, 0.000, 0.050, 0.000, -0.050, 0.000, 0.050, 0.000],
     [0.500, 0.550, 0.500, 0.450, 0.500, 0.550, 0.500, 0.450, 0.500, 0.550, 0.500],
     [0.500, 0.650, 0.500, 0.350, 0.500, 0.650, 0.500, 0.350, 0.500, 0.650, 0.500],
     [-0.500, -0.350, -0.500, -0.650, -0.500, -0.350, -0.500, -0.650, -0.500, -0.350, -0.500]
    ]

t = np.linspace(0,10, 11)
t_inter = np.linspace(0,10,1000)

A_vector_inter_func = scipy.interpolate.interp1d(t, A_vector, kind='cubic')
A_vector_inter = A_vector_inter_func(t_inter)
B_vector_inter_func = scipy.interpolate.interp1d(t, B_vector_list[1], kind='cubic')
B_vector_inter = B_vector_inter_func(t_inter)

dot_product = np.array(A_vector)*np.array(B_vector_list[1])

RES = 100

# plt.rcParams.update({'axes.facecolor':'#FAF4F6'})
plt.rcdefaults()
plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)
plt.rc('font', family='Arial')

plt.figure(figsize = [4.8, 2.07], dpi=RES)
plt.axhline(y=0,color='black', linewidth=0.8)
plt.plot(t_inter, A_vector_inter, 'C0-', alpha = 0.3)
plt.plot(t_inter, B_vector_inter, 'C2-', alpha = 0.3)
plt.plot(t, A_vector, 'C0o', label = 'A')
plt.plot(t, B_vector_list[1], 'C2o', label = 'B')
plt.xticks(ticks = t, labels=range(0,11))
plt.legend(loc = 'lower center', ncol=2 , bbox_to_anchor=(0.5, 1), framealpha=0)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.grid(axis='x')

plt.figure(figsize = [4.8, 2.07], dpi=RES)
plt.axhline(y=0,color='black', linewidth=0.8)
markerline, stemline, baseline, = plt.stem(t, dot_product, linefmt = 'C1', markerfmt='o', basefmt = ' ')
plt.setp(markerline, color = 'C1')
plt.title('A * B')
plt.xticks(ticks = t, labels=range(0,11))
plt.yticks(np.linspace(-0.1, 0.4, 6))
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.grid(axis='x')
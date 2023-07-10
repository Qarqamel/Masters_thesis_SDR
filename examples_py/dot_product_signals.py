import numpy as np
import matplotlib.pyplot as plt
from auxiliary_lib import my_plot
import string

def arb_function_1(x):
    return -1/3*np.sin(x) - 1/4*np.sin(2*x)

def arb_function_2(x):
    return -1/3*np.sin(x-np.pi/4) - 1/2*np.sin(2*x + np.pi/4)

angles = np.linspace(-4, 4, 1001)
arb_func_1 = [arb_function_1(ang) for ang in angles]
arb_func_2 = [arb_function_2(ang) for ang in angles]

angles_samp = angles[0::100]
arb_func_samp_1 = arb_func_1[0::100]
arb_func_samp_2 = arb_func_2[0::100]

dot_product = np.array(arb_func_samp_1)*np.array(arb_func_samp_2)

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

plt.figure(figsize = [6.4, 3.2], dpi=RES)
plt.plot(angles, arb_func_1, 'C0-', label = 'A')
plt.plot(angles, arb_func_2, 'C2-', label = 'B')
plt.plot(angles_samp, arb_func_samp_1, 'C0o')
plt.plot(angles_samp, arb_func_samp_2, 'C2o')
plt.axhline(y=0,color='black', linewidth=0.8)
plt.xticks(ticks = angles_samp, labels=range(0,11))
plt.legend(loc = 'lower center', ncol=2 , bbox_to_anchor=(0.5, 1), framealpha=0)
plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
plt.grid()

plt.figure(figsize = [6.4, 3.2], dpi=RES)
markerline, stemline, baseline, = plt.stem(angles_samp, dot_product, linefmt = 'red', markerfmt='o', basefmt = ' ')
plt.setp(markerline, color = 'red')
plt.title('A * B')
plt.axhline(y=0,color='black', linewidth=0.8)
plt.xticks(ticks = angles_samp, labels=range(0,11))
plt.yticks(np.linspace(-0.1, 0.4, 6))
# plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
plt.grid()
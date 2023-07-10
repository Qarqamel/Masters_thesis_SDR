import numpy as np
import matplotlib.pyplot as plt
from auxiliary_lib import my_plot
import string

def arb_function_1(x):
    return -1/3*np.sin(x) - 1/4*np.sin(2*x)

def arb_function_2(x):
    return -1/3*np.sin(x-np.pi/4) - 1/4*np.sin(2*x + np.pi/4)




angles = np.linspace(-4, 4, 1001)
arb_func_1 = [arb_function_1(ang) for ang in angles]
angles_samp = angles[0::100]
arb_func_samp_1 = arb_func_1[0::100]

arb_function_for_dot_list = [
    [9/10*arb_function_1(ang) for ang in angles],
    [arb_function_2(ang) for ang in angles],
    [-arb_function_2(ang) for ang in angles],
    [-9/10*arb_function_1(ang) for ang in angles],
    np.cos(angles)/10,
    np.cos(angles)/10+0.35,
    np.sin(angles-np.pi/2)/5+0.35,
    np.sin(angles-np.pi/2)/5-0.35,
    ]
for arb_func_2, i in zip(arb_function_for_dot_list, range(len(arb_function_for_dot_list))):
    arb_func_samp_2 = arb_func_2[0::100]
    
    dot_product = np.array(arb_func_samp_1)*np.array(arb_func_samp_2)
    
    print(sum(dot_product))
    
    RES = 500
    
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
    
    plt.figure(figsize = [1.6, 0.8], dpi=RES)
    plt.title(round(sum(dot_product),4) if (sum(dot_product)>0.1 or sum(dot_product)<-0.1) else 0)
    plt.axhline(y=0,color='black', linewidth=0.8)
    plt.plot(angles, arb_func_1, 'C0-')
    plt.plot(angles, arb_func_2, 'C2-')
    plt.plot(angles_samp, arb_func_samp_1, 'C0.')
    plt.plot(angles_samp, arb_func_samp_2, 'C2.')
    plt.xticks(ticks = angles_samp, labels=range(0,11))
    plt.ylim(-0.6, 0.6)
    if i == 0 or i ==4:
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
    else:
        plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.grid()
    
    plt.figure(figsize = [1.6, 0.8], dpi=RES)
    plt.axhline(y=0,color='black', linewidth=0.8)
    markerline, stemline, baseline, = plt.stem(angles_samp, dot_product, linefmt = 'red', markerfmt='.', basefmt = ' ')
    plt.setp(markerline, color = 'red')
    plt.xticks(ticks = angles_samp, labels=range(0,11))
    plt.ylim(-0.3, 0.3)
    plt.yticks([-0.2,0,0.2])
    if i == 0 or i ==4:
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
    else:
        plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.grid()

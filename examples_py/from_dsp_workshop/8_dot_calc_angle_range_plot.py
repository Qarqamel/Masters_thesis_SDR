from mylib import rotate_vector
import numpy as np
import matplotlib.pyplot as plt
from auxiliary_lib import my_plot

v = [0, 1]

angle_list = list()
dot_list = list()

angle_short = list()
dot_short = list()

for angle in range(0, 370, 10):    
    angle_list.append(angle)    
    v_rot = rotate_vector(v, angle)
    dot = np.dot(v, v_rot)
    dot_list.append(dot)

for angle in range(0, 360, 45):    
    angle_short.append(angle)    
    v_rot = rotate_vector(v, angle)
    dot = np.dot(v, v_rot)
    dot_short.append(dot)

RES = 150

# plt.rcParams.update({'axes.facecolor':'#FAF4F6'})
plt.rcdefaults()
plt.rc('font', size=8)
plt.rc('font', family='Arial')

#my_plot(angle_list, {'dot':dot_list})
plt.figure(figsize = [6.4, 3.2], dpi=RES)
plt.plot(angle_list,dot_list, '-', color = 'black')
plt.plot(angle_short,dot_short, '.', color = 'black', markersize=15)
plt.axhline(y=0,color='black', linewidth=0.8)
plt.xticks(list(np.arange(0,370, step=45)))
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

plt.xlabel('kąt [°]')
plt.ylabel('iloczyn skalarny')

plt.grid(axis='x')


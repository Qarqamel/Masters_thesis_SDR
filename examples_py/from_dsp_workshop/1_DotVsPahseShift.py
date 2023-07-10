import numpy as np
import matplotlib.pyplot as plt
from mylib import rotate_vector
from auxiliary_lib import my_plot

RES = 500
PI = np.pi

# PARAMETER
PHASE_SHIFT_LIST = np.linspace(0, 7/4*PI,8, endpoint=True)

dot_list = []

plt.rcdefaults()
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('font', size=8)
plt.rc('font', family='Arial')
# plt.rcParams.update({'axes.facecolor':'#FAF4F6'})

for shift in PHASE_SHIFT_LIST:
    # VECTORS
    t = np.linspace(0, 2*PI,1000, endpoint=False)
    
    Ref = np.sin(t)
    if shift == PHASE_SHIFT_LIST[0]:
        Shifted = np.sin(t+shift+PI/100)
    else:
        Shifted = np.sin(t+shift)
    Ref_mult_Shifted = Ref*Shifted
    dot_product = np.sum(Ref_mult_Shifted)
    dot_list.append(dot_product)
    
    
    plt.figure(figsize = [1.6, 0.8], dpi=RES)
    plt.plot(t, Ref, '-', color='C0', label='Ref')
    plt.plot(t, Shifted, '-', color='C2', label='Shifted')
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
        plt.yticks([-1, 0, 1])
    else:
        plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.axhline(y=0,color='black', linewidth=0.8)
    plt.ylim(-1.1,1.1)
    if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
        plt.legend(framealpha = 0.5)
    plt.show()
    
    plt.figure(figsize = [1.6, 0.8], dpi=RES)
    # plt.plot(t, Ref_mult_Shifted, '-', color = 'C1', alpha = 0.1, label='Mult')
    plt.fill_between(t, Ref_mult_Shifted, color = 'C1', step="pre", alpha=0.3, label='Mult')
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
        plt.yticks([-1, 0, 1])
    else:
        plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.axhline(y=0,color='black', linewidth=0.8)
    plt.axhline(y=np.mean(Ref_mult_Shifted), color='red', linestyle='-')
    plt.ylim(-1.1,1.1)
    if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
        plt.legend(framealpha = 0.5)
    plt.show()
    # print phase shift and dot product value
    print(f'phase_shift = {shift : 0.2f}')
    print(f'dot_product = {dot_product : 0.2f}')
    
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

plt.rc('ytick', labelsize=8)
#my_plot(angle_list, {'dot':dot_list})
plt.figure(figsize = [6.4, 2.5], dpi=RES)
plt.axhline(y=0,color='black', linewidth=0.8)
plt.plot(angle_list,dot_list, '-', color = 'black')
plt.plot(angle_short,dot_short, '.', color = 'red', markersize=15)
plt.xticks(list(np.arange(0,370, step=45)))
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

plt.xlabel('przesunięcie fazowe [°]')
plt.ylabel('iloczyn skalarny')

plt.grid(axis='x')
plt.show()

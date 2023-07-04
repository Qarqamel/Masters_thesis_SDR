import numpy as np
import matplotlib.pyplot as plt
from mylib import rotate_vector

RES = 100
PI = np.pi

# PARAMETER
PHASE_SHIFT_LIST = np.linspace(0, 7/4*PI,8, endpoint=True)

dot_list = []

for shift in PHASE_SHIFT_LIST:
    # VECTORS
    t = np.linspace(0, 2*PI,30, endpoint=False)
    
    Ref = np.sin(t)
    if shift == PHASE_SHIFT_LIST[0]:
        Shifted = np.sin(t+shift+PI/100)
    else:
        Shifted = np.sin(t+shift)
    Ref_mult_Shifted = Ref*Shifted
    dot_product = np.sum(Ref_mult_Shifted)
    dot_list.append(dot_product)
    
    
    plt.figure(figsize = [6.4, 3.2], dpi=RES, facecolor='#FAF4F6')
    plt.plot(t, Ref, 'p-', color='C0', label='Ref')
    plt.plot(t, Shifted, 'p-', color='C2', label='Shifted')
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    # if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
    #     plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
    # else:
    #     plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.axhline(y=0,color='black')
    plt.ylim(-1.1,1.1)
    if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
        plt.legend()
    plt.show()
    
    plt.figure(figsize = [6.4, 3.2], dpi=RES, facecolor='#FAF4F6')
    plt.stem(t, Ref_mult_Shifted, linefmt = 'C1', markerfmt = 'C1o', basefmt = ' ', label='Ref_mult_Shifted')
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    # if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
    #     plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
    # else:
    #     plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.axhline(y=0,color='black')
    plt.axhline(y=np.mean(Ref_mult_Shifted), color='C1', linestyle='--')
    plt.ylim(-1.1,1.1)
    if shift == PHASE_SHIFT_LIST[0] or shift == PHASE_SHIFT_LIST[4]:
        plt.legend()
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

plt.rcdefaults()
plt.rcParams.update({'axes.facecolor':'#FAF4F6'})

#my_plot(angle_list, {'dot':dot_list})
plt.figure(figsize = [6.4, 2.5], dpi=RES, facecolor='#FAF4F6')
plt.plot(angle_list,dot_list, 'C1-')
plt.plot(angle_short,dot_short, 'C1.', markersize=15)
plt.xticks(list(np.arange(0,370, step=45)))

plt.xlabel('shift')
plt.ylabel('dot product')

# plt.grid()
plt.show()

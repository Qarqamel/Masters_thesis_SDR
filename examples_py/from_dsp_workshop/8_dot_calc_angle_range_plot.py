from mylib import rotate_vector
import numpy as np
import matplotlib.pyplot as plt

v = [0, 1]

angle_list = list()
dot_list = list()

for angle in range(0, 370, 10):    
    angle_list.append(angle)    
    v_rot = rotate_vector(v, angle)
    dot = np.dot(v, v_rot)
    dot_list.append(dot)

plt.plot(angle_list,dot_list, '-p')

plt.xlabel('angle')
plt.ylabel('dot product')

plt.grid()


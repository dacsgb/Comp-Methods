import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

T_data, p_data, R_data = np.loadtxt('Tests\Test 2 Part 2\Exam2_data.txt',unpack=True)

R_600 = np.empty(0)
R_700 = np.empty(0)
R_800 = np.empty(0)
T = np.empty(0)

Ti = 100
Tf = 700
step = 100
inc = (Tf-Ti)/step

for i in range(step):
    T = np.append(T,Ti + i*inc)
    R_600 = np.append(R_600, float(griddata((T_data,p_data),R_data,(T[-1],600))))
    R_700 = np.append(R_700, float(griddata((T_data,p_data),R_data,(T[-1],700))))
    R_800 = np.append(R_800, float(griddata((T_data,p_data),R_data,(T[-1],800))))

plt.figure(1)
plt.plot(T,R_600,label='p = 600 psi')
plt.plot(T,R_700,label='p = 700 psi')
plt.plot(T,R_800,label='p = 800 psi')
plt.xlabel('Temperature - [F]')
plt.ylabel('Reluctance - [%]')
plt.legend()
plt.show()

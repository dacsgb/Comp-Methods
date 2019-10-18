import numpy as np

T, p, R = np.loadtxt('Tests\Test 2 Part 2\Exam2_data.txt',unpack=True)

T_avg = np.average(T)
p_avg = np.average(p)
R_avg = np.average(R)

print('The mean temperature value is: {:.1f} F'.format(T_avg))
print('The mean pressure value is: {:.1f} psi'.format(p_avg))
print('The mean reluctance value is: {:.4f} %'.format(R_avg))
'''
Created on 31.08.2014

@author: proSingularity
'''
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])    
data_x = [0, 1, 2, 2, 3, 4]
data_y = [1.5, 1., 0.7, 2.5, 1, 1.5]
plt.plot(data_x, data_y, 'or')

plt.plot(1,25, 'or')
plt.ylabel('some numbers')
plt.show()

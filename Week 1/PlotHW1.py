#import numpy and matlibplots module


#generate array of x values from 0 to 6pi

#calculate y values for sin wave

#calculate y values for cosine wave

#plot x and y values for both functions 

#set dashed line for sine wave and solide line for cosine wave

#add legend


#leave comment here with your information
#Name:
#Date:
#import numpy and matlibplots module
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
#generate array of x values from 0 to 6pi

#calculate y values for sin wave

#calculate y values for cosine wave
#
#plot x and y values for both functions 

#set dashed line for sine wave and solide line for cosine wave

#add legend

#leave comment here with your information
#Name: Obinna Okonkwo       
#Date: 1/17/2016
x = np.linspace(0, 2*3.14, 101)
y1 = np.sin(x)
y2 = np.cos(x)
plt.legend(['Sin = Red, Cos = Blue'], loc='right', shadow=True)
plt.plot(x, y1, x, y2)
plt.title("Obi's Graph")
plt.show()


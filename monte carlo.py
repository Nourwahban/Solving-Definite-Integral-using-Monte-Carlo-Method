import math
import numpy as np
import matplotlib.pyplot as plt

#number of trials
N=(100000)

#range of the integral a=-5 , b=5
x=np.random.uniform(-5,5,N)

#f(x) 
y = np.exp((-x**2) / 2)

#get the min and max points for y 
max=np.max(y)
min=np.min(y)

#get the points of y that lies in the range
ycoord=np.random.uniform(min,max,N)

#check if the points lie within the range or not
points_inside= ycoord<= np.exp((-x**2) / 2)

#total number of points that lies within the range
in_area=sum(points_inside)

#the area of the drawn box
Boxarea= 10

print("approximate value is: ",(in_area/N)*Boxarea)
# Plotting
plt.figure(figsize=(8, 6))

# Plot all points
plt.scatter(x, y_coord, s=1, color='blue', label='All Points')

# Plot points inside the range
plt.scatter(x[points_inside], y_coord[points_inside], s=1, color='red', label='Points Inside')

# Plot the function
x_values = np.linspace(-5, 5, 1000)
plt.plot(x_values, np.exp((-x_values**2) / 2), color='green', label='Function e^(-x^2/2)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Points and Function e^(-x^2/2)')
plt.legend()
plt.grid(True)
plt.show()

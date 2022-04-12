from matplotlib import pyplot as plt 
x_axis = [0, 0, 2.82 , 0]
y_axis = [0, 2.82, 2.82 , 0]
plt.plot(x_axis,y_axis,'b',marker = 'o',linewidth =4,)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('fig-1')
plt.legend()
plt.grid(True)
plt.show()

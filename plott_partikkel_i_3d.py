from mpl_toolkits.mplot3d import  axes3d
import numpy as np
import matplotlib.pyplot as plt

SIZE_X = 512
SIZE_Y = 1024
NUM_SENSORS = 1  # Number of stacked sensors
sensor = np.empty(shape=(SIZE_X, SIZE_Y))  # 512 x 1024 pixels. 0 for no hit, 1 for hit from a particle

for i in range(NUM_SENSORS):
    rand_x_val = np.random.randint(0, SIZE_X)
    rand_y_val = np.random.randint(0, SIZE_Y)
    sensor[rand_x_val][rand_y_val] = 1  # Mark particle hit



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.xlim(0, SIZE_X)
plt.ylim(0, SIZE_Y)
x = [rand_x_val]
y = [rand_y_val]
z = [NUM_SENSORS]
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter(x, y, z)
ax.legend()
plt.show()
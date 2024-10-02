import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
nodes = np.array([
    [0, 0],
    [1, 0],
    [0.5, 1],
])
tri = Delaunay(nodes)
plt.triplot(nodes[:,0], nodes[:,1], tri.simplices)
plt.plot(nodes[:,0], nodes[:,1], 'o')
plt.title('Delaunay Triangulation')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
import numpy as np
import sisi_geo

polygon = np.array([[1.0, 1.0],
                    [1.0, 2.0],
                    [2.0, 1.0]])
result = sisi_geo.point_poly_c(1.3, 1.3, polygon)
print("Point inside polygon:", result)

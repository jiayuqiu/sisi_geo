# sisi_geo
refine sisi geo function

## Install

1. Install dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```

2. Build the Cython extension:
```bash
python setup.py build_ext --inplace
```

3. Invoke the function interactively:
```
python
>>> import numpy as np
>>> import sisi_geo
>>> # Define a sample polygon (each row: [lat, lng])
>>> polygon = np.array([[1.0, 1.0],
...                     [1.0, 2.0],
...                     [2.0, 1.0]])
>>> # Test a point, e.g., lng=1.3, lat=1.3
>>> result = sisi_geo.point_poly_c(1.3, 1.3, polygon)
>>> print("Point inside polygon:", result)
Point inside polygon: True
```

Or
```bash
python tmp/demo.py
```
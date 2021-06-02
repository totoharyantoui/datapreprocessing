import numpy as np
x = np.arange(10)
print(x)
y = np.arange(9,-1,-1)
print(y)

import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(type(a))

import pandas as pd
from google.colab import files
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/DataPreprocessing.csv')
print(data)

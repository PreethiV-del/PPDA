import numpy as np
import pandas as pd

A = np.random.randn(5, 10)
print(A, type(A))
dfA = pd.DataFrame(A)
print(dfA,type(dfA))
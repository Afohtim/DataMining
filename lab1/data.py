import pandas as pd
import numpy as np

arr = np.array([[0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0],
                [1, 1, 1, 1, 0]])

columns = ['Q1', 'Q2', 'Q3', 'Q4', 'S']

df = pd.DataFrame(data=arr, columns=columns)

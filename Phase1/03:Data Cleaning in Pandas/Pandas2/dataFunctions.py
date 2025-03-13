import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def inspect_dataset(path):
  df = pd.read_csv(path)

  print('-----Data Info-----')
  print(df.info())

  print('-----Data Description-----')
  print(df.describe())

  return df
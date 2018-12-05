import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Object Creation
# Creating a Series by passing a list of values, letting pandas create a default integer index:

s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

# The columns of the resulting DataFrame have different dtypes.
df2.dtypes

# Viewing Data
df.head()
df.tail(3)

# Display the index, columns, and the underlying NumPy data:
df.index

df.values

# describe() shows a quick statistic summary of your data:
df.describe()

# Transposing your data:
df.T

# Sorting by an axis:
df.sort_index(axis=1, ascending=False)

# Sorting by values:
df.sort_values(by='B')
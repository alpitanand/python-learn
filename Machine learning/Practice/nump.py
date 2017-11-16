import numpy as np
import pandas as pd
number = [1, 2, 3, 4, 5, 0, 9, 4, 6]
print(np.mean(number))
print(np.median(number))
print(np.std(number))
m = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(m)
k = {'a': 0, 'b': 2, 'c': 3}
l = pd.Series(k, index=['b', 'a', 'c', 'r'])
print(l)

print(m[m > m.median()])
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
print(pd.DataFrame(d))
f = [{'a': 1, 'b': 4}, {'a': 4, 'b': 4, 'c': 5}]
print(pd.DataFrame(f, index=['a', 'b']))


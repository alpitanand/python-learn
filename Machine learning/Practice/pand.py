import pandas as pd

data_type = {'name': pd.Series(['Bradund', 'Heniken', 'Cumming', 'Allen'], index=['a', 'b', 'c', 'd']),
             'age': pd.Series([22, 38, 22, 36], index=['a', 'b', 'c', 'd']),
             'fare': pd.Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
             'survival': pd.Series([False, True, True, False], index=['a', 'b', 'c', 'd'])}
k = pd.DataFrame(data_type, index=['a', 'b', 'c', 'd'])
print(k)

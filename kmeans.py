import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def read_date():
    df = pd.read_excel('data.xlsx')
    str_grade = df.iloc[:,5]
    str_rank = df.iloc[:,6]
    node = []
    for s,g in zip(str_rank,str_grade):
        if (s[0] == '前'):
            continue
        r = float(s.split('/')[0])
        _tmp = []
        _tmp.append(r)
        _tmp.append(float(g))
        node.append(_tmp)
    return np.array(node)
data = read_date()
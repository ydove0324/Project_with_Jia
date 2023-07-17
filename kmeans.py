import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

n_cluster = 6

kmeans = KMeans(n_clusters=n_cluster, random_state=0)
cluster = kmeans.fit(data)

y_pred = cluster.labels_
color = ['blue','red','yellow','pink','black','white','gray']

# print(y_pred)
image = plt.subplots(1)[1]

for i in range(n_cluster):
    image.scatter(data[y_pred==i,0],data[y_pred==i,1],
                  marker = 'o',
                  c = color[i])

# image.show()
image.set_xlabel('rank')
image.set_ylabel('gpa')
plt.show()
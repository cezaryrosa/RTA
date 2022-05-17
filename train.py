import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
import joblib
from sklearn import Perceptron


iris = load_iris()

df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names'] + ['target'])


model = Perceptron()

X, y = df.iloc[:100, [0,2]].values, df.iloc[:100, 4]

def a(x):
    if x == 0:
        return -1
    else:
        return 1
    
y = y.map(a)

iris['feature_names'] + ['target']
y = y.values
model.fit(X,y)
model.w_
model.predict([3.4, 3.1])
joblib.dump(model, 'model.pkl')

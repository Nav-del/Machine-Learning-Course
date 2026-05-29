import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def marks_prediction(marks):
    df = pd.read_csv('Hours and Scores.csv')
    print(df.head())

    X = df['Hours'].values
    Y = df['Scores'].values

    model = LinearRegression()

    X_reshaped = X.reshape(-1, 1)
    model.fit(X_reshaped, Y)

    X_test = np.array(marks).reshape(-1, 1)
    return model.predict(X_test)

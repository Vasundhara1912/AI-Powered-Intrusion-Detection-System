import pandas as pd
from sklearn.ensemble import IsolationForest

def train_model():
    data = pd.read_csv("data/sample_traffic.csv")
    features = data[['proto']]

    model = IsolationForest(contamination=0.1)
    model.fit(features)

    return model

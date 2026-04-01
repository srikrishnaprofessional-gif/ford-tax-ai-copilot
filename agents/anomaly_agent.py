import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies():

    data = pd.read_csv("data/invoices.csv")

    model = IsolationForest(contamination=0.2)

    model.fit(data[["invoice_amount"]])

    data["anomaly"] = model.predict(data[["invoice_amount"]])

    anomalies = data[data["anomaly"] == -1]

    return anomalies
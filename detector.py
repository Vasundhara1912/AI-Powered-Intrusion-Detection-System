def detect_anomaly(model, packet_data):
    if packet_data is None:
        return None

    proto = packet_data['proto']
    prediction = model.predict([[proto]])

    if prediction[0] == -1:
        return True
    return False

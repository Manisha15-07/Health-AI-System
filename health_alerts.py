def health_recommendation(data):
    alerts = []

    if data['blood_pressure'] > 130:
        alerts.append("High blood pressure detected. Reduce salt and consult doctor.")
    else:
        alerts.append("Blood pressure is normal.")

    if data['blood_sugar'] > 140:
        alerts.append("High blood sugar. Reduce sugar intake.")
    else:
        alerts.append("Blood sugar is normal.")

    if data['cholesterol'] > 200:
        alerts.append("High cholesterol. Increase fiber intake.")
    else:
        alerts.append("Cholesterol is within normal range.")

    return alerts

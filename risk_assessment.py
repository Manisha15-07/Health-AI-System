def heart_risk(age, bp, cholesterol, smoker):
    risk_score = 0
    if age > 45: risk_score += 1
    if bp > 140: risk_score += 1
    if cholesterol > 240: risk_score += 1
    if smoker: risk_score += 1

    if risk_score >= 3:
        return "High risk of heart disease. Lifestyle changes advised."
    elif risk_score == 2:
        return "Moderate risk. Monitor regularly."
    else:
        return "Low risk."

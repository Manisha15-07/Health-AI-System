def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi < 24.9:
        return bmi, "Normal"
    elif bmi < 29.9:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"

def bmi(weight,height):
    a = weight/(height**2);
    if a <= 18.5: return "Underweight";
    elif 18.5 < a <= 25.0: return "Normal";
    elif 25.0 < a <= 30.0: return "Overweight";
    else: return 'Obese';
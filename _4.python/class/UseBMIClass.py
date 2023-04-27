from BMI import BMI

bmi1 = BMI("John Doe", 18, 145, 70)
print("The BMI for", bmi1.getName(), "is", bmi1.getBMI(), bmi1.getStatus())
    
bmi2 = BMI("Peter King", 50, 215, 70)
print("The BMI for", bmi2.getName(), "is", bmi2.getBMI(), bmi2.getStatus())


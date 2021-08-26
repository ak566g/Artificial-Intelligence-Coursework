weight = float(input("Enter Weight in Pounds: ")) 
hei = float(input("Enter Height in Inches: ")) 
hei = hei**2 
bmi = weight/hei 
bmi = bmi*703 
if bmi < 18.5: 
    print("You have a BMI of ",bmi," and your weight status is Underwight") 
elif bmi >= 18.5 and bmi <= 24.9: 
    print("You have a BMI of ",bmi," and your weight status is Normal") 
elif bmi >= 25 and bmi <= 29.9: 
    print("You have a BMI of ",bmi," and your weight status is Overweight") 
elif bmi > 30: 
    print("You have a BMI of ",bmi," and your weight status is Obese")

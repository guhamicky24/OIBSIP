## BMI calculater by Micky Guha...
h=float(input("Enter your height: "))
W=float(input("Enter your wight: "))
#Calculating the height in metre...
H=(h/100)
#Calculating the BMI...
BMI=(W/(H*H))
print(f'The BMI is: {BMI}')
#Checking the BMI for result...
if(BMI>0):
    if(BMI<=16.0):
        print("Severly UnderBMI ..")
    elif(BMI<=18.0):
        print(" UnderBMI..")
    elif(BMI<=24.9):
        print("Normal BMI..")
    elif(BMI<=29.9):
        print("OverBMI..")
    elif(BMI<=34.9):
        print("Moderately Obese..")
    elif(BMI<=39.9):
        print("Severly Obese..")
    else:
        print("Morbidly Obese..")
else:
    print("Invalid Information")
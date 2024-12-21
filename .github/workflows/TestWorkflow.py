# BMI Calculator Program

# Step 1: Get user input for weight (kg) and height (m)
weight = float(input("Enter your weight in kilograms: "))  # Prompt user for weight
height = float(input("Enter your height in meters: "))  # Prompt user for height

# Step 2: Validate the inputs to ensure they are positive numbers
if weight <= 0 or height <= 0:
    print("Please enter valid positive numbers for weight and height.")
else:
    # Step 3: Calculate BMI
    bmi = weight / (height ** 2)

    # Step 4: Classify the BMI result
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi < 24.9:
        classification = "Normal weight"
    elif 25 <= bmi < 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"

    # Step 5: Output the result to the user
    print(f"Your BMI is {bmi:.2f}, which is considered {classification}.")

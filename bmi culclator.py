# BMI Calculator Project

def calculate_bmi(weight, height):
    """
    Function to calculate BMI.
    BMI = weight (kg) / height (m)^2
    """
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """
    Function to categorize BMI based on standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI CALCULATOR")
    try:
        # Input weight and height
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        # Validate input
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers!")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        
        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()

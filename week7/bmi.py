import pandas as pd

def calculate_risk(bmi):
    if bmi < 18.5:
        return "Nutrient deficient"
    elif 18.5 <= bmi <= 24.9:
        return "Lower risk"
    elif 25 <= bmi <= 29.9:
        return "Heart disease risk"
    elif 30 <= bmi <= 34.9:
        return "Higher risk of diabetes, heart disease"
    elif bmi >= 40:
        return "Serious health condition risk"
    else:
        return "Moderate risk"

def main():
    try:
        df = pd.read_csv("weight_height.csv")
        
        # Calculate BMI (weight / height as per your instruction)
        # If height is in cm, you might want to convert it to meters or adjust the formula
        df['BMI'] = df['weight'] / df['height']

        # Calculate Risk based on BMI
        df['Risk'] = df['BMI'].apply(calculate_risk)

        print(df)

        # Optional: save updated dataframe to a new csv file
        df.to_csv("weight_height_with_bmi.csv", index=False)
        print("\nData saved to 'weight_height_with_bmi.csv'")

    except FileNotFoundError:
        print("Error: 'weight_height.csv' not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt

def plot_scatter(df, x_col, y_col):
    plt.figure(figsize=(6,4))
    plt.scatter(df[x_col], df[y_col], alpha=0.7)
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.title(f"{y_col.capitalize()} vs {x_col.capitalize()}")
    plt.grid(True)
    plt.show()

def main():
    try:
        df = pd.read_csv("weight_height.csv")
        print("CSV file loaded successfully!")
        
        # Check columns available
        print("Columns found:", df.columns.tolist())

        # Plotting various scatter plots
        plot_scatter(df, "weight", "height")
        plot_scatter(df, "age", "weight")
        plot_scatter(df, "height", "age")

        # For gender plots, if gender is categorical, encode it numerically
        if df["gender"].dtype == 'object':
            df["gender_code"] = df["gender"].astype('category').cat.codes
        else:
            df["gender_code"] = df["gender"]

        plot_scatter(df, "gender_code", "height")
        plot_scatter(df, "gender_code", "weight")

    except FileNotFoundError:
        print("Error: 'weight_height.csv' file not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

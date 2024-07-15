import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height) / 100  # converting cm to m
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ValueError:
        return None

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to display BMI
def display_bmi():
    weight = weight_entry.get()
    height = height_entry.get()
    user = user_entry.get()

    if not weight or not height or not user:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    bmi = calculate_bmi(weight, height)
    if bmi is None:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
        return

    category = categorize_bmi(bmi)
    result_label.config(text=f"BMI: {bmi}\nCategory: {category}")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")  # Set window size
root.configure(bg="blue")  # Set background color

tk.Label(root, text="User", bg="blue", fg="white").grid(row=0, column=0, pady=10)
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1, pady=10)

tk.Label(root, text="Weight (kg)", bg="blue", fg="white").grid(row=1, column=0, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, pady=10)

tk.Label(root, text="Height (cm)", bg="blue", fg="white").grid(row=2, column=0, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=display_bmi)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="", bg="blue", fg="white")
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()

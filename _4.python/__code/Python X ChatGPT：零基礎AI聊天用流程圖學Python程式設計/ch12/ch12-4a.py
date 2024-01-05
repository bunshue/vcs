import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100  # 將身高從公分轉換為公尺
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}")

window = tk.Tk()
window.title("BMI 計算機")

height_label = tk.Label(text="身高（公分）：")
height_label.pack()

height_entry = tk.Entry()
height_entry.pack()

weight_label = tk.Label(text="體重（公斤）：")
weight_label.pack()

weight_entry = tk.Entry()
weight_entry.pack()

calculate_button = tk.Button(text="計算 BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label()
result_label.pack()

window.mainloop()

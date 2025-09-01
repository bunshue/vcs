"""
在tkinter上使用matplotlib畫圖

"""

# Dummy data
sales_data = {
    "Product A": 100,
    "Product B": 200,
    "Product C": 600,
    "Product D": 400,
    "Product E": 500,
}

inventory_data = {
    "Product A": 150,
    "Product B": 75,
    "Product C": 100,
    "Product D": 125,
    "Product E": 150,
}

product_data = {"A": 10, "B": 40, "C": 30, "D": 20, "E": 50}

sales_year_data = {2018: 5000, 2019: 17500, 2020: 10000, 2021: 7500, 2022: 15000}

inventory_month_data = {
    "Jan": 200,
    "Feb": 300,
    "Mar": 800,
    "Apr": 1300,
    "May": 600,
    "Jun": 900,
    "Jul": 700,
    "Aug": 900,
    "Sep": 1000,
    "Oct": 300,
    "Nov": 450,
    "Dec": 1300,
}

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"]
)

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
# plt.show()

# Chart 2: Horizontal bar chart of inventory data
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Inventory by Product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")
# plt.show()

# Chart 3: Pie chart of product data
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct="%1.1f%%")
ax3.set_title("Product \nBreakdown")
# plt.show()

# Chart 4: Line chart of sales by year
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")
# plt.show()

# Chart 5: Area chart of inventory by month
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")
# plt.show()

# Create a window and add charts
window = tk.Tk()
window.title("Dashboard")
window.state("zoomed")

side_frame = tk.Frame(window, bg="#4C2A85")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=25)
label.pack(pady=50, padx=20)

charts_frame = tk.Frame(window)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

window.mainloop()

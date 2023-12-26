# ch21_21.py
import json

# 客戶數據管理
customer_data = [
    {"id":1, "name":"Tom", "email":"tom@example.com", "purchases":3},
    {"id":2, "name":"Bob", "email":"bob@example.com", "purchases":5}
]
with open('customers.json', 'w') as file:
    json.dump(customer_data, file)

# 庫存管理
inventory = {
    "products": [
        {"id":101, "name":"Laptop", "stock":40},
        {"id":102, "name":"Smartphone", "stock":100}
    ]
}
with open('inventory.json', 'w') as file:
    json.dump(inventory, file)

# 員工記錄
employees = [
    {"id":"E01", "name":"John Doe", "position":"Manager"},
    {"id":"E02", "name":"Jane Smith", "position":"Developer"}
]
with open('employees.json', 'w') as file:
    json.dump(employees, file)

# 銷售數據分析
sales_data = {
    "year": 2023,
    "sales": [
        {"month":"January", "total_sales":5000},
        {"month":"February", "total_sales":7000}
    ]
}
with open('sales_data.json', 'w') as file:
    json.dump(sales_data, file)

# 商業應用設定
config_settings = {
    "application":"Accounting Software",
    "version":"1.2.0",
    "features": {
        "auto_backup":True,
        "cloud_sync":True
    }
}
with open('config_settings.json', 'w') as file:
    json.dump(config_settings, file)



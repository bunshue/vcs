# Filename: pex03_10.py
pweight = float(input("請輸入體重(英磅)："))
plength = float(input("請輸入身高(英吋)："))
pweight=pweight*0.45359237
plength=plength*0.0254
pbmi=pweight/(plength**2)
print("BMI值為%6.2f"%(pbmi))
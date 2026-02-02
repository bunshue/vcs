# ch2_25.py
import xlwt

fn = 'out2_25.xls'
datahead = ['Phone', 'TV', 'Notebook']
price = ['35000', '18000', '28000']
wb = xlwt.Workbook()
sh = wb.add_sheet('sheet1', cell_overwrite_ok=True)
for i in range(len(datahead)):
    sh.write(0, i, datahead[i])     # 寫入datahead list
for j in range(len(price)):
    sh.write(1, j, price[j])        # 寫入price list

wb.save(fn)





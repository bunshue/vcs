#設置底薪(BaseSalary)、結案獎金件數(Case)、職位獎金(OfficeBonus)
BaseSalary = 25000
CaseBonus = 1000
OfficeBonus = 5000


#請輸入職位名稱(Engineer)、結案獎金金額(CaseAmount)變數
Engineer = str(input("請輸入職位名稱："))
Case = int(input("請輸入結案案件數(整數)："))


#計算獎金function
def CalculateCase(case, caseBonus):
    return case * caseBonus

def CalculateSalary(baseSalary, officeBonus):
    return baseSalary + officeBonus

CaseAmount = CalculateCase(Case, CaseBonus)
SalaryAmount = CalculateSalary(BaseSalary, OfficeBonus)

print("該工程師薪資：", CaseAmount + SalaryAmount)

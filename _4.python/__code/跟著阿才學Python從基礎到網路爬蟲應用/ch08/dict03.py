dictBook={"A001":["木偶奇遇記",199]}
print("編輯前字典內容：",dictBook)

dictBook["A002"] = ["三隻小豬",120]
print("新增後字典內容：",dictBook)

dictBook["A002"] = ["白雪公主",120]
print("修改後字典內容：",dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)

del dictBook["A001"] 
print("刪除後字典內容：",dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)
        
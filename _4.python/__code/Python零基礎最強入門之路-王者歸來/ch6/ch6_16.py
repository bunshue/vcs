# ch6_16.py
cars = ['Toyota', 'Nissan', 'Honda']
print("cars串列長度是 = %d" %  len(cars))
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print("cars串列長度是 = %d" % len(cars))
else:
    print("cars串列內沒有元素資料")
nums = []
print("nums串列長度是 = %d" % len(nums))
if len(nums) != 0:
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")


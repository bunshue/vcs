def map_range(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# 測試範例
input_value = 50
input_min = 0
input_max = 100
output_min = 0
output_max = 255

mapped_value = map_range(input_value, input_min, input_max, output_min, output_max)
print("Mapped value:", mapped_value)

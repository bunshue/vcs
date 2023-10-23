def parse_line(line):
    """ 解析氣象資料的每行紀錄 
        並移除代表無紀錄值的-9999
    """
    # 若遇到空行則回傳None
    if not line:
        return None

    # 將前4個欄位放到record變數，每日紀錄值放到temperature_string變數
    record, temperature_string = (line[:11], int(line[11:15]), 
        int(line[15:17]), line[17:21]), line[21:]

    # 檢查若temperature_string長度太短則拋出例外
    if len(temperature_string) < 248:
        raise ValueError("字串長度不足 - {} {}".format(
            temperature_string, str(line)))

    # 將每日紀錄的溫度值轉為浮點數，並且剃除沒有觀測值的-9999
    values = [float(temperature_string[i:i + 5])/10 
              for i in range(0, 248, 8) 
              if not temperature_string[i:i + 5].startswith("-9999")]

    # 計算該月有紀錄的天數，以及最大值、最小值、平均值
    count = len(values)
    tmax = round(max(values), 1)
    tmin = round(min(values), 1)
    mean = round(sum(values)/count, 1)

    # 回傳解析後的資料
    return record + (tmax, tmin, mean, count)


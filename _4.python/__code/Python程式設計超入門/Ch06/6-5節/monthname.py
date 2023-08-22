def japanese(month):
    month_name = {
        1:"睦月", 2:"如月", 3:"彌生", 4:"卯月", 5:"皐月", 6:"水無月",
        7:"文月", 8:"葉月", 9:"長月", 10:"神無月", 11:"霜月", 12:"師走"
    }
    try:
        response = month_name[month]
    except:
        response = '請輸入月份數字。'

    return response
if __name__ == '__main__':
    print('此為模組檔案，請import匯入後再使用')

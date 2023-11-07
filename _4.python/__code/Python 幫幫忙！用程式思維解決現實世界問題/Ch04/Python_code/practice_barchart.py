import sys
import os
import operator
from collections import Counter
import matplotlib.pyplot as plt

def load_file(infile):
    """載入文字檔並以小寫字串傳回"""
    with open(infile) as f:
        text = f.read().lower()
    return text

def main():
    infile = 'lost.txt'
    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile),
              file=sys.stderr)
        sys.exit(1)
       
    text = load_file(infile)
    
    # 使用字串中的每個字元的出現頻率繪製長條圖
    char_freq = Counter(text)
    char_freq_sorted = sorted(char_freq.items(),
                              key=operator.itemgetter(1), reverse=True)
    x, y = zip(*char_freq_sorted)  # 星號 * 可以解壓縮可迭代物件
    fig, ax = plt.subplots()
    ax.bar(x, y)
    fig.show()
    input()

if __name__ == '__main__':
    main()

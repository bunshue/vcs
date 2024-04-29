import operator

cal_dict = {
    "加": operator.add,
    "減": operator.sub,
    "乘": operator.mul,
    "除": operator.truediv,
    "整除": operator.floordiv,
    "次方": operator.pow,
    "無": lambda: None,
}


def calculator(x, operator, y):
    return cal_dict.get(operator, cal_dict["無"])(x, y)


print(calculator(10, "整除", 3))


print("------------------------------------------------------------")  # 60個

import operator

print("統計字數")

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/engnews.txt"
# filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/琵琶行.txt'
with open(filename, "r", encoding="utf-8") as f:
    # with open(filename, "r", encoding="big5") as f:
    data = f.read()
data = data.translate({ord(c): None for c in list("(),.“”")})
data = data.split()
word_freq = dict()
for word in data:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
for w, c in ordered_freq:
    print(w, c)


print("------------------------------------------------------------")  # 60個

print("字典串列排序")
rows = [
    {"ename": "mouse", "cname": "鼠", "weight": 3},
    {"ename": "ox", "cname": "牛", "weight": 48},
    {"ename": "tiger", "cname": "虎", "weight": 33},
    {"ename": "rabbit", "cname": "兔", "weight": 8},
]

import operator

rows_by_ename = sorted(rows, key=operator.itemgetter("ename"))
rows_by_weight = sorted(rows, key=operator.itemgetter("weight"))
print(rows_by_ename)
print(rows_by_weight)

rows_by_cename = sorted(rows, key=operator.itemgetter("cname", "ename"))
print(rows_by_cename)

print("------------------------------------------------------------")  # 60個


# 用排版格式輸出容器資料

import operator


def sorted_grades(grades):
    grades.sort(key=operator.itemgetter(2), reverse=True)
    output = []
    for first, last, grade in grades:
        output.append(f"{last:12s}{first:10s}{grade:.1f}")
    return "\n".join(output)


grades = [
    ("Alice", "Wooding", 89),
    ("Bob", "Johnson", 86),
    ("Cindy", "Letterman", 93),
    ("David", "Moor", 86),
    ("Eddie", "Williams", 91),
]

print(sorted_grades(grades))

print("------------------------------------------------------------")  # 60個

# 尋找單字中重複最多次的字母

import operator


def most_repeated_letter(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter, word.count(letter)))
    result = sorted(letters_count, key=operator.itemgetter(1))[-1]
    print(f"{result[0]} 重複了 {result[1]} 次")


most_repeated_letter("independence")

print("------------------------------------------------------------")  # 60個

# 簡易前序式計算機

import operator


def prefix_cal(to_solve):
    operation = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    op, num1, num2 = to_solve.split()
    return operation[op](float(num1), float(num2))


print(prefix_cal("+ 2 3"))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# F1750 練習 30

def flatten(data):
    return [sub_element
            for element in data
                for sub_element in element]

print(flatten([[1,2], [3,4]]))

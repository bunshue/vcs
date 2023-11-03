# F1750 練習 32

def flipped_dict(input_dict):
    return {value: key
            for key, value in input_dict.items()}

print(flipped_dict({'a': 1, 'b': 2, 'c': 3}))

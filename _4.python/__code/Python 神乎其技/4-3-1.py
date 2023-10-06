# 4-3-1 定義自訂例外類別

class PasswordTooShortError(ValueError):
    pass

def validate(password):
    if len(password) < 10:
        raise PasswordTooShortError(password)


validate('pw')
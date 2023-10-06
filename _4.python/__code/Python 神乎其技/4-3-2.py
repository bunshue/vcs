# 4-3-2 打造例外類別的階層架構

class BaseValidateError(ValueError):
    pass

class PasswordTooShortError(BaseValidateError):
    pass

class PasswordTooLongError(BaseValidateError):
    pass


def validate(password):
    if len(password) < 10:
        raise PasswordTooShortError(password)
    elif len(password) > 40:
        raise PasswordTooLongError(password)


try:
    validate('pw')

except BaseValidateError as err:
    print(err.with_traceback)

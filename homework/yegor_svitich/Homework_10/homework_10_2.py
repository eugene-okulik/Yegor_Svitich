from functools import wraps


def repeat_me(count=1):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for x in range(count):
                result = func(*args, **kwargs)
                results.append(result)
            return results[-1]

        return wrapper

    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')

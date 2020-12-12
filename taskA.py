def author(author_name):
    def decorator(func):
        func.author = author_name
        return func
    return decorator


if __name__ == '__main__':
    @author('Captain Friedrich Von Non')
    def add2(num: int) -> int:
        return num + 2

    print(add2.author)

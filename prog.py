
def func(n=5):
    i = 0  # а так тоже ошибка (i = 0)?
    while i != n-1:
        print(i)
        i += 1
    print(i, end="")


if __name__ == "__main__":
    func()

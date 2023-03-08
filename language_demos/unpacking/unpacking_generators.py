def do_it():
    yield 1
    yield 2
    yield 3


print(list(do_it()))
print(*do_it())
def fibonacci():
    
    print("started fib")

    num_1 = 0
    num_2 = 1

    yield 0

    while True:

        print("fib in loop")

        next_num = num_1 + num_2
        yield next_num
        num_1 = num_2
        num_2 = next_num


fib_gen = fibonacci()

print("a")
print(next(fib_gen))
print("b")
print(next(fib_gen))
print("c")
print(next(fib_gen))
print("d")
print(next(fib_gen))
print("e")

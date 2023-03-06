

first_name = "Bob"

# performs side-effect
def print_name(fname, lname):
    print(fname + " " + lname)

def output_to_console(text):
    print("App > " + text)

# do not perform side-effects
def full_name(fname, lname):
    return fname + " " + lname


print(first_name)
print_name(first_name, "Smith")
output_to_console(full_name(first_name, "Smith"))
print(first_name)

def another_func(fn):
    fn("call me!!!")


def call_me(msg):
    print(msg)

another_func(call_me)


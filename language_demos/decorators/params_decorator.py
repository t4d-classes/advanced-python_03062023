

class App:
    
    def __init__(self):
        self.__routes = {}
  
    def route(self, path):
        def wrapper(fn):
            self.__routes[path] = fn
            def inner(*args, **kwargs):
                print(f"path: {path}")
                return fn(*args, **kwargs)
            return inner
        return wrapper
    

    def run(self, path, *args, **kwargs):
        fn = self.__routes[path]
        return fn(*args, **kwargs)



app = App()

@app.route("/add")
def add(a,b):
    return a + b

@app.route("/sub")
def subtract(a,b):
    return a - b


# not really what I want to do
# do_it(1,2)

print(app.run("/add", 1,2))
print(app.run("/sub", 1,2))
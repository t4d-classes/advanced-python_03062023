

class Person:
    
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def full_name(self):
      return f"{self.__first_name} {self.__last_name}"
    
    # def set_first_name(self, first_name):
    #    if len(first_name) > 0:
    #       self.__first_name = first_name

    @property
    def first_name(self):
       return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if len(first_name) > 0:
            self.__first_name = first_name


person = Person("Bob", "Smith")
print(person.full_name())

print(person.first_name)

person.first_name = "Sally"
#person.set_first_name("Sally")

print(person.full_name())

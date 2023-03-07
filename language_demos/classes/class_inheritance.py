
# super class, base class, parent class
class Person:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def record_info(self):
        return f"{self.last_name}, {self.first_name}"
    
# sub class, child class
class Worker(Person):
   
    def __init__(self, first_name, last_name, job_title):
        # Person.__init__(self, first_name, last_name)
        super().__init__(first_name, last_name)
        self.job_title = job_title

    def cube_sign(self):
        return f"{self.last_name}, {self.first_name} - {self.job_title}"
    
    def record_info(self):
        return f"{self.job_title}: {super().record_info()}"
    

worker = Worker("Tim", "Johnson", "Analyst")
print(worker.full_name())
print(worker.cube_sign())
print(worker.record_info())

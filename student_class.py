class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def update_age(self, new_age):
        if 18 <= new_age <= 30:
            self.age = new_age
        else:
            print('Invalid age')

student1 = Student("Alice", 20)
print(f"Before update: {student1.name}'s age is {student1.get_age()}") # Before update: Alice's age is 20
student1.update_age(200) # Invalid age range. Age not updated.
print(f"After update: {student1.name}'s age is {student1.get_age()}") # After update: Alice's age is 20

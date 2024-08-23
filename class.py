# This is our blueprint (class) called Student
class Student:
    # The __init__ method is like the student's ID card, given when they join the school.
    def __init__(self, name, age, grade):
        self.name = name  # Student's name
        self.age = age    # Student's age
        self.grade = grade  # Student's grade

    # This method lets a student introduce themselves.
    def introduce(self):
        print("hi my name is cynthia and am from delta state")
        # print(f"Hi, I'm {self.name}, I'm {self.age} years old, and I'm in grade {self.grade}.")

# # Creating a student named Alice who is 14 years old and in grade 9.
# alice = Student("Alice", 14, 9)

# # Alice introduces herself.
# alice.introduce()

# # You can create more students with the same blueprint.
# bob = Student("Bob", 15, 10)
# bob.introduce()


# Why Use Classes?
# Classes help us organize our code better. Instead of writing everything from scratch each time we create a student, we can use the Student class to create as many students as we want with the same basic information.

# This example keeps it simple and shows how classes help us create and manage multiple objects(students) easily.
# Class: Think of it like a cookie cutter. The Student class is the cutter, and each student(Alice, Bob) is a cookie.
# Attributes: These are like the details on each cookie, like the shape, size, and color. In our case, it's the student's name, age, and grade.
# Methods: These are like actions a student can perform, like introducing themselves.


class Dog:

    # class attribute
    attr1 = "ears"
    attr2 = "tail"

    # Instance attribute
    def __init__(self, name, breed, time):
        self.name = name
        self.breed = breed
        self.time = time
        # self.age = age
        
    def barking(self):
        i = 0
        for  i in range(5):
            print(f"the dog has been barking hahahahq hahahahq for {self.time} hours")
        # pass
        
    def reproduction(self):
        pass
    
    def bite(self):
        print("the dog is biting mr okoro")

# Driver code
# Object instantiation
jimmy = Dog("Jimmy", "German Shepherd", 2)


jimmy.barking()


# dog1.barking()
# Tommy = Dog("Tommy")

# Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))

# # Accessing instance attributes
# print("My name is {}".format(Rodger.breed))
# print("My name is {}".format(Tommy.name))


class Game:
    pass
    # method 1 game
    # method 2
    # method 3
    
    # g = Game()
    #g.method1
def print_ages(david, john):
    print("ene is the new girl in class")
    if(david == 10):
        print("david is 10 years old")
    elif(john == 20):
        print("john is 20 years old")
    else:
        print("it looks we don't know their ages")

print_ages(10,20)

# def add_unknown(x, y):
#     result = x + y
#     print(result)
    
# add_unknown(10,40)

#this func prints the names of the two students who missed class yesterday
def new_students():
    student1 = "Triumph"
    student2 = "felix"
    print(student1, " " + student2)


# new_students()


def count_new_students(a, b, c):
    print("the names of the two students that missed the class")
    print("are ", b, "and ", c)
    print("the total number of students are ", a)
    
# count_new_students(2, "felix", "triumph")


def my_function(fname):
  print(fname + " Anulika")


# my_function("Ojor")
# my_function("Tobias")
# my_function("Linus")
    

def people(**names):
    print()


def pamelas_favourite_food(food_name="jollof rice", *pop, **nn, ):
    
    print(food_name)
    

def pamelas_favourite_food(food_name="jollof rice", **nn, ):

    print(food_name)
    
# pamelas_favourite_food()
# pamelas_favourite_food("owo soup")
# pamelas_favourite_food("banga soup")
# pamelas_favourite_food("white soup")
# pamelas_favourite_food("okro soup")


# def add_2(*me):
#     print(me[::1])
    
# add_2("ada", "grace", 0, 22, 33.3, "theo", "picture")
    
    
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

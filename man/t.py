import random

# i = 0
# while i < 6:
#   i += 1
# #   print(i)  
#   if i == 3:
#     print('print the value for sheyi',i)
#     continue
#   print(i)
  
# for x in range(6):
#   print(x)

# for x in range(6):
#   # print(x)
#   if x == 2: 
#     break
#   print(x)
#   print("Finally finished!")
# else:
#   print("Finally finished!")


# s = [0.5, "ade", "nneka", "runor"]
# bayo = ["22.5", "bike", "okon", "daramfon"]
# for p in [0, 2, 3]:
#   pass

# my_name = "my_name_is_david_i_am_happy_to_be_here"

# def my_function(uzoma, chioma):
#   sum = uzoma + chioma
#   print("the sum of the arguments are ", sum)
#   # n = 1
#   # b = 2 b
#   # print(sum)

# my_function(1, 2)
#   # sum = n +

# def david(e, y):
#   # print(e + " " + y)
#   print(e , y)

# david("victor", 0.6)

# def data_science(*kids):
#   # name1 = "runor"
#   print("The students in the class are ", kids[2] ,kids[3])

# data_science("Blessing", "victor", "RUNOR", "emmanuel", "uzoma", "stephanie", "gabrielle", "pere", "rokerfeller", "solomon")

# def my_function(**kid):
#   print("His last name is " + kid["lname"], kid["boy"])

# my_function(fname = "Tobias", lname = "Refsnes", boy = "pere")


# def my_function(food, b):
#   for x in food:
#     for v in b:
#       pass
#     print(x, v)

# fruits = ["apple", "banana", "cherry"]
# bruits = ["mango", "pawpaw"]

# my_function(fruits, bruits)

def tri_recursion(k):
  if(k == 5):
    print('the current k value is', k)
    result = k + tri_recursion(k - 1)
    print('the result at the end of this recursion is ', result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")

tri_recursion(5)
# divine = k

def pair_names(name_list):
    # Make sure there are at least two names in the list
    if len(name_list) < 2:
        print("Error: The list must contain at least two names.")
        return
    # Randomly shuffle the list
    random.shuffle(name_list)
    # Print the pairs
    for i in range(0, len(name_list), 6):
        if i + 1 < len(name_list):
            print(f"({name_list[i]} : {name_list[i + 1]}: {name_list[i + 2]}: {name_list[i + 3]} : {name_list[i + 4]} : {name_list[i + 5]})")
        else:
            print(f"({name_list[i]})")

name_list = ["uzoma", "gabrielle", "chioma", "jaiye", "blessing", "stephanie", "ike", "divine", "solomon", "orobosa", "runor", "divine ajiri", "emmanuel", "kenneth", "victor", "pere", "rockefeller", "elijah"]
pair_names(name_list)




# import datetime

# # prints the current date and time for us
# my_date = datetime.datetime.now()
# print(my_date)
# print(my_date.strftime)


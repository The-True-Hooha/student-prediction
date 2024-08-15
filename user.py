import random
def get_names():
    names_list = []
    while True:
        print("Welcome to the new class register")
        name = input("Add your full name here: ").strip()
    

        if name in names_list:
            print(f"this {name} already exists, please try a new one.")
            for i in range(1, 100):
                suggestion = f"{name}{i}"
                if suggestion not in names_list:
                    print(f"Suggestion: {suggestion}")
                    break

        else:
            names_list.append(name)
            print(f"Name {name} added successfully!")
        add_more = input(
            "Do you want to add another name? (yes/no): ").strip().lower()
        if add_more != "yes":
            break
    print("Final list of names:", ", ".join(names_list))


# get_names()


# def get_names_t():
#     names_tuple = ()
#     while True:
#         print("Welcome to the new class register")
#         name = input("Add your first name here: ").strip()

#         # Check for duplicate names
#         if name in names_tuple:
#             print(f"{name} already exists, try a new one.")
#             # Suggesting a new name by adding a number to the name
#             for i in range(1, 100):
#                 suggestion = f"{name}{i}"
#                 if suggestion not in names_tuple:
#                     print(f"Suggestion: {suggestion}")
#                     break
#         else:
#             names_tuple += (name,)  # Adding a name to the tuple
#             print(f"Name {name} added successfully!")

#         # Optional: Break the loop if no more names need to be added
#         add_more = input(
#             "Do you want to add another name? (yes/no): ").strip().lower()
#         if add_more != "yes":
#             break

#     print("Final list of names:", names_tuple)


# get_names_t()

u = int(input("input a number"))
m = random.randint(1, 100)

if m == u:
    print("correct")
else:
    pass
    #do something here on your own

food = ("rice", "beans", "yam", "fufu", "starch")

num = (1, 2, 3, 6, 5, 7, 9, 0)

# for g in num:
#     print(g)
#     if g == 4:
#         print("welcome to the good life")
#     else:
#         print("there is no 4 in this tuple")


# print(type(food[::1]))
count = 0
# for i in food:
#     if i == "beans":
#         break
# count =count+1
# print(type(i))
# print(i)
# print(count)

# print("the total number of times it took to iterate is ", count)


# Generating numbers from 1 to 10 using a for loop
# for g in range(1, 11):
#     print(g)


# Generating numbers from 1 to 10 using a while loop
# number = 1
# while number <= 10:
#     print(number)
# number += 1  # Increment the number by 1 each time


# Generating pairs of numbers from 1 to 3
# for i in range(1, 5):
#     for j in range(1, 5):
#         print(f"Pair: ({i}, {j})")


# List of lists
# list_of_lists = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Iterating through the list of lists
# for sublist in list_of_lists:
#     for number in sublist:
#         print(number, end=" ")
#     print()  # Move to the next line after each sublist


# Tuple of tuples
# tuple_of_tuples = (
#     (10, 20, 30),
#     (40, 50, 60),
#     (70, 80, 90)
# )

# Iterating through the tuple of tuples
# for subtuple in tuple_of_tuples:
#     for number in subtuple:
#         print(number, end=" ")
#     print()  # Move to the next line after each subtuple



alphabets = (("a", "apple"), ("b", "ball"), ("c", "cat"))


alphabets2 = (
    ('A', 'Apple', "Computer", 10), ('B', 'Ball'), ('C', 'Cat'), ('D', 'Dog'), ('E', 'Elephant'),
    ('F', 'Fish'), ('G', 'Goat'), ('H', 'Hat'), ('I', 'Ice Cream'), ('J', 'Jug'),
    ('K', 'Kite'), ('L', 'Lion'), ('M', 'Monkey'), ('N', 'Nest'), ('O', 'Owl'),
    ('P', 'Parrot'), ('Q', 'Queen'), ('R', 'Rabbit'), ('S', 'Sun'), ('T', 'Tiger'),
    ('U', 'Umbrella'), ('V', 'Violin'), ('W','Whale'), ('X', 'Xylophone'), ('Y', 'Yacht'),
    ('Z', 'Zebra')
)

# print(len(alphabets2))

# using a while loop to iterate through the nested tuples
# i = 0
# while i < len(alphabets2):
#     a, b, c, d = alphabets2[i]
# #     d = d+ 20
#     print(f"{a} - {b} - {c} - {d}")
#     break
#     # i += 2


# with the assignment inside a function
# def letter_word_generator(pairs):
#     for letter, word in pairs:
#         yield f"{letter} - {word}"


# for item in letter_word_generator(letter_word_pairs):
#     print(item)


p = ("A", "B", "C", "D")
e = ("Apple", "Ball", "Cat", "Dog")

# for i in range(len(p)):
#     print(f"{p[i]} - {e[i]}")

# ebube = 0
# while ebube < len(p):
#     print(f"{p[ebube]} ")
#     ebube += 1


# using the for loop
def print_numbers(start, stop):
    for i in range(start, stop):
        print(i)

print_numbers(0, 6)

# using the while loop
# def print_numbers2(start, stop):
#     i = 0
#     length = stop - start + 1
#     while i < length:
#         print(start + i)
#         i += 1

# print_numbers2(0, 5)


b = "Hello, World!"
print(b[2:5])

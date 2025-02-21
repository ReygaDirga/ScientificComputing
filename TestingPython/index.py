# y = 9
# x = input("Enter a number ")
# print(x, end=" ")
# print(type(x))
# print(y)

x = 5
# x = x + 5
# x += 5

# x = x - 5
# x -= 5

# x = x * 5
# x *= 5

# x = x / 5
# x /= 5

# x = x ** 2

# x = x % 5
# print(x)

# if x < 50 :
#     print("Lebih kecil dari 50")
#     if x < 20 or x > 30 :
#         print("Lebih kecil dari 20 atau lebih besar dari 30")
# elif x > 50 :
#     print("Lebih besar dari 50")
#     if x > 60 and x < 80 :
#         print("Lebih besar dari 60 dan kurang dari 80")
        
# udamandi = True
# if not udamandi :
#     print("ih bau")
# else:
#     print("udah wangi")
    
# for i in range (10, 5, -2):
#     print(i)
    
# word = "123yhf"
# word = word.upper()
# word = word.lower()
# word = word.capitalize()
# word = word.title()
# # print(word)
# print(len(word))
# print(word.count('o'))

# if word.isalnum():
#     print("Word is alphanumeric")
# else:
#     print("Word is not aphanumeric")
    
# List, Set, Tuple
# list => []
# test_list = [1, 2, 3, "hallo", True]
# print(test_list[0])
# print(test_list[3])
# print(test_list)
# test_list.append(10)
# test_list.pop()
# for item in test_list:
    # print(item)
# data slicing
# print(test_list[1:4])

# for idx, item in enumerate(test_list):
#     if int(idx) >= 1 and int(idx) <= 3:
#         print(item)


# set => {}
numbers = {2, 3, 1}
numbers.add(3)
numbers.remove(1)
numbers.pop()
print(numbers)


# tuple => ()
test_tuple = (1, 1, 2)
print(test_tuple)

# list => ordered, mutable
# set  => unordered, immutable
# tuple => unordered, immutable

# Dictionary
# key value pair
person = {
    "name" : "bertrand",
    "age" : 19,
    "gender" : "Male"
}
print(person)
print(person["name"])


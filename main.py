"""
1. Write a Python program to check whether a specified value is contained in a group of values.
Test Data:
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

2. Write a Python program that will accept the base and height of a triangle and compute the area.

3. Write a Python program that takes a user's input of time (minutes:seconds) and converts all units of time into seconds.
Test Data:
5:25 -> 325
Butt -> Display Appropriate Error 30 -> 1800
15:799 -> Display Appropriate Error

4. Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.
Test Data:
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

5. Write a Python program to compute the difference between two lists.
Test Data:
["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"] Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
"""
import time


def check_member():
    print("Check membership")
    group = [1, 5, 8, 3]
    val = int(input("enter value: "))
    print(val in group)


def triangle_area():
    base = int(input("enter base: "))
    height = int(input("enter height: "))
    area = (base * height) / 2
    print(f"the area of the triangle is {area}")


def seconds():
    print("what would you like to convert to seconds?")
    to_sec = input("enter times as minutes:seconds :  ")
    try:
        struct_time = time.strptime(to_sec, '%M:%S')
        print((struct_time[4] * 60) + struct_time[5])         # index 4 is min and 5 is sec
    except:
        raise TypeError("incorrect format")


def dict_from_str():
    to_dict = "w3resource"
    for letter in to_dict:
        my_dict = {letter: to_dict.count(letter)}

        print(my_dict)


def difference_between_lists():
    color_1 = ["red", "orange", "green", "blue", "white"]
    color_2 = ["black", "yellow", "green", "blue"]
    color1 = []
    color2 = []
    for item in color_1:
        if item not in color_2:
            color1.append(item)
    for item in color_2:
        if item not in color_1:
            color2.append(item)
    print(f"Color1 - Color2: {color1}")
    print(f"Color2 - Color1: {color2}")


# difference_between_lists()        yes
dict_from_str()
# seconds()                         yes
# triangle_area()                   yes
# check_member()                    yes

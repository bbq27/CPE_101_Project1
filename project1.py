#Name: Berfredd Quezon
#Section: 11

from data import *
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
'''Design Recipe (Write your design recipe here!)
input: string
output: integer number
purpose: return the number of vowels in a string
steps:
1. create a variable count to store the number of vowels
2. check if string is empty
3. iterate through each index in the string
    3.1 check if character in string is a vowel
        3.1.1 add 1 to count if true
4. return count
    
'''
# Implementation
def vowel_count(word:str) -> Optional[int]:
    count = 0
    if word == '':
        return count
    for n in word:
        if n.lower() == 'a' or n.lower() == 'e' or n.lower() == 'i' or n.lower() == 'o' or n.lower() == "u":
            count += 1
    return count

# Part 2
'''Design Recipe (Write your design recipe here!)
input: list of list of integer numbers
output: list of lists of integer numbers
purpose: create a list with lists whose length is equal to 2
steps:
1. check if list is empty 
    1.1 return None if true
2. create an empty list to store the lists whose length is equal to 2
3. iterate through the big list
    3.1. check if nested list is not empty and the length is equal to 2
        3.1.1. add the list to the new list
        3.1.2. loop to next index
    3.2. loop to next index
4. return new list
'''
# Implementation
def short_lists(L:list[list[int]]) -> Optional[list[list[int]]]:
    if not L:
        return None
    new_list = []
    n = 0
    while n < len(L):
        if L[n] != [] and len(L[n]) == 2:
            new_list.append(L[n])
            n += 1
        else:
            n += 1
    return new_list

# Part 3
'''Design Recipe (Write your design recipe here!)
input: list of list of integers
output: list of list of integers
purpose: create a new list to add each element from the original list but change 
the order to ascending order of lists whose length is 2
steps:
1. check if big list is empty
    1.1 return None if true
2. create empty list to store new list with ascending pairs
3. loop through list
    3.1 check if nested list has a length equal to 2
        3.1.1 check if first element is less than second element
            3.1.1.1 reverse order of list
            3.1.1.2 add list to new list
        3.1.2 else add nested list to new list
    3.2 add nested list to new list
    3.3 loop to next index
4. return new list
'''
# Implementation
def ascending_pairs(big:list[list[int]]) -> Optional[list[list[int]]]:
    if not big:
        return None
    new_list = []
    for small in big:
        if len(small) == 2:
            if small[0] > small[1]:
                small.reverse()
            new_list.append(small)
        else:
            new_list.append(small)

    return new_list

# Part 4
'''Design Recipe (Write your design recipe here!)
input: two price objects
output: price object
purpose: add two price objects and return a price object whose cents value is no bigger than 99
steps:
1. create variable to store added cent values
2. create variable to store added dollars value
3. create count variable
4. check if added cent value is greater than 99
    4.1 if true subtract 100 cents from current cent value and add 1 to current dollar value
5. return new Price object with new dollar and new cent

'''
# Implementation
def add_prices(item1:Price, item2:Price) -> Price:
    total_cent = item1.cents + item2.cents
    total_dollar = item1.dollars + item2.dollars
    if total_cent > 99:
        total_cent -= 100
        total_dollar += 1
    return Price(total_dollar,total_cent)
    #return Price(item1.dollars + item2.dollars, item1.cents + item2.cents) old code

# Part 5
'''Design Recipe (Write your design recipe here!)
input: rectangle object
output: float
purpose: return the area of a rectangle object
steps:
1. find the height of the rectangle
    1.1 find the point of intersection between the top left and bottom right coordinates
    1.2 use the euclidean distance function to find the distance between the top left coord
        and intersection point
2. find the width of the rectangle
    2.1 find the point of intersection between the top left and bottom right coordinates
    2.2 use the euclidean distance function to find the distance between the bottom right coord 
        and intersection point
3. return the height * width
'''
# Implementation
'''
input: two point objects
output: a float
purpose: return the euclidean distance (square root of the difference of the points squared) between two points
steps:
1. create variable to store answer
2. find the euclidean distance between the points
3. return answer
'''
def euclidean_distance(P1:Point,P2:Point) -> float:
    answer = math.sqrt(math.pow(P1.x-P2.x,2)+math.pow(P1.y-P2.y,2))
    return answer

'''
input: two point objects
output: point object
purpose: find a point of intersection between the x coord of one point and y coord of the other
steps:
1. return a point object with the x coord of the first point and the y coord of the second point
'''
def find_intersection(P1:Point,P2:Point) -> Point:
    return Point(P1.x,P2.y)

def rectangle_area(rect:Rectangle) -> float:
    height = euclidean_distance(rect.top_left, find_intersection(rect.top_left, rect.bottom_right))
    width = euclidean_distance(find_intersection(rect.top_left, rect.bottom_right), rect.bottom_right)
    return height * width

# Part 6
'''Design Recipe (Write your design recipe here!)
input: string and a list of Book objects
output: list of Book objects
purpose: create a list with a list of book objects with a specific inputted author
steps:
1. check if list of book objects is empty
    1.1 if true return none
2. create an empty list new_list to store the books by the given author
3. loop through the list of books
    3.1 check if the author name is in the list of authors in each book in the list of books
        3.1.1 if true add that book to new_list
4. return new_list
'''
# Implementation
def books_by_author(author_name:str, book_list:list[Book]) -> Optional[list[Book]]:
    if not book_list:
        return None
    new_list = []
    for book in book_list:
        if author_name in book.authors:
            new_list.append(book)
    return new_list

# Part 7
'''Design Recipe (Write your design recipe here!)
input: rectangle object
output: Circle object
purpose: create the smallest possible circle that encompasses a given rectangle
steps:
1. create a variable to store the center of the rectangle
    1.1 use the find_center function to find the center of the circle
2. create a variable to store the radius of the function
    2.1 find the euclidean distance between the center and a corner point
3. return a circle object with the new center and radius
'''
# Implementation
'''
input: two point objects
output: one point object
purpose: find the center between two points
steps:
1. create a variable to store the sum of the x coords for both points
2. create a variable to store the sum of the y coords for both points
3. return a new point object with the new x coord and y coord
'''
def find_center(P1:Point, P2:Point) -> Point:
    center_x = (P1.x+P2.x)/2
    center_y = (P1.y+P2.y)/2
    return Point(center_x,center_y)

def circle_bound(rect:Rectangle) -> Circle:
    center = find_center(rect.top_left, rect.bottom_right)
    radius = round(euclidean_distance(rect.top_left, center), 1)
    return Circle(center, radius)

# Part 8
'''Design Recipe (Write your design recipe here!)
input: list of employee objects
output: list of string(s)
purpose: create a list of names of employee's who's pay is below the average pay in a given list
steps:
1. check if list is empty
    1.1 return None if true
2. set a variable for employee count in a list to 0
3. set a variable for average_pay in a list to 0
4. loop through each item in the employee list
    4.1 add the employee pay rate to the average_pay variable
    4.2 add 1 to the employee_count
5. divide average_pay by employee_count to find actual average pay
6. create an empty list below_avg to store employee names that are below the average pay
7. loop through each employee in the list
    7.1 check if the employee pay rate is less than the average pay
        7.2 if true add the employee name to below_avg
8. return below_avg
'''
# Implementation
def below_pay_average(employee_list:list[Employee]) -> Optional[list[str]]:
    if not employee_list:
        return None
    employee_count = 0
    average_pay = 0
    for employee in employee_list:
        average_pay += employee.pay_rate
        employee_count += 1
    average_pay /= employee_count
    below_avg = []
    for employee in employee_list:
        if employee.pay_rate < average_pay:
            below_avg.append(employee.name)
    return below_avg

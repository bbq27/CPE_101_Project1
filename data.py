import math

# Representation of a price in integer dollars and cents.
class Price:
    # Initialize a new Price object.
    # input: dollars as an integer
    # input: cents as an integer
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    # Provide a developer-friendly string representation of the object.
    # input: Price for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Price({}, {})'.format(self.dollars, self.cents)


    # Compare the Price object with another value to determine equality.
    # input: Price against which to compare
    # input: Another value to compare to the Price
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Price and
                self.dollars == other.dollars and
                self.cents == other.cents)

# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))


# Representation of an axis-aligned rectangle.
class Rectangle:
    # Initialize a new Rectangle object.
    # input: top-left corner as a Point
    # input: bottom-right corner as a Point
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right


    # Provide a developer-friendly string representation of the object.
    # input: Rectangle for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.top_left, self.bottom_right)


    # Compare the Rectangle object with another value to determine equality.
    # input: Rectangle against which to compare
    # input: Another value to compare to the Rectangle
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)


# Representation of a circle.
class Circle:
    # Initialize a new Circle object.
    # input: center as a Point
    # input: radius as a float
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


    # Provide a developer-friendly string representation of the object.
    # input: Circle for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Circle({}, {})'.format(self.center, self.radius)


    # Compare the Circle object with another value to determine equality.
    # input: Circle against which to compare
    # input: Another value to compare to the Circle
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Circle and
                self.center == other.center and
                math.isclose(self.radius, other.radius))


# Representation of a book.
class Book:
    # Initialize a new Book object.
    # input: the book's authors as a list of strings
    # input: the book's title as a string
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title


    # Provide a developer-friendly string representation of the object.
    # input: Book for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return "Book({}, '{}')".format(self.authors, self.title)


    # Compare the Book object with another value to determine equality.
    # input: Book against which to compare
    # input: Another value to compare to the Book
    # output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == Book and
                self.authors == other.authors and
                self.title == other.title)


# Abbreviated representation of an employee.
class Employee:
    # Initialize a new Employee object.
    # input: the employee's name as a string
    # input: the employee's pay rate as an integer (for simplicity)
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate


    # Provide a developer-friendly string representation of the object.
    # input: Employee for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return "Employee('{}', {})".format(self.name, self.pay_rate)


    # Compare the Employee object with another value to determine equality.
    # input: Employee against which to compare
    # input: Another value to compare to the Employee
    # output: boolean indicating equality
    def __eq__(self, other):
        return (other is self or
                type(other) == Employee and
                self.name == other.name and
                self.pay_rate == other.pay_rate)

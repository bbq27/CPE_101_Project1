import data
import unittest


class TestCases(unittest.TestCase):
    def test_Price_1(self):
        price = data.Price(1, 20)
        self.assertEqual(price.dollars, 1)
        self.assertEqual(price.cents, 20)


    def test_Price_2(self):
        price = data.Price(4, 19)
        self.assertEqual(price.dollars, 4)
        self.assertEqual(price.cents, 19)


    def test_Price_eq_1(self):
        price1 = data.Price(1, 20)
        price2 = data.Price(1, 20)
        self.assertEqual(price1, price2)


    def test_Price_eq_2(self):
        price1 = data.Price(1, 20)
        self.assertEqual(price1, price1)


    def test_Price_eq_3(self):
        price1 = data.Price(1, 20)
        price2 = data.Price(2, 20)
        self.assertNotEqual(price1, price2)


    def test_Price_eq_4(self):
        price = data.Price(1, 20)
        other = 1.20
        self.assertNotEqual(price, other)


    def test_Price_repr(self):
        price = data.Price(5, 75)
        self.assertEqual(repr(price), 'Price(5, 75)')


    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(point.x, 7)
        self.assertAlmostEqual(point.y, 20)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(point.x, 4)
        self.assertAlmostEqual(point.y, 19)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual(repr(point), 'Point(5, 75)')


    def test_Rectangle_1(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(rectangle.top_left, data.Point(7, 20))
        self.assertEqual(rectangle.bottom_right, data.Point(12, 10))


    def test_Rectangle_eq_1(self):
        rectangle1 = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        rectangle2 = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(rectangle1, rectangle2)


    def test_Rectangle_eq_2(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(rectangle, rectangle)


    def test_Rectangle_eq_3(self):
        rectangle1 = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        rectangle2 = data.Rectangle(data.Point(4, 17), data.Point(12, 10))
        self.assertNotEqual(rectangle1, rectangle2)


    def test_Rectangle_eq_4(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        other = 1.20
        self.assertNotEqual(rectangle, other)


    def test_Rectangle_repr(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(repr(rectangle),
            'Rectangle(Point(7, 20), Point(12, 10))')


    def test_Circle_1(self):
        circle = data.Circle(data.Point(7, 20), 6.2)
        self.assertEqual(circle.center, data.Point(7, 20))
        self.assertEqual(circle.radius, 6.2)


    def test_Circle_eq_1(self):
        circle1 = data.Circle(data.Point(7, 20), 6.2)
        circle2 = data.Circle(data.Point(7, 20), 6.2)
        self.assertEqual(circle1, circle2)


    def test_Circle_eq_2(self):
        circle = data.Circle(data.Point(7, 19), 4.7)
        self.assertEqual(circle, circle)


    def test_Circle_eq_3(self):
        circle1 = data.Circle(data.Point(7, 20), 4.7)
        circle2 = data.Circle(data.Point(4, 17), 4.7)
        self.assertNotEqual(circle1, circle2)


    def test_Circle_eq_4(self):
        circle1 = data.Circle(data.Point(7, 20), 4.7)
        circle2 = data.Circle(data.Point(7, 20), 4.6)
        self.assertNotEqual(circle1, circle2)


    def test_Circle_eq_5(self):
        circle = data.Circle(data.Point(7, 20), 4.7)
        other = 1.20
        self.assertNotEqual(circle, other)


    def test_Circle_repr(self):
        circle = data.Circle(data.Point(7, 20), 2)
        self.assertEqual(repr(circle), 'Circle(Point(7, 20), 2)')


    def test_Book_1(self):
        book = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(book.authors, ['Neil Gaiman', 'Terry Pratchett'])
        self.assertEqual(book.title, 'Good Omens')


    def test_Book_eq_1(self):
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(book1, book2)


    def test_Book_eq_2(self):
        book = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(book, book)


    def test_Book_eq_3(self):
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(['Terry Pratchett', 'Neil Gaiman'], 'Good Omens')
        self.assertNotEqual(book1, book2)


    def test_Book_eq_4(self):
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(['Neil Gaiman', 'Terry Pratchett'],
            'Illustrated Good Omens')
        self.assertNotEqual(book1, book2)


    def test_Book_eq_5(self):
        book = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        other = 1.20
        self.assertNotEqual(book, other)


    def test_Book_repr(self):
        book = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(repr(book),
            "Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')")


    def test_Employee_1(self):
        employee = data.Employee('Neil', 5)
        self.assertEqual(employee.name, 'Neil')
        self.assertEqual(employee.pay_rate, 5)


    def test_Employee_eq_1(self):
        employee1 = data.Employee('Neil', 5)
        employee2 = data.Employee('Neil', 5)
        self.assertEqual(employee1, employee2)


    def test_Employee_eq_2(self):
        employee = data.Employee('Neil', 5)
        self.assertEqual(employee, employee)


    def test_Employee_eq_3(self):
        employee1 = data.Employee('Neil', 5)
        employee2 = data.Employee('Terry', 5)
        self.assertNotEqual(employee1, employee2)


    def test_Employee_eq_4(self):
        employee1 = data.Employee('Neil', 5)
        employee2 = data.Employee('Neil', 7)
        self.assertNotEqual(employee1, employee2)


    def test_Employee_eq_5(self):
        employee = data.Employee('Neil', 5)
        other = 1.20
        self.assertNotEqual(employee, other)


    def test_Employee_repr(self):
        employee = data.Employee('Neil', 5)
        self.assertEqual(repr(employee), "Employee('Neil', 5)")


if __name__ == '__main__':
    unittest.main()

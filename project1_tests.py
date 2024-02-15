#Name: Berfredd Quezon
#Section: 11

import data
from project1 import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        str1 = 'ThIs is A test for vowEls'
        expected = 7
        self.assertEqual(expected, vowel_count(str1))

    def test_vowel_count2(self):
        str2 = ''
        expected = 0
        self.assertEqual(expected, vowel_count(str2))

    def test_vowel_count(self):
        str3 = 'str1 + str2'
        expected = 0
        self.assertEqual(expected, vowel_count(str3))

    # Part 2
    def test_short_lists1(self):
        list1 = [[12, 2, 3], [1, 2], [-9, 0, 9, 78], [5, 6]]
        expected = [[1, 2], [5, 6]]
        self.assertEqual(expected, short_lists(list1))

    def test_short_lists2(self):
        lst = [[12, 2, 3], [1, 0, 2], [-9, 0, 9, 78], [1, 5, 6]]
        expected = []
        self.assertEqual(expected, short_lists(lst))

    def test_short_lists3(self):
        lst = []
        expected = None
        self.assertEqual(expected, short_lists(lst))

    # Part 3
    def test_ascending_pairs1(self):
        lst = [[12,2,3],[10,2],[-9,0,9,78],[15,6],[1,2]]
        expected = [[12,2,3],[2,10],[-9,0,9,78],[6,15],[1,2]]
        self.assertEqual(expected, ascending_pairs(lst))

    def test_ascending_pairs2(self):
        lst = [[12,2,3],[10,2,0],[-9,0,9,78],[1,5,6]]
        expected = [[12,2,3],[10,2,0],[-9,0,9,78],[1,5,6]]
        self.assertEqual(expected, ascending_pairs(lst))

    def test_ascending_pairs3(self):
        lst = []
        expected = None
        self.assertEqual(expected, ascending_pairs(lst))

    # Part 4
    def test_Price_add1(self):
        price1 = Price(1, 20)
        price2 = Price(1, 20)
        expected = Price(2, 40)
        self.assertEqual(expected, add_prices(price1,price2))

    def test_Price_add2(self):
        price1 = Price(1, 70)
        price2 = Price(10, 40)
        expected = Price(12, 10)
        self.assertEqual(expected, add_prices(price1,price2))

    def test_Price_add3(self):
        price1 = Price(1,99)
        price2 = Price(5,99)
        expected = Price(7,98)
        self.assertEqual(expected, add_prices(price1,price2))

    # Part 5
    def test_euclidean_distance1(self):
        point1 = Point(-10, -12)
        point2 = Point(48, -3)
        result = euclidean_distance(point1, point2)
        expected = 58.69
        self.assertAlmostEqual(expected, result, 2)

    def test_euclidean_distance2(self):
        result = euclidean_distance(Point(1,4), Point(3,3))
        expected = 2.24
        self.assertAlmostEqual(expected, result, 2)

    def test_find_intersection1(self):
        result = find_intersection(Point(-2,3),Point(2,-6))
        expected = Point(-2,-6)
        self.assertEqual(expected, result)

    def test_find_intersection2(self):
        result = find_intersection(Point(1,1), Point(2,0))
        expected = Point(1,0)
        self.assertEqual(expected,result)

    def test_area1(self):
        rect = Rectangle(Point(1, 1),Point(2, 0))
        expected = 1
        self.assertEqual(expected, rectangle_area(rect))

    def test_area2(self):
        rect = Rectangle(Point(-2, 3),Point(2, -6))
        expected = 36
        self.assertEqual(expected, rectangle_area(rect))

    # Part 6
    def test_books_by_author_1(self):
        library_3 = [Book(["Alice Walker"], "The Color Purple"),\
                     Book(["Lana del Rey"], "Violet Bent Backwards over the Grass"),\
                     Book(["Maria Semple"], "Where'd You Go, Bernadette?"),\
                     Book(["Alice Walker"], "Meridian"),\
                     Book(["Barbara T. Christian", "Alice Walker"], "Everyday Use")]
        result = books_by_author("Alice Walker", library_3)
        expected = [Book(['Alice Walker'], 'The Color Purple'),
                    Book(['Alice Walker'], 'Meridian'),\
                    Book(['Barbara T. Christian', 'Alice Walker'],'Everyday Use')]
        self.assertEqual(len(expected), len(result))

    def test_author_1(self):
        book_lst = [Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')\
                   ,Book(['Neil Gaiman', 'Terry Pratchett'],\
                         'Illustrated Good Omens')]
        expected = [Book(['Neil Gaiman','Terry Pratchett'], 'Good Omens'),\
                    Book(['Neil Gaiman','Terry Pratchett'], 'Illustrated Good Omens')]
        res = books_by_author('Neil Gaiman',book_lst)
        self.assertEqual(res,expected)

    # Part 7
    def test_find_center1(self):
        result = find_center(Point(6,20),Point(12,10))
        expected = Point(9,15)
        self.assertEqual(expected, result)

    def test_find_center2(self):
        result = find_center(Point(-1,4),Point(2,-2))
        expected = Point(1.5,3)
        self.assertEqual(expected, result)

    def test_circle_bound_1(self):
        rec = Rectangle(data.Point(7, 20), data.Point(12, 10))
        circle = circle_bound(rec)
        self.assertEqual(Circle(Point(9.5,15.0),5.6), circle)

    def test_circle_bound_2(self):
        rec = Rectangle(data.Point(1, 4), data.Point(5, 2))
        circle = circle_bound(rec)
        self.assertEqual(Circle(Point(3.0, 3.0), 2.2), circle)

    # Part 8
    def test_avg_pay1(self):
        emps = [Employee('Sam', 3000.0),Employee('Tom',5000.0),\
                Employee('Mary', 4000.0)]
        expected = ['Sam']
        self.assertEqual(expected, below_pay_average(emps))

    def test_avg_pay2(self):
        emps = [Employee('Sam', 4000.0),Employee('Tom',4000.0),\
                Employee('Mary', 4000.0)]
        expected = []
        self.assertEqual(expected, below_pay_average(emps))

    def test_avg_pay3(self):
        emps = []
        expected = None
        self.assertEqual(expected, below_pay_average(emps))



if __name__ == '__main__':
    unittest.main()

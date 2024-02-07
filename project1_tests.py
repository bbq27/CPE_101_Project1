#Name: Berfredd Quezon
#Section: 11

import data
from project1_SOL import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        str1 = 'This is a test for vowels'
        expected = 7
        self.assertEqual(vowel_count(str1), expected)

    def test_vowel_count2(self):
        str1 = ''
        expected = 0
        self.assertEqual(vowel_count(str1), expected)

    def test_vowel_count(self):
        str1 = 'str1 + str2'
        expected = 0
        self.assertEqual(vowel_count(str1), expected)

    # Part 2
    def test_short_lists1(self):
        lst = [[12,2,3],[1,2],[-9,0,9,78],[5,6]]
        expected = [[1,2],[5,6]]
        self.assertEqual(short_lists(lst),expected)

    def test_short_lists2(self):
        lst = [[12, 2, 3], [1, 0, 2], [-9, 0, 9, 78], [1, 5, 6]]
        expected = []
        self.assertEqual(short_lists(lst), expected)
    def test_short_lists3(self):
        lst = []
        expected = []
        self.assertEqual(short_lists(lst), expected)

    # Part 3
    def test_ascending_pairs1(self):
        lst = [[12,2,3],[10,2],[-9,0,9,78],[15,6],[1,2]]
        expected = [[12,2,3],[2,10],[-9,0,9,78],[6,15],[1,2]]
        self.assertEqual(ascending_pairs(lst),expected)
    def test_ascending_pairs2(self):
        lst = [[12,2,3],[10,2,0],[-9,0,9,78],[1,5,6]]
        expected = [[12,2,3],[10,2,0],[-9,0,9,78],[1,5,6]]
        self.assertEqual(ascending_pairs(lst),expected)
    def test_ascending_pairs3(self):
        lst = []
        expected = []
        self.assertEqual(ascending_pairs(lst),expected)

    # Part 4
    def test_Price_add1(self):
        price1 = Price(1, 20)
        price2 = Price(1, 20)
        expected = Price(2, 40)
        self.assertEqual(add_prices(price1,price2), expected)
    def test_Price_add2(self):
        price1 = Price(1, 70)
        price2 = Price(10, 40)
        expected = Price(12, 10)
        self.assertEqual(add_prices(price1,price2), expected)

    # Part 5
    def test_area1(self):
        rect = Rectangle(Point(1, 1),Point(2, 0))
        expected = 1
        self.assertEqual(rectangle_area(rect), expected)

    def test_area2(self):
        rect = Rectangle(Point(-2, 3),Point(2, -6))
        expected = 36
        self.assertEqual(rectangle_area(rect), expected)
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
        book_lst = [data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')\
                   ,data.Book(['Neil Gaiman', 'Terry Pratchett'],\
                          'Illustrated Good Omens')]
        expected = [Book(['Neil Gaiman'], 'Good Omens'), Book(['Neil Gaiman'], 'Illustrated Good Omens')]
        res = books_by_author('Neil Gaiman',book_lst)
        self.assertEqual(res,expected)


    # Part 7
    def test_circle_bound_1(self):
        rec = Rectangle(data.Point(7, 20), data.Point(12, 10))
        circle = circle_bound(rec)
        self.assertEqual(circle, Circle(data.Point(5,10),10.20 ))

    def test_circle_bound_2(self):
        rec = Rectangle(data.Point(1, 4), data.Point(5, 2))
        circle = circle_bound(rec)
        self.assertEqual(circle, Circle(data.Point(4, 2), 3.61))

    # Part 8
    def test_avg_pay1(self):
        emps = [Employee('Sam', 3000.0),Employee('Tom',5000.0),\
                Employee('Mary', 4000.0)]
        expected = ['Sam']
        self.assertEqual(below_pay_average(emps), expected)
    def test_avg_pay2(self):
        emps = [Employee('Sam', 4000.0),Employee('Tom',4000.0),\
                Employee('Mary', 4000.0)]
        expected = []
        self.assertEqual(below_pay_average(emps), expected)

    def test_avg_pay3(self):
        emps = []
        expected = []
        self.assertEqual(below_pay_average(emps), expected)



if __name__ == '__main__':
    unittest.main()

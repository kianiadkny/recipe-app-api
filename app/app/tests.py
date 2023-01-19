
'''
Samples Test
'''

from django.test import SimpleTestCase

from app import calc 

class CalcTests(SimpleTestCase):
    ''' Test the calculator module
    '''

    def test_add_numbers(self):
        '''' Test Adding numbers together'''

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subract_numbers(self):
        ''' Test for subtracting numbers'''

        res = calc.subtract(10,15)

        self.assertEqual(res, 5)
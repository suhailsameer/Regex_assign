import unittest
from regex import task1, task2, task3, task4

class TestRegexTasks(unittest.TestCase):

    def test_task1(self):
        # Test for extracting phone numbers
        expected = [
            '123-456-7890', '(123) 456-7890', '123-456-7890',
            '111-222-3333'
        ]
        with self.assertLogs() as captured:
            task1()
        output = captured.output[0].split("INFO:root:")[1].strip()
        self.assertEqual(eval(output), expected)

    def test_task2(self):
        # Test for password strength
        expected = ['1bcdefgA', '1234abcdADD', 'EHHHFada12333', 'ADBCDUUA1234']
        with self.assertLogs() as captured:
            task2()
        output = captured.output[0].split("INFO:root:")[1].strip()
        self.assertEqual(eval(output), expected)

    def test_task3(self):
        # Test for finding dates
        expected = ['12/31/2020', '01-01-2021', '31/12/2020']
        with self.assertLogs() as captured:
            task3()
        output = captured.output[0].split("INFO:root:")[1].strip()
        self.assertEqual(eval(output), expected)

    def test_task4(self):
        # Test for replacing special characters
        expected = """
    Hello_ World_
    Python_3_8
    Regex_101
    This            sentence      has     big      spaces_____
    """
        with self.assertLogs() as captured:
            task4()
        output = captured.output[0].split("INFO:root:")[1].strip()
        self.assertEqual(output, expected.strip())

if __name__ == '__main__':
    unittest.main()
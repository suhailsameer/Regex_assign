import re

def task1(): # Extract all phone numbers
    p = re.compile(r'\(?\d{3}\)?[-\s]?\d{3}-\d{4}',re.MULTILINE)
    test = """
    123-456-7890
    (123) 456-7890
    1234567890
    123.456.7890
    1234567890
    123-4567890
    123 456 7890
    123-456-7890
    111-222-3333
    """
    print(p.findall(test))
def task2(): # Check password strength
    p = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}')
    test = """
    1bcdefgA
    12345678
    abcdefghij
    Abcdefghij
    abcde1234
    1234abcdADD
    EHHHFada12333
    ADBCDUUA1234
    """
    print(p.findall(test))

def task3(): # Find all dates in a text
    p = re.compile(r'\d{1,2}([/-])\d{1,2}\1\d{4}')
    test = """
    12/31/2020
    01-01-2021
    31/12/2020
    2020-12-31
    2020/12/31
    12-31/2020
    12/31-2020"""
    print([match.group(0) for match in p.finditer(test)])

def task4(): # Replace all special characters in a string with an underscore
    p = re.compile(r'[^\w\s\n]')
    test = """
    Hello, World!
    Python@3.8
    Regex#101
    This            sentence      has     big      spaces.....
    """
    print(p.sub('_', test))
    #print(test)   

task2()
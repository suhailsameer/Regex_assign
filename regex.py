import re

def task1(): # Extract all phone numbers
    p = re.compile(r'\(?\d{3}\)?[-\s]\d{3}-\d{4}',re.MULTILINE)
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
    print(f"Task 1:- {test}\nCorrect Expressions:- {p.findall(test)}")
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
    print(f"Task 2:- {test}\nCorrect Expressions:- {p.findall(test)}")

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
    print(f"Task 3:- {test}\nCorrect Expressions:- {[match.group(0) for match in p.finditer(test)]}")

def task4(): # Replace all special characters in a string with an underscore
    p = re.compile(r'[^\w\s\n]')
    test = """
    Hello, World!
    Python@3.8
    Regex#101
    This            sentence      has     big      spaces.....
    """
    print(f"Task 4:- {test}\nCorrected Text:- {p.sub('_', test)}")
    #print(test) 
 
def task5():
    p = re.compile(r'[A-Z][a-z\'A-Z]*')
    test = """
   Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel suscipit diam, eu venenatis mauris. Etiam varius ultricies tortor, vitae commodo leo venenatis ut. Pellentesque et lorem ultricies, imperdiet tortor et, sagittis massa. Praesent eu tortor at odio elementum imperdiet. Vestibulum id turpis tristique, fringilla quam sed, laoreet odio. Nulla facilisi. Aliquam tempus ante in sapien porta pellentesque. Praesent nulla sapien, lacinia nec nulla non, malesuada gravida nulla. Mauris ac neque efficitur, imperdiet magna vel, sodales leo. Aliquam sagittis lacus leo, nec rhoncus orci dignissim quis. Cras iaculis nulla sit amet consequat rutrum.

Proin eleifend, metus nec iaculis eleifend, est tortor tempus metus, sit amet commodo eros nulla id tellus. Phasellus sed sodales urna, vulputate mattis nunc. Proin eu est nec orci volutpat sagittis et ut turpis. Aliquam quam arcu, eleifend id cursus eu, vulputate in erat. Aliquam convallis libero metus, vitae hendrerit nisl mollis in. Nulla id congue lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce a nibh quis sapien blandit volutpat.

Morbi eu tellus magna. Vivamus tristique finibus feugiat. Etiam sagittis faucibus sapien nec dapibus. Aenean blandit maximus ligula, sit amet elementum velit vestibulum eu. Suspendisse potenti. Etiam feugiat eros ac nunc dictum, ac mollis tortor suscipit. Praesent hendrerit at elit iaculis condimentum.

Donec est nisl, porta finibus viverra eget, fringilla id neque. Etiam diam ipsum, euismod a lorem eu, vestibulum gravida arcu. Praesent eu pretium eros. Proin eget dui at nisl condimentum bibendum. Vivamus pellentesque ante sit amet magna blandit dignissim. Maecenas mattis ornare tortor, eu venenatis quam lacinia id. Ut in laoreet est, id bibendum mi. Duis erat lorem, egestas sit amet erat vitae, gravida dapibus ante. Cras sodales sit amet sapien tincidunt mollis. Vivamus lacinia justo sed varius sagittis. Phasellus varius dui sit amet sapien iaculis ullamcorper ac sit amet odio. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus vel egestas ante. Etiam porttitor iaculis diam, et blandit quam blandit dictum. Ut eu velit eu risus tempus hendrerit.

Etiam vel lobortis leo. Curabitur fermentum imperdiet massa, ut sodales dui hendrerit sed. Integer varius, leo ut venenatis scelerisque, mi urna placerat urna, nec ultrices sapien ex ut dolor. Cras sed turpis sem. Praesent quis sodales augue. Mauris nec eleifend nunc. Maecenas scelerisque condimentum arcu, non pulvinar sapien sollicitudin vitae. Maecenas lectus metus, consectetur vitae porta at, venenatis vel erat. Etiam eu eros elit. Nam mauris arcu, fringilla in neque at, pellentesque rhoncus ante. They're
    """
    print(f"Task 5(Ipsem Lorum):- {p.findall(test)}") 

task1()
task2()
task3()
task4()
task5()
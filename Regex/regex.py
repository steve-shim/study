import re

# urls = """
# http://python-engineer.com
# http://www.pyeng.net
# """
# pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match)
#     print(match.group(), match.span(), match.start(), match.end())


test_string = """
hello
01.04.2020

2020.04.01

2020-04-01
2020-06-11
2020-07-31
2020-12-31

2020/5/31

2020_12_04
2020_01_04
"""
pattern = re.compile(r'\d{4}[-/]\d?[5-7][-/]\d\d')
matches = pattern.finditer(test_string)

# match, search(), findall(), finditer()
# matchobject -> group, start, end, span
for match in matches:
    print(match)
    print(match.group(), match.span(), match.start(), match.end())

dmy_string = """
Mr Simpson
1223
2020-05-20
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
Python-engineer@gms.de
Python-engineer123@my-domain.org
steveshim496@gmail.com
"""
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = pattern.finditer(dmy_string)
for match in matches:
    print(match)
    print(match.group(), match.span(), match.start(), match.end())

pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.(com|de|org)')
matches = pattern.finditer(dmy_string)
for match in matches:
    print(match)
    print(match.group(), match.span(), match.start(), match.end())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

# matches = pattern.findall(test_string)
# print(matches)

# match = pattern.match(test_string)
# print(match) # None

# match = pattern.search(test_string)
# print(match) 
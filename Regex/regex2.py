import re

test_string = """abc123ABCDEF456789abc123ABC"""
pattern = re.compile(r'123')
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match)
#     print(match.group(), match.span(), match.start(), match.end())
splitted = pattern.split(test_string)
print(splitted)

test_string = """hello world, you are the best world"""
pattern = re.compile(r"world")
subbed_string = pattern.sub("planet", test_string)
print(subbed_string)

urls = """
hello
2020-05-20
https://www.python-engineer.com
https://python-engineer.com
http://www.pyeng.net
"""
pattern = re.compile(r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
matches = pattern.finditer(urls)
for match in matches:
    print(match.group())

subbed_urls = pattern.sub(r"\3_shim_\2", urls)
print(subbed_urls)

my_string = "Hello WorlD"
pattern = re.compile(r"world", re.IGNORECASE)
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

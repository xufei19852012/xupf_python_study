import re

phoneregex = re.compile(r'\d{3}-\d{4}-\d{4}')
mo = phoneregex.search('my phone num is 132-6068-2152 ')
print('phone num is ' + mo.group())
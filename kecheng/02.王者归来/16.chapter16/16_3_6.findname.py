import re
msg = 'johnson will attend my party tonight'
pattern = 'john(na)?son'
txt = re.search(pattern,msg)
print(txt.group())

msg = 'johnnason will attend my party tonight'
pattern = 'john((na)?son)'
txt = re.search(pattern,msg)
print(txt.group())
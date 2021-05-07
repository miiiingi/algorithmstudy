import re
p = re.compile('a[e]c')
m = p.match('adec')
print(m.group())
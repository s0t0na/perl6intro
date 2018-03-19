import re

text = "Bob|19|01012017"
pat = re.compile("(?P<name>.+)\|.*\|(?P<bday>.+)") 
result = pat.match(text)
d = result.groupdict()

print d
